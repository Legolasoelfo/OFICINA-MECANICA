# MEMORY - Contexto de trabalho e decisões arquiteturais

## Domínio da aplicação

Sistema de controle de ocupação dos **8 boxes/elevadores** de uma oficina
mecânica durante o expediente, com contabilização do total de carros
efetivamente atendidos no dia. Não há persistência entre expedientes: cada
execução do programa representa um único dia de trabalho.

## Estruturas de dados

- `vetorBoxes`: lista de 8 posições (`int`), uma por box. Valores possíveis:
  - `0` (`BOX_VAZIO`) - box livre;
  - `1` (`BOX_OCUPADO`) - box em uso.
  Essa lista é a fonte única de verdade sobre o estado dos boxes e participa
  diretamente da lógica (contagem via `sum()`, atualização de cada botão em
  um laço `for`).
- `totalCarrosAtendidos`: inteiro, incrementado **apenas** no instante em que
  um box passa de vazio para ocupado.
- `expedienteEncerrado`: booleano que trava novas alterações após o
  encerramento do expediente.

## Regra de negócio formal (Dado/Quando/Então)

- **Dado** um box vazio, **quando** o usuário clica nele, **então** o box
  passa a ocupado e o contador de atendidos é incrementado.
- **Dado** um box ocupado, **quando** o usuário clica nele, **então** o box
  volta a vazio, sem alterar o contador.
- **Dado** o expediente encerrado, **quando** o usuário tenta alterar
  qualquer box, **então** o sistema exibe um aviso e ignora a ação.

## Decisões arquiteturais

- **Paradigma procedural puro**: proibido usar `class`; todo o estado vive em
  variáveis globais e é manipulado por funções. Essa é uma restrição
  pedagógica da disciplina, não uma limitação técnica.
- **Uso de atalhos nativos permitido, mas sempre comentado**: por exemplo,
  `sum(vetorBoxes)` substitui um laço manual de acumulação, e isso é
  explicado em comentário no código, junto ao ponto de uso.
- **Três estruturas de Böhm-Jacopini evidenciadas no código**:
  - Sequência: montagem da interface (`construirInterface`) e fluxo principal
    (`if __name__ == "__main__"`).
  - Seleção: `if/else` em `alternarBox()`, `atualizarInterface()` e
    `encerrarExpediente()`.
  - Repetição: laços `for` na criação dos 8 botões e na atualização de cada
    um deles conforme `vetorBoxes`.
- **Interface "estilo Windows"**: uso de `ttk.Style` com tema `clam`, botões
  coloridos (verde/vermelho) para indicar o estado de cada box, em vez de
  texto puro em console.
- **Fechamento de closures em loop**: o `command` de cada `ttk.Button` usa
  `lambda indice=i: alternarBox(indice)` para capturar o valor de `i` no
  momento da criação do botão, evitando que todos os botões acabem chamando
  `alternarBox()` com o último índice do laço.

## Escopo explicitamente excluído

Cadastro de clientes/funcionários/veículos, controle financeiro, estoque,
ordens de serviço, agendamento, login, banco de dados, histórico entre
expedientes, pagamentos e integrações externas. Qualquer sugestão de IA que
introduza esses itens deve ser descartada nesta entrega.

## Ferramentas de IA usadas na construção

- VS Code com modelos de IA habilitados via API do **Gemini** e do
  **OpenRouter**.
- Prompt-base em [`ia/Prompt Python.md`](./ia/Prompt%20Python.md), que define
  as restrições pedagógicas (paradigma procedural, comentários obrigatórios
  sobre atalhos nativos, estruturas de Böhm-Jacopini) e o contexto do domínio
  descrito acima.
