# Organizador Financeiro: Visão

**Versão:** 0.5 (rascunho para revisão)  
**Fase do projeto:** Visão e escopo  
**Atualização:** 23/11/2026 — carteiras individuais, carteira compartilhada e contribuições

---

## Declaração de visão

Para pessoas e casais que querem organizar as finanças sem depender de planilhas, o **Organizador Financeiro** é um aplicativo de planejamento financeiro pessoal que gera o resumo do mês, divide a sobra em envelopes e fecha cada mês com conferência. Diferente de uma planilha ou de um aplicativo de banco, ele calcula tudo o que pode ser calculado, congela o histórico e ajuda a entender para onde o dinheiro vai, sem nunca movimentar dinheiro de verdade.

> **"Mais do que controlar seu dinheiro. Entenda sua vida financeira."**

## Origem do projeto

O projeto nasceu de uma planilha mensal usada por um casal para organizar as contas. A planilha é a **inspiração** e serve como exemplo de uso real (compromissos fixos, parcelas, divisão da sobra em partes). Ela não é a base do app: o app é um **upgrade** dessa ideia, e não uma cópia dela.

## Problema

Organizar as finanças pessoais é difícil por razões que não dependem da ferramenta usada:

- **Não é claro para onde o dinheiro vai**, principalmente nos gastos variáveis do dia a dia.
- **Compromissos de longo prazo são fáceis de perder de vista.** Parcelas e assinaturas se acumulam, e esquecer quando terminam esconde dinheiro que poderia ser liberado.
- **Com renda variável, é difícil saber quanto sobra** e quanto realmente se pode gastar no mês.
- **Guardar e dividir o dinheiro exige disciplina.** Separar valores para poupar, para lazer e para cada pessoa só funciona se as regras forem seguidas todo mês.
- **Em casal ou família, várias pessoas usam o mesmo dinheiro** e falta uma visão compartilhada do que está acontecendo, sem necessariamente abrir mão da privacidade individual.
- **Sem acompanhar mês a mês, não se aprende com os erros e acertos.** Falta uma retrospectiva que mostre o que mudou e o que precisa ser ajustado.

**Causa raiz:** manter o controle depende de trabalho manual e constante. Cadernos e planilhas resolvem parte do problema, mas exigem que a pessoa monte e confira tudo a cada mês, e esse esforço faz muita gente desistir.

## Para quem

- **Primeiro cenário validado (V1):** um casal que organiza a vida financeira com uma planilha e quer substituir o trabalho manual por um fluxo local de planejamento e fechamento. Na V1 o aplicativo usa uma única conta de planejamento, sem identidades individuais.
- **Segundo cenário (V2):** duas pessoas com rendas e despesas próprias, que querem manter carteiras individuais privadas e participar de uma carteira compartilhada para as despesas e metas do casal.
- **Público futuro:** qualquer pessoa que quer organizar a vida financeira sem gostar de planilhas, desde que tenha o mínimo de organização para saber onde guarda o próprio dinheiro.

## Objetivos e critérios de sucesso

*(propostas a validar)*

- Fechar um mês em poucos minutos (meta inicial: até 10 minutos).
- Substituir a planilha por pelo menos 3 meses seguidos.
- Nenhum valor calculável (parcela atual, sobra, saldo de envelope) digitado à mão.
- Em todo fechamento, o total real confere com o total esperado, ou a diferença fica visível e explicada.
- Na V2, conseguir distinguir sem ambiguidade **o dinheiro individual**, **o dinheiro compartilhado** e **o valor apenas planejado para contribuição**.

## Escopo por versão

**Versão 1 (MVP):**
- Um dispositivo, uso do casal sem login e uma única conta local de planejamento.
- Compromissos recorrentes e parcelamentos com parcela atual calculada.
- Entradas do mês (renda variável).
- Envelopes criados pelo usuário, com percentuais para dividir a sobra.
- Destino da sobra de cada envelope, escolhido pelo usuário (manter ou mover para outro envelope).
- Movimentos entre envelopes, com origem e destino.
- Resumo do mês gerado automaticamente.
- Fechamento mensal em ordem, com conciliação e histórico congelado.
- Gastos variáveis informados por envelope no fechamento, com aviso quando um envelope estourou ou sobrou valor.

