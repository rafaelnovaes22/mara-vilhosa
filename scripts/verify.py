"""Verificação comando único Mara Vilhosa. Uso: python scripts/verify.py."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"
CASES = ROOT / "evals" / "cases.json"
NGINX = ROOT / "nginx.conf"
RAILWAY = ROOT / "railway.json"
WHATS_REAL = "5511989272470"
WHATS_FAKE = "5511999990000"


def fail(msg: str, got: str = "") -> None:
    detail = f" | recebido={got!r}" if got else ""
    print(json.dumps({"ok": False, "erro": msg + detail}))
    raise SystemExit(1)


def check_html() -> str:
    if not HTML.exists():
        fail("index.html ausente", str(HTML))
    raw: str = HTML.read_text(encoding="utf-8")
    lines: int = raw.count("\n") + 1
    if lines > 500:
        fail("index.html acima de 500 linhas", str(lines))
    if len(raw.encode("utf-8")) > 100_000:
        fail("index.html acima de 100KB")
    if WHATS_FAKE in raw:
        fail("placeholder de WhatsApp ainda presente", WHATS_FAKE)
    # PORQUÊ: links montados via var W contam como pontos reais (cRet, qgo, assistente).
    pontos: int = raw.count(WHATS_REAL) + raw.count('wa.me/"+W')
    if pontos < 5:
        fail("WhatsApp real em menos de 5 pontos", str(pontos))
    for link in ["ifood.com.br", "whatsmenu.com.br", "instagram.com/mara_vilhosa_e_o_sabor"]:
        if link not in raw:
            fail("link real ausente", link)
    return raw


def norm(text: str) -> str:
    import unicodedata

    flat: str = unicodedata.normalize("NFD", str(text or "").lower())
    return "".join(c for c in flat if unicodedata.category(c) != "Mn")


def kb_answer(entry: dict, text: str) -> str:
    lowered: str = norm(text)
    best: str = ""
    best_score: int = 0
    for item in entry:
        keys: list = [norm(k) for k in item["k"]]
        score: int = sum(len(k) for k in keys if k in lowered)
        if score > best_score:
            best_score = score
            best = item["a"]
    return best if best else "Chama no zap (11) 98927-2470 que a família responde."


def check_evals(html: str) -> None:
    if not CASES.exists():
        fail("evals/cases.json ausente")
    cases: list = json.loads(CASES.read_text(encoding="utf-8"))
    kb_raw: str = html.split("var KB=")[1].split("];")[0] + "]" if "var KB=" in html else ""
    if not kb_raw:
        fail("KB do assistente não encontrada no index.html")
    import re

    pairs: list = re.findall(r'\{k:\[(.*?)\],a:"(.*?)"\}', kb_raw)
    kb: list = [{"k": re.findall(r'"(.*?)"', k), "a": a} for k, a in pairs]
    if not kb:
        fail("KB vazia após parse", kb_raw[:80])
    for case in cases:
        ans: str = kb_answer(kb, case["input"])
        for must in case["must_contain"]:
            if must.lower() not in ans.lower():
                fail(f"eval {case['id']} sem {must!r}", ans)


def check_infra() -> None:
    nginx: str = NGINX.read_text(encoding="utf-8")
    if "location = /health" not in nginx or "return 200" not in nginx:
        fail("/health ausente no nginx.conf")
    if "8080" not in nginx:
        fail("porta 8080 ausente no nginx.conf")
    rail: dict = json.loads(RAILWAY.read_text(encoding="utf-8"))
    if rail.get("deploy", {}).get("healthcheckPath") != "/health":
        fail("healthcheckPath != /health no railway.json")


def main() -> None:
    html: str = check_html()
    check_evals(html)
    check_infra()
    print(json.dumps({"ok": True, "checks": ["html", "evals:5", "infra:health"]}))


if __name__ == "__main__":
    main()
