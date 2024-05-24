from __future__ import annotations
from __init__ import funcionamento_basico
from manuseio import localizar_arquivo

if funcionamento_basico is True:
	lideres = {'tsuki': '≠±¬°°≈‹Susumo Tsuki', 'inu': 'Meeh Inu', 'ivory': '~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory',
			   'zuky': '~‹‹≈¤°°ຊ€Yu Zuky', 'uzuki': 'None', 'shiro': 'None', 'akaguma': '~-ຊ±¬°Chaos Akaguma',
			   'terepasu': 'None', 'yoso': 'None', 'kokyu': 'None', 'kieta': 'None', 'runbon': '≈Shi Runbon',
			   'kurai': '≈Ninguem Kurai', 'senko': 'None', 'kori': 'None', 'same': 'None', 'shio': 'None'}

loca = localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm',
						 arquivo='registro.xlsx')
nome_arquivo = loca[ 2 ]


def sair():
	print(f"Até logo!")
	print(f"\n", "-=" * 15, end="-\n")
	exit()


def ver_contas(tipo_do_registro='Completo',
			   nome_arquivo=nome_arquivo,
			   contas=None,
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
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	from locale import setlocale, LC_MONETARY
	setlocale(LC_MONETARY, 'pt_br')

	def ver_reg_completo():
		from controles import values_fc, fee_fc, capta_fc, pib_real_fc, list_persons_fc
		import store
		from Funcs import iterar, money_func, prevent, magnatas_fc, recort
		from locale import currency
		vals = values_fc(contas)
		val2 = [ ]
		for valor in vals:
			if type(list()) != type(valor) != type(dict()):
				val2.append(float(valor))
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
			if 'none' not in secao and 'none' not in classes:
				if contas[ secao ].values().__len__() > 0:  # Caso seção tenha classes , então mostra:
					print(f"""\n	━━━━━━━━━  ✠  ━━━━━━━━━\n""")
					print(f"""*●-  -=- {secao.upper()} -=-    -●*\n""",
						  f""" ፧⠂ *PVMS do Reino:* {currency(float(moneypersec[ secao ]))}$\n""",
						  """ ፧⠂ *Taxa Selic do Reino:* {}\n""".format(
							  currency(float(moneypersec[ secao ] - PIB_Per_Capita_persec[ secao ]))),
						  F""" ፧⠂ *IPCA:* {currency(float(ipcapersec[ secao ]))}% _({'Taxa Selic negativa: some +IPCA% em suas compras (inflação)' if feepersec[ secao ] < 0 else 'Taxa selic positiva: diminua -IPCA% em suas compras (deflação)'})_\n""",
						  # """ ፧⠂ *PIB_Per_Capita:* {}\n""".format(f"{money_func(PIB_real / totcontpersec[ secao ])}" if totcontpersec[secao ] > 0 else f"{money_func(00)}"),
						  """ ፧⠂ *PIB Nominal Per Capita:* {}\n""".format(
							  f"{currency(float(PIB_Nominal_persec[ secao ]))}"),
						  F""" ፧⠂ *BOLSA da seção:* {currency(float(bolsapersec[ secao ]))} \n""",
						  f""" ፧⠂ *Leis:* {'Barradas' if prevent(store.reinantes, secao) == 'None' else 'Ativas'}\n""",
						  f""" ፧⠂ *Classes:* {iterar(prevent(store.classes_c2, secao)) if prevent(store.classes_c2, secao) != 'None' else 'None'}\n""",
						  F""" ፧⠂ *Total de contas:* {len(totcontpersec[ secao ])}\n""")
					if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
						print(f""" ፧⠂ *Reinante:* {prevent(store.reinantes, secao)}\n""")
					print(f"""	━━━━━━━━━━  ✠  ━━━━━━━━━━\n""")
					for classe, persons in classes.items():
						if 'none' not in classe and persons != 'none' and contas[ secao ][
							classe ].values().__len__() > 0 and persons.__len__() > 0:  # Caso classe tenha pessoas, então mostra
							if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
								print(f"""*Classe: {classe.title()}*""")
							else:
								print(f"*{classe.upper()}*")
							if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
								print(f"""*Líder:* {prevent(store.lideres, classe).title()}""")
							for name, saldo in persons.items():
								if name != 'none' and 'none' != saldo:
									print(f"\n - {name.title()}: ", end="")
									for index, val in enumerate(saldo):
										if val != 'none':
											val = float(val)
											print(f" {currency(val)}{'$ / ' if (index % 2) == 0 else 'EXP'}", end="")
										else:
											print(f" 0,0 ")
							print(f"""\n		-━━━━━━━━━  ✠  ━━━━━━━━━-\n""")
		temp = pib_real_fc()
		PIB_real, TBF = temp[ 0 ], temp[ 1 ]
		valor_guardado = PIB_real - vms
		all_persons = list_persons_fc(registro=contas)
		lismag = magnatas_fc(registro=contas)[ 0 ]
		print(f"\n– *VMS🌐:* {currency(vms)}",
			  f"– *Meta Selic/Tesouro💰:* {currency(PIB_real - vms)}",
			  f"– *EMS✨:* {currency(ems)}",
			  f"– *TBF🪙:*' {currency((PIB_real - vms) - vms)}",
			  F"– *PIB_real💎:* {currency(PIB_real)}",
			  f"– *PIB Per Capita:* *{currency(PIB_Per_Capita)}*\n"
			  f"– *PIB Nominal:* *{currency(PIB_Nominal)}*\n"
			  F"– *BOLSA DE VALORES📊:* {currency(bolsa)}\n"
			  F"— *PIB_Per_Capita Mundial⚖️:* {currency(PIB_real / all_persons.__len__())}\n"
			  F"– *ETF:* *{currency(ETF)}*"
			  f"\n\n   ~-=-|~ *MAGNATAS*: ~|-=-~",
			  "– {}\n".format(iterar(recort(lismag, 4), ', \n- ')),
			  f"\n*VERIFICAÇÕES:*",
			  f"_¬   Soma de todos PVMS: {currency(tot_pvms)}_ _{'é igual ao VMS.' if tot_pvms == vms else f'ATENÇÃO: Não é igual ao VMS. Isso significa que este registro não está valido! Diferença: {vms - tot_pvms}'}_",
			  f"¬   _Soma de todas as taxas: {currency(tot_fee, 2)}_ ",
			  f"¬   _VMS + META SELIC SEMPRE ser == {currency(PIB_real)}. Total: {currency(vms + (PIB_real - vms))}._ {'' if (vms + tesouro) == PIB_real else f'_ATENÇÃO: O resultado não é o valor guardado.. Este registro está dado como inválido._'}",
			  f"¬   _Diferença entre VMS e META SELIC: {currency(tesouro - vms)} (TBF)_",
			  F"¬  _Total de IPCA: {currency(IPCA)}_"
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
		from Funcs import money_func
		from locale import currency
		print(f"\n",
			  f".    ╔╦════•  •✠• ❀•✠ • •═══╦╗\n",
			  f"       *Registro Bancário Mundial*\n",
			  f"    ╚╩════• •✠• ❀ •✠ • •═══╩╝ \n\n",
			  f"*Staffs (novos e antigos):*\n	Meyko Ivory,\n	Meeh Inu,\n	Susumo Tsuki,\n 	Naomi Uzuki,\n	Yu Zuky,\n	Chaos Akaguma,\n 	Naruko Namikaze,\n 	Yang Uchiha,\n	Rimawari Hyuuga,\n	Isa Akaguma")
		for secao, classes in contas.items():
			if secao != 'none' != classes and contas[
				secao ].keys().__len__() > 0:  # Caso seção tenha classes , então mostra:
				print(f"""\n	━━━━━━━━━  ✠  ━━━━━━━━━\n""")
				print(f"""*●-  -=- {secao.upper()} -=-    -●*\n""")
				print(f"""	━━━━━━━━━━  ✠  ━━━━━━━━━━\n""")
				for classe, persons in classes.items():
					if secao != 'none' != classes and contas[ secao ][
						classe ].keys().__len__() > 0:  # Caso classe tenha pessoas, então mostra
						print(f"""*Classe: {classe.title()}*""")
						for name, saldo in persons.items():
							print(f"\n - {name.title()}: ", end="")
							for index, val in enumerate(saldo):
								print(f" {currency(val)}{'$ / ' if (index % 2) == 0 else 'EXP'}", end="")
						print(f"""\n		-━━━━━━━━━  ✠  ━━━━━━━━━-""")
		print(f"Esta é uma versão simplificada do registro bancário NWM. Usada para atualizações rápidas,"
			  f" pequenas conferências e exibição apenas do saldo e EXP de todos ladinos,"
			  f" sem demais infoemações de contabilidade ou verificações.")

	def ver_vars():
		from store import classes_c2, avisos, leis, reinantes, itens, lideres
		"""
		Ver variáveis consideradas importantes (função filha, ativa caso 'vars=True')
		Returns: vars

		"""
		# MOSTRA VARIAVEL "CONTAS" ATUAL:
		print(F"\n\n VER VARIAVEIS: \n")
		print(f"{contas=}")
		# MOSTRA VÁRIAVEL "classes_c2" ATUAL:
		print(f"\nCLASSES_C2:\n{classes_c2=}")
		# MOSTRA VÁRIAVEL "store.lideres"
		print(f"\nLIDERES:\n{lideres=}")
		# MOSTRA VÁRIAVEL "leis":
		print(f"\nLEIS: \n {leis=}")
		# MOSTRA VÁRIAVEL "store.reinantes" ATUAL:
		print(f"\nstore.reinantes: \n {reinantes=}")
		print(f"\n{avisos=}\n")
		print(f"\n{itens=}\n")

	if 'C' == tipo_do_registro.upper().strip() or tipo_do_registro.upper().strip() == 'COMPLETO':
		ver_reg_completo()
	elif 'M' == tipo_do_registro.upper().strip() or tipo_do_registro.upper().strip() == 'MINIMO' or 'MÍNIMO':
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
		nome_arquivo=nome_arquivo,
		section=None, cla=None, grana=None, EXP=None, name=None, contas=None,
		save_in_archive=True):
	"""
	cadastra um novo indivíduo.
	Args:
		nome_arquivo: caminho + arquivo.xlsx (do excel) a qual o novo indivíduo será salvo.
		section: Agiliza escolha da seção do indivíduo (se for agilizar a seção, deve agilizar a classe também). Caso None, não agiliza, então usuário quem escolherá a seção.
		cla: Caso dado, agiliza escolha da classe do indivíduo (se agilizar classe, também declare o parametro section)
		grana: agiliza/previamente diz a quantia de Money do indivíduo
		EXP: agiliza/ previamente diz a quantia de EXP do indivíduo, para User não precisar escolher.
		name: agiliza nome do indivíduo a ser salvo.
		save_in_archive: Caso True, a mudança feita é diretamente salva no arquivo. Caso False, a mudança ainda não é salva no arquivo, apenas é adicionado indivíduo na variável 'contas'

	Returns:
		var 'contas' retornado caso sucesso aparente
		None if error during a run of the code.

	"""
	from Funcs import classes_func, give_fc, confirm
	from manuseio import convet_xlsx_to_contas, convert_contas_to_xlsx
	# Obtem o registro em modo dicionário:
	if contas is None or type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	# CADASTRAR NOVO INDIVIDUO:
	# salva todos indivíduos em uma lista de listas / matriz:
	ValuesToList = [ ]
	for reino_, classes_ in contas.items():
		if reino_ != 'none' != classes_:
			for classe_, person in classes_.items():
				if person != 'none' != classe_:
					for name_, saldo_ in person.items():
						if name_ != 'none' != saldo_:
							money_ = saldo_[ 0 ]
							exp_ = saldo_[ 1 ]
							ValuesToList.append([ reino_, classe_, name_, money_, exp_ ])
	# Seleciona reino e classe:
	if section is None or cla is None or type(section) != type(cla) != type(str()):
		sc = classes_func(registro=contas)
		if sc is None:
			print(f" - Não foi possível escolher seção e classe. Operação cancelada.")
			return None
		classe_select, classe_value, secao_selected, secao_value, contas_da_classe, reg_classe = sc
	else:
		classe_select = cla.lower().strip()
		secao_selected = section.lower().strip()
	# Informa nome:
	if name is None or type(name) != type(""):
		nome_novo = input(
			str(f" - Nome do indivíduo (não precisa escrever classe): ")).lower().strip() + f" {classe_select.lower().strip()}"
	else:
		nome_novo = name.lower().strip() + f" {classe_select.lower().strip()}"
	if nome_novo.split(' ')[ 0 ] == "":
		print(" - O nome não pode estar em branco. Operação cancelada.")
		return False
	# Da o saldo:
	if grana is None and EXP is None:
		print(f" - Agora cite o saldo de {nome_novo.title()}...")
		din, exp = give_fc(registro=contas)
	else:
		if grana is None:
			din = give_fc(registro=contas, type="money")
		else:
			din = grana
		if EXP is not None:
			exp = EXP
		else:
			din = give_fc(registro=contas, type="exp")
		din, exp = float(din), float(exp)
	# Verifica existencia da seção e da classe:
	lis_sec = list(contas.keys())
	lis_clas = [ list(clas.keys()) for clas in contas.values() ][ 0 ]
	lis_person = [ ]
	for classes in contas.values():
		if classes != 'none':
			for persons in classes.values():
				if persons != 'none':
					for nome in persons.keys():
						if nome != 'none':
							lis_person.append(nome.lower())
	if secao_selected not in lis_sec or classe_select not in lis_clas:
		print(
			f"\n - A seção '{secao_selected}' ou classe '{classe_select} 'não está incluída na var Contas/No registro.\n - {lis_clas=}\n{lis_sec=}")
		return None
	# Caso uma pessoa existente seja selecionada, informa se deseja a substituição:
	if nome_novo in lis_person:
		escolha = int(input(f"Já existe uma conta com este nome no registro. Você deseja continuar? "))
	# Confirma operação:
	print(
		f"\n - Conta a ser registrada:\n nome: {nome_novo}\nSaldo: {din}$ / {exp}EXP. Na seção: {secao_selected} e classe {classe_select}. \nConfirma?")
	if confirm(' - [S/N] >>> '):
		print(" - Certo. Vá ao menu e digite 7 para atualizar.")
		# ---- Salva nova conta ----#
		r = contas[ secao_selected ][ classe_select ][ nome_novo ] = [ din, exp ]
		desc = f"desc: Cadastrado novo indivíduo ({nome_novo} com saldo de {din}$/{exp}EXP). (fora do arquivo/somente var contas/Sem mudanças no arquivo)"
		if save_in_archive is True:
			convert_contas_to_xlsx(contas, nome_arquivo=nome_arquivo, verificar=True)
			print(f" - ATENÇÃO, AS MUDANÇAS FORAM SALVAS DIRETAMENTE NO ARQUIVO.")
			desc = f"desc: Cadastrado novo indivíduo ({nome_novo} com saldo de {din}$/{exp}EXP). (Mudança direta no arquivo)"
	else:
		print(f" - Operação cancelada.")
		desc = 'Confirmação da operacão foi negada.'
	return [ contas, desc, nome_novo, classe_select, secao_selected ]


def verificar_presença(contas=None, registro=nome_arquivo, nome_sect=None, nome_cla=None, nome_pp=None,
					   oque_procurar: None | int = None):
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
	if type(contas) != type(dict()):
		from manuseio import convet_xlsx_to_contas
		contas = convet_xlsx_to_contas(nome_arquivo=registro)
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
			print(
				f"Não encontrado {nome_sect} em {registro}. Verifique o caminho do arquivo ou procure em outros lugares.")
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


def remover_conta(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False):
	desc = ''
	from Funcs import select_account_fc
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	print(f"SELECIONE O INDIVÍDUO: ")
	pp = select_account_fc(contas)
	if pp is None:
		print(f"Não foi possível obter o indivíduo. Operação cancelada.")
		return None
	num, name, classe, section, person = pp
	qtia_persons = contas[ section ][ classe ].__len__()
	if qtia_persons >= 2:
		del contas[ section ][ classe ][ name ]
	elif qtia_persons == 1:
		contas[ section ][ classe ] = {'none': [ 'none', 'none' ]}
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(contas, nome_arquivo=nome_arquivo, verificar=True)
	return [ contas, desc, name, classe, section, person ]


def transferencia(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False):
	from Funcs import select_account_fc, confirm
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	print(
		f"SELECIONE primeiro o indivíduo a transferir(perder dinheiro) e em seguida o indivíduo a ganhar o dinheiro.: ")
	ValuesToList = [ ]
	desc = ''
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
	num, name, classe, section, person = ValuesToList[ 0 ]
	num2, name2, classe2, section2, person2 = ValuesToList[ -1 ]
	try:
		movido = round(float(input(f"Quantos reais deseja mover? {name} tem {person[ 0 ]}R$ disponíveis: ")), 2)
	except ValueError:
		print(f"Valores inválidos. Operação cancelada.")
		return None
	extraido = person[ 0 ] - movido
	ganho = person2[ 0 ] + movido
	print(f" < Saldo restante de {name.title()}: {person[ 0 ]} - {movido} = {extraido}>\n "
		  f" < Saldo total de {name2.title()}: {person2[ 0 ]} + {movido} = {ganho}")
	if extraido > person[ 0 ]:  # Caso valor seja maior que creditário realmente tenha:
		print(f"O valor a ser transferido ultrapassa o valor possuído de {name}. Operação cancelada.")
		return None
	if confirm(f"\n -> Você confirma a operação? [S/N]: ") is False:
		print(f'Operação cancelada.')
		return None
	contas[ section ][ classe ][ name ][ 0 ] = extraido
	contas[ section2 ][ classe2 ][ name2 ][ 0 ] = ganho
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
	return [ contas, desc, name, name2, movido ]


def add_classe(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False, secao_selected=None, nome_novo=None):
	from Funcs import secoes_func
	from controles import values_fc
	desc = ''
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		from manuseio import convet_xlsx_to_contas
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	print(f" Escolha a classe ")
	if secao_selected == None:
		sc = secoes_func(registro=contas)
		if sc is not None:
			secao_selected = sc[ -2 ]
		else:
			print(F"Houve um erro na captura da função Funcs.secoes_func(). Operação cancelada")
			return None
	vals = values_fc(registro=contas)
	if vals is not None:
		vms, ems, all_sections, all_class, tot_pvms, vpms, pvms, totcontpersec, acconts, accontsdict, bolsa, bolsapersec, tesouropersec = vals
	else:
		print(F"Houve um erro na captura da função controles.values_fc(). Operação cancelada")
		return None
	if nome_novo is None:
		nome_novo = str(input("Nome da classe nova: ")).lower().strip()
	else:
		nome_novo = nome_novo.lower().strip()
	if nome_novo == "":
		print(f"O nome da classe não pode estar em branco. Operação cancelada.")
		del nome_novo
		return None
	elif nome_novo in all_class:
		print(f"ATENÇÃO: Esta classe parece já existir. Tente outros nomes. Operação cancelada.")
		del nome_novo
		return None
	else:
		from Funcs import confirm
		if confirm(
				f"Classe a ser cadastrada: {nome_novo}\nReino Pertencente: {secao_selected}. Confirma?\n [S/N] >>> "):
			from store import classes_c2
			classes_c2[ secao_selected ].append(nome_novo)
			contas[ secao_selected ][ nome_novo ] = {'none': [ 'none', 'none' ]}
			if save_in_archive:
				from manuseio import convert_contas_to_xlsx
				convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
	return [ contas, desc, secao_selected, nome_novo ]


def descontar(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False):
	from Funcs import select_account_fc, confirm
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	print(f"SELECIONE o indivíduo a ter a conta descontada: ")
	ValuesToList = [ ]
	desc = ''
	for c in range(0, 1):
		pp = select_account_fc(contas)
		if pp is None:
			print(f"Não foi possível obter o indivíduo. Operação cancelada.")
			return None
		if pp in ValuesToList:
			print(f"Você já escolheu este indivíduo. Operação cancelada.")
			return None
		ValuesToList.append(pp)
	num, name, classe, section, person = ValuesToList[ 0 ]
	try:
		movido = round(float(input(f"Quantos reais deseja retirar? {name} tem {person[ 0 ]} reais. \n [float] >>> ")),
					   2)
		exp = round(float(input(f"Quantos EXP deseja retirar? {name} tem {person[ 1 ]} EXP. \n [float] >>> ")), 2)
	except ValueError:
		print(f"Valores inválidos. Operação cancelada.")
		return None
	extraido = [ float(person[ 0 ]) - movido, float(person[ 1 ]) - exp ]
	print(f" < Saldo restante de {name.title()}: {person[ 0 ]} - {movido} = {extraido[ 0 ]}>\n "
		  f" < EXP: {person[ 1 ]} - {exp} = {extraido[ 1 ]}")
	if confirm(f"\n -> Você confirma a operação? \n[S/N] >>> ") is False:
		print(f'Operação cancelada.')
		return None
	contas[ section ][ classe ][ name ] = extraido
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
	return [ contas, desc, name, movido, exp ]


def abonar(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False):
	from Funcs import select_account_fc, confirm, give_fc
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	print(f"SELECIONE o indivíduo a ter a conta creditada: ")
	ValuesToList = [ ]
	desc = ''
	for c in range(0, 1):
		pp = select_account_fc(contas)
		if pp is None:
			print(f"Não foi possível obter o indivíduo. Operação cancelada.")
			return None
		if pp in ValuesToList:
			print(f"Você já escolheu este indivíduo. Operação cancelada.")
			return None
		ValuesToList.append(pp)
	num, name, classe, section, person = ValuesToList[ 0 ]
	print(F"Digite quantos Ryos e quantos EXP serão SOMADOS: ")
	din, exp = give_fc(registro=contas)
	extraido = [ float(person[ 0 ]) + din, float(person[ 1 ]) + exp ]
	print(f" < Saldo restante de {name.title()}: {person[ 0 ]} + {din} = {extraido[ 0 ]}>\n "
		  f" < EXP: {person[ 1 ]} + {exp} = {extraido[ 1 ]}")
	if confirm(f"\n -> Você confirma a operação? \n[S/N] >>> ") is False:
		print(f'Operação cancelada.')
		return None
	contas[ section ][ classe ][ name ] = extraido
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
	return [ contas, desc, name, din, exp ]


def formatar_contas(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False, vezes=None):
	from Funcs import select_account_fc, confirm, give_fc
	from controles import list_persons_fc
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	all_persons = list_persons_fc(registro=contas)
	desc = ''
	if len(all_persons) == 1:
		vezes = 1
	elif len(all_persons) < 1:
		print(F"Não há indivíduos no registro. Operação cancelada.")
		desc = 'Tentativa falha por registro estar sem indivíduos.'
		return None
	if vezes is None:
		while True:
			vezes = str(input(
				f"QUANTOS INDIVÍDUOS DESEJA REMANEJAR? (-1 para cancelar, -2 para selecionar todos) \n [0 ~ {len(all_persons)}] >>> "))
			if vezes.isnumeric():
				vezes = int(vezes)
				if vezes == -1:
					print('cancelando...')
					return None
				elif vezes == -2:
					vezes = len(all_persons)
				if vezes <= len(all_persons) and vezes > 0:
					break
			print(F"Tente novamente.")
	print(f"SELECIONE o indivíduo a ter a conta alterada: ")
	ValuesToList = [ ]
	nomes = [ ]
	for c in range(0, vezes):
		pp = select_account_fc(contas)
		print(f" INDIVÍDUOS SELECIONADOS: {c} - {nomes}")
		if pp is None:
			print(f"Não foi possível obter o indivíduo. Operação cancelada.")
			return None
		if pp in ValuesToList:
			print(f"Você já escolheu este indivíduo. Tente novamente.")
			return None
		else:
			ValuesToList.append(pp)
			num, name, classe, section, person = ValuesToList[ -1 ]
			nomes.append(name)
			print(F"Digite quantos Ryos e quantos EXP serão FIXADOS (remanejo, não adição nem subtração) ")
			din, exp = give_fc(registro=contas)
			saldo = [ din, exp ]
			print(f" < Saldo de {name.title()}: {saldo}>\n ")
			if confirm(f"\n -> Você confirma a operação? \n[S/N] >>> ") is False:
				print(f'Operação cancelada.')
				return None
			contas[ section ][ classe ][ name ] = saldo
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
	return [ contas, desc, name, din, exp ]


def add_section(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False, nome_novo=None):
	from Funcs import secoes_func
	from controles import values_fc
	desc = ''
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		from manuseio import convet_xlsx_to_contas
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	all_sections = list(contas.keys())
	if nome_novo is None:
		nome_novo = str(input("Nome da seção nova: ")).lower().strip()
	else:
		nome_novo = nome_novo.lower().strip()
	if nome_novo == "":
		print(f"O nome da classe não pode estar em branco. Operação cancelada.")
		del nome_novo
		return None
	elif nome_novo in all_sections:
		print(f"ATENÇÃO: Essa seção parece já existir. Tente outros nomes. Operação cancelada.")
		del nome_novo
		return None
	else:
		from Funcs import confirm
		if confirm(f"Seção nova a ser cadastrada: {nome_novo}. Confirma?\n [S/N] >>> ") is False:
			print('operação cancelada.\n')
			return None
		from store import classes_c2
		classes_c2[ nome_novo ] = [ None ]
		contas[ nome_novo ] = {'none': {'none': [ 'none', 'none' ]}}
		if save_in_archive:
			from manuseio import convert_contas_to_xlsx
			convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
	return [ contas, desc, nome_novo ]


def mundar_todas_captais():
	pass

