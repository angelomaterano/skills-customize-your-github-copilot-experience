# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Padrões de Commits

Este projeto segue o padrão de Conventional Commits para manter um histórico de mudanças claro e consistente.

### Formato

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

### Tipos de Commit

- **feat**: Uma nova funcionalidade
- **fix**: Correção de bug
- **style**: Mudanças que não afetam o significado do código (espaços em branco, formatação, etc)
- **refactor**: Mudança de código que não corrige um bug nem adiciona uma funcionalidade
- **perf**: Mudança de código que melhora a performance
- **test**: Adição ou correção de testes
- **chore**: Mudanças no processo de build ou ferramentas auxiliares

### Exemplos

```
feat(assignments): adiciona tarefa de estruturas de dados

Cria nova tarefa sobre listas, pilhas e filas com exemplos práticos
e exercícios progressivos para iniciantes.

Closes #42
```

```
fix(css): corrige responsividade do header em mobile

O logo estava sobrepondo o título em telas menores que 768px.
Ajusta o layout para usar flexbox com wrap.
```

```
docs(readme): atualiza instruções de instalação

Adiciona pré-requisitos e passos detalhados para configuração
do ambiente de desenvolvimento.
```

```
refactor(js): simplifica lógica de carregamento de assignments

Remove código duplicado e consolida funções de fetch em uma única
função utilitária reutilizável.
```

```
chore: atualiza dependências do projeto
```