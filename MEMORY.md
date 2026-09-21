# MEMÓRIA DO PROJETO — Mara Vilhosa e o Sabor
Salvo em: 2026-09-21 (America/Sao_Paulo). Retomar daqui.

## 1. Doutrina oficial
- **Método de trabalho:** Método Rafaviolinista — https://orbita-engenharia-ia.rafaeldenovaes.chatgpt.site/
- Trilha M00–M18 (19 módulos, 51 aulas): fundamentos, produto antes do modelo (M02), RAG (M04), agentes (M05), arquitetura (M06), avaliação (M07), operação/economia (M08), segurança (M09/M10), governança ISO 42001 (M11), piloto (M12), vender valor (M15), gestão (M16), TI (M17), escala (M18).
- **Regra de retroalimentação (decisão do Rafael):** projetos se retroalimentam; todo conceito considera conhecimentos de todos os projetos; próximo sempre melhor que o anterior.

## 2. Base GitHub (inventário feito)
- Conta-alvo: **https://github.com/rafaelnovaes22** — 34 repos públicos.
- Flagships: bitnet-gateway (Python, gateway híbrido BitNet+Muse Spark 1.3), banco-aifirst (TS), ai-cfo-platform (Fastify+LangGraph+Prisma+BullMQ, eval-gated), multi-agent-company-os (150+ agentes), agent-governance-framework (constitution + gates SHADOW→AUTONOMOUS), marketing-ai-agents (7 agentes), CarInsight + carinsight-backend (NestJS) + carinsight-frontend, facilIAuto, clickup-automation, seekerh-signal, escolta-ai, marcos-ai.
- Fábrica SMB: 15 sites HTML molde caio-gusmao (wellington-reboucas, gem-jardim-nair, alfaiataria-ai, lanchonete-ai etc.).
- Local `C:\Users\Rafael\Projetos` (10 pastas): 7 com .git (maioria origin `dantia-startup/*`), 3 sem git. `dantia-forge` = framework canônico; `nucleo` tem AGENTS.md próprio + forge_check; `DantIA` remote `rafaelnovaes22/dantia-governanca-ia` (nome diverge da pasta).
- Base direta deste projeto: `rafaelnovaes22/lanchonete-ai` (Podrão.AI, index.html único, cardápio clicável + combo IA + assistente + pedido no zap, Railway nginx:8080, WhatsApp placeholder `5511999990000`).

## 3. Cliente: Mara Vilhosa Salgados (amigo do Rafael)
- Instagram: https://instagram.com/mara_vilhosa_e_o_sabor/ — `@mara_vilhosa_e_o_sabor`, 40 posts, 492 seguidores, 675 seguindo. Bio: Família Empreendedora, Sabores Caseiros, Salgados Artesanais.
- Endereço: Av. Dos Ipês, 1302 B, São Paulo 08161-142 (Itaim Paulista / Jardim dos Ipês).
- Contatos: WhatsApp (11) 98927-2470 → `https://wa.me/5511989272470`; catálogo `wa.me/c/5511994286290`; WhatsMenu `https://whatsmenu.com.br/maravinhosasalgados`; iFood `https://www.ifood.com.br/delivery/sao-paulo-sp/mara-vilhosa-salgados-jardim-dos-ipes/589033f2-2156-43ec-bd85-8a1af168f99e`.
- Oferta (prints): salgados a partir de R$2, Combo Degustação sem desperdício + brinde Gini nostálgica, cento/festa ("Faça a festa e deixe o salgado por nossa conta"), pão de queijo sem glúten (sem conservante/corante/aroma, queijo meia cura), empadas, kibe (teste de produto / em breve novo sabor), caixa octogonal MS. Prova: Cliente Adriana #Recomendadíssimo + suquinho brinde.
- Delivery: sex/sáb 19h–22h via plataformas. Grade do Insta inconsistente (foto boa + arte amadora).

## 4. Decisões travadas com o Rafael
1. Site + plataforma AI-first para eles atuarem **só na especialidade (fazer salgado)**.
2. **Sem entregadores exclusivos/parceiros** — pedidos só via plataformas (iFood + WhatsMenu) ou **retirada no balcão** (sem taxa, com brinde quando houver).
3. Escopo piloto: **só Mara Vilhosa** (sem pool multi-lojas).
4. **Criar novo repo** (não evoluir `lanchonete-ai` in place).
5. Aplicar conceitos dos **5 melhores sites do tema no Awwwards de forma irrastreável** (abstrair padrão, zero cópia de paleta/fonte/texto/código/motion).