**Versão 2:**
- Cadastro/login individual e convite por e-mail, com aceite do convite em outro dispositivo.
- Cada usuário possui uma **carteira individual privada** e pode participar de **carteira compartilhada** (inicialmente com duas pessoas).
- Informações individuais não são automaticamente exibidas na carteira do casal; somente dados compartilhados ou explicitamente autorizados são acessíveis aos participantes.
- Planejamento da contribuição mensal por três métodos: **igualitário**, **proporcional à renda de referência** e **flexível**.
- Contribuições **planejadas** separadas de contribuições **efetivamente registradas**. O aplicativo não realiza transferências bancárias.
- Lançamento de cada gasto durante o mês.
- Retrospectiva com insights ("lazer estourou 3 meses seguidos").
- Metas com prazo e contribuição mensal recomendada, individuais ou compartilhadas.
- Possibilidade de moeda de referência por carteira (EUR, BRL, USD); conversão automática não faz parte da V2 inicial.

**Ideias futuras:** importação de extrato, assistente que responde com base nos dados do usuário, notificações de vencimento e suporte a grupos com mais de dois participantes.

## Funcionamento das carteiras (decisão V2)

1. Uma pessoa cria uma conta de usuário e tem uma **carteira individual**. Pode utilizá-la sem convidar ninguém.
2. Duas pessoas podem criar ou aceitar convite para uma **carteira compartilhada**, que mantém seus próprios compromissos, envelopes, metas e fechamento.
3. O casal define uma **meta de contribuição mensal** que pode incluir despesas conjuntas previstas e uma reserva planejada.
4. Escolhe o método de divisão: igualitário, proporcional à renda de referência informada privadamente ou valores livres por participante.
5. O sistema **calcula uma proposta** para aquele mês. Proposta não altera saldos.
6. A contribuição passa a ser considerada realizada apenas quando é **registrada/confirmada** pelo participante autorizado. O aplicativo registra uma transferência **virtual**, com origem e destino; não envia dinheiro a bancos.
7. O planejamento da carteira compartilhada passa a considerar as contribuições **realizadas** como recursos internos recebidos. No consolidado do casal, a transferência interna não pode ser contada como renda nova.
8. Ambos acompanham os compromissos e envelopes da carteira compartilhada; rendas, envelopes e despesas da carteira individual do outro continuam privados.

**Exemplo:** a meta conjunta é 1.400 €. Com rendas de referência de 2.000 € e 1.600 €, a divisão igualitária sugere 700 €/700 €; a proporcional sugere 777,78 €/622,22 €; a flexível pode ser combinada como 800 €/600 €. Esses são valores *previstos*, não contribuições realizadas.

**Privacidade importante:** no método proporcional, exibir proporções e contribuições pode permitir inferir dados sobre a renda da outra pessoa. A interface deve informar essa consequência antes de ativar o método.

## Princípios de projeto

- **Calcular em vez de guardar.** O que pode ser derivado de outros dados (parcela atual, sobra, saldo de cada envelope) é calculado, não digitado.
- **Mês aberto calcula ao vivo; mês fechado congela.** Depois de fechado, o resultado de um mês não muda, mesmo que as regras mudem depois.
- **Fechamento em ordem.** Um mês só fecha depois do anterior, porque os valores acumulados dependem dos meses passados.
- **O dinheiro não aparece do nada.** Toda mudança de saldo entre envelopes é um movimento com origem e destino; transferências entre carteiras têm origem e destino próprios.
- **Planejar não é realizar.** Uma contribuição prevista ou uma sugestão de distribuição nunca deve ser confundida com dinheiro já movimentado ou reservado.
- **Privacidade por padrão.** Participar da carteira conjunta não dá acesso à carteira individual da outra pessoa.
- **O app registra; não movimenta dinheiro.** Onde o dinheiro fica guardado de verdade (gaveta, banco, poupança) é responsabilidade do usuário e indiferente para o app.
- **Foco.** Antes de incluir qualquer funcionalidade, perguntar: *isso ajuda o usuário a entender ou melhorar sua vida financeira?*

## Premissas e restrições

**Premissas**
- O usuário tem o mínimo de organização para saber onde o dinheiro está guardado.
- O usuário consegue informar as entradas reais e o total que tem no fechamento do mês.
- Na V2, participantes registram contribuições de forma consciente; não existe conexão bancária automática.

**Restrições**
- Projeto individual e feito em tempo limitado, então o escopo precisa ser pequeno e entregável em etapas.
- Custo baixo ou zero.
- Os dados são financeiros e sensíveis: segurança e privacidade pesam em qualquer decisão técnica.

## Riscos

