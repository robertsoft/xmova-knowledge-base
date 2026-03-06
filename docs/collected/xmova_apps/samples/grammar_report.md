# Grammar inference report for .xmv samples

Files analyzed: 20

## Top tokens

- fieldlabel: 321

- entitylabel: 88

- de: 82

- boletim: 73

- os: 61

- da: 49

- crudoptionsactionlabel: 47

- sub: 42

- foto: 39

- apontamentosubosmanut: 31

- do: 30

- data: 29

- ponto: 27

- motivo: 27

- apontamento: 26

- apontamentosubosdesmobilizacao: 26

- custom: 24

- booleaninputscreenyesactionlabel: 24

- apontamentotermocautelar: 24

- registrar: 23

- hardware: 23

- para: 22

- chamado: 22

- apontamentosubosinstall: 22

- apontar: 21

- return: 21

- rio: 20

- digo: 20

- descri: 20

- atividade: 20

- observa: 20

- tipo: 20

- booleaninputscreennoactionlabel: 20

- deseja: 19

- assinatura: 19

- despesa: 19

- descricao: 19

- if: 19

- resumo: 18

- registraobs: 18


## Top line starts (likely keywords)

- fieldlabel: 321

- entitylabel: 88

- crudoptionsactionlabel: 47

- custom: 24

- booleaninputscreenyesactionlabel: 24

- apontamento: 21

- return: 21

- booleaninputscreennoactionlabel: 20

- if: 19

- recordlist: 11

- recorddetail: 11

- events: 11

- tipo: 10

- 1: 10

- 2: 10

- views: 10

- beforeclose: 10

- beforeinit: 9

- booleaninputscreenbackactionlabel: 8

- boletim: 7

- resumo: 7

- else: 6

- datalibaux: 6

- menu: 5

- cliente: 4

- long: 4

- defini: 3

- crudcreateconfirmmessage: 3

- 3: 3

- tipoadiantamento: 3

- _resumoapontamento: 3

- _resumototal: 3

- _resumoapontamentosemanal: 3

- _resumobancohoras: 3

- _resumopontopainel: 3

- _resumoespelhoponto: 3

- _resumolapsossemanal: 3

- _resumoespelholapso: 3

- _resumobnc: 3

- _resumotermocautelar: 3


## Top normalized line patterns

- (23) `/<PATH>`

- (11) `events`

- (10) `views`

- (10) `beforeClose`

- (9) `beforeInit`

- (7) `if menuAdiantamento.flagPrimeiroApontamento == <NUM>`

- (6) `else`

- (5) `return false`

- (5) `dataLibAux = addDate dataLibAux <NUM> @h`

- (5) `if diaSemana == <NUM>`

- (4) `return true`

- (2) `/<PATH> OS`

- (2) `/<PATH> TERMO CAUTELAR`

- (2) `/<PATH> DESPESA`

- (2) `/<PATH> INSTALACAO`

- (2) `sync`

- (2) `recordDetail fields=DATA_REAL,horarioPonto,STATUS,MOTIVO labels`

- (2) `if FALTOU_HORAS == <NUM>`

- (2) `id inc`

- (2) `boletim Boletim hide`

- (2) `seqFuncionario SeqFuncionario hide`

- (2) `flagOnline int notFill onlineFlagCreate`

- (2) `return generateUuid`

- (1) `/<PATH> que podem ser definidas para serem apresentadas no Mobile`

- (1) `custom.msgCustomConfirmaConfig = Funcionário: %nomeFuncionario\n\nDeseja Confirmar a Configuração?`

- (1) `custom.msgCustomConfirmaRegistroRefeicaoI = Deseja Registrar o ponto de inicio de refeição?\n\nData do Ponto: %data`

- (1) `custom.msgCustomConfirmaPonto = Confirmar o Registro de Ponto?\n\nData do Ponto: %data`

- (1) `custom.msgCustomConfirmaPonto2 = Confirmar o Registro de Ponto?\n\nData do Ponto: %data\n\nO tempo mínimo de <NUM> minutos entre um ponto e outro não foi atingido\n\nO intervalo entre esse registro e o anterior será de: %duracao`

- (1) `custom.msgBloqueiaFim = Para encerrar a OS é necessário a assinatura do Cliente`

- (1) `custom.msgInterrupcao = Deslocamento interrompido pelo motivo <%motivo>.\nAo finalizar interrupção pressione "<STR>" para retomar o deslocamento.`

- (1) `custom.deslocamentoKmFinalMenorKmInicial = Km Final informado (%kmFinal) menor que o KM Inicial (%kmInicial). Confirma?`

- (1) `custom.deslocamentoKmAtualMenorKmInicial = Km Atual informado (%kmAtual) menor que o KM Inicial (%kmInicial). Confirma?`

- (1) `custom.msgBloqueiaHorimetroMarte = Necessária pelo menos <NUM> foto para prosseguir.`

- (1) `custom.msgBloqueiaFimMarte = Para pausar<PATH> a OS é necessário finalizar a instalação do Marte`

- (1) `custom.msgHodometroInvalido = Hodômetro inválido!`

- (1) `custom.msgManutSucesso = Manutenção Realizada Com Sucesso!`

- (1) `custom.msgCustomInstSucesso = Instalação Realizada com Sucesso!`

- (1) `custom.msgCustomDesmSucesso = Desmobilização Realizada com Sucesso!`

- (1) `custom.msgTermoCautelarSucesso = Termo Cautelar realizado com sucesso!`

- (1) `custom.msgNotificarNenhumRegistro = Tempo de boletim iniciado sem Registro de ponto excedido. Por favor, registre o ponto!`


## Top token bigrams

- sub os: 42

- crudoptionsactionlabel boletim: 39

- n o: 37

- fieldlabel apontamentotermocautelar: 22

- c digo: 20

- descri o: 20

- observa o: 20

- fieldlabel apontamentosubosmanut: 18

- descricao descri: 17

- instala o: 16

- motivo da: 16

- fieldlabel apontamentosubosdesmobilizacao: 15

- codigo c: 13

- observacao observa: 13

- fieldlabel hardware: 13

- fieldlabel apontamentosubosinstall: 13

- de ponto: 12

- lista de: 12

- motivodesconectado motivo: 12

- da desconex: 12

- desconex o: 12

- fieldlabel apontamentodespesa: 11

- recordlist getrecords: 11

- recorddetail fields: 11

- fieldlabel apontamentobnc: 10

- sa da: 10

- fieldlabel resumoespelhoponto: 10

- tablelayout title: 10

- select from: 10

- o do: 9

- fieldlabel authinput: 9

- chamado chamado: 9

- fieldlabel resumotermocautelar: 9

- desmobiliza o: 8

- de presen: 8

- presen a: 8

- foto foto: 8

- fieldlabel resumopontopainel: 8

- o de: 7

- servi o: 7


## Observations and next steps

- Tokens and line-starts suggest a keyword-driven DSL (many uppercase identifiers).

- Normalized line patterns provide candidate production rules (convert placeholders `<STR>`/`<NUM>` to terminals).

- Pr�ximo: mapear padr�es comuns para regras BNF e tentar parse com um parser gerado (e.g., lark).