## 5. Referências Awwwards (conceitos abstraídos)
1. **Crav Burgers (Anyflow, SOTD 7.25)** — ordering lúdico 3 toques, Next.js+GSAP, creme+vermelho → aplicado como funil `Escolha → Monte → Retirar/iFood` com micro-motion CSS próprio.
2. **VOLDOG FOOD (CHP Studio, HM)** — e-commerce com personalidade + switch de modo → aplicado como toggle original `Modo Fome / Modo Festa`.
3. **LÜKS KEBAB (BLACKT)** — street-food gourmet + monte o seu (10 molhos/4 pães) → aplicado como `Monte seu cento` + claim `Não é só salgado, é Mara Vilhosa`.
4. **PausaPiadina (chain artesanal IT)** — artesanal sem mesa, só balcão/retirada → aplicado como operação 2 fluxos (retirada + plataforma).
5. **Snack With Benefits (Cut the Code, HM)** — storytelling + horizontal scroll + design system → aplicado como narrativa `De família para família` + prova Adriana em scroll horizontal próprio, paleta MS original (marrom #211004 / creme #fff6e9 / dourado #d99a2b / terracota #c0521e — NÃO copiar #f5e3cd/#f91814 nem #101820/#EAFF00).

## 6. O que foi construído (local)
Pasta: `C:\Users\Rafael\Projetos\mara-vilhosa\`
- `index.html` (24.814 bytes, single-file, sem fotos externas): hero MS, toggle Festa/Fome, cardápio 8 itens (coxinha 2,50 / kibe 2,50 / bolinha 2 / empada 6 / pão de queijo sem glúten 4 / degustação 29 / caixa 50 R$120 / cento R$230), combo IA 2 perguntas, carrinho com `Retirar no balcão →` (wa.me/5511989272470) e `Ver plataformas` (iFood), assistente local por regras (KB: entrega, retirada, cento, degustação, sem glúten, preço, horário, pagamento + blocklist injection), FAQ, footer. Whats real em 5 pontos (`var W="5511989272470"`). Zero `5511999990000`.
- `README.md`, `governance/constitution.md` (Foundry lite C1–C8), `evals/cases.json` (5 casos), `Dockerfile` + `nginx.conf` + `railway.json` (copiados de lanchonete-ai, porta 8080), `.gitignore`, `assets/` (vazio).
- Git local: `master`, commit `ccd5423 "feat: Mara Vilhosa e o Sabor site AI-first (retirada + plataformas, sem entrega propria)"`, 8 arquivos. **Sem remote.**

## 7. Status do push — ONDE PAROU
- `gh` autenticado como **`dantia-startup`** (keyring). Tentativa `gh repo create rafaelnovaes22/mara-vilhosa` falhou: `dantia-startup cannot create a repository for rafaelnovaes22 (createRepository)`.
- `gh repo view rafaelnovaes22/mara-vilhosa` → `Could not resolve to a Repository` (não existe).
- Tentativa `gh auth login` gerou fluxo device (`github.com/login/device/authorize`) que no navegador do Rafael deu **404 "This is not the web page you are looking for"** (print enviado). Rafael perguntou "o que está acontecendo? pq deu erro?".
- **Pendente:** autenticar `gh` como `rafaelnovaes22`, depois:
  ```
  cd C:\Users\Rafael\Projetos\mara-vilhosa
  git branch -M main
  gh repo create rafaelnovaes22/mara-vilhosa --public --source=. --push --description='Mara Vilhosa e o Sabor - salgados artesanais AI-first: retirada sem taxa + iFood/WhatsMenu. Evolucao de lanchonete-ai.'
  ```
- Alternativa (se login pessoal travar): criar como `dantia-startup/mara-vilhosa` e transferir depois — **aguardar decisão do Rafael, não fazer sem ele**.

## 8. Resposta ao erro 404 (para retomar)
Explicar: o 404 foi na página de autorização do device flow (código expirado ou aba trocada), não no projeto. Caminho correto: `gh auth login` → escolher GitHub.com → HTTPS → `Login with a web browser` → copiar o código de 8 letras mostrado NO TERMINAL → abrir `github.com/login/device` manualmente (não o link /authorize direto) → colar código → autorizar → `gh auth switch --user rafaelnovaes22` → `gh auth status` deve mostrar rafaelnovaes22 ativo → só então criar o repo.

## 9. Próximos passos (ao retomar)
1. Confirmar `gh auth status` = rafaelnovaes22.
2. Criar + push do repo (comando acima).
3. Deploy Railway (projeto `mara-vilhosa`, Dockerfile nginx 8080) + domínio.
4. Teste manual: montar pedido → Retirar (zap com mensagem) → iFood/WhatsMenu → assistente (5 evals) → mobile.
5. `playbook-extract`: devolver molde SMB v2 para `lanchonete-ai` (loop: próximo melhor que anterior).
6. Mostrar para o dono: QR balcão + link bio Instagram.
