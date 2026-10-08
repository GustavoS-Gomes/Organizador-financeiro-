# Organizador Financeiro: Visão

**Versão:** 0.4 (rascunho para revisão)
**Fase do projeto:** Visão e escopo

---

## Declaração de visão

Para pessoas e casais que querem organizar as finanças sem depender de planilhas, o **Organizador Financeiro** é um aplicativo de planejamento financeiro pessoal que gera o resumo do mês, divide a sobra em envelopes e fecha cada mês com conferência. Diferente de uma planilha ou de um aplicativo de banco, ele calcula tudo o que pode ser calculado, congela o histórico e ajuda a entender para onde o dinheiro vai, sem nunca movimentar dinheiro.

> **"Mais do que controlar seu dinheiro. Entenda sua vida financeira."**

## Origem do projeto

O projeto nasceu de uma planilha mensal usada por um casal para organizar as contas. A planilha é a **inspiração** e serve como exemplo de uso real (compromissos fixos, parcelas, divisão da sobra em partes). Ela não é a base do app: o app é um **upgrade** dessa ideia, e não uma cópia dela.

## Problema

Organizar as finanças pessoais é difícil por razões que não dependem da ferramenta usada:

- **Não é claro para onde o dinheiro vai**, principalmente nos gastos variáveis do dia a dia.
- **Compromissos de longo prazo são fáceis de perder de vista.** Parcelas e assinaturas se acumulam, e esquecer quando terminam esconde dinheiro que poderia ser liberado.
- **Com renda variável, é difícil saber quanto sobra** e quanto realmente se pode gastar no mês.
- **Guardar e dividir o dinheiro exige disciplina.** Separar valores para poupar, para lazer e para cada pessoa só funciona se as regras forem seguidas todo mês.
- **Em casal ou família, várias pessoas usam o mesmo dinheiro** e falta uma visão compartilhada do que está acontecendo.
- **Sem acompanhar mês a mês, não se aprende com os erros e acertos.** Falta uma retrospectiva que mostre o que mudou e o que precisa ser ajustado.

**Causa raiz:** manter o controle depende de trabalho manual e constante. Cadernos e planilhas resolvem parte do problema, mas exigem que a pessoa monte e confira tudo a cada mês, e esse esforço faz muita gente desistir.

## Para quem

- **Primeiro público:** um casal que usa uma única conta bancária conjunta e tem renda variável.
- **Público futuro:** qualquer pessoa que quer organizar a vida financeira sem gostar de planilhas, desde que tenha o mínimo de organização para saber onde guarda o próprio dinheiro.

## Objetivos e critérios de sucesso

*(propostas a validar)*

- Fechar um mês em poucos minutos (meta inicial: até 10 minutos).
- Substituir a planilha por pelo menos 3 meses seguidos.
- Nenhum valor calculável (parcela atual, sobra, saldo de envelope) digitado à mão.
- Em todo fechamento, o total real confere com o total esperado, ou a diferença fica visível e explicada.

## Escopo por versão

**Versão 1 (MVP):**
- Um dispositivo, uso do casal sem login.
- Compromissos recorrentes e parcelamentos com parcela atual calculada.
- Entradas do mês (renda variável).
- Envelopes criados pelo usuário, com percentuais para dividir a sobra.
- Destino da sobra de cada envelope, escolhido pelo usuário (manter ou mover para outro envelope).
- Movimentos entre envelopes, com origem e destino.
- Resumo do mês gerado automaticamente.
- Fechamento mensal em ordem, com conciliação e histórico congelado.
- Gastos variáveis informados por envelope no fechamento, com aviso quando um envelope estourou ou sobrou valor.

**Versão 2:**
- Convite por e-mail e conta compartilhada entre dois logins, em dois dispositivos.
- Lançamento de cada gasto durante o mês.
- Retrospectiva com insights ("lazer estourou 3 meses seguidos").
- Metas com prazo e contribuição mensal recomendada.

**Ideias futuras:** importação de extrato, assistente que responde com base nos dados do usuário.

## Princípios de projeto

