# Roadmap

## v1.0 - MVP (entrega atual)

- [x] Vetor de 8 posições controlando o estado de cada box (`0` vazio / `1` ocupado).
- [x] Toggle de box: clique em vazio ocupa e incrementa o contador; clique em
      ocupado libera sem alterar o contador.
- [x] Indicadores em tempo real: boxes ocupados e total de carros atendidos.
- [x] Botão "Encerrar expediente" com confirmação e resumo final.
- [x] Interface em `tkinter`/`ttk`, estilo nativo, sem uso de classes
      (paradigma procedural puro).
- [x] Validações e mensagens via `messagebox` para ações inválidas.

## v1.1 - Melhorias de interface (dentro do escopo)

- [ ] Indicador visual de "pico de ocupação" do expediente (maior número de
      boxes ocupados simultaneamente).
- [ ] Botão "Reiniciar expediente" para zerar o vetor e o contador sem fechar
      o programa (útil para testes em sala/apresentação).
- [ ] Ajustes de responsividade da janela (redimensionamento).

## v1.2 - Qualidade e organização do código

- [ ] Separar constantes de estilo (`cores`, fontes) em uma seção única de
      configuração visual.
- [ ] Cobrir a lógica de `contarOcupados()` e `alternarBox()` com testes
      simples (ex.: `unittest`), mantendo o restante do app procedural.

## Fora do roadmap (fora do escopo do projeto)

Persistência em banco de dados, autenticação/login, cadastro de
clientes/funcionários/veículos, controle financeiro, estoque, ordens de
serviço, agendamento, histórico entre expedientes e integrações externas —
esses itens não fazem parte do cenário proposto para esta atividade.
