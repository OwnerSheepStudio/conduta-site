# CLAUDE.md

Guia para agentes que trabalham neste repositório.

## Projeto

Site estático do **Conduta** (OwnerSheep Studio), publicado em **ownersheep.com.br** (pt-BR na raiz, `/en/` e `/es/`). Página principal com história, regras, condutas, times, habilidades, fichas, roadmap e chamadas para a Play Store e o Discord. A política de privacidade (`/conduta/policy`) e a exclusão de conta (`/conduta/account-deletion`) são exigidas pela Google Play: **nunca remover**. Nenhuma das duas tem link nas páginas de idioma.

## Onde está o que vai ao ar

```
site/                      → raiz publicada em ownersheep.com.br
  index.html               → /            (pt-BR)
  en/index.html            → /en/
  es/index.html            → /es/
  conduta/policy.html      → /conduta/policy (política de privacidade)
  conduta/account-deletion.html → /conduta/account-deletion (exclusão de conta, exigida pela Google Play)
  ds-v2.css                → camada do Design System v2 (todas as línguas)
  fonts/                   → fontes auto-hospedadas
  portraits/<funcao>.webp  → retratos das fichas = retratos atuais do jogo (Assets/_Project/Art/Sprites/Roles/<Role>.png)
  icons/<nome>.svg         → ícones do site, gerados por tools/icones/gerar.py (não editar à mão)
  flags/{br,us,es}.svg     → bandeiras do seletor de idioma (dropdown <details>, fecha ao clicar fora)
```

## Ícones

Desenho a lápis grafite com sombra de carvão, no estilo dos ícones que a UI artist pintou nas placas do jogo. A fonte é `tools/icones/gerar.py`: cada ícone é um SVG 64×64 transparente com três camadas (sombra em hachura, traço com tremor de lápis, risco claro de realce). Para criar ou mudar um ícone, edite o gerador e rode:

```bash
python tools/icones/gerar.py && cp tools/icones/svg/*.svg site/icons/
```

`tools/icones/folha.html` mostra todos sobre a placa de metal para revisão. No site, os ícones ficam sobre uma placa `--aco-400` chanfrada nos cantos superior esquerdo e inferior direito, como os cards (`--placa-chanfro`; grafite sobre ela: 4,7:1), classes `ico-*` em `ds-v2.css`. As fichas retidas usam `ficha_retida.svg`; não usar a pintura de personagem bloqueado da artista ali.

As três páginas de língua têm a mesma estrutura: uma mudança visual vale para as três. Os textos ficam no próprio HTML de cada língua.

`public/` e os HTML soltos na raiz (`conduta.html`, `terms.html`, `privacy.html`, `vercel.json`) são a versão antiga da Vercel (abril/2026) e **não** vão ao ar.

## Design System

O site segue o **Design System v2 "Casa de Máquinas"** do Conduta (Drive: `02-estudio/00-ips/Conduta/Design System/conduta-design-system-v2-rascunho.md`). As páginas ainda carregam o CSS v1.3.2 embutido; `site/ds-v2.css` vem depois e redefine os **valores** das mesmas variáveis (`--surface-*`, `--ink-*`, `--accent`…), então use sempre `var(--…)` e nunca cor solta.

- Metal frio (`--aco-*`, `--patina-*`), papel (`--papel-*`), luz da lâmpada (`--luz-300` = `--accent`) e ferrugem só como textura.
- CTA = placa de metal pintado (`--patina-600` com texto `--papel-50`).
- Títulos em Rokkitt (substituta livre da Rockwell usada na UI do jogo); corpo em Barlow; Special Elite só em metadados de arquivo.
- Cores de time e conduta mantêm os valores do jogo, sempre com ícone e palavra.
- Texto com contraste ≥ 4,5:1.

## Deploy (Cloudflare Workers, só arquivos estáticos)

Deploy em produção **só com autorização explícita** do Nikolas no chat.

```bash
npx wrangler@4 deploy --dry-run   # confere sem publicar
npx wrangler@4 deploy             # publica site/ no Worker conduta-site
```

O domínio está ligado ao Worker no painel da Cloudflare; `wrangler.jsonc` não declara rotas para não mexer nisso.

**Atenção:** o deploy substitui o conjunto inteiro de arquivos do Worker. Arquivo que não estiver em `site/` sai do ar. Em 19/11/2026 isso derrubou `/conduta/account-deletion` por dois dias. Antes de publicar, confira que as duas páginas legais estão em `site/conduta/`.

Para conferir localmente: `python -m http.server 8787 --directory site`.

## Regras de conversão

- CTAs da Play Store e do Discord abrem com `target="_blank" rel="noopener noreferrer"`.
- Toda mudança de texto vale para as três línguas.