- **Calcular em vez de guardar.** O que pode ser derivado de outros dados (parcela atual, sobra, saldo de cada envelope) é calculado, não digitado.
- **Mês aberto calcula ao vivo; mês fechado congela.** Depois de fechado, o resultado de um mês não muda, mesmo que as regras mudem depois.
- **Fechamento em ordem.** Um mês só fecha depois do anterior, porque os valores acumulados dependem dos meses passados.
- **O dinheiro não aparece do nada.** Toda mudança de saldo entre envelopes é um movimento com origem e destino.
- **O app registra; não movimenta dinheiro.** Onde o dinheiro fica guardado de verdade (gaveta, banco, poupança) é responsabilidade do usuário e indiferente para o app.
- **Foco.** Antes de incluir qualquer funcionalidade, perguntar: *isso ajuda o usuário a entender ou melhorar sua vida financeira?*

## Premissas e restrições

**Premissas**
- O usuário tem o mínimo de organização para saber onde o dinheiro está guardado.
- O usuário consegue informar as entradas reais e o total que tem no fechamento do mês.

**Restrições**
- Projeto individual e feito em tempo limitado, então o escopo precisa ser pequeno e entregável em etapas.
- Custo baixo ou zero.
- Os dados são financeiros e sensíveis: segurança e privacidade pesam em qualquer decisão técnica.

## Riscos

| Risco | Como reduzir |
|---|---|
| O uso exigir tanto esforço quanto a planilha e o usuário desistir | Gerar tudo o que for possível automaticamente; medir o tempo de fechamento |
| O escopo crescer antes da primeira versão funcionar | Manter o MVP acima e adiar o resto para as versões seguintes |
| Dados financeiros expostos | Não guardar dados reais no repositório; decidir a proteção na etapa de arquitetura |
| Regras de envelopes ficarem complicadas demais | Poucas opções na versão 1 (manter ou mover) |

## O que fica de fora

- Conta bancária, transferências, PIX, cartão, empréstimos, financiamentos e pagamentos. O app não é um banco.
- Investimentos como função principal.
- Importação automática de extrato bancário (possível evolução futura).
- Controle de em qual conta ou lugar o dinheiro está (no máximo, uma anotação de texto livre e opcional).

## Decisões tomadas

- A sobra de cada envelope tem um destino escolhido pelo usuário: manter no envelope ou mover para outro. **Padrão:** manter. O app propõe a movimentação no fechamento e o usuário confirma.
- Se um envelope estoura, o app pergunta de qual outro envelope sai o dinheiro e registra a origem.
- O acesso do casal será por **convite por e-mail a uma conta compartilhada**, com dois logins associados. Entra na versão 2; o modelo de dados já separa usuário e conta para isso.
- Na conta compartilhada, os dois participantes têm as mesmas permissões e veem todos os envelopes, inclusive os pessoais *(padrão proposto, pode mudar)*.
- Onde o dinheiro está guardado de verdade é indiferente para o app.
- **Gastos variáveis na versão 1:** o usuário informa o total gasto de cada envelope no fechamento, e o app avisa quando um envelope estourou o limite ou quando sobrou valor. O lançamento de cada gasto durante o mês fica para a versão 2.

## Decisões em aberto

Nenhuma pendente nesta fase. A **tecnologia** não é decisão de visão: será tomada na etapa de arquitetura, depois dos requisitos e da modelagem.

## Glossário

- **Compromisso:** gasto que se repete e é conhecido de antemão (aluguel, internet, assinaturas).
- **Parcelamento:** dívida com número fixo de parcelas, que começa em uma data e termina em outra.
- **Sobra:** entradas do mês menos compromissos.
- **Envelope:** parte da sobra reservada para um fim (lazer, viagem, guardar...). É um registro lógico, não uma conta bancária.
- **Movimento:** transferência de valor entre envelopes, com origem e destino.
- **Fechamento:** conferência final do mês, depois da qual ele deixa de poder ser alterado.
- **Conciliação:** comparar o total que o app espera com o total real que o usuário tem.
