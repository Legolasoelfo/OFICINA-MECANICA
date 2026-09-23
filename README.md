# Oficina Mecânica - Controle de Ocupação de Boxes

Sistema desktop em **Python + Tkinter** para controlar a ocupação dos 8
boxes/elevadores de uma oficina mecânica durante o expediente, e contabilizar
o total de carros efetivamente atendidos no dia.

Projeto acadêmico desenvolvido para a disciplina de lógica de programação,
com auxílio de modelos de IA (Gemini / OpenRouter) integrados ao VS Code.

## Equipe

- Victor Silva Granja
- Davi da Silva Fonseca Vilete
- Eurico

## Cenário / Regras de negócio

- A oficina possui **8 boxes fixos**, representados internamente por um vetor
  de 8 posições, onde cada posição guarda `0` (vazio) ou `1` (ocupado).
- Todos os boxes começam **vazios** no início do expediente.
- Ao clicar em um box **vazio**, ele passa a **ocupado** e o contador de
  carros atendidos é incrementado **nesse momento** (na ocupação, não na
  liberação).
- Ao clicar em um box **ocupado**, ele volta a **vazio**, sem alterar o
  contador de atendidos.
- O botão **"Encerrar expediente"** bloqueia novas alterações nos boxes e
  exibe um resumo com o total de carros atendidos no dia.

### Fora do escopo (intencionalmente)

Cadastro de clientes/funcionários/veículos, controle financeiro, estoque,
ordens de serviço, agendamento, login, banco de dados, histórico de dias
anteriores, pagamentos e integrações externas.

## Interface

- Identificação do sistema no topo da janela.
- 8 boxes exibidos como botões coloridos (verde = livre, vermelho = ocupado).
- Indicadores de boxes ocupados e de total de carros atendidos, atualizados
  imediatamente após cada ação.
- Mensagens claras via `messagebox` em ações inválidas (ex.: tentar alterar
  um box após o expediente encerrado).

## Paradigma de programação

O código segue **estritamente o paradigma procedural**: apenas funções e
variáveis (locais/globais), sem uso da palavra-chave `class`. O uso de
funções nativas de alto nível (como `sum()`) é permitido e está sempre
comentado, explicando o que a função faz por baixo dos panos e qual
algoritmo tradicional ela substitui.

## Como executar

Pré-requisitos: Python 3.x (o módulo `tkinter` já vem incluso na instalação
padrão do Python na maioria dos sistemas).

```bash
python main.py
```

## Estrutura do projeto

```
oficina-mecanica/
├── MEMORY.md            # Memória de trabalho e contexto arquitetural
├── ROADMAP.md           # Planejamento de releases e novas funcionalidades
├── README.md            # Este arquivo
├── main.py              # Código-fonte principal (procedural + Tkinter)
└── ia/
    └── Prompt Python.md # Prompt usado para orientar a IA na construção do código
```

## Documentação relacionada

- [ROADMAP.md](./ROADMAP.md) - planejamento de versões e melhorias futuras.
- [MEMORY.md](./MEMORY.md) - contexto arquitetural e decisões de projeto.
- [ia/Prompt Python.md](./ia/Prompt%20Python.md) - especificação usada para
  gerar o código com auxílio de IA.
