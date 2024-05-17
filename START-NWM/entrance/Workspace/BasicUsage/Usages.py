from __future__ import annotations
from entrance import funcionamento_basico


if funcionamento_basico is True:
	lideres = {'tsuki': '≠±¬°°≈‹Susumo Tsuki', 'inu': 'Meeh Inu', 'ivory': '~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory',
			   'zuky': '~‹‹≈¤°°ຊ€Yu Zuky', 'uzuki': 'None', 'shiro': 'None', 'akaguma': '~-ຊ±¬°Chaos Akaguma',
			   'terepasu': 'None', 'yoso': 'None', 'kokyu': 'None', 'kieta': 'None', 'runbon': '≈Shi Runbon',
			   'kurai': '≈Ninguem Kurai', 'senko': 'None', 'kori': 'None', 'same': 'None', 'shio': 'None'}


def sair():
	print(f"Até logo!")
	print(f"\n", "-=" * 15, end="-\n")
	exit()


def ver_contas(tipo_do_registro='Completo',
			   nome_arquivo='/Users/terencepettine/Desktop/BACKUP MACOS 4.2024/PYTHONCODES/START-NWM/entrance/registro/registro.xlsx',
			   vars=False):
	"""
	Opção de visualizar na tela(sys.stdout) o arquivo 'registro.xlsx' no modo 'contas' (dict para uso do programa) em estética decorada e informativa.
	Args:
		tipo_do_registro: str
			'Completo' = ver_reg_completo() == Mostra registro completo
			'Minimo' = ver_reg_minimo() == Mostra registro de forma simples
		nome_arquivo: str(caminho do arquivo 'registro.xlsx')
		vars: bool
			True == Mostra as variáveis consideradas importantes (contas, ValuesToList, líderes, itens, etc)

	Returns: None

	"""
	from entrance.registro.manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)

	def ver_reg_completo():
		from entrance.Workspace.controles import values_fc, fee_fc, capta_fc, pib_real_fc, persons_fc
		from entrance.Store_fold import store
		from entrance.Workspace.Funcs import iterar, money_func, prevent, magnatas_fc, recort

		vms, ems, all_sections, all_class, tot_pvms, vpms, pvms, totcontpersec, \
			acconts, accontsdict, bolsa, bolsapersec, moneypersec = values_fc(contas)
		feepersec, tot_fee, ipcapersec, IPCA, PIB_Nominal_persec, PIB_Nominal, ETF, ETF_persec, tesouro = fee_fc(
			registro=contas)
		PIB_Per_Capita_persec, PIB_Per_Capita = capta_fc(registro=contas)
		print(f"\n",
			  f".    ╔╦════•  •✠• ❀•✠ • •═══╦╗\n",
			  f"       *Registro Bancário Mundial*\n",
			  f"    ╚╩════• •✠• ❀ •✠ • •═══╩╝ \n\n",
			  f"*Staffs (novos e antigos):*\n	Meyko Ivory,\n	Meeh Inu,\n	Susumo Tsuki,\n 	Naomi Uzuki,\n	Yu Zuky,\n	Chaos Akaguma,\n 	Naruko Namikaze,\n 	Yang Uchiha,\n	Rimawari Hyuuga,\n	Isa Akaguma")
		for secao, classes in contas.items():
			if contas[ secao ].keys().__len__() > 0:  # Caso seção tenha classes , então mostra:
				print(f"""\n	━━━━━━━━━  ✠  ━━━━━━━━━\n""")
				print(f"""*●-  -=- {secao.upper()} -=-    -●*\n""",
					  f""" ፧⠂ *PVMS do Reino:* {money_func(moneypersec[ secao ])}$\n""",
					  """ ፧⠂ *Taxa Selic do Reino:* {}\n""".format(
						  money_func(moneypersec[ secao ] - PIB_Per_Capita_persec[ secao ])),
					  F""" ፧⠂ *IPCA:* {money_func(ipcapersec[ secao ])}% _({'Taxa Selic negativa: some +IPCA% em suas compras (inflação)' if feepersec[ secao ] < 0 else 'Taxa selic positiva: diminua -IPCA% em suas compras (deflação)'})_\n""",
					  # """ ፧⠂ *PIB_Per_Capita:* {}\n""".format(f"{money_func(PIB_real / totcontpersec[ secao ])}" if totcontpersec[secao ] > 0 else f"{money_func(00)}"),
					  """ ፧⠂ *PIB Nominal Per Capita:* {}\n""".format(f"{money_func(PIB_Nominal_persec[ secao ])}"),
					  F""" ፧⠂ *BOLSA da seção:* {money_func(bolsapersec[ secao ])} \n""",
					  f""" ፧⠂ *Leis:* {'Barradas' if prevent(store.reinantes, secao) == 'None' else 'Ativas'}\n""",
					  f""" ፧⠂ *Classes:* {iterar(prevent(store.classes_c2, secao)) if prevent(store.classes_c2, secao) != 'None' else 'None'}\n""",
					  F""" ፧⠂ *Total de contas:* {totcontpersec[ secao ]}\n""")
				if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
					print(f""" ፧⠂ *Reinante:* {prevent(store.reinantes, secao)}\n""")
				print(f"""	━━━━━━━━━━  ✠  ━━━━━━━━━━\n""")
				for classe, persons in classes.items():
					if contas[ secao ][ classe ].keys().__len__() > 0:  # Caso classe tenha pessoas, então mostra
						if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
							print(f"""*Classe: {classe.title()}*""")
						else:
							print(f"*{classe.upper()}*")
						if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
							print(f"""*Líder:* {prevent(lideres, classe).title()}""")
						for name, saldo in persons.items():
							print(f"\n - {name.title()}: ", end="")
							for index, val in enumerate(saldo):
								print(f" {money_func(val)}{'$ / ' if (index % 2) == 0 else 'EXP'}", end="")
						print(f"""\n		-━━━━━━━━━  ✠  ━━━━━━━━━-\n""")
		temp = pib_real_fc()
		PIB_real, TBF = temp[ 0 ], temp[ 1 ]
		valor_guardado = PIB_real - vms
		all_persons = persons_fc()
		lismag = magnatas_fc(registro=contas)[ 0 ]
		print(f"\n– *VMS🌐:* {money_func(vms)}",
			  f"– *Meta Selic/Tesouro💰:* {money_func(tesouro)}",
			  f"– *EMS✨:* {money_func(ems)}",
			  f"– *TBF🪙:*' {money_func(tesouro - vms)}",
			  F"– *PIB_real💎:* {money_func(PIB_real)}",
			  f"– *PIB Per Capita:* *{money_func(PIB_Per_Capita)}*\n"
			  f"– *PIB Nominal:* *{money_func(PIB_Nominal)}*\n"
			  F"– *BOLSA DE VALORES📊:* {money_func(bolsa)}\n"
			  F"— *PIB_Per_Capita Mundial⚖️:* {money_func(PIB_real / all_persons.__len__())}\n"
			  F"– *ETF:* *{money_func(ETF)}*"
			  f"\n\n   ~-=-|~ *MAGNATAS*: ~|-=-~",
			  "– {}\n".format(iterar(recort(lismag, 4), ', \n- ')),
			  f"\n*VERIFICAÇÕES:*",
			  f"_¬   Soma de todos PVMS: {money_func(tot_pvms)}_ _{'é igual ao VMS.' if tot_pvms == vms else f'ATENÇÃO: Não é igual ao VMS. Isso significa que este registro não está valido! Diferença: {vms - tot_pvms}'}_",
			  f"¬   _Soma de todas as taxas: {money_func(tot_fee, 2)}_ ",
			  f"¬   _VMS + META SELIC SEMPRE ser == {money_func(PIB_real)}. Total: {money_func(vms + tesouro)}._ {'' if (vms + tesouro) == PIB_real else f'_ATENÇÃO: O resultado não é o valor guardado.. Este registro está dado como inválido._'}",
			  f"¬   _Diferença entre VMS e META SELIC: {money_func(tesouro - vms)} (TBF)_",
			  F"¬  _Total de IPCA: {money_func(IPCA)}_"
			  f"\n\n        ~-=-|~ *NOTAS:* ~|-=-~",
			  f"– PVMS = Parte do Valor Mundial Situado: quanto uma certa seção representa do VMS;",
			  F"- EMS = Total de EXP;",
			  F"- VMS = Total de grana em mãos;",
			  F"- META SELIC = Dinheiro guardado no banco;",
			  F"- TAXA SELIC = cálculo da diferença entre o que seu reino tem VPMS - o que seu reino deveria ter PIB_Per_Capita",
			  F"- PIB_real = soma dos preços de todos os store.itens (original/Bruto); ",
			  F"- IPCA = Medidor de inflação e deflação de cada reino. Valor positivo = muito dinheiro circulação (deflação), valor negativo = pouco dinheiro em mãos e store.itens caros (inflação) Pode ser definida também como a porcentagem da taxa selic;",
			  F"- TBF= Tributo básico financeiro: Variação do valor entre o VMS e M.Selic; ",
			  F"- Bolsa de Valores: Soma de todas as dívidas;",
			  F"- PIB_Per_Capita = (PIB_real ÷ contas) Calcula PIB_real por quantia de contas de cada seção (é dada como a meta de tributo que cada seção deveria alcançar);",
			  F"- PIB_Nominal = PIB_Per_capita com a diferença da inflação",
			  F"– ETF = Echange Trade Fund - Fundo de Índice comercial: Diferença entre PIB_Real (sem inflação) Para o PIB nominal (PIB com inflação)",
			  f"–> Total de seções: {contas.__len__()}",
			  f"–> Total de classes ativas: {all_class.__len__()}",
			  f"–> Total de contas: {all_persons.__len__()}\n\n", sep='\n')

	# print(f"\nAVISOS:\n Para o registro: {data_select}:\n aviso de atualização: {avisos[ 0 ][ 'avisos de atualizacoes' ][ f'{data_select}' ]}")

	def ver_reg_minimo():
		from entrance.Workspace.Funcs import money_func
		print(f"\n",
			  f".    ╔╦════•  •✠• ❀•✠ • •═══╦╗\n",
			  f"       *Registro Bancário Mundial*\n",
			  f"    ╚╩════• •✠• ❀ •✠ • •═══╩╝ \n\n",
			  f"*Staffs (novos e antigos):*\n	Meyko Ivory,\n	Meeh Inu,\n	Susumo Tsuki,\n 	Naomi Uzuki,\n	Yu Zuky,\n	Chaos Akaguma,\n 	Naruko Namikaze,\n 	Yang Uchiha,\n	Rimawari Hyuuga,\n	Isa Akaguma")
		for secao, classes in contas.items():
			if contas[ secao ].keys().__len__() > 0:  # Caso seção tenha classes , então mostra:
				print(f"""\n	━━━━━━━━━  ✠  ━━━━━━━━━\n""")
				print(f"""*●-  -=- {secao.upper()} -=-    -●*\n""")
				print(f"""	━━━━━━━━━━  ✠  ━━━━━━━━━━\n""")
				for classe, persons in classes.items():
					if contas[ secao ][ classe ].keys().__len__() > 0:  # Caso classe tenha pessoas, então mostra
						print(f"""*Classe: {classe.title()}*""")
						for name, saldo in persons.items():
							print(f"\n - {name.title()}: ", end="")
							for index, val in enumerate(saldo):
								print(f" {money_func(val)}{'$ / ' if (index % 2) == 0 else 'EXP'}", end="")
						print(f"""\n		-━━━━━━━━━  ✠  ━━━━━━━━━-""")
		print(f"Esta é uma versão simplificada do registro bancário NWM. Usada para atualizações rápidas,"
			  f" pequenas conferências e exibição apenas do saldo e EXP de todos ladinos,"
			  f" sem demais infoemações de contabilidade ou verificações.")

	def ver_vars():
		from entrance.Store_fold.store import classes_c2, avisos, leis, reinantes, itens
		"""
		Ver variáveis consideradas importantes (função filha, ativa caso 'vars=True')
		Returns: vars

		"""
		# MOSTRA VARIAVEL "CONTAS" ATUAL:
		print(F"\n\n VER VARIAVEIS: \n")
		print(f"{contas=}")
		# MOSTRA VÁRIAVEL "classes_c2" ATUAL:
		print(f"\nCLASSES_C2:\n{classes_c2=}")
		# MOSTRA VÁRIAVEL "lideres"
		print(f"\nLIDERES:\n{lideres=}")
		# MOSTRA VÁRIAVEL "leis":
		print(f"\nLEIS: \n {leis=}")
		# MOSTRA VÁRIAVEL "store.reinantes" ATUAL:
		print(f"\nstore.reinantes: \n {reinantes=}")
		print(f"\n{avisos=}\n")
		print(f"\n{itens=}\n")

	if 'C' == tipo_do_registro.upper() or tipo_do_registro == 'Completo'.upper():
		ver_reg_completo()
	elif 'M' == tipo_do_registro or tipo_do_registro == 'Mimimo':
		ver_reg_minimo()
	else:
		while True:
			escolha = str(
				input(f"Você deve escolher a versão a ser vista do registro.\n1 = Completo,\n2 = Minimo\n>>> ")).strip()
			if escolha.isalnum() is True and escolha in [ '1', '2' ]:
				break
			print(f"Valor incorreto. Tente novamente.")
		if escolha == '1':
			ver_reg_completo()
		else:
			ver_reg_minimo()
	if vars is True:
		ver_vars()


