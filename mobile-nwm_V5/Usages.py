"""
v 4.6.1(Bank) - V3 of this code
"""
from __future__ import annotations

from __init__ import funcionamento_basico
from manuseio import localizar_arquivo
from babel.numbers import format_currency
argv = 'Usages.py'

# format_currency(1234.5, '', locale='pt_br')


if funcionamento_basico is True:
	lideres = {'tsuki': '≠±¬°°≈‹Susumo Tsuki', 'inu': 'Meeh Inu', 'ivory': '~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory',
			   'zuky': '~‹‹≈¤°°ຊ€Yu Zuky', 'uzuki': 'None', 'shiro': 'None', 'akaguma': '~-ຊ±¬°Chaos Akaguma',
			   'terepasu': 'None', 'yoso': 'None', 'kokyu': 'None', 'kieta': 'None', 'runbon': '≈Shi Runbon',
			   'kurai': '≈Ninguem Kurai', 'senko': 'None', 'kori': 'None', 'same': 'None', 'shio': 'None'}

loca = localizar_arquivo(criar=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx', test_open=True)
nome_arquivo = loca[ 2 ]


def sair():
	"""
	Saí do programa.
	Returns: None
	"""
	print(f"\nAlerta de: {argv} >\n",f"Até logo!")
	print(f"\n", "-=" * 15, end="-\n")
	exit()


def ver_contas(tipo_do_registro='Completo', nome_arquivo=nome_arquivo, contas=None, itens=None, obj=None, vars=False, view=True):
	"""
	Opção de visualizar na tela(sys.stdout) o arquivo 'superreg.xlsx' no modo 'contas' (dict para uso do programa) em estética decorada e informativa.
	Args:
		tipo_do_registro: str
			'Completo' = ver_reg_completo() == Mostra registro completo
			'Minimo' = ver_reg_minimo() == Mostra registro de forma simples
			"Sem" = ver_vars() == Não mostra registro, apenas as variáveis.
		nome_arquivo: str(caminho do arquivo 'superreg.xlsx'). Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
		vars: bool
			True == Mostra as variáveis consideradas importantes (contas, ValuesToList, líderes, itens, etc).
			False == não mostra
	Returns:
	 	case tipo_do_registro != 'sem' == return None
		case tipo_do_registro == 'sem' == return variáveis

	"""
	desc = f"\nAlerta de: {argv} >\n"
	if type(contas) != type(dict()) or type(obj) != type(list()):
		from manuseio import convet_xlsx_to_contas
		# Obtem o registro em modo dicionário:
		var = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
		contas = var[0]
		reinantes = var[1]
		lideres = var[2]
		classes_c2 = var[3]
	elif type(obj) == type(list()):
		reinantes = obj[ 0 ]
		lideres = obj[ 1 ]
		classes_c2 = obj[ 2 ]
	if type(itens) != type(dict()):
		from manuseio import convert_things_to_items
		itens = convert_things_to_items(nome_arquivo=nome_arquivo)

	def ver_reg_completo():
		from controles import values_fc, fee_fc, capta_fc, pib_real_fc, list_persons_fc, totcontspersec_fc
		from Funcs import iterar, prevent, magnatas_fc, recort
		vals = values_fc(contas)
		val2 = [ ]
		for valor in vals:
			if type(list()) != type(valor) != type(dict()):
				val2.append(float(valor))
		vms, ems, all_sections, all_class, tot_pvms, vpms, pvms, totcontpersec, \
			acconts, accontsdict, bolsa, bolsapersec, moneypersec = values_fc(contas)
		totcontpersec = totcontspersec_fc(registro=contas, ignore_none=True)
		feepersec, tot_fee, ipcapersec, IPCA, PIB_Nominal_persec, PIB_Nominal, ETF, ETF_persec, tesouro = fee_fc(
			registro=contas, itens=itens)
		PIB_Per_Capita_persec, PIB_Per_Capita = capta_fc(registro=contas)
		top = [ f"\n",
				f".    ╔╦════•  •✠• ❀•✠ • •═══╦╗\n",
				f"       *Registro Bancário Mundial*\n",
				f"    ╚╩════• •✠• ❀ •✠ • •═══╩╝ \n\n",
				f"*Staffs (novos e antigos):*\n	Meyko Ivory,\n	Meeh Inu,\n	Susumo Tsuki,\n 	Naomi Uzuki,\n	Yu Zuky,\n	Chaos Akaguma,\n 	Naruko Namikaze,\n 	Yang Uchiha,\n	Rimawari Hyuuga,\n	Isa Akaguma\n" ]
		part = f"""\n	━━━━━━━━  ✠  ━━━━━━━━\n"""
		part2 = f"""\n	    -━━━━━━━━-  ✠  -━━━━━━━━-\n"""
		sec_parts = top
		# print(*top, end='')
		for secao, classes in contas.items():
			if 'none' not in secao and 'none' not in classes:
				if contas[ secao ].values().__len__() > 0:  # Caso seção tenha classes , então mostra:
					sect_part = [ part, f"""\n*●-  -=- {secao.upper()} -=-    -●*\n""",
								  f""" ፧⠂ *PVMS do Reino:* {format_currency(round(moneypersec[ secao ], 2), '', locale='pt_br')}$\n""",
								  """ ፧⠂ *Taxa Selic do Reino:* {}\n""".format(
									  format_currency(round(moneypersec[ secao ] - PIB_Per_Capita_persec[ secao ], 2), '',
													  locale='pt_br')),
								  F""" ፧⠂ *IPCA:* {format_currency(round(ipcapersec[ secao ], 2), '', locale='pt_br')}% _({'Taxa Selic negativa: some +IPCA% em suas compras (inflação)' if feepersec[ secao ] < 0 else 'Taxa selic positiva: diminua -IPCA% em suas compras (deflação)'})_\n""",
								  # """ ፧⠂ *PIB_Per_Capita:* {}\n""".format(f"{money_func(PIB_real / totcontpersec[ secao ])}" if totcontpersec[secao ] > 0 else f"{money_func(00)}"),
								  """ ፧⠂ *PIB Nominal Per Capita:* {}\n""".format(
									  f"{format_currency(round(PIB_Nominal_persec[ secao ], 2), '', locale='pt_br')}"),
								  F""" ፧⠂ *BOLSA da seção:* {format_currency(round(bolsapersec[ secao ], 2), '', locale='pt_br')} \n""",
								  f""" ፧⠂ *Leis:* {'Barradas' if prevent(reinantes, secao) == 'None' else 'Ativas'}\n""",
								  f""" ፧⠂ *Classes:* {iterar(prevent(classes_c2, secao)) if prevent(classes_c2, secao) != 'None' else 'None'}\n""",
								  F""" ፧⠂ *Total de contas:* {totcontpersec[ secao ].__len__()}\n"""
								  F""" ፧⠂ *Terrenos:* {0+0}\n"""]
					sec_parts.append(''.join(sect_part))
					# print(*sect_part, end='')
					if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
						secpart_rei = f""" ፧⠂ *Reinante:* {prevent(reinantes, secao).title().strip()}\n"""
						sec_parts.append(secpart_rei)
					# print(secpart_rei)
					# print(part, end='')
					sec_parts.append(part)
					for classe, persons in classes.items():
						if persons != 'none' and contas[ secao ][ classe ].values().__len__() > 0 and [
							persons.keys().__len__() == 1 and str(list(persons.keys())[ 0 ]) == 'none' ] == [
							False ]:  # Caso classe tenha pessoas, e não 'none', então mostra
							if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
								contas_part = f"*Classe: {classe.title()}*\n"
							# print(contas_part, end='')
							else:
								contas_part = f"\n*{classe.upper()}*\n"
							# print(contas_part, end='')
							sec_parts.append(contas_part)
							if 'contas em conj' not in secao:  # Caso a seção atual não seja 'contas em conjunto/NPC'
								lider_part = f"*Líder:* {prevent(lideres, classe).title()}\n"
								sec_parts.append(lider_part)
							# print(lider_part, end='')
							for name, saldo in persons.items():
								if name.strip().lower() != 'none' and type(saldo) == type(list()):
									name_part = f"\n- > {name.title():}: "
									sec_parts.append(name_part)
									# print(name_part, end="")
									for index, val in enumerate(saldo):
										if index in [0, 1]:
											val = round(float(val), 2)
											val_part = f"{format_currency(val, '', locale='pt_br')}{'$ |' if (index % 2) == 0 else 'EXP'}"
											sec_parts.append(val_part)
										# print(val_part, end="")
										'''elif str(val).isnumeric() is False and index in [0, 1]:
											val_part = f" 0,0 "
											sec_parts.append(val_part)'''
										if index == 9:
											sec_parts.append(f"\nPatente: {val}")
										# print(val_part)
							# print(part2, end='')
							sec_parts.append(part2)
		temp = pib_real_fc()
		PIB_real, TBF = temp[ 0 ], temp[ 1 ]
		valor_guardado = PIB_real - vms
		all_persons = list_persons_fc(registro=contas)
		lismag = magnatas_fc(registro=contas)[ 0 ]
		finnal_part = [ f"\n– *VMS🌐:* {format_currency(vms, '', locale='pt_br')}\n",
						f"– *Meta Selic/Tesouro💰:* {format_currency(PIB_real - vms, '', locale='pt_br')}\n",
						f"– *EMS✨:* {format_currency(ems, '', locale='pt_br')}\n",
						f"– *TBF🪙:*' {format_currency((PIB_real - vms) - vms, '', locale='pt_br')}\n",
						F"– *PIB_real💎:* {format_currency(PIB_real, '', locale='pt_br')}\n",
						f"– *PIB Per Capita:* *{format_currency(PIB_Per_Capita, '', locale='pt_br')}*\n"
						f"– *PIB Nominal:* *{format_currency(PIB_Nominal, '', locale='pt_br')}*\n"
						F"– *BOLSA DE VALORES📊:* {format_currency(bolsa, '', locale='pt_br')}\n"
						F"— *PIB_Per_Capita Mundial⚖️:* {format_currency(PIB_real / all_persons.__len__(), '', locale='pt_br')}\n"
						F"– *ETF:* *{format_currency(ETF, '', locale='pt_br')}*"
						f"\n\n   ~-=-|~ *MAGNATAS*: ~|-=-~\n",
						"– {}\n".format(iterar(recort(lismag, 4), ', \n- ')),
						f"\n*VERIFICAÇÕES:*\n",
						f"_¬   Soma de todos PVMS: {format_currency(tot_pvms, '', locale='pt_br')}_ _{'é igual ao VMS.' if tot_pvms == vms else f'ATENÇÃO: Não é igual ao VMS. Isso significa que este registro não está valido! Diferença: {vms - tot_pvms}'}_\n",
						f"¬   _Soma de todas as taxas: {format_currency(tot_fee, '', locale='pt_br')}\n",
						f"¬   _VMS + META SELIC SEMPRE ser == {format_currency(PIB_real, '', locale='pt_br')}. Total: {format_currency(vms + (PIB_real - vms), '', locale='pt_br')}._ {'' if (vms + tesouro) == PIB_real else f'_ATENÇÃO: O resultado não é o valor guardado.. Este registro está dado como inválido._'}\n",
						f"¬   _Diferença entre VMS e META SELIC: {format_currency(tesouro - vms, '', locale='pt_br')} (TBF)\n",
						F"¬  _Total de IPCA: {format_currency(IPCA, '', locale='pt_br')}"
						f"\n\n        ~-=-|~ *NOTAS:* ~|-=-~",
						f"\n– PVMS = Parte do Valor Mundial Situado: quanto uma certa seção representa do VMS;\n",
						F"- EMS = Total de EXP;\n",
						F"- VMS = Total de grana em mãos;\n",
						F"- META SELIC = Dinheiro guardado no banco;\n",
						F"- TAXA SELIC = cálculo da diferença entre o que seu reino tem VPMS - o que seu reino deveria ter PIB_Per_Capita\n",
						F"- PIB_real = soma dos preços de todos os Itens (original/Bruto);\n",
						F"- IPCA = Medidor de inflação e deflação de cada reino. Valor positivo = muito dinheiro circulação (deflação), valor negativo = pouco dinheiro em mãos e itens caros (inflação) Pode ser definida também como a porcentagem da taxa selic;\n",
						F"- TBF= Tributo básico financeiro: Variação do valor entre o VMS e M.Selic;\n",
						F"- Bolsa de Valores: Soma de todas as dívidas;\n",
						F"- PIB_Per_Capita = (PIB_real ÷ contas) Calcula PIB_real por quantia de contas de cada seção (é dada como a meta de tributo que cada seção deveria alcançar);\n",
						F"- PIB_Nominal = PIB_Per_capita com a diferença da inflação\n",
						F"– ETF = Echange Trade Fund - Fundo de Índice comercial: Diferença entre PIB_Real (sem inflação) Para o PIB nominal (PIB com inflação)\n",
						f"–> Total de seções: {contas.__len__()}\n",
						f"–> Total de classes ativas: {all_class.__len__()}\n",
						f"–> Total de contas: {all_persons.__len__()}\n\n" ]
		# print(*finnal_part)

		sec_parts.append(''.join(finnal_part))
		view_reg = ''.join(sec_parts)
		if view:
			print(view_reg)
		# import sys
		# print(f"{platform.platform() = }, {platform.system() = }")
		from Funcs import confirm
		if confirm(f"Deseja copiar automaticamente o registro para sua área de transferência?\n[S/N] >>> "):
			import clipboard
			clipboard.copy(view_reg)

	# print(f"\nAVISOS:\n Para o registro: {data_select}:\n aviso de atualização: {avisos[ 0 ][ 'avisos de atualizacoes' ][ f'{data_select}' ]}")

	def ver_reg_minimo(contas=contas, itens=itens):
		if type(contas) != type(dict()) or type(obj) != type(list()):
			from manuseio import convet_xlsx_to_contas
			# Obtem o registro em modo dicionário:
			var = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
			contas = var[ 0 ]
			reinantes = var[ 1 ]
			lideres = var[ 2 ]
			classes_c2 = var[ 3 ]
		elif type(obj) == type(list()):
			reinantes = obj[ 0 ]
			lideres = obj[ 1 ]
			classes_c2 = obj[ 2 ]
		if type(itens) != type(dict()):
			from manuseio import convert_things_to_items
			itens = convert_things_to_items(nome_arquivo=nome_arquivo)
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
								print(
									f" {format_currency(val, '', locale='pt_br')}{'$ / ' if (index % 2) == 0 else 'EXP'}",
									end="")
						print(f"""\n		-━━━━━━━━━  ✠  ━━━━━━━━━-""")
		print(f"Esta é uma versão simplificada do registro bancário NWM. Usada para atualizações rápidas,"
			  f" pequenas conferências e exibição apenas do saldo e EXP de todos ladinos,"
			  f" sem demais infoemações de contabilidade ou verificações.")

	def ver_vars(contas=contas, itens=itens):
		if type(contas) != type(dict()) or type(obj) != type(list()):
			from manuseio import convet_xlsx_to_contas
			# Obtem o registro em modo dicionário:
			var = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
			contas = var[ 0 ]
			reinantes = var[ 1 ]
			lideres = var[ 2 ]
			classes_c2 = var[ 3 ]
		if type(itens) != type(dict()):
			from manuseio import convert_things_to_items
			itens = convert_things_to_items(nome_arquivo=nome_arquivo)
		#from store import classes_c2, avisos, leis, reinantes, itens, lideres
		"""
		Ver variáveis consideradas importantes (função filha, ativa caso 'vars=True')
		Returns: vars

		"""
		if vars is True:
			# MOSTRA VARIAVEL "CONTAS" ATUAL:
			print(F"\n\n VER VARIAVEIS: \n")
			print(f"{contas=}")
			# MOSTRA VÁRIAVEL "classes_c2" ATUAL:
			print(f"\nCLASSES_C2:\n{classes_c2=}")
			# MOSTRA VÁRIAVEL "lideres"
			print(f"\nLIDERES:\n{lideres=}")
			# MOSTRA VÁRIAVEL "leis":
			#print(f"\nLEIS: \n {leis=}")
			# MOSTRA VÁRIAVEL "reinantes" ATUAL:
			print(f"\nreinantes: \n {reinantes=}")
			#print(f"\n{avisos=}\n")
			print(f"\n{itens=}\n")
		return [ contas, classes_c2, lideres, reinantes, itens ]

	if 'C' == tipo_do_registro.upper().strip() or tipo_do_registro.upper().strip() == 'COMPLETO':
		ver_reg_completo()
	elif 'M' == tipo_do_registro.upper().strip() or tipo_do_registro.upper().strip() == 'MINIMO':
		ver_reg_minimo()
	elif 'S' == tipo_do_registro.upper().strip() or tipo_do_registro.upper().strip() == 'SEM':
		ver_vars()
	else:
		while True:
			escolha = str(input(
				f"Você deve escolher a versão a ser vista do registro.\n1 = Completo,\n2 = Minimo\n3 = Ver variáveis\n >>> ")).strip()
			if escolha.isalnum() is True and escolha in [ '1', '2', '3' ]:
				break
			print(f"Valor incorreto. Tente novamente.")
		if escolha == '1':
			ver_reg_completo()
		elif escolha == '2':
			ver_reg_minimo()
		else:
			ver_vars()
	if vars is True:
		ver_vars()


def cadastrar_conta(
		nome_arquivo=nome_arquivo,
		section=None, cla=None, grana=None, EXP=None, name=None, contas=None, employ=None,
		save_in_archive=True):
	"""
	cadastra um novo indivíduo.
	Args:
		nome_arquivo: caminho + arquivo.xlsx (do excel) a qual o novo indivíduo será salvo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
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

	def check_name(nome_novo, text='O nome não pode estar em branco. Operação cancelada.', view=True):
		"""Check if name is not allocated"""
		if nome_novo.strip().split(' ')[ 0 ].strip() == "" or nome_novo.strip() == "":
			desc = f"\nAlerta de: {argv} / cadastrar_conta()>check_name() >\n - {text}"
			if view:
				print(desc)
			return desc
		return ''

	desc = f"\nAlerta de: {argv} >\n"
	from Funcs import classes_func, give_fc, confirm
	from manuseio import convet_xlsx_to_contas, convert_contas_to_xlsx
	# Obtem o registro em modo dicionário:
	if contas is None or type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	# CADASTRAR NOVO INDIVIDUO:
	# salva todos indivíduos numa lista de listas / matriz:
	ValuesToList = [ ]
	lis_clas = [ ]
	lis_person = []
	lis_sec = []
	for reino_, classes_ in contas.items():
		if reino_ != 'none' != classes_:
			lis_sec.append(reino_)
			for classe_, person in classes_.items():
				lis_clas.append(classe_)
				if person != 'none' != classe_:
					for name_, info_ in person.items():
						if name_ != 'none' and type(info_) == type(list()):
							if info_.__len__() > 3:
								money_, exp_, works_, fights, hunts, matches, parasites_murdered_, missions_, level_, patent_ = info_
							elif info_.__len__() == 2:
								money_, exp_ = info_
								works_= fights= hunts= matches= parasites_murdered_= missions_= level_= patent_ = 'none'
							else:
								money_, exp_ = 0, 0
								works_ = fights = hunts = matches = parasites_murdered_ = missions_ = level_ = patent_ = 'none'
							ValuesToList.append([ reino_, classe_, name_, money_, exp_, works_, fights, hunts, matches, parasites_murdered_, missions_, level_, patent_])
							lis_person.append(name_.lower())
	# Seleciona reino e classe:
	if section is None or cla is None or type(section) != type(cla) != type(str()):
		selecionar = confirm(f"S= Deseja selecionar seção e classe ou\n N=criar seção e classe nova? [S/N]: ")
		if selecionar:
			sc = classes_func(registro=contas)
			if sc is None:
				desc += "\n - Não foi possível escolher seção e classe. Operação cancelada."
				return desc
			classe_select, classe_value, secao_selected, secao_value, contas_da_classe, reg_classe = sc
		else:
			secao_selected = str(input("Digite o nome da seção nova: ")).strip().lower()
			classe_select = str(input("Digite o nome da classe nova: ")).strip().lower()
			desc += f"Seção {secao_selected} e classe {classe_select} foram criadas junto com a conta."
	else:
		classe_select = cla.lower().strip()
		secao_selected = section.lower().strip()
	text = check_name(secao_selected, text=f"Seção {secao_selected} incorreta. Operação cancelada.")
	text += check_name(secao_selected, text=f"Classe {classe_select} incorreta. Operação cancelada.")
	if text != '':
		return text
	# Informa nome:
	if type(name) != type(""):
		nome_novo = input(str(f" - Nome do indivíduo (não precisa escrever classe): ")).lower().strip() + f" {classe_select.lower().strip()}"
	else:
		nome_novo = name.lower().strip() + f" {classe_select.lower().strip()}"
	text = check_name(nome_novo, text=f"Nome {nome_novo} incorreto. Operação cancelada.")
	if text != '':
		return text
	# Da o saldo:
	if grana is None and EXP is None:
		print(f"\nAlerta de: {argv} >\n",f" - Agora cite o saldo de {nome_novo.title()}...")
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
	if secao_selected not in lis_sec or classe_select not in lis_clas:
		selecionar = False
	# Caso uma pessoa existente seja selecionada, informa se deseja a substituição:
	if nome_novo in lis_person:
		escolha = int(input(f"Já existe uma conta com este nome no registro. Você deseja continuar? "))
	# Seleciona os empregos:
	from manuseio import convert_works_to_employmap
	EmployMap = convert_works_to_employmap()
	if employ is None:
		print(f"\nAlerta de: {argv} >\n",F"Escolha quais empregos ele terá:\n")
		from Funcs import employ_fc
		dict_work = {}
		while employ != '':
			es, label, employ = employ_fc(registro=contas, operation='List')
			dict_work[employ] = label
			print(f"\n> {employ}\n")
			if not confirm(f"Continuar? <adicionar mais um emprego?> [S/N]: "):
				break
		for k, v in dict_work.items():
			label += v
			employ += f"{employ},"
		if employ[-1] == ',':
			employ = employ[0:-1].replace(',,', ',').strip()
	else:  # Caso emprego seja passado como parametro, valida ele:
		employ = employ.lower().strip()
		for k, v in EmployMap.items():
			if employ == v.lower().strip() or employ == k.lower().strip():
				employ = v
				label = k
				break
		else:  # Caso chegue no final do loop sem ser interrompido, significa que não encontrou correspondência.
			print(f"\nAlerta de: {argv} >\n", F"Parâmetro Employ inválido. Escolha quais empregos ele terá:\n")
			from Funcs import employ_fc
			es, label, employ = employ_fc(registro=contas, operation='List')
		if label in ['none', 'nan', 'NaN', 'None', None]:
			label = ''
	if employ == '' or label == 'none':
		employ = 'none'
		label = ''
	nome_novo = f"{label.strip().lower()}{nome_novo.strip().lower()}".replace('none', '')
	text = check_name(nome_novo, text=f"Nome 'none'/{nome_novo} incorreto. Operação cancelada.")
	if text != '':
		return text
	if confirm("Deseja manusear Partidas, Missões, Lutas, Nível e Patente?\n[S/N] >>> "):
		print(f"\nAlerta de: {argv} >\n", f'{"Use -1 para parar. Zero é o padrão.":^20}')
		patent_ = input(f"Digite a patente (Noumin/Workin/Maxin/Sennin/Supremo): ").strip().lower()
		try:
			text = ["Digite o nível [1–5]: ", "Digite quantia de lutas [int]: ", "Digite quantia de caças [int]: ", "Digite quantia de parasitas assassinados [int]: ", "Digite quantia de partidas [int]: ", "Digite quantia de missões [int]: " ]
			escolhas = []
			for e in text:
				es = int(input(e).lower().strip())
				if -1 in es:
					break
				escolhas.append(es)
			level_ = escolhas[0]
			fights = escolhas[1]
			hunts = escolhas[2]
			parasites_murdered_ = escolhas[3]
			matches = escolhas[4]
			missions_ = escolhas[5]
		except:
			fights = hunts = matches = parasites_murdered_ = missions_ = level_ = 'none'
			print(f"\nAlerta de: {argv} >\n", f"Houve um erro de index em algum dos passos. Eles serão definidos como padrão.")
	else:
		fights = hunts = matches = parasites_murdered_ = missions_ = level_ = 'none'
	# Provê o dinheiro ao Líder da Classe e Rei do Reino com a chegada do novo morador:

	# Confirma operação:
	if not confirm(f"\n - Conta a ser registrada:\n nome: {nome_novo}\nSaldo: {din}$ / {exp}EXP. Na seção: {secao_selected} e classe {classe_select}. Empregos: {employ}. Informações: {fights=}, {hunts=}, {matches=}, {parasites_murdered_=}, {missions_=}, {level_=}, {patent_=} \nConfirma?\n - [S/N] >>> "):
		print(f"\nAlerta de: {argv} >\n", f" - Operação cancelada.")
		desc += '\nConfirmação da operacão foi negada.'
		return desc
	print(f"\nAlerta de: {argv} >\n", " - Certo. Vá ao menu e digite 7 para atualizar.")
	# ---- Salva nova conta ----#
	if selecionar:
		contas[ secao_selected ][ classe_select ][ nome_novo ] = [ float(din), float(exp), employ, fights, hunts, matches, parasites_murdered_, missions_, level_, patent_ ]
	else:
		contas[secao_selected] = {classe_select: {nome_novo: [ float(din), float(exp), employ, fights, hunts, matches, parasites_murdered_, missions_, level_, patent_ ] }}
	if save_in_archive is True:
		convert_contas_to_xlsx(contas, nome_arquivo=nome_arquivo, verificar=True)
		print(f"\nAlerta de: {argv} >\n", f" - ATENÇÃO, AS MUDANÇAS FORAM SALVAS DIRETAMENTE NO ARQUIVO.")
		desc = f"desc: Cadastrado novo indivíduo ({nome_novo} com saldo de {din}$/{exp}EXP). Informações: {employ=}, {fights=}, {hunts=}, {matches=}, {parasites_murdered_=}, {missions_=}, {level_=}, {patent_=}\n (Mudança direta no arquivo)"
	else:
		desc = f"desc: Cadastrado novo indivíduo ({nome_novo} com saldo de {din}$/{exp}EXP). Informações: {employ=}, {fights=}, {hunts=}, {matches=}, {parasites_murdered_=}, {missions_=}, {level_=}, {patent_=}\n (fora do arquivo/somente var contas/Sem mudanças no arquivo)"
	return [ contas, desc, nome_novo, classe_select, secao_selected ]

#cadastrar_conta()

def verificar_presença(contas=None, registro=nome_arquivo, nome_sect=None, nome_cla=None, nome_pp=None,
					   oque_procurar: None | int = None):
	"""

	Args:
		registro: str - patch file superreg.xlsx. Commum==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
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
		print(f"\nAlerta de: {argv} >\n", f"Houve um erro na captura do arquivo <conert_xlsx_to_contas>. Operação cancelada.")
		return None
	# Realiza operação:
	if oque_procurar is None:
		while True:
			oque_procurar = str(input("Deseja procurar\n1 - seção\n2 - Classe\n3 - Pessoa\nno arquivo? [1,2,3]: "))
			if oque_procurar.isnumeric():
				if int(oque_procurar) in [ 1, 2, 3 ]:
					break
			print(f"\nAlerta de: {argv} >\n", f"Valor incorreto. Tente novamente.")
	if oque_procurar == 1:  # seção
		if nome_sect is None:
			nome_sect = str(input(f"Digite o nome do reino a ser procurado: ")).strip()
		lis_sect = list(sect.lower for sect in contas.keys())
		if nome_sect.lower() in lis_sect:
			print(f"\nAlerta de: {argv} >\n", f"Encontrado {nome_sect} em {registro}.")
			return True
		else:
			print(f"\nAlerta de: {argv} >\n",
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
			print(f"\nAlerta de: {argv} >\n", f"Encontrado {nome_cla} em {registro}.")
			return True
		else:
			print(f"\nAlerta de: {argv} >\n", f"Não encontrado {nome_cla} em {registro}.")
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
		# Verifica existência do indivíduo selecionado:
		if nome_pp.lower() in lis_persons:
			retu = [ True, f"Encontrado {nome_pp} em {registro}." ]
		else:
			print(f"\nAlerta de: {argv} >\n", f"Não encontrado {nome_pp} em {registro}.")
			retu = [ True, f"Encontrado {nome_pp} em {registro}." ]


def remover_conta(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False, name=None, classe=None, section=None):
	"""
	Remove conta da variável Contas.
	Args:
		classe: seleciona a classe da conta a ser removida
		section: seleciona seção cujo a conta pertence (Caso None, então escolha manual é feita)
		name: str = Nome da conta a ser removida
		nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2] Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
		contas: Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local
		save_in_archive: bool {True (Save) | False (Not save)}fará com que a mudança seja salva diretamente no arquivo.

	Returns: if erro: None | Desc
		else: return list(
		 contas,  # Variável contas atualizada pós operação
		 desc,  # Descrição do ocorrido
		 classe,  # Classe onde indivíduo pertence
		 section,  # Seção cujo a classe pertence
		 name,  # Nome do indivíduo
		 person  # saldo da conta removida
		  )
	"""
	desc = f"\nAlerta de: {argv} >\n"
	from Funcs import select_account_fc
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	print(f"\nAlerta de: {argv} >\n", f"SELECIONE O INDIVÍDUO: ")
	if None in [ name, classe, section ]:
		pp = select_account_fc(contas)
		if pp is None:
			desc += "\nNão foi possível obter o indivíduo. Operação cancelada."
			print(desc)
			return [ None, desc ]
		num, name, classe, section, person = pp
	try:
		qtia_persons = contas[ section ][ classe ].__len__()
		if qtia_persons >= 2:
			del contas[ section ][ classe ][ name ]
		elif qtia_persons == 1:
			contas[ section ][ classe ] = {'none': [ 'none', 'none' ]}
		desc += f"\nRemovido conta {name} de {section} - {classe}, com sucesso. quantia de indivíduos da classe: {qtia_persons - 1}."
	except:
		desc += "\nalgo não foi localizado na variável Contas. Operação cancelada. "
		print(desc)
		return [ None, desc ]
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(contas, nome_arquivo=nome_arquivo, verificar=True)
		desc += '.. A operação foi salva diretamente no arquivo.'
	return [ contas, desc, name, classe, section, person ]


def transferencia(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False,
				  name=None, classe=None, section=None,
				  name2=None, classe2=None, section2=None, movido=None):
	"""
	Transfere dinheiro de name para name2
	Args: Opcionais argumentos com padrão em None:
		classe: seleciona a classe da conta contribuente (que dará dinheiro)
		section: seleciona seção cujo o contribuente pertence (Caso None, então escolha manual é feita)
		name: str = seleciona nome do contribuente
		name2: menciona o nome do beneficiário (que receberá dinheiro)
		section2: menciona a seção do beneficiário
		classe2: str = menciona a classe onde reside o beneficiário
		movido: float = Quantos ryos serão movidos
		nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo.
		contas: dict = Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local
		save_in_archive: bool {True|False}, fará com que a mudança seja salva diretamente no arquivo.

	Returns: if erro: None | Desc
		else: return list(
		 contas,  # Variável contas atualizada pós operação
		 desc,  # Descrição do ocorrido
		 section,  # Seção cujo a classe pertence
		 nome_novo  # Nome da classe nova
		  )
	"""
	desc = f"\nAlerta de: {argv} >\n"
	from Funcs import select_account_fc, confirm
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	print(f"\nAlerta de: {argv} >\n",
		f"SELECIONE primeiro o indivíduo a transferir(perder dinheiro) e em seguida o indivíduo a ganhar o dinheiro.: ")
	if None in [ name, name2 ]:
		ValuesToList = [ ]
		for c in range(0, 2):
			pp = select_account_fc(contas)
			if pp is None:
				desc += "\nNão foi possível obter o indivíduo. Operação cancelada."
				print(desc)
				return [ None, desc ]
			if pp in ValuesToList:
				desc += "\nVocê já escolheu este indivíduo. Operação cancelada."
				print(desc)
				return [ None, desc ]
			ValuesToList.append(pp)
		print(f"\nAlerta de: {argv} >\n", f"{ValuesToList=}")
		num, name, classe, section, person = ValuesToList[ 0 ]
		num2, name2, classe2, section2, person2 = ValuesToList[ -1 ]
	try:
		if movido is None:
			movido = round(float(input(f"Quantos reais deseja mover? {name} tem {person[ 0 ]}R$ disponíveis: ")), 2)
		else:
			movido = round(float(movido))
	except ValueError:
		desc += f"\nValor {movido=} inválido. Operação cancelada."
		print(desc)
		return [ None, desc ]
	extraido = person[ 0 ] - movido
	ganho = person2[ 0 ] + movido
	print(f"\nAlerta de: {argv} >\n", f" < Saldo restante de {name.title()}: {person[ 0 ]} - {movido} = {extraido}>\n "
		  f" < Saldo total de {name2.title()}: {person2[ 0 ]} + {movido} = {ganho}")
	if extraido > person[ 0 ]:  # Caso valor seja maior que creditário realmente tenha:
		desc += f"\nO valor a ser transferido ultrapassa o valor possuído de {name}. Operação cancelada."
		print(desc)
		return [ None, desc ]
	if confirm(f"\n -> Você confirma a operação? [S/N]: ") is False:
		desc += '\nOperação cancelada pelo usuário.'
		print(desc)
		return [ None, desc ]
	try:
		contas[ section ][ classe ][ name ][ 0 ] = extraido
		contas[ section2 ][ classe2 ][ name2 ][ 0 ] = ganho
		desc += f"\nOperação bem sucedida. Movido {movido}$ de {name} para {name}"
	except:
		desc += "\nalgo não foi localizado na variável Contas. Operação cancelada. "
		print(desc)
		return [ None, desc ]
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
		desc += '.. A operação foi salva diretamente no arquivo.'
	return [ contas, desc, name, name2, movido ]


def add_classe(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False, secao_selected=None, nome_novo=None):
	"""
	Adiciona uma nova classe ao registro/contas
	Args:
		nome_novo: str = diz o nome da nova classe a ser adicionada
		section: seleciona cuja a classe pertence (Caso None, então escolha manual é feita)
		nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
		contas: Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local
		save_in_archive: bool {True (Save) | False (Not save)}fará com que a mudança seja salva diretamente no arquivo.

	Returns: if erro: None | Desc
		else: return list(
		 contas,  # Variável contas atualizada pós operação
		 desc,  # Descrição do ocorrido
		 section,  # Seção cujo a classe pertence
		 nome_novo  # Nome da classe nova
		  )
	"""
	from Funcs import secoes_func
	from controles import values_fc
	desc = f"\nAlerta de: {argv} >\n"
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		from manuseio import convet_xlsx_to_contas
		contas, reinantes, lideres, classes_c2 = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
	print(f"\nAlerta de: {argv} >\n", f" Escolha a classe ")
	if secao_selected == None:
		sc = secoes_func(registro=contas)
		if sc is not None:
			secao_selected = sc[ -2 ]
		else:
			desc += "\nHouve um erro na captura da função Funcs.secoes_func(). Operação cancelada"
			print(desc)
			return [ None, desc ]
	vals = values_fc(registro=contas)
	if vals is not None:
		vms, ems, all_sections, all_class, tot_pvms, vpms, pvms, totcontpersec, acconts, accontsdict, bolsa, bolsapersec, tesouropersec = vals
	else:
		desc += "\nHouve um erro na captura da função controles.values_fc(). Operação cancelada"
		print(desc)
		return [ None, desc ]
	if nome_novo is None:
		nome_novo = str(input("Nome da classe nova: ")).lower().strip()
	else:
		nome_novo = nome_novo.lower().strip()
	if nome_novo == "":
		desc += "\nO nome da classe não pode estar em branco. Operação cancelada."
		del nome_novo
		print(desc)
		return [ None, desc ]
	elif nome_novo in all_class:
		desc += "\nATENÇÃO: Esta classe parece já existir. Tente outros nomes. Operação cancelada."
		print(desc)
		return [ None, desc ]
	else:
		from Funcs import confirm
		if confirm(
				f"Classe a ser cadastrada: {nome_novo}\nReino Pertencente: {secao_selected}. Confirma?\n [S/N] >>> ") is False:
			desc += '\nOperação cancelada.'
			print(desc)
			return [ None, desc ]
		try:
			classes_c2[ secao_selected ].append(nome_novo)
			contas[ secao_selected ][ nome_novo ] = {'none': []}
		except:
			desc += "\nalgo não foi localizado na variável Contas. Operação cancelada. "
			print(desc)
			return [ None, desc ]
		if save_in_archive:
			from manuseio import convert_contas_to_xlsx
			convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
			desc += '.. A operação foi salva diretamente no arquivo.'
	return [ contas, desc, secao_selected, nome_novo ]


def descontar(nome_arquivo=nome_arquivo, name=None, classe=None, section=None, contas=None, dinheiro=None, exp=None,
			  save_in_archive=False):
	"""
	Desconta dinheiro e EXP a uma conta escolhida caso ela exista na variável Contas
	Args:
		classe: seleciona a classe do indivíduo
		section: seleciona seção cujo a indivíduo pertence (Caso None, então escolha manual é feita)
		name: str = Diz o nome do indivíduo a perder dinhero|EXP
		dinheiro: float = Quantos ryos serão removidos
		exp: float = quantos EXP serão removidos
		nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
		contas: Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local
		save_in_archive: bool {True (Save) | False (Not save)}fará com que a mudança seja salva diretamente no arquivo.

	Returns: if erro: None | Desc
		else: return list(
		 contas,  # Variável contas atualizada pós operação
		 desc,  # Descrição do ocorrido
		 classe,  # Classe removida
		 section,  # Seção cujo a classe pertence
		 qtia_persons  # Quantia de pessoas da classe removida
		  )
	"""
	from Funcs import select_account_fc, confirm
	from manuseio import convet_xlsx_to_contas
	desc = f"\nAlerta de: {argv} >\n"
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	if None in [ name, classe, section ]:
		print(f"\nAlerta de: {argv} >\n", f"SELECIONE o indivíduo a ter a conta descontada: ")
		ValuesToList = [ ]
		for c in range(0, 1):
			pp = select_account_fc(contas)
			if pp is None:
				print(f"\nAlerta de: {argv} >\n", f"Não foi possível obter o indivíduo. Operação cancelada.")
				return None
			if pp in ValuesToList:
				print(f"\nAlerta de: {argv} >\n", f"Você já escolheu este indivíduo. Operação cancelada.")
				return None
			ValuesToList.append(pp)
		num, name, classe, section, person = ValuesToList[ 0 ]
	try:
		if None in [ dinheiro, exp ]:
			dinheiro = round(float(input(f"Quantos reais deseja retirar? {name} tem {person[ 0 ]} reais. "
										 f"\n [float] >>> ")), 2)
			exp = round(float(input(f"Quantos EXP deseja retirar? {name} tem {person[ 1 ]} EXP. \n [float] >>> ")), 2)
		else:
			dinheiro = round(float(dinheiro), 2)
			exp = round(float(exp), 1)
	except ValueError:
		desc += "\nValores inválidos. Operação cancelada."
		print(desc)
		return [ None, desc ]
	extraido = [ float(person[ 0 ]) - dinheiro, float(person[ 1 ]) - exp ]
	print(f"\nAlerta de: {argv} >\n", f" < Saldo restante de {name.title()}: {person[ 0 ]} - {dinheiro} = {extraido[ 0 ]}>\n "
		  f" < EXP: {person[ 1 ]} - {exp} = {extraido[ 1 ]}")
	if confirm(f"\n -> Você confirma a operação? \n[S/N] >>> ") is False:
		desc += '\nOperação cancelada.'
		print(desc)
		return [ None, desc ]
	try:
		contas[ section ][ classe ][ name ] = extraido
		desc += f"\nExtraído {extraido} de {name} classe {classe} da seção {section}, com sucesso. "
	except:
		desc += "\nalgo não foi localizado na variável Contas. Operação cancelada. "
		print(desc)
		return [ None, desc ]
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
		desc += 'A operação foi salva diretamente no arquivo.'
	return [ contas, desc, name, dinheiro, exp ]


def abonar(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False, name=None, classe=None, section=None):
	"""
	Abona dinheiro e EXP a uma conta escolhida caso ela exista na variável Contas
	Args:
		classe: seleciona a classe a ser removida
		section: seleciona cujo a classe pertence (Caso None, então escolha manual é feita)
		nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
		contas: Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local
		save_in_archive: bool {True (Save) | False (Not save)}fará com que a mudança seja salva diretamente no arquivo.

	Returns: if erro: None | Desc
		else: return list(
		 contas,  # Variável contas atualizada pós operação
		 desc,  # Descrição do ocorrido
		 classe,  # Classe removida
		 section,  # Seção cujo a classe pertence
		 qtia_persons  # Quantia de pessoas da classe removida
		  )
	"""
	from Funcs import select_account_fc, confirm, give_fc
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	print(f"\nAlerta de: {argv} >\n", f"SELECIONE o indivíduo a ter a conta creditada: ")
	desc = f"\nAlerta de: {argv} >\n"
	if None in [ name, classe, section ]:
		pp = select_account_fc(contas)
		if pp is None:
			desc += "\nNão foi possível obter o indivíduo. Operação cancelada."
			print(desc)
			return desc
		num, name, classe, section, person = pp
	print(f"\nAlerta de: {argv} >\n Digite quantos Ryos e quantos EXP serão SOMADOS: ")
	din, exp = give_fc(registro=contas)
	extraido = [ float(person[ 0 ]) + din, float(person[ 1 ]) + exp ]
	print(f"\nAlerta de: {argv} >\n", f" < Saldo restante de {name.title()}: {person[ 0 ]} + {din} = {extraido[ 0 ]}>\n "
		  f" < EXP: {person[ 1 ]} + {exp} = {extraido[ 1 ]}")
	if confirm(f"\n -> Você confirma a operação? \n[S/N] >>> ") is False:
		desc += '\nOperação cancelada pelo usuário. '
		print(desc)
		return desc
	try:
		contas[ section ][ classe ][ name ] = extraido
	except:
		desc += "\nConta não localizada. Operação cancelada. "
		print(desc)
		return desc
	desc += f"Conta {name} de {section} - {classe}, ganhou +{din} +{exp}. "
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
		desc += 'A operação foi salva diretamente no arquivo.'
		desc += 'A operação foi salva diretamente no arquivo.'
	return [ contas, desc, name, din, exp ]


def formatar_contas(nome_arquivo=nome_arquivo, contas=None, save_in_archive=False, vezes=None):
	"""
		Formata o saldo (ryo e EXP) de vários indivíduos.
		Args:
			vezes: float = menciona o número inteiro quantos indivíduos serão tratados
			nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo.
			contas: dict = Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local
			save_in_archive: bool: True | False = fará com que a mudança seja salva diretamente no arquivo.

		Returns: if erro: None | Desc
			else: return list(
			 contas,  # Variável contas atualizada pós operação
			 desc,  # Descrição do ocorrido
			 nomes  # lista dos nomes das contas modificadas
			  )
		"""
	from Funcs import select_account_fc, confirm, give_fc
	from controles import list_persons_fc
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	all_persons = list_persons_fc(registro=contas)
	desc = f"\nAlerta de: {argv} >\n"
	if len(all_persons) == 1:
		vezes = 1
	elif len(all_persons) < 1:
		print(f"\nAlerta de: {argv} >\n", F"Não há indivíduos no registro. Operação cancelada.")
		desc += '\nTentativa falha por registro estar sem indivíduos.'
		return None
	if vezes is None:
		while True:
			vezes = str(input(
				f"QUANTOS INDIVÍDUOS DESEJA REMANEJAR? (-1 para cancelar, -2 para selecionar todos) \n [0 ~ {len(all_persons)}] >>> "))
			if vezes.isnumeric():
				vezes = int(vezes)
				if vezes == -1:
					print(f"\nAlerta de: {argv} >\n", 'cancelando...')
					desc += '\nOperação cancelada pelo usuário'
					return None
				elif vezes == -2:
					vezes = len(all_persons)
				if vezes <= len(all_persons) and vezes > 0:
					break
			print(f"\nAlerta de: {argv} >\n", F"Tente novamente.")
	print(f"\nAlerta de: {argv} >\n", f"SELECIONE o indivíduo a ter a conta alterada: ")
	ValuesToList = [ ]
	nomes = [ ]
	c = 0
	while c < vezes:
		pp = select_account_fc(contas)
		print(f"\nAlerta de: {argv} >\n", f" INDIVÍDUOS SELECIONADOS: {c} - {nomes}")
		if pp is None:
			desc += "\nNão foi possível obter o indivíduo. Operação cancelada."
			print(desc)
			return None
		elif pp in ValuesToList:
			print(f"\nAlerta de: {argv} >\n", "Você já escolheu este indivíduo. Tente novamente.")
			continue
		else:
			ValuesToList.append(pp)
			num, name, classe, section, person = ValuesToList[ -1 ]
			nomes.append(name)
			print(f"\nAlerta de: {argv} >\n", F"Digite quantos Ryos e quantos EXP serão FIXADOS (remanejo, não adição nem subtração) ")
			din, exp = give_fc(registro=contas)
			saldo = [ din, exp ]
			print(f"\nAlerta de: {argv} >\n", f" < Saldo de {name.title()}: {saldo}>\n ")
			if confirm(f"\n -> Você confirma a operação? \n[S/N] >>> ") is False:
				print(f"\nAlerta de: {argv} >\n", f'Operação cancelada.')
				continue
			try:
				contas[ section ][ classe ][ name ] = saldo
			except:
				desc += "\nConta não localizada. Operação cancelada. "
				print(desc)
				return [ None, desc ]
		c += 1
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
		desc += 'A operação foi salva diretamente no arquivo.'
	return [ contas, desc, nomes ]


def add_section(nome_arquivo=nome_arquivo, classes_c2=None, contas=None, save_in_archive=False, nome_novo=None):
	"""
	adiciona uma seção caso ela não exista na variável Contas
	Args:
		nome_novo: define o nome da seção nova
		nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
		classes_c2: dict(key='Nome_section', value=str('classes into a section'))
		contas: Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local
		save_in_archive: bool {True (Save) | False (Not save)}fará com que a mudança seja salva diretamente no arquivo.

	Returns: if erro: None | Desc
		else: return list(
		 contas,  # Variável contas atualizada pós operação
		 desc,  # Descrição do ocorrido
		 classe,  # Classe removida
		nome_novo  # Nome da seção nova
		  )
	"""
	desc = f"\nAlerta de: {argv} >\n"
	# Obtem o registro em modo dicionário:
	# Informa nome:
	if type(nome_novo) != type(""):
		nome_novo = input(
			str(f" - Nome da seção nova: ")).lower().strip().replace('_', ' ')
	else:
		nome_novo = nome_novo.lower().strip().replace('_', ' ')
	if nome_novo.split(' ')[ 0 ].strip() == "" or nome_novo.split(' ')[-1].strip() == '':
		desc += "\n - O nome não pode estar em branco. Operação cancelada."
		return desc
	# Captura variável contas e classes_c2:
	if type(contas) != type(dict()) or type(classes_c2) != type(dict()):
		from manuseio import convet_xlsx_to_contas
		# Obtem o registro em modo dicionário:
		var = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
		contas = var[ 0 ]
		classes_c2 = var[ 3 ]
	all_sections = list(contas.keys())
	if nome_novo in all_sections:
		desc = f"\nAlerta de: {argv} >\n ATENÇÃO: Essa seção {nome_novo=} parece já existir. Tente outros nomes. Operação cancelada."
		print(*desc)
		return desc
	from Funcs import confirm
	if confirm(f"Seção nova a ser cadastrada: {nome_novo}. Confirma?\n [S/N] >>> ") is False:
		desc = f"\nAlerta de: {argv} >\n", 'operação cancelada pelo usuário.\n'
		return desc
	classes_c2[ nome_novo ] = [ None ]
	try:
		contas[ nome_novo ] = {'none': {'none': [ 'none', 'none' ]}}
	except:
		desc += "\nalgo deu errado na operação 'add_section()' e variável Contas. Operação cancelada. "
		print(desc)
		return desc
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(nome_arquivo=nome_arquivo, contas=contas, verificar=True)
		desc += 'A operação foi salva diretamente no arquivo.'
	return [ contas, desc, nome_novo ]


def remover_classe(classe=None, section=None, nome_arquivo=nome_arquivo, contas=None, save_in_archive=False):
	"""
	remove uma classe escolhida caso ela exista na variável Contas
	Args:
		classe: seleciona a classe a ser removida
		section: seleciona cujo a classe pertence (Caso None, então escolha manual é feita)
		nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
		contas: Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local
		save_in_archive: bool {True (Save) | False (Not save)}fará com que a mudança seja salva diretamente no arquivo.

	Returns: if erro: None | Desc
		else: return list(
		 contas,  # Variável contas atualizada pós operação
		 desc,  # Descrição do ocorrido
		 classe,  # Classe removida
		 section,  # Seção cujo a classe pertence
		 qtia_persons  # Quantia de pessoas da classe removida
		  )
	"""
	desc = f"\nAlerta de: {argv} >\n"
	#desc += '\nOperação cancelada'
	from manuseio import convet_xlsx_to_contas
	from Funcs import classes_func, confirm
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	# Obtem classe e seção caso não definidas:
	if type(classe) != type(str()) or section is None:
		print(f"\nAlerta de: {argv} >\n", f"SELECIONE A CLASSE: ")
		clas = classes_func(contas)
		if clas is None:
			desc = f"\nAlerta de: {argv} >\n Não foi possível obter a classe. Operação cancelada."
			print(desc)
			return desc
		classe, classe_value, section, secao_value, contas_da_classe, reg_classe = clas
	# Verifica classe:
	lis_cla = [ ]
	for classes in contas.values():
		for classe_name in classes.keys():
			lis_cla.append(classe_name.strip().lower())
	if classe.strip().lower() not in lis_cla:
		desc = f"\nAlerta de: {argv} >\n", f" A classe {classe} não foi encontrada no registro. Operação cancelada."
		print(desc)
		return desc
	qtia_persons = contas[ section ][ classe ].__len__()
	if qtia_persons > 0:
		print(f"\nAlerta de: {argv} >\n Há {qtia_persons} contas nesta classe, sendo: {list(contas[ section ][ classe ].keys())}. ")
	if confirm(f" Você confirma a exclusão da classe e todas possíveis contas pertencentes?\n [S/N] >>> ") is False:
		desc += "\nOperação cancelada pelo usuário."
		print(desc)
		return desc
	try:
		del contas[ section ][ classe ]
		desc += f'\nDeletado classe {classe} com {qtia_persons} indivíduos, da seção {section}.'
	except:
		desc += "\nalgo não foi localizado na variável Contas. Operação cancelada. "
		print(desc)
		return desc
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(contas, nome_arquivo=nome_arquivo, verificar=True)
		desc += 'A operação foi salva diretamente no arquivo.'
	return [ contas, desc, classe, section, qtia_persons ]


def remover_secao(section=None, nome_arquivo=nome_arquivo, contas=None, save_in_archive=False):
	"""
	remove uma seção escolhida caso ela exista na variável Contas
	Args:
		section: seleciona a seção a ser removida
		nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
		contas: dict = Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local. Padrão==None (pega Contas do arquivo)
		save_in_archive: bool {True (Save) | False (Not save)}fará com que a mudança seja salva diretamente no arquivo.

	Returns: if erro: None | Desc
		else: return list(
		 contas,  # Variável contas atualizada pós operação
		 desc,  # Descrição do ocorrido
		 section,  # nome da Seção a ser removida
		 qtia_persons  # Quantia de pessoas da classe removida
		  )
	"""
	desc = f"\nAlerta de: {argv} >\n"
	#desc += '\nOperação cancelada'
	from manuseio import convet_xlsx_to_contas
	from Funcs import classes_func, confirm
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	# Obtem classe e seção caso não definidas:
	if type(section) != type(str()):
		print(f"\nAlerta de: {argv} >\n", f"SELECIONE A SEÇÃO: ")
		clas = classes_func(contas)
		if clas is None:
			desc += "\nNão foi possível obter a classe. Operação cancelada."
			print(desc)
			return desc
		classe, classe_value, section, secao_value, contas_da_classe, reg_classe = clas
	else:
		section = section.strip().lower()
	# Verifica classe:
	lis_cla = [ ]
	lis_sec = [ ]
	for sect, classes in contas.items():
		sect = sect.strip().lower()
		lis_sec.append(sect)
		if sect == section:
			for classe_name in classes.keys():
				lis_cla.append(classe_name.strip().lower())
	if section.strip().lower() not in lis_sec:
		desc += f"\n A seção {section} não foi encontrada no registro. Operação cancelada."
		print(desc)
		return desc
	print(f"\nAlerta de: {argv} >\n", F"Há {lis_cla.__len__()} classes nesta seção, sendo: {list(contas[ section ].keys())}. ")
	if confirm(f" Você confirma a exclusão da seção e todas possíveis classes e contas pertencentes?\n [S/N] >>> ") is False:
		desc += "\nOperação cancelada pelo usuário."
		print(desc)
		return [ None, desc ]
	try:
		del contas[ section ][ classe ]
		desc += f'\nDeletado seção {section}.'
	except:
		desc += "\nalgo não foi localizado na variável Contas. Operação cancelada. "
		print(desc)
		return desc
	if save_in_archive:
		from manuseio import convert_contas_to_xlsx
		convert_contas_to_xlsx(contas, nome_arquivo=nome_arquivo, verificar=True)
		desc += 'A operação foi salva diretamente no arquivo.'
	return [ contas, desc, section ]


def Help(cmd=None):
	from Metadados_banco import github, requires_python
	if cmd == None:
		print(f"\nAlerta de: {argv} >\n", "HELP & DESCRIPTION \n	 N.W.M BANK.\n Este é um programa de código abérto, desenvolvido "
			  "para um sistema de game via Chat usando Bots para dadas tarefas.\n Também é usado para ensinamentos "
			  "e demonstrações, neste caso, muitos trechos podem ter sido criados a fins de demostração à 'alunos'.\n"
			  f"Github: {github}\n"
			  f"Você deve ter um compilador de código python, executando a versão {requires_python}, "
			  "de preferência use a versão 3.12. Instale as dependências descritas em 'dependences.txt' "
			  "caso necessário (pode usar' cd <local_onde_script_está>' e 'pip install <nome_pacote>', "
			  "em algum terminal (termux/cmd/ssh/power shell, integrado, etc).\n"
			  "		Você pode obter mais informações em 'Metadados_banco.py' ou procurando o 'read.me' do código. \n"
			  "		Funcionamento: Você deve executar o __main__.py. Este script agrupa todas as operações úteis ao "
			  "usuário. Cada operação, pode chamar alguma função do script 'Usages.py'. Este contém funções de operações"
			  " de remoção/adição e visualização da varíavel contas, obtida pelo arquivo 'superreg.xlsx'. O arquivo "
			  "'superreg.xlsx' armazena todas as contas em 5 colunas (seção, classe, nome, money, exp). Cada linha "
			  "sendo uma conta. O módulo 'manuseio.py' trata de manusear os arquivos, como criar, escrever/reescrever, "
			  "localizar e obter em modo de uso do programa (como var 'contas') o arquivo já mencionado e operações "
			  "parecidas com o arquivo 'BACKUP.TXT', o qual guarda registros e variáveis antigas. \n"
			  " O script controles.py agrega ao sistema de inflação, obtendo dados monetários e outros índices que definirão, no RPG, a situação de cada indivíduo.\n"
			  "Já o script 'Funcs.py', porta funções para agilizar todos os outros scripts citados acima.  Estes são os principais documentos/arguivos do programa.\n\n"
			  "COMO USAR:\n Você pode:\n"
			  "1 - manusear diretamente o arquivo exel 'superreg.xlsx' e ainda usar o programa apenas para obter a visualização do registro bancário (/see)\n"
			  "2 - Usar os númeos de cada operação em '__main__.py', realizando uma operação por vez\n"
			  "3 - Usar os comandos de cada operação de '__main__.py'. Tal qual '/ADD_CLA -Sect=reino_X "
			  "-Classe=Nome_classe_nova'. Note que neste caso, a sintax é 1- comando (/ADD_CLA), 2- argumentos (-Sect=X)."
			  " Quando definir argumentos, use '_' underline no lugar de espaços.\n"
			  "4- Você também pode buscar ajuda usando '/help <comando>', como '/help /ADD_CLA'.")
	else:
		from manuseio import convert_contas_to_xlsx
		cmd = cmd.replace('/', '').strip().lower()
		try:
			lis = {'see': ver_contas, 'add_co': cadastrar_conta, 'del_co': remover_conta, 'transf': transferencia,
				   'des_co': descontar, 'soma_co': abonar, 'add_cla': add_classe, 'fv_co': formatar_contas,
				   'add_sec': add_section, '/ok': convert_contas_to_xlsx, 'del_cla': remover_classe,
				   'ver_vars': ver_contas,
				   'auto_save': f'{cmd} == Faz com que as mudanças sejam salvas em tempo-real, mas ainda não aloca no Backup'
								f' a var Contas. save=False (padrão, não salvar automaticamente) '
								f'//save=True (ligar save automático)',
				   'help': Help, 'sel_reg': select_backup, 'ok': save_backup}
			print(help(lis[ cmd ]))
		except KeyError as msg:
			print(f"\nAlerta de: {argv} >\n", f"\n{KeyError}: {msg}\n Não foi possível localizar a descrição de ajuda da função citada.\n")

	return None


def validar(contas=None, nome_arquivo=nome_arquivo):
	"""
		Compara a variável contas atual com a variável contas capturada momentaneamente do arqivo, para atestar se o arquivo está atualizado com as últimas informaçoes.
		Args:
			section: seleciona a seção a ser removida
			nome_arquivo: str = Caso 'contas=None', é pego objeto Contas novo diretamente do tal arquivo. Padrão==localizar_arquivo(criar=True, test_open=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx')[2]
			contas: dict = Caso contas != None, as operações não serão feitas com o registro em arquivo, mas sim com o objeto Contas, que pode já estar diferente do superreg.xlsx (registro em arquivo). Mudança local. Padrão==None (pega Contas do arquivo)

		Returns: True if contas_atual==contas_do_arquivo (verdadeiro caso arquivo atualizado) else False
		"""
	desc = f"\nAlerta de: {argv} >\n"
	from manuseio import convet_xlsx_to_contas
	# Obtem o registro em modo dicionário:
	if type(contas) != type(dict()):
		contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)[0]
	# Obtem classe e seção caso não definidas:
	contas2 = str(convet_xlsx_to_contas(local=None, nome_arquivo=nome_arquivo, modo='rb')).replace('"', '').replace("'",
																													"").strip().lower()
	contas = str(contas).replace('"', '').replace("'", "").strip().lower()
	return True if contas2 == contas is True else False


def save_backup(contas=None, nome_arquivo='BACKUP.txt'):
	"""
	Salva a var contas atual no arquivo de backup....
	Args:
		contas:
		nome_arquivo:

	Returns: [ListBackup, desc]

	"""
	if type(contas) != type(dict()):
		from manuseio import convet_xlsx_to_contas
		contas = convet_xlsx_to_contas(nome_arquivo="superreg.xlsx")
	from manuseio import convert_contas_to_xlsx
	from Funcs import atual_data
	from Historico import contas_antigas
	data_atual = atual_data()
	desc = retorno = convert_contas_to_xlsx(contas=contas, nome_arquivo="superreg.xlsx", verificar=True)
	comment = str(input("Digite um comentário do registro atual a ser salvo (Não precisa de data): "))
	if desc is not None:
		print(f"\nAlerta de: {argv} >\n", f" salvo {nome_arquivo}\n - com sucesso.")
		from manuseio import manuseio_backup
		ListBackup = [ [ "REG", data_atual, comment, contas ] ]
		manuseio_backup(operation="ADD", arquivo='BACKUP.txt', ListBackup=ListBackup)
		desc += ' REGISTRO atual foi SALVO com sucesso.'
		retorno = [ ListBackup, desc ]
		contas_antigas.append([ data_atual, contas ])
	return retorno


def select_backup(tipo='REG', arquivo='BACKUP.txt', contas=None):
	"""
	Percorre o arquivo de backup e seleciona o item a ser resgatado.
	Args:
		tipo:
		arquivo:

	Returns:

	"""
	from manuseio import manuseio_backup, convert_contas_to_xlsx
	from Funcs import confirm
	ListBackup = manuseio_backup(operation='C', arquivo=arquivo)
	print(f"\nAlerta de: {argv} >\n", f"ESCOLHA: ")
	desc = f"\nAlerta de: {argv} >\n"
	for pos, item in enumerate(ListBackup):
		print(f"{'-' * 10}>{pos:^5}<{'-' * 10}")
		tip = item[ 0 ]
		data = item[ 1 ]
		comment = item[ -2 ]
		conts = item[ -1 ]
		if tip.strip().upper() == tipo.strip().upper():
			print(f"	[ {data = }\n	comentário: {comment}\n 	item: {conts}\n	]")
	while True:
		es = str(input(f'[0~{pos}] >>> '))
		if es.isnumeric():
			es = int(es)
			if es >= 0 and es <= pos:
				break
	if confirm(f"SELECIONADO: {pos}  == {ListBackup[ es ]}\n Confirma?\n [S/N] >>> ") is False:
		desc += '\nOperação cancelada pelo usuário.'
		print(desc)
		return desc
	resgatado = ListBackup[ es ]
	data = resgatado[ 1 ]
	item = resgatado[ 3 ]
	if confirm(f"Você deseja fazer backup do registro anterior antes de capturar o registro novo/antigo?\n[S/N] >>> "):
		if type(contas) != type(dict()):
			from manuseio import convet_xlsx_to_contas
			contas = convet_xlsx_to_contas(nome_arquivo="superreg.xlsx")
		desc = save_backup(contas=contas)[ 0 ]
	desc += f".. Do backup, Foi pego um registro do dia {data}, como registro principal."
	contas = convert_contas_to_xlsx(contas=item)
	return [ contas, desc ]


def feitosemon():
	from Funcs import atual_data
	data_atual = atual_data()
	Rank = {'nome': {'lutas': 0, 'partidas': 0, 'caças': 0, 'missões': 0, 'parasitas assassinados': 0, 'nível atual': 0,
					 'patente atual': 1},
			'nome2': {'lutas': 0, 'partidas': 0, 'caças': 0, 'missões': 0, 'parasitas assassinados': 0,
					  'nível atual': 0, 'patente atual': 4}}
	desc = f"\nAlerta de: {argv} >\n"
	print(f"\n(SELECIONADO: RANK DE FEITOS EM ON)\n")
	# --- Definições de Vars. ---#
	# --- Código ---#
	# -- flag --#
	cont_loop2 = cont_loop1 = total = Nível_Considerado = 0
	print(
		f".   ~┏─━─━─━─━─━∞♟️∞━─━─━─━─━─┓~",
		f"```-=❢=-``` *RANK DE FEITOS EM ON* ```-=❢=-```",
		f"    ~┗─━─━─━─━─━∞♟️∞━─━─━─━─━─┛~\n",
		f"> _Em ordem de 'chegada' - {data_atual}_\n"
		f'      °==========° """ °==========°"', sep='\n', end='\n\n')
	for name, ranks in Rank.items():
		cont_loop1 += 1
		print(F"\n-> {cont_loop1} - {name.title()}: ", end='\n〖')
		cont_loop2 = 0
		Nível_Considerado = 0  # Sempre que muda de pessoa, nível considerado reseta
		for feito, qtia in ranks.items():
			cont_loop2 += 1
			if feito != 'nível atual' and feito != 'patente atual':
				print(f" ```.{qtia} {feito.title().strip()}.``` ", end='/')
				total += qtia
			for c in range(1, qtia + 1):
				if feito == 'lutas':  # A cada 4 lutas = +1 nivel
					if c % 4 == 0:
						Nível_Considerado += 1
				elif feito == "partidas":
					if c % 4 == 0:
						Nível_Considerado += 1
				elif feito == "caças":
					if c % 2 == 0:
						Nível_Considerado += 1
				elif feito == "missões":
					Nível_Considerado += 1
				elif feito == 'parasitas assassinados':
					if c % 2 == 0:
						Nível_Considerado += 1
			if cont_loop2 == 4:
				print(f" *({total})* 〗")
				total = 0
		print(f"- Nível Considerado: ", end='')
		if Nível_Considerado <= 5:
			print(f"{Nível_Considerado}/Noumin")
		elif Nível_Considerado <= 10:
			print(f"{int(Nível_Considerado / 2)}/Workin")
		else:
			if Nível_Considerado >= 6 and Nível_Considerado < 100:
				Nível_Considerado = 5
				print(f"{int(Nível_Considerado / 3)}/Maxin")
			elif Nível_Considerado <= 150:  # Entre 100 e 150
				print(f"01/SÁBIO *SENNIN* ")
			elif Nível_Considerado <= 200:  # Entre 151 e 200:
				print(f"02/SÁBIO *SENNIN* ")
			elif Nível_Considerado <= 300:  # Entre 201 e 300:
				print(f"03/SÁBIO *SENNIN* ")
			elif Nível_Considerado <= 400:  # Entre 301 e 400:
				print(f" *01/SUPREMO* ")
			elif Nível_Considerado <= 600:  # Entre 401 e 500:
				print(f" *02/SUPREMO* ")
			elif Nível_Considerado > 999:
				print(f" *SUPREMO SÁBIO ABSOLUTO - PATENTE MÁXIMA* ")
		if feito == 'nível atual' or feito == 'patente atual':
			if feito == 'patente atual':
				if qtia <= 1:
					_qtia = 'noumin'
				elif qtia == 2:
					_qtia = 'workin'
				elif qtia == 3:
					_qtia = 'maxin'
				elif qtia == 4:
					_qtia = 'sennin'
				else:
					_qtia = '?'
				print(f'- Patente atual: {Rank[name]["nível atual"]}/{_qtia.title()}')
	print(f"\n\n_(apenas lutas/caça/partidas/missões, válidas e processadas no grupo Banco, são contadas)_",
		  f"_Lutas contadas de 1/1/22 a 27/01/2023 - (espaço perdido) + 20/02/2024 -> hoje_",
		  f"_caças contadas de 4/4/22 a 27/01/2023 - (espaço perdido) + 20/02/2024 -> hoje_",
		  f"_partidas contadas de 27/7/22 a 27/01/2023 - (espaço perdido) + 20/02/2024 -> hoje_",
		  f"_missões contadas de 17/4/22 a 27/01/2023 - (espaço perdido) + 20/02/2024 -> hoje_",
		  f"_Ou seja,, começaram dia X/2022, pararam dia Y/2023, e contagem voltou então dia N/2024 até hoje (ano de 2023 perdido. 2022 sem garantias também)_",
		  F"A CADA 4 lutas = +1 lvl, 4 Partidas = +1lvl, 2 Caças = +1lvl, 1 Missão = +1lvl. A CADA 6 Níveis UP de Patente",
		  f"PATENTES POR NÍVEIS: 0 - 5: NOUMIN, 6 - 10: WORKIN, 11 - 100: MAXIN; 101 - 150: SENNIN, 150 - 200: SÁBIO SENNIN, 201 - 300: SENNIN SUPREMO, 400 = SUPREMO, 600 = SÁBIO SUPREMO, 1.000 = SUPREMO SÁBIO ABSOLUTO "
		  , sep='\n', end='\n.\n')
	print(f"\n{Rank = }\n")
	print(f"Operação concluída. Digite 7 para validar.")
	print(f"\n", "-=" * 15, end="-\n")
	desc += f"\nFoi visto o Rank de Feitos em ON"
	end = True
	# -- Deleta as var usadas --#
	# -- flag --#
	if desc == '':
		desc += '\nNone'
	if end == True:
		finalizacao = 'Operação bem-sucedida.'
	elif end == False:
		finalizacao = 'Operação interrompida ou falha.'
	elif end == None:
		finalizacao = 'Operação em aberto ou não conclusiva.'
	finalizacao += f' {desc}.'
	return finalizacao


def mundar_todas_captais():
	pass

