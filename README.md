# Le Jardin — Jardin vivant

Novo conceito visual, criado a partir de `cirosouzatecno/SiteLeJardin`, commit de referência `4f747938c074679921f7b0ba10598609bb53eb17`.

## Hospedagem

Repositório de destino: `cirosouzatecno/NovoModeloSiteLeJardin`. Projeto Vercel: `novosite`.

O `vercel.json` publica somente a pasta `dist`, como site estático. O build verifica a sintaxe e executa os testes; não há banco nem variáveis secretas necessárias para esta apresentação. O Node.js é usado apenas para validação e desenvolvimento local. O projeto inclui a prévia autossuficiente para uso offline, que não é necessária no servidor.

## Abrir

Abra `LeJardin_Preview.html` no navegador para experimentar a versão completa, sem instalação e sem internet para carregar imagens. O arquivo é autossuficiente.

Para desenvolver, com Node.js 18 ou superior:

```sh
npm run dev
```

Acesse `http://localhost:4173`. Não há dependências para instalar. O código editável está em `dist/index.html`, `dist/styles.css`, `dist/catalog.js` e `dist/app.js`.

## Experiência

- Abertura cinematográfica com arte floral conceitual, pétalas, pontos luminosos e folhagens em camadas.
- Parallax na rolagem e um jardim ilustrado que cresce ao navegar.
- Coleção com cinco produtos reais do catálogo versionado, busca sem acentos e filtros combinados.
- Detalhes em modal com navegação por teclado, recado opcional e link para consultar pelo WhatsApp.
- Seleção por ocasião, contato, Instagram e acesso ao catálogo completo existente.
- Layout para celular, menu móvel, redução de movimento do sistema e controle manual de animações.
- Imagens locais otimizadas; nenhuma biblioteca externa ou fonte remota é necessária.

## Escopo

É uma nova apresentação navegável para avaliar o design. O site oficial e o repositório remoto não foram modificados. O painel administrativo, o banco, os uploads e a instrumentação de produção existentes não estão integrados nesta versão. Os valores e a disponibilidade são consultados com a equipe. O WhatsApp abre uma mensagem preenchida; o visitante decide se vai enviá-la.

As cinco fotos de produtos vêm do repositório original. A abertura é uma imagem gerada para ambientação, identificada como conceitual na página; não representa produto à venda. Os desenhos de folhagens são SVGs originais. Os nomes de categorias desta seleção foram organizados para navegação; IDs e nomes de produtos foram mantidos.

## Evolução para produção

Reaproveitar o backend Next.js existente e substituir a interface pública por componentes com este design. Consumir `/api/catalog`, manter produtos/categorias por URL, validar a integração com o painel e preservar SEO, métricas e políticas. Revisar o conteúdo com a loja antes de publicar. A prévia tem `noindex,nofollow` intencionalmente.

## Verificação

Execute `npm run check` e `node --test tests/interaction.test.mjs`. A verificação automatizada cobre filtros, busca, modal, recado e links. A inspeção visual interativa da nova versão não pôde ser concluída nesta sessão: o navegador não alcançou o servidor local e o acesso a arquivos locais pelo navegador automatizado é bloqueado. O site oficial foi consultado em modo de leitura.

Leia `ANALISE_E_ESTRUTURA.md` para a análise e o plano de integração.