def cadastrar_pandasdf(
		nome_arquivo='/Users/terencepettine/Desktop/BACKUP MACOS 4.2024/PYTHONCODES/START-NWM/entrance/registro/registro.xlsx',
		section=None, cla=None, grana=None, EXP=None, name=None, contas=None, salve_in_archive=True):
	"""
	cadastra um novo indivíduo.
	Args:
		nome_arquivo: caminho + arquivo.xlsx (do excel) a qual o novo indivíduo será salvo.
		section: Agiliza escolha da seção do indivíduo (se for agilizar a seção, deve agilizar a classe também). Caso None, não agiliza, então usuário quem escolherá a seção.
		cla: Caso dado, agiliza escolha da classe do indivíduo (se agilizar classe, também declare o parametro section)
		grana: agiliza/previamente diz a quantia de Money do indivíduo
		EXP: agiliza/ previamente diz a quantia de EXP do indivíduo, para User não precisar escolher.
		name: agiliza nome do indivíduo a ser salvo.
		salve_in_archive: Caso True, a mudança feita é diretamente salva no arquivo. Caso False, a mudança ainda não é salva no arquivo, apenas é adicionado indivíduo na variável 'contas'

	Returns:
		var 'contas' retornado caso sucesso aparente
		None if error during a run of the code.

	"""
	from entrance.Workspace.Funcs import classes_func, give_fc, confirm
	from entrance.registro.manuseio import convet_xlsx_to_contas, convert_contas_to_xlsx
	# Obtem o registro em modo dicionário:
	if contas is None or type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	# CADASTRAR NOVO INDIVIDUO:
	# salva todos indivíduos em uma lista de listas / matriz:
	ValuesToList = [ ]
	for reino_, classes_ in contas.items():
		for classe_, person in classes_.items():
			for name_, saldo_ in person.items():
				money_ = saldo_[ 0 ]
				exp_ = saldo_[ 1 ]
				ValuesToList.append([ reino_, classe_, name_, money_, exp_ ])
	# Seleciona reino e classe:
	if section is None or cla is None or type(section) != type(cla) != type(str()):
		sc = classes_func(registro=contas)
		if sc is None:
			print(f"Não foi possível escolher seção e classe. Operação cancelada.")
			return None
		classe_select, classe_value, secao_selected, secao_value, contas_da_classe, reg_classe = sc
	else:
		classe_select = cla.lower().strip()
		secao_selected = section.lower().strip()
	# Informa nome:
	if name is None or type(name) != type(""):
		nome_novo = input(str(f" Nome do indivíduo (não precisa escrever classe): ")).lower().strip() + f" {classe_select.lower().strip()}"
	else:
		nome_novo = name.lower().strip() + f" {classe_select.lower().strip()}"
	if nome_novo.split(' ')[0] == "":
		print("O nome não pode estar em branco. Operação cancelada.")
		return False
	# Da o saldo:
	if grana is None and EXP is None:
		print(f"Agora cite o saldo de {nome_novo.title()}...")
		din, exp = give_fc()
	else:
		if grana is None:
			din = give_fc(type="money")
		else:
			din = grana
		if EXP is not None:
			exp = EXP
		else:
			din = give_fc(type="exp")
		din, exp = float(din), float(exp)
	# Verifica existencia da seção e da classe:
	lis_sec = list(contas.keys())
	lis_clas = [list(clas.keys()) for clas in contas.values()][0]
	lis_person = []
	for classes in contas.values():
		for persons in classes.values():
			for nome in persons.keys():
				lis_person.append(nome.lower())
	if secao_selected not in lis_sec or classe_select not in lis_clas:
		print(f"\nA seção '{secao_selected}' ou classe '{classe_select} 'não está incluída na var Contas/No registro.\n{lis_clas=}\n{lis_sec=}")
		return None
	#Caso uma pessoa existente seja selecionada, informa se deseja a substituição:
	print(f"{lis_person=}")
	if nome_novo in lis_person:
		escolha = int(input(f"Já existe uma conta com este nome no registro. Você deseja continuar? "))
	# Confirma operação:
	print(f"Conta a ser registrada:\n nome: {nome_novo}\nSaldo: {din}$ / {exp}EXP. Na seção: {secao_selected} e classe {classe_select}. \nConfirma?")
	if confirm():
		print("Certo. Vá ao menu e digite 7 para atualizar.")
		# ---- Salva nova conta ----#
		r = contas[ secao_selected ][ classe_select ][ nome_novo ] = [ din, exp ]
		desc = f"desc: Cadastrado novo indivíduo ({nome_novo} com saldo de {din}$/{exp}EXP). (fora do arquivo/somente var contas/Sem mudanças no arquivo)"
		if salve_in_archive is True:
			convert_contas_to_xlsx(contas, nome_arquivo=nome_arquivo, verificar=True)
			print(f"ATENÇÃO, AS MUDANÇAS FORAM SALVAS DIRETAMENTE NO ARQUIVO.")
			desc = f"desc: Cadastrado novo indivíduo ({nome_novo} com saldo de {din}$/{exp}EXP). (Mudança direta no arquivo)"
	else:
		print(f"Operação cancelada.")
		desc = 'Confirmação da operacão foi negada.'
	return [contas, desc, nome_novo, classe_select, secao_selected]



