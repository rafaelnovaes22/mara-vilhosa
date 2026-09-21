# Mara Vilhosa e o Sabor — site AI-first

Site + plataforma AI-first da lanchonete familiar do Jardim dos Ipês (Av. Dos Ipês, 1302 B, São Paulo).
Eles cozinham — a plataforma resolve o resto.

Evolução de `lanchonete-ai` (Podrão.AI single-file) para o caso real Mara Vilhosa.
Novo repo, traço original MS — padrões premiados abstraídos de forma irrastreável (zero cópia).

## Modelo
- **Retirada no balcão sem taxa** (código do pedido, brinde quando disponível)
- **Entrega só via plataformas**: iFood + WhatsMenu (sex/sáb 19h–22h)
- Sem entregadores exclusivos, sem parceiros — por decisão do dono

## Rodar
```powershell
python -m http.server 8000
```
Deploy: Railway, Dockerfile nginx porta 8080 (igual `lanchonete-ai`).

## Links reais
- Whats: https://wa.me/5511989272470
- iFood: https://www.ifood.com.br/delivery/sao-paulo-sp/mara-vilhosa-salgados-jardim-dos-ipes/589033f2-2156-43ec-bd85-8a1af168f99e
- WhatsMenu: https://whatsmenu.com.br/maravinhosasalgados
- Instagram: https://instagram.com/mara_vilhosa_e_o_sabor/

## Governança
Ver `governance/constitution.md`. Assistente local por regras, sem backend LLM alegado.
Evals em `evals/cases.json` — preço, horário, retirada vs plataforma.
