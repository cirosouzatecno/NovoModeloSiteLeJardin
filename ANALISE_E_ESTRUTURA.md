# Análise e nova estrutura — Le Jardin

Referência: repositório privado `cirosouzatecno/SiteLeJardin`, branch `main`, commit `4f747938c074679921f7b0ba10598609bb53eb17`. Consulta em 11/11/2026. Análise do código e leitura da página pública `https://lejardinfleurs.com.br/`. Não é uma auditoria de segurança, desempenho medido ou dos dados privados de produção.

## O que o projeto atual oferece

| Área | Estrutura encontrada |
|---|---|
| Plataforma | Next.js 16 e React 19; produção na Vercel conforme README |
| Vitrine | Carrossel, categorias visuais, busca por texto/ocasião, galeria, detalhes de produtos e imagens/vídeos |
| Catálogo | `/api/catalog`; catálogo inicial versionado e catálogo persistido em Redis |
| Compra | `/api/whatsapp` valida produto ativo, estoque e telefone antes de montar a mensagem |
| Administração | Login, catálogo, categorias, imagens/vídeos, destaques, vitrine, compartilhamento e métricas |
| Persistência | Upstash Redis para configurações, sessões, tentativas de login, pedidos e eventos; armazenamento em memória restrito a desenvolvimento |
| Arquivos | Vercel Blob descrito para uploads; arquivos legados versionados |
| Conteúdo | Flores, boxes, buquês, cestas, balões, cakes, arranjos, Natal, condolências e festas |
| SEO | Metadados, canonical, sitemap de produtos/categorias, robots e páginas individuais |
| Medição | Google Analytics, Vercel Analytics/Speed Insights e eventos próprios |
| Identidade | Verde, serifas, assinatura Fleurs Boutique; São José do Rio Preto e região; Instagram @lejardinfleurs.rp |

## Diagnóstico da experiência

1. **A mensagem principal aparece tarde.** A ordem de `StoreView.tsx` coloca carrossel, categorias e coleção antes do hero institucional. Na leitura pública, essa ordem também apareceu. O visitante recebe várias opções antes de entender a proposta.
2. **A entrada tem muitos caminhos simultâneos.** Menu, catálogo externo, faixa natalina, carrossel, categorias, ocasiões e filtros disputam a atenção. A nova versão dá uma ação principal por momento.
3. **A galeria depende da configuração de destaques.** Na leitura pública apareceu “Os produtos selecionados como Destaque aparecerão aqui.” Isso é uma observação daquele carregamento; não confirma ausência de produtos no banco. A nova seleção evita que a primeira experiência dependa dessa configuração.
4. **A personalidade pode ir além da cor.** O CSS atual usa predominantemente Arial e Georgia, superfícies verdes e componentes convencionais. A nova direção usa escala tipográfica editorial, espaços de respiro e contraste entre jardim escuro e páginas claras.
5. **Animações precisam ter propósito.** A proposta conecta movimento à natureza: folhas revelam a cena, flores flutuam sutilmente, e a rolagem faz o jardim crescer. O visitante pode pausar; a preferência de movimento reduzido é respeitada.
6. **É essencial manter a compra clara.** O atendimento pelo WhatsApp continua central. Valores não foram inventados. Os produtos selecionados têm preço sob consulta no catálogo versionado.
7. **Há conteúdo a revisar antes da integração integral.** O catálogo legado contém nomes genéricos como “Box 100”, categorias amplas e descrições sob consulta. A interface não deve gerar promessas a partir desses registros. A nova seleção usa cinco registros identificáveis.
8. **A base operacional pode ser reaproveitada.** Não há motivo para substituir o banco, os uploads ou a gestão para mudar a aparência. O caminho de produção é integrar esta nova interface ao backend existente.

## Conceito: Jardin vivant

Uma boutique floral que parece um jardim se revelando. Verde profundo `#0b211b`, marfim `#f5f1e8`, rosa pétala `#e8b6a4` e verdes botânicos. A imagem conceitual cria atmosfera; as fotos reais identificam aquilo que o visitante pode consultar.

| Seção | Objetivo | Comportamento |
|---|---|---|
| Abertura | Apresentar o universo e convidar a explorar | Arte cinematográfica, parallax, pétalas e folhas independentes |
| Faixa botânica | Conectar as duas atmosferas | Texto contínuo com pausa por preferência de movimento |
| A essência | Dar significado ao gesto | Jardim ilustrado crescendo durante a rolagem |
| Coleção | Facilitar a escolha | Fotos reais, filtros, busca e cinco detalhes completos |
| Ocasiões | Ajudar quem ainda não sabe o que escolher | Sugestão contextual e consulta pelo WhatsApp |
| Contato | Encaminhar a decisão | Uma ação de atendimento clara |
| Rodapé | Reunir canais e controles | Telefone, Instagram, WhatsApp, topo e controle de movimento |

## Arquitetura entregue

- `dist/index.html`: estrutura semântica, navegação, seções e diálogos.
- `dist/styles.css`: identidade, layout, animações e breakpoints.
- `dist/catalog.js`: seleção estática versionada para revisão.
- `dist/app.js`: busca/filtros, modais, WhatsApp, links, menu e movimento.
- `dist/assets/`: cinco fotos reais, logotipo de referência e arte otimizada.
- `server.mjs`: servidor estático local, restrito a loopback.
- `LeJardin_Preview.html`: cópia autossuficiente da experiência para abrir diretamente.

## Integração recomendada no projeto original

1. Separar apresentação em `SiteHeader`, `ImmersiveHero`, `LivingGarden`, `Collection`, `ProductDialog`, `Occasions` e `SiteFooter`.
2. Trocar o catálogo estático pelo retorno de `/api/catalog`, mantendo filtros e condições reais de ativo/estoque.
3. Manter IDs, páginas individuais, canonical, política de devolução e sitemap. Remover `noindex` apenas na versão aprovada para produção.
4. Usar `/api/whatsapp` para disponibilidade e registrar cliques com `trackMetric`. Recados devem ser tratados como entrada do visitante.
5. Preservar o painel e conectar destaques/promocionais à curadoria da nova coleção; tratar catálogo sem destaques de forma explícita.
6. Usar lazy loading abaixo da dobra, carregar apenas a imagem principal com prioridade e não reproduzir vídeos pesados automaticamente em todos os cards.
7. Validar teclado, contraste, dispositivos físicos, tamanhos de tela, preferência de movimento, carregamento e desempenho com o catálogo integral.
8. Publicar uma prévia separada antes de promover a nova interface no domínio oficial.

## Limites da avaliação

O acesso Git via terminal não estava disponível, então a análise usou o conector GitHub. Foram lidos a árvore completa e os arquivos centrais de vitrine, CSS, catálogo, layout, persistência, API administrativa, API WhatsApp, métricas, página individual, SEO e testes de produção. O site público foi lido, sem alterações. Não foram consultados o Redis de produção, credenciais nem o painel autenticado. A nova versão foi validada por sintaxe, integridade de arquivos e testes de comportamento em ambiente DOM simulado; o navegador não conseguiu abrir a prévia local nesta sessão. Não há afirmação de teste visual concluído, pontuação Lighthouse ou integração de backend realizada.