def verificar_presença(registro='/Users/terencepettine/Desktop/BACKUP MACOS 4.2024/PYTHONCODES/START-NWM/entrance/registro/registro.xlsx', nome_sect=None, nome_cla=None, nome_pp=None, oque_procurar: None | int = None):
	"""

	Args:
		registro: str - patch file registro.xlsx
		nome_sect: 	None - set the name of a section during the execution of a code function
			str - optionally param to set name of a section to find in the file. Usege case tipo=1
		nome_cla: None - set the name of a class during the execution of a code function
			str - optionally param to set name of a class to find in the file. Usege caso tipo=2
		nome_pp:
			None - set the name of a person during the execution of a code function
			str - optionally param to set name of a person to find in the file. Usege case tipo=3
		oque_procurar: None|int
			1 == find section
			2 == find class
			3 == find person
			None == escolhe o tipo (1,2,3) durante a execução.

	Returns: bool
		True case find
		False case not find.
	"""
	# Captura arquivo:
	from entrance.registro.manuseio import convet_xlsx_to_contas
	contas = convet_xlsx_to_contas(nome_arquivo=registro)
	print(contas)
	if contas is None:
		print(f"Houve um erro na captura do arquivo <conert_xlsx_to_contas>. Operação cancelada.")
		return None
	# Realiza operação:
	if oque_procurar is None:
		while True:
			oque_procurar = str(input("Deseja procurar\n1 - seção\n2 - Classe\n3 - Pessoa\nno arquivo? [1,2,3]: "))
			if oque_procurar.isnumeric():
				if int(oque_procurar) in [ 1, 2, 3 ]:
					break
			print(f"Valor incorreto. Tente novamente.")
	if oque_procurar == 1:  # seção
		if nome_sect is None:
			nome_sect = str(input(f"Digite o nome do reino a ser procurado: ")).strip()
		lis_sect = list(sect.lower for sect in contas.keys())
		if nome_sect.lower() in lis_sect:
			print(f"Encontrado {nome_sect} em {registro}.")
			return True
		else:
			print(f"Não encontrado {nome_sect} em {registro}. Verifique o caminho do arquivo ou procure em outros lugares.")
			return False
	elif oque_procurar == 2:  # Classe
		if nome_cla is None:
			nome_cla = str(input('Digite o nome da classe a ser procurada: ')).strip()
		# Popula:
		lis_clas = [ ]
		for classes in contas.values():
			for classe in classes.keys():
				lis_clas.append(classe.lower())
		# Verifica:
		if nome_cla.lower() in lis_clas:
			print(f"Encontrado {nome_cla} em {registro}.")
			return True
		else:
			print(f"Não encontrado {nome_cla} em {registro}.")
			return False
	elif oque_procurar == 3:  # Pessoa
		if nome_pp is None:
			nome_pp = str(input('Diga o nome do indivíduo a ser procurado: ')).strip()
		# popula:
		lis_persons = [ ]
		for classes in contas.values():
			for persons in classes.values():
				for nome in persons.keys():
					lis_persons.append(nome.lower())
		# Verifica:
		if nome_pp.lower() in lis_persons:
			print(f"Encontrado {nome_pp} em {registro}.")
			return True
		else:
			print(f"Não encontrado {nome_pp} em {registro}.")
			return False


