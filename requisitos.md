# Organizador Financeiro: Requisitos

**Versão:** 0.2 (rascunho para revisão)
**Baseado em:** `docs/01-visao/visao.md` (v0.4)

---

## Como ler este documento

- **RF** (requisito funcional): o que o sistema faz.
- **RNF** (requisito não funcional): como ele deve ser, sob quais condições.
- **RN** (regra de negócio): regra do domínio, que valeria mesmo numa planilha ou num caderno.
- **Prioridade** (método MoSCoW): **Must** = obrigatório; **Should** = importante, mas o produto funciona sem; **Could** = desejável.
- **Versão:** V1 = MVP; V2 = depois do MVP.
- Itens marcados com **(proposta)** são sugestões para você validar ou trocar.

---

## 1. Requisitos funcionais

### Compromissos e parcelamentos

| ID | Requisito | Prioridade | Versão |
|---|---|---|---|
| RF01 | O sistema deve permitir cadastrar um compromisso recorrente com descrição, valor e dia do mês. | Must | V1 |
| RF02 | O sistema deve permitir alterar ou encerrar um compromisso recorrente a partir de um mês, sem modificar meses já fechados. | Must | V1 |
| RF03 | O sistema deve permitir cadastrar um parcelamento com descrição, valor da parcela, número total de parcelas e mês da primeira parcela. | Must | V1 |
| RF04 | O sistema deve calcular e exibir, para qualquer mês, a parcela atual e o mês da última parcela de cada parcelamento. | Must | V1 |
| RF05 | O sistema deve incluir automaticamente, ao abrir um mês, os compromissos recorrentes e as parcelas devidas naquele mês. | Must | V1 |

### Entradas e resumo do mês

| ID | Requisito | Prioridade | Versão |
|---|---|---|---|
| RF06 | O sistema deve permitir registrar entradas em um mês, com descrição, valor e data, aceitando valores diferentes a cada mês. | Must | V1 |
| RF07 | O sistema deve calcular e exibir a sobra do mês, atualizada a cada alteração enquanto o mês estiver aberto. | Must | V1 |
| RF08 | O sistema deve exibir um resumo do mês com entradas, compromissos, sobra e situação de cada envelope. | Must | V1 |

### Envelopes

| ID | Requisito | Prioridade | Versão |
|---|---|---|---|
| RF09 | O sistema deve permitir criar, renomear e apagar envelopes. | Must | V1 |
| RF10 | O sistema deve permitir definir o percentual da sobra destinado a cada envelope. | Must | V1 |
| RF11 | O sistema deve dividir a sobra do mês entre os envelopes conforme os percentuais definidos. | Must | V1 |
| RF12 | O sistema deve permitir definir, para cada envelope, o destino da sobra no fechamento: manter no envelope ou mover para outro envelope. | Must | V1 |
| RF13 | O sistema deve permitir mover valor entre envelopes, registrando origem, destino, valor, data e motivo opcional. | Must | V1 |
| RF14 | O sistema deve calcular o saldo de cada envelope a partir dos seus movimentos. | Must | V1 |
| RF27 | O sistema deve permitir informar, ao começar a usar o aplicativo, o mês de início e o saldo inicial de cada envelope. | Must | V1 |

### Fechamento do mês

| ID | Requisito | Prioridade | Versão |
|---|---|---|---|
| RF15 | O sistema deve permitir informar, no fechamento, o total gasto de cada envelope. | Must | V1 |
| RF16 | O sistema deve avisar, no fechamento, quando um envelope estourou o limite e quando sobrou valor. | Must | V1 |
| RF17 | O sistema deve, quando um envelope estourou, perguntar de qual outro envelope sai o valor de cobertura e registrar esse movimento. | Must | V1 |
| RF18 | O sistema deve propor, no fechamento, as movimentações de sobra conforme a política de cada envelope e aplicá-las somente após confirmação do usuário. | Must | V1 |
| RF19 | O sistema deve permitir informar o total real que o usuário tem guardado, compará-lo com o total esperado e exibir a diferença. | Must | V1 |
| RF20 | O sistema deve fechar o mês após confirmação, gravando um registro permanente com entradas, compromissos, sobra, gasto e saldo de cada envelope e a diferença da conciliação. | Must | V1 |
| RF21 | O sistema deve listar os meses fechados e permitir consultar o fechamento de cada um. | Must | V1 |
| RF22 | O sistema deve permitir ajustar os percentuais dos envelopes para o mês seguinte durante o fechamento. | Should | V1 |