| Risco | Como reduzir |
|---|---|
| O uso exigir tanto esforço quanto a planilha e o usuário desistir | Gerar tudo o que for possível automaticamente; medir o tempo de fechamento |
| O escopo crescer antes da primeira versão funcionar | Manter o MVP local e adiar a colaboração real para V2 |
| Dados financeiros expostos | Não guardar dados reais no repositório; autenticação, autorização e isolamento por carteira na V2 |
| Regras de envelopes ficarem complicadas demais | Poucas opções na versão 1 (manter ou mover) |
| Contribuição planejada ser confundida com dinheiro real | Exibir previsto/realizado separadamente e exigir confirmação |
| Contar transferências internas duas vezes | Rastrear origem e destino e excluir transferência interna de renda externa consolidada |
| Divisão proporcional revelar renda privada por inferência | Alertar sobre a informação dedutível e nunca exibir renda absoluta do outro sem consentimento |

## O que fica de fora

- Conta bancária real, transferências **bancárias**, PIX, cartão, empréstimos, financiamentos e pagamentos. O app não é um banco. **Transferências virtuais entre carteiras** são apenas registros de organização financeira.
- Investimentos como função principal.
- Importação automática de extrato bancário (possível evolução futura).
- Controle de em qual conta bancária ou lugar físico o dinheiro está (no máximo, uma anotação de texto livre e opcional).

## Decisões tomadas

- A sobra de cada envelope tem um destino escolhido pelo usuário: manter no envelope ou mover para outro. **Padrão:** manter. O app propõe a movimentação no fechamento e o usuário confirma.
- Se um envelope estoura, o app pergunta de qual outro envelope sai o dinheiro e registra a origem.
- O MVP continua **local, sem login e com uma única conta de planejamento**; não será refeito como aplicativo multiusuário antes de funcionar.
- Na V2, o acesso à carteira compartilhada será por **convite por e-mail**, com dois logins associados inicialmente.
- Na V2, **cada pessoa tem uma carteira individual privada**; a carteira compartilhada só exibe seus próprios dados e contribuições referentes a ela.
- Na V2, são aceitos os métodos de contribuição **igualitário, proporcional e flexível**. A escolha vale para o planejamento de cada mês, preservando os meses fechados.
- Participantes da carteira compartilhada têm, inicialmente, permissões equivalentes dentro dela; esse acesso não inclui dados pessoais da carteira individual do outro.
- Onde o dinheiro está guardado de verdade é indiferente para o app.
- **Gastos variáveis na V1:** o usuário informa o total gasto de cada envelope no fechamento, e o app avisa quando um envelope estourou ou sobrou valor. O lançamento de cada gasto durante o mês fica para a V2.

## Decisões em aberto

- **Migração V1 → V2:** como vincular dados da conta local aos novos usuários sem atribuir históricos individuais incorretamente.
- **Conciliação entre carteiras (V2):** como evitar dupla contagem entre saldos de carteiras, saldos de envelopes e registros de contribuição.
- **Critérios de autorização da V2:** revisão detalhada de edição, exclusão, saída do grupo e acesso ao histórico.
- **Tecnologia:** será escolhida na etapa de arquitetura, depois dos requisitos e da modelagem.

## Glossário

- **Compromisso:** gasto que se repete e é conhecido de antemão (aluguel, internet, assinaturas).
- **Parcelamento:** dívida com número fixo de parcelas, que começa em uma data e termina em outra.
- **Sobra:** na V1, entradas do mês menos compromissos. Não é automaticamente o saldo bancário disponível.
- **Envelope:** parte da sobra reservada para um fim (lazer, viagem, guardar...). É um registro lógico, não uma conta bancária.
- **Movimento:** transferência de valor entre envelopes, com origem e destino, ou entrada/saída lógica de valor de um envelope.
- **Carteira individual:** área financeira privada de uma pessoa (V2).
- **Carteira compartilhada:** área financeira acessível aos participantes convidados (V2).
- **Meta de contribuição:** total planejado para sustentar as despesas e reservas de uma carteira compartilhada em um mês.
- **Contribuição prevista:** quanto se espera que uma pessoa destine à carteira compartilhada; não modifica saldos.
- **Contribuição realizada:** transferência virtual registrada entre as carteiras, sem movimentação bancária.
- **Fechamento:** conferência final do mês, depois da qual ele deixa de poder ser alterado.
- **Conciliação:** comparar o total que o app espera com o total real que o usuário tem.