def remover_conta(nome_arquivo='/Users/terencepettine/Desktop/BACKUP MACOS 4.2024/PYTHONCODES/START-NWM/entrance/registro/registro.xlsx', contas=None, save_in_archive=False):
	from entrance.Workspace.Funcs import select_account_fc
	from entrance.registro.manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	print(f"SELECIONE O INDIVÍDUO: ")
	pp = select_account_fc(contas)
	if pp is None:
		print(f"Não foi possível obter o indivíduo. Operação cancelada.")
		return None
	num, name, classe, section, person = pp
	del contas[section][classe][name]
	if save_in_archive:
		from entrance.registro.manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(contas, nome_arquivo=nome_arquivo, verificar=True)
	return [contas, name, classe, section, person]

def transferencia(nome_arquivo='/Users/terencepettine/Desktop/BACKUP MACOS 4.2024/PYTHONCODES/START-NWM/entrance/registro/registro.xlsx', contas=None, save_in_archive=False):
	from entrance.Workspace.Funcs import select_account_fc, confirm
	from entrance.registro.manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)

	print(f"SELECIONE primeiro o indivíduo a transferir(perder dinheiro) e em seguida o indivíduo a ganhar o dinheiro.: ")
	ValuesToList = []
	for c in range(0, 2):
		pp = select_account_fc(contas)
		if pp is None:
			print(f"Não foi possível obter o indivíduo. Operação cancelada.")
			return None
		if pp in ValuesToList:
			print(f"Você já escolheu este indivíduo. Operação cancelada.")
			return None
		ValuesToList.append(pp)
	print(f"{ValuesToList=}")
	num, name, classe, section, person = ValuesToList[0]
	num2, name2, classe2, section2, person2 = ValuesToList[-1]
	try:
		movido = round(float(input(f"Quantos reais deseja mover? {name} tem {person[0]}R$ disponíveis: ")), 2)
	except ValueError:
		print(f"Valores inválidos. Operação cancelada.")
		return None
	extraido = person[ 0 ] - movido
	ganho = person2[ 0 ] + movido
	print(f" < Saldo restante de {name.title()}: {person[ 0 ]} - {movido} = {extraido}>\n "
		  f" < Saldo total de {name2.title()}: {person2[ 0 ]} + {movido} = {ganho}")
	if extraido > person[0]: # Caso valor seja maior que creditário realmente tenha:
		print(f"O valor a ser transferido ultrapassa o valor possuído de {name}. Operação cancelada.")
		return None
	if confirm(f"\n -> Você confirma a operação? [S/N]: ") is False:
		print(f'Operação cancelada.')
		return None
	contas[section][classe][name][0] = extraido
	contas[section2][classe2][name2][0] = ganho
	if save_in_archive:
		from entrance.registro.manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
transferencia()