### Evoluções

| ID | Requisito | Prioridade | Versão |
|---|---|---|---|
| RF23 | O sistema deve permitir que um usuário convide outra pessoa, por e-mail, para participar da mesma conta compartilhada. | Should | V2 |
| RF24 | O sistema deve permitir lançar cada gasto durante o mês, escolhendo o envelope. | Should | V2 |
| RF25 | O sistema deve exibir uma retrospectiva com padrões entre meses (por exemplo, envelope que estourou vários meses seguidos). | Should | V2 |
| RF26 | O sistema deve permitir definir metas com valor, prazo e contribuição mensal recomendada. | Could | V2 |

---

## 2. Regras de negócio

| ID | Regra |
|---|---|
| RN01 | Um mês só pode ser fechado depois de todos os meses anteriores estarem fechados. |
| RN02 | Um mês fechado não pode ser alterado. |
| RN03 | Um envelope não pode ficar com saldo negativo sem que se indique de qual outro envelope sai a cobertura. |
| RN04 | Mover valor entre envelopes não altera a soma total dos saldos dos envelopes. |
| RN05 | A sobra do mês é igual ao total de entradas menos o total de compromissos do mês. |
| RN06 | A parcela atual de um parcelamento é calculada a partir do mês da primeira parcela; depois da última parcela, o parcelamento deixa de aparecer nos meses seguintes. |
| RN07 | Os percentuais de divisão da sobra entre os envelopes devem somar 100%. **(proposta)** |
| RN08 | A movimentação de sobra no fechamento é calculada sobre os saldos do fim do mês, sem encadeamento: a sobra movida do envelope A para o B não é movida de novo pela regra do B. **(proposta)** |
| RN09 | Se a sobra do mês for negativa (compromissos maiores que entradas), o sistema não a divide entre os envelopes e informa o valor do déficit. **(proposta)** |
| RN10 | Um envelope só pode ser apagado se o saldo for zero. **(proposta)** |
| RN11 | Alterar ou encerrar um compromisso, parcelamento ou envelope não modifica o histórico dos meses já fechados. |
| RN12 | Na conta compartilhada (V2), os dois participantes têm as mesmas permissões e veem todos os envelopes, inclusive os pessoais. **(proposta)** |
| RN13 | Um envelope estoura no fechamento quando o gasto informado do mês é maior que o seu saldo no início desse mês. **(proposta)** |
| RN14 | A sobra do mês é dividida entre os envelopes no fechamento e fica disponível a partir do mês seguinte. **(proposta)** |

---

## 3. Requisitos não funcionais

| ID | Categoria | Requisito | Prioridade |
|---|---|---|---|
| RNF01 | Desempenho | O resumo do mês deve abrir em até 2 segundos, com 36 meses de histórico. **(proposta)** | Should |
| RNF02 | Usabilidade | O fechamento de um mês deve poder ser concluído em até 10 minutos. **(proposta, vem do critério de sucesso da visão)** | Should |
| RNF03 | Precisão | Todos os cálculos monetários devem ser exatos ao centavo, sem erros de arredondamento. | Must |
| RNF04 | Confiabilidade | Dados já registrados não podem ser perdidos caso o aplicativo seja fechado de forma inesperada. | Must |
| RNF05 | Privacidade | Na V1, os dados financeiros ficam apenas no dispositivo do usuário e não são enviados a terceiros. | Must |
| RNF06 | Portabilidade | O sistema deve funcionar no computador do usuário. A necessidade de funcionar também no celular será definida na etapa de arquitetura. | Must |
| RNF07 | Localização | A interface deve estar em português e os valores devem ser exibidos em euro (€). | Must |

---

## 4. Para você validar

1. Os itens marcados **(proposta)**, principalmente RN07 a RN10, RN13 e RN14 (casos de borda que inventei para não deixar o sistema sem resposta) e os números de RNF01 e RNF02.
2. Se algum RF Must da V1 pode virar V2 para deixar o MVP menor.
3. RNF06: no começo, o app precisa rodar no celular ou só no computador?
