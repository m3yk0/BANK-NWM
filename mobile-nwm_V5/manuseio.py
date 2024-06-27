"""
V 4.6.1 Bank Mobile - V 2 of this code
"""
import os.path as path
from typing import  Any
argv = 'manuseio.py'

dir = 'START-NWM/mobile-nwm_V5'
complete_dir = path.abspath(path.expanduser(path.expandvars(".")))




def criar_arquivo(local='START-NWM/mobile-nwm_v5', nome_arquivo='superreg.xlsx',
				  colunas=[ '', 'SECTION', 'CLASSE', 'PERSON', 'MONEY', 'EXP', 'WORKS',"FIGHTS", "HUNTS", "MATCHES", "PARASITES_MURDERED", "MISSIONS", "LEVEL", "PATENT" ],
				  mini_data=[ [ 'reino da folha', 'inu', 'meeh', 0, 0, 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none'] ], pandas=False):
	"""
	Usado para ocorrencia de <create_file==True> para tentar criar o arquivo faltante
	Returns:
		create_file # create_file bool.
			If True == o arquivo <nome_arquivo> precisa ser criado.
			False == <nome_arquivo> já joi criado no <patch_atual>

	"""
	from pandas import DataFrame
	create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
		criar=False, text=False, dir=local, arquivo=nome_arquivo, modo='w', pandas=pandas, test_open=True)
	if create_file is True and correspondencia in patch_atual:
		if pandas is True:
			# Crie o arquivo e Insere dados básicos:
			df = DataFrame(data=mini_data, columns=colunas)
			df.to_excel(nome_arquivo)
			arquivo_retornado = localizar_arquivo()[ -1 ]
			create_file = False
			print(F"\n Alerta de: {argv}:\n >Arquivo criado com pandas.df.toexcel")
		else:
			try:
				open(complete_archive, 'a')
				create_file = False
			except:
				create_file = True
		if arquivo_retornado is None:
			print(f'\nAlerta de: {argv}\n> ATENÇÃO: Não conseguimos construir o arquivo: {nome_arquivo} no diretório atual \n',
				  f'({patch_atual}). O programa pode não funcionar corretamente.')
	elif create_file is True and correspondencia not in patch_atual:
		print(f'\nAlerta de: {argv}\n> É necessário encontrar ou criar o diretório {patch_esperado}. ')
	return create_file


def localizar_arquivo(criar=False, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx', modo='rb',
					  pandas=False, test_open=True):
	"""
	localiza o arquivo de registro de pps necessário para o uso básico do programa.
	Args:
		text: True == printa os textos

	Returns: list(
		create_file # create_file bool. If True == o arquivo <nome_arquivo> precisa ser criado. False == <nome_arquivo> já joi criado no <patch_atual>
		patch_atual # diretório onde o arquivo manuseio.py está rodando.
		patch_esperado # local onde <nome_arquivo> deve ser encontrado
		correspondencia # expressa se <patch_esperado> corresponde ao <patch_atual>
		onde_ir # patch correspondente a onde <nome_arquivo> deve estar
		arquivo_retornado # None == Significa que arquivo ainda não foi encontrado. != (diferente de None) então o arquivo foi criado e se refere ao arquivo então.
		)
	"""
	from os import path, getcwd, chdir
	from pandas import read_excel
	from numpy import nan
	import sys
	create_file = None  # True = precisa criar o diretorio/arquivo, False = não precisa, já existe.
	patch_esperado = correspondencia = dir
	complete_archive = path.join(dir, arquivo)
	patch_atual = getcwd()
	onde_ir = path.abspath(path.expanduser(path.expandvars(complete_archive)))
	arquivo_retornado = None
	if patch_esperado in onde_ir and arquivo in onde_ir:
		patch_esperado = complete_archive = onde_ir
	find = onde_ir.find('START-NWM/')
	onde_ir = path.join(onde_ir[ 0: find ], correspondencia)
	if correspondencia not in patch_atual:
		chdir(onde_ir)
		patch_atual = getcwd()
	complete_archive = path.join(onde_ir, arquivo)

	# print(F"\n Alerta de: {argv}:\n >\n{complete_archive=}\n{onde_ir=}\n{correspondencia=}\n{patch_atual=}")
	def abrir():
		if correspondencia in patch_atual:
			try:
				if pandas is False:
					arquivo_retornado = open(complete_archive, modo)
				if pandas is True:
					arquivo_retornado = read_excel(complete_archive, header=0).replace(nan, 'none')
					print(f"\nAlerta de: {argv} >\n", arquivo_retornado)
				create_file = False
				if text:
					print(F"\n Alerta de: {argv}:\n > Arquivo {arquivo} encontrado e aberto.\n")
			except FileNotFoundError as msg:
				if text is True:
					print(f"\n Alerta de: {argv}:\n > O arquivo {arquivo} de registro não foi localizado.")
					if criar:
						print(f"\nAlerta de: {argv}\n>  iremos criar um 'em branco'...\n")
						create_file = criar_arquivo(local=onde_ir, nome_arquivo=arquivo, pandas=pandas)
					else:
						create_file = True
		else:
			if text is True:
				print(f"\nAlerta de: {argv}\n> O diretório atual não é o diretório esperado para correr o script manuseio.py corretamente.",  # MSG
				F"\n>Diretório atual: {patch_atual}\n Diretório esperado: {onde_ir}",  # INFO
				f"\n> Tente encontrar ou então criar o diretório esperado, alocar o arquivo 'manuseio.py' para criar 'superreg.xlsx'.",  # SOLUTION
				F"\n>Este erro pode ser evitado caso siga o código do github. Caso esteja realmente seguindo o ",
				f"\ncódigo do github sem quaisquer mudanças e esteja vendo este erro, crie um 'issue'.")  # COMMENT
			create_file = True

	if test_open is True or criar is True:
		abrir()
	return [ create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado ]


def obter_arquivo(local=None, arquivo=None, modo='rb', pandas=False):
	"""

	Args:
		arquivo: str - nome do arquivo
		modo: str - Util apenas caso 'pandas=False', modo ['r', 'rb', 'a', 'w', ...]
		pandas: Bool - False == Obter registro via comando 'open' do python. True == obter registro via comando 'pandas.read_excel()'

	Returns: arquivo <None==Não obteu o arquivo. <Class

	"""
	if arquivo is None or local is None:
		create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
			criar=False, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx', modo='rb', pandas=False,
			test_open=True)
	# Captura do registro bancário:
	for tentativa in range(1, 4):
		print(F"\n Alerta de: {argv}:\n >{tentativa=}")
		if tentativa == 1:
			create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
				criar=False, text=False, dir=local, arquivo=arquivo, modo=modo, pandas=pandas, test_open=False)

			if create_file is False:
				break
		elif tentativa == 2:
			create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
				criar=True, text=True, dir=local, arquivo=arquivo, modo=modo, pandas=pandas, test_open=True)
		else:
			if arquivo == 'superreg.xlsx':
				# Tenta ultima vez no modo básico:
				funcionamento_basico = True
				colunas = [ 'REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ]
				create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
					criar=True, text=True, dir=dir, arquivo='superreg.xlsx', modo='w', pandas=False, test_open=True)
				if create_file is True:
					c_file = criar_arquivo()
					if c_file is True:
						print(F"\n Alerta de: {argv}:\n >Não foi possivel continuar o programa pois houve problemas na captura do registro.")
				# exit & break
				print(f"\nAlerta de: {argv}\n> Conseguimos tratar problemas de inicialização nivel 1 do programa e botamos o script em modo básico.")
				return None
			elif arquivo == "BACKUP.txt":
				create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
					criar=True, text=True, dir=dir, arquivo='BACKUP.txt', modo='w', pandas=False, test_open=True)
	return [ create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado ]


def valuestolist(operation, df=False, obj=None, vtl=None):
	"""

	Args:
		operation: int
			1 = convert contas to ValuesToList(contas)
			2 = convert str(contas) to ValuesToList(contas)
			3 = convert ValuesToList(contas) to contas
			4 = convert ValuesToList(things) to items
			5 = convert items to ValueToList(things)
		obj: dict() | str(dict()) to pack on list var 'ValuesToList' if operation==2|3
		vtl: list() to unpack into a dict var 'contas', if operation==1

	Returns: [contas:dict, vtl:list/ValuesToList]
	if operation ==3:
	Returns: list[list[dict(contas), dict(reinantes), dict(lideres), dict(classes)], vtl:list]

	"""
	if operation in [1, 'contas-vtl']:
		"""contas to VTL"""
		if obj is None:
			print(F"\n Alerta de: {argv}:\n >ALERTA DE 'manuseio.py': PREENCHA CORRETAMENTE os parametros da função valuestolist().")
			return None
		ValuesToList = [ ]
		c = 0
		for reino, classes in obj.items():
			for classe, person in classes.items():
				for name, features in person.items():
					data = []
					for pos, val in enumerate(features):
						if val == '' or str(val).strip().lower() == 'none':
							val = 0
						if pos == 0 or pos == 1:
							data.append(float(val)) # Caso coluna seja 'money' ou 'exp', então valor tem casas decimais como moeda
						elif pos in [2, 9]:
							data.append(str(val).strip().lower())  # caso seja coluna 'patente', ou 'works', valor é string
						else:
							data.append(int(val))  # ao contrário de moeda e string, são valores inteiros.
					data2 = [str(e).strip().lower() for e in [reino, classe, name]]
					data2.extend(data) # une as listas (nome/identificação + dados)
					ValuesToList.append(data2)
					c += 1
		vtl = ValuesToList
	elif operation in [2, 'str-contas-vtl']:
		if obj is None:
			print(F"\n Alerta de: {argv}:\n >ALERTA DE 'manuseio.py': PREENCHA CORRETAMENTE os parametros da função valuestolist().")
			return None
		"""string(contas) to VTL"""
		obj = str(obj)
		from ast import literal_eval  # ast module
		obj = literal_eval(obj)
		vtl = valuestolist(operation=1, obj=obj)[-1 ]
	elif operation in [3, 'vtl-contas']:
		"""VTL to contas"""
		if vtl is None:
			print(F"\n Alerta de: {argv}:\n >ALERTA DE 'manuseio.py': PREENCHA CORRETAMENTE os parametros da função valuestolist().")
			return None
		# Converte para uso:
		reinos = dict(dict(dict())) # dict(key='Sect', Value=dict(k='classe', v={person: [float(money), float(exp), str(works), int(fights), int(hunts), int(matches), int(parasites_murderes), int(missions), int(level), str(patent)]}))
		reinos_alocados = ['', 'none', 'nan']
		classes_alocadas: list[ Any ] = ['', 'none', 'nan']
		pps_alocados = ['', 'none', 'nan']
		reinantes = {} #Dict(key="Sect", Value=[str("Person with 'rei' work"), str(leis)]
		lideres = {}  # dict(key="sect", Value=str("Person witth 'lider' work")
		classes = {}  # dict(key=str(reino), value=list[classes]
		for cont, line in enumerate(vtl):
			if type(line[ 0 ]) == type(int()):
				reino: str = str(line[ 1 ]).lower().strip() # str [1:3, 13]
				classe: str = str(line[ 2 ]).lower().strip()
				pp: str = str(line[ 3 ]).lower().strip()
				works: str = str(line[ 6 ])
				try:
					money: float = float(line[ 4 ]) # float [4, 5]
					exp: float = float(line[ 5 ])
					# 6= works
					fights: int = int(line[ 7 ])  # int [7:12]
					hunts: int = int(line[ 8 ])
					matches: int = int(line[ 9 ])
					parasites_murderes: int = int(line[ 10 ])
					missions: int = int(line[ 11 ])
					level: int = int(line[ 12 ])
				except ValueError:
					money = exp = fights = hunts = matches = parasites_murderes = missions = level = 0
				patent: str = str(line[ 13 ]).lower().strip()
			else:
				line2 = [float(e) if str(e).isnumeric() else str(e) for e in line]
				reino, classe, pp, money, exp, works, fights, hunts, matches, parasites_murderes, missions, level, patent = line2
				#reino, classe, pp, money, exp, works, fights, hunts, matches, parasites_murderes, missions, level, patent = [ reino.lower().strip().strip(), classe.lower().strip(), pp.lower().strip(), str(money).strip().lower(), str(exp).strip().lower(), str(works).strip().lower(), str(fights).strip().lower(), str(hunts).strip().lower(), str(matches).strip().lower(), str(parasites_murderes).strip().lower(), str(missions).strip().lower(), str(level).strip().lower(), str(patent).strip().lower() ]
			if cont == 0:
				reinos_alocados.append(reino)
				reinos[ reino ] = {classe: {
					pp: [ money, exp, works, fights, hunts, matches, parasites_murderes, missions, level, patent ]}}
				classes_alocadas.append(classe)
				classes[reino] = [classe]
			else:
				if reino not in reinos_alocados and pp not in pps_alocados:
					reinos_alocados.append(reino)
					reinos[ reino ] = {classe: {pp: [ money, exp, works, fights, hunts, matches,
													  parasites_murderes, missions, level, patent ]}}
					classes_alocadas.append(classe)
					classes[reino] = classe
				elif reino in reinos_alocados and pp not in pps_alocados:  # Caso reino já alocado:
					if classe not in classes_alocadas  and pp not in pps_alocados:
						reinos[ reino ][ classe ] = {pp: [ money, exp, works, fights, hunts, matches,
														   parasites_murderes, missions, level, patent ]}
						classes_alocadas.append(classe)
						classes[reino].append(classe)
					elif classe in classes_alocadas and pp not in pps_alocados:
						reinos[ reino ][ classe ][ pp ] = [ money, exp, works, fights, hunts, matches,
															parasites_murderes, missions, level, patent ]
			if 'rei' in works and pp.strip().lower() not in ['', 'none', 'nan']:
				reinantes[reino] = pp
			if 'lider' in works and pp.strip().lower() not in ['', 'none', 'nan']:
				lideres[classe] = pp
			#classes[''].append(classe)
		obj = [reinos, reinantes, lideres, classes]
	elif operation in [4, 'vtl-itens']:
		"""VTL(items) to dict(items)"""
		if vtl is None:
			print(F"\n Alerta de: {argv}:\n >ALERTA DE 'manuseio.py': PREENCHA CORRETAMENTE os parametros da função valuestolist().")
			return None
		# Converte para uso:
		items = {str(): list([float(), str(), str(), str()])}
		itens_alocados = [ ]
		for cont, line in enumerate(vtl):
			if type(line[ 0 ]) == type(int()):  # Caso primeira coluna seja escala de números de linhas (padrão de dataframe):
				name = line[1]
				value = float(line[2])
				if line.__len__() >= 5:
					description = line[3]
					materials = line[4]
					category = line[5]
				else:
					description = materials = category = 'none'
			else:
				name = line[ 0 ]
				value = float(line[ 1 ])
				if line.__len__() >= 5:
					description = line[ 2 ]
					materials = line[ 3 ]
					category = line[ 4 ]
				else:
					description, materials, category = 'none'
			if value == 'none':
				value = 0
			if cont == 0:
				items[name] = [value, description, materials, category]
				itens_alocados.append(name)
			elif cont >= 1:
				if name not in itens_alocados and name != '':
					items[ name ] = [value, description, materials, category]
					itens_alocados.append(name)
		try:
			del items['']
		except KeyError:
			pass
		obj = items
	elif operation in [6, 'itens-vtl']:
		"""items to VTL"""
		if obj is None:
			print(F"\n Alerta de: {argv}:\n >ALERTA DE 'manuseio.py': PREENCHA CORRETAMENTE os parametros da função valuestolist().")
			return None
		ValuesToList = [ ]
		c = 0
		for name, val in obj.items():
			c += 1
			if type(val) == type(list()):
				value = val[0]
				description = str(val[1]).lower().strip()
				materials = str(val[2]).lower().strip()
				category = str(val[3]).lower().strip()
			else:
				value = val
				description = materials = category = 'none'

			ValuesToList.append([str(name).lower().strip(), float(value), description, materials, category])
		vtl = ValuesToList
	elif operation in [7, 'emp-vtl']:
		if obj is None:
			print(F"\n Alerta de: {argv}:\n >ALERTA DE 'manuseio.py': PREENCHA CORRETAMENTE os parametros da função valuestolist().")
			return None
		ValuesToList = [ ]
		c = 0
		for label, office in obj.items():
			ValuesToList.append([str(label).strip(), str(office).strip().lower()])
		vtl = ValuesToList
	elif operation in [8, 'vtl-emp']:
		"""VTL(employmap) to dict(employmap)"""
		if vtl is None:
			print(F"\n Alerta de: {argv}:\n >ALERTA DE 'manuseio.py': PREENCHA CORRETAMENTE os parametros da função valuestolist().")
			return None
		# Converte para uso:
		employmap = {str(): str()}
		itens_alocados = [ ]
		for cont, line in enumerate(vtl):
			if type(line[ 0 ]) == type(int()):  # Caso primeira coluna seja escala de números de linhas (padrão de dataframe):
				label = line[ 1 ]
				office = line[2]
			else:
				label = line[ 0 ]
				office = line[ 1 ]
			office = str(office).strip().lower()
			label = str(label).strip().lower()
			if cont == 0:
				employmap[label] = office
				itens_alocados.append(label)
			elif cont >= 1:
				if label not in itens_alocados and label != '':
					employmap[ label ] = office
					itens_alocados.append(label)
		try:
			del employmap[ '' ]
		except KeyError:
			pass
		obj = employmap
	else:
		print(F"\n Alerta de: {argv}:\n >argumento 'operation'={operation}, inválido.")
	return [ obj, vtl ]


def convet_xlsx_to_contas(local=None, nome_arquivo=None, modo='rb', see=False):
	"""

	Args:
		local:
		nome_arquivo:
		modo:

	Returns: list[dict(contas), dict(reinantes), dict(lideres), dict(classes)]

	"""
	if local is None:
		if nome_arquivo is None:
			nome_arquivo = 'superreg.xlsx'
		create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
			criar=False, text=False, arquivo=nome_arquivo, modo='rb', pandas=False, test_open=False)
		local = onde_ir
	else:
		complete_archive = path.join(local, nome_arquivo)
	# Pega o arquivo 'superreg.xlsx'
	from pandas import read_excel
	from numpy import nan
	with open(complete_archive, modo) as arquivo:
		df = read_excel(arquivo, header=0, sheet_name='Sheet1').replace(nan, 'none')  # , colunas=[ '', 'SECTION', 'CLASSE', 'PERSON', 'MONEY', 'EXP', 'WORKS',"FIGHTS", "HUNTS", "MATCHES", "PARASITES_MURDERED", "MISSIONS", "LEVEL", "PATENT" ]
		colunas_atuais = list(read_excel(arquivo, nrows=0).columns.values.tolist())
		ValuesToList = df.values.tolist()
	if see:
		print(F"\n Alerta de: {argv}:\n >Arquivo (em df): \n", df,f"\n{colunas_atuais=}")
	# Converte para uso:
	reinos = valuestolist(operation=3, vtl=ValuesToList)[0]
	return reinos


def convert_contas_to_xlsx(contas={'reino da folha': {'tesouro1': {'patrimonio publico': ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none']}}},
						   nome_arquivo=f'{complete_dir}/superreg.xlsx',
						   colunas=[ 'SECTION', 'CLASSE', 'PERSON', 'MONEY', 'EXP', 'WORKS',"FIGHTS", "HUNTS", "MATCHES", "PARASITES_MURDERED", "MISSIONS", "LEVEL", "PATENT" ],
						   verificar=False):
	"""
	Salva 'Contas' (dict usado como classe para operações o programa) em um arquivo Excel
	Args:
		contas: Objeto a ser salvo
		nome_arquivo: nome do arquivo excel
		colunas: liste as colunas desejadas (evem condizer com Contas)
		verificar: Caso True, após o salvamento do objeto, o objeto é capturado do próprio arquivo com 'convert_xlsx_to_contas()' e é feita uma comparação se os objetos são iguais (esperado) ou diferentes (algo deu errado)

	Returns: None

	"""
	desc = ''
	from pandas import DataFrame, ExcelWriter
	from numpy import nan
	# Converte para xlsx:
	if type(contas) == type(str()):
		operation = 2
	elif type(contas) == type(dict()):
		operation = 1
	else:
		desc += f"\nAlerta de: {argv}\n> \nA variável 'contas' não está correta: {contas}\nOperação cancelada."
		print(desc)
		return [None, desc]
	ValuesToList = valuestolist(operation, obj=contas)[ -1 ]
	df = DataFrame(ValuesToList, columns=colunas).replace(nan, 'none')

	if verificar:
		print(f"\nAlerta de: {argv} >\n", ValuesToList, contas,
			f"Planilha:\n{df}\n")
	# Salva:
	with ExcelWriter(nome_arquivo, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
		df.to_excel(writer, columns=colunas, sheet_name='Sheet1', engine='openpyxl')
	#writer = ExcelWriter(nome_arquivo)
	colunas_atuais = list(df.columns)
	if colunas_atuais != colunas:
		desc += f"\nAlerta de: {argv}\n>  \nHouve uma mudança nas colunas do arquivo: {colunas_atuais=}. Isto pode impactar em incompatibilidades em outras funções. Ajuste o arquivo, ou lembre-se de ajustar o parâmetro 'colunas' de cada função que as usa."
		print(desc)
	#writer.close()
	# Verifica se deu certo:
	if verificar is True:
		def verificar():
			contas2 = convet_xlsx_to_contas(nome_arquivo=nome_arquivo, see=True)[0]
			nonlocal desc
			if contas2 == contas:
				desc += f'\nAlerta de: {argv}\n> \nArquivo foi atualizado com sucesso.'
				print(desc)
			else:
				desc += f"\nAlerta de: {argv}\n> \nO arquivo não foi atualizado corretamente."
				print(desc)
				print(F"\n Alerta de: {argv}:\n >{contas=}\n{contas2=}\n Iguais?: {contas==contas2=}")
		verificar()
	return desc


def manuseio_backup(operation=None, local=None, arquivo='BACKUP.txt',
					ListBackup=[ [ 'REG', '22/05/2024-14:00:01', 'None backup', {'none': {'none': {'none': ['none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none']}}} ] ]):
	"""
	operações sobre o arquivo BACKUP.txt, cujo armazena registros antigos e outras variáveis.
	Args:
		operation: str | int
			'C' | 1 | 'CAPTURE' == capturar backup
			Returns: ListBackup
			'A' | 'ADD' | 2 == Registrar Backup adcionando novas linhas
			'F' | 'FORMAT' | 3 = Registrar Backup formatando-o por completo (perderá o arquivo antigo)
			Returns: WriteBackup
		local: str = diretório onde achar o arquivo
		arquivo: str = nome do arquivo

	Returns: None case fail

	"""
	op = str(operation).upper().strip()

	def LB_to_strbackup(ListBackup: list = ListBackup):
		"""
		Convert ListBackup to strBackup for write this str in a 'BACKUP.txt' file
		Args:
			ListBackup: list var to convert

		Returns: strBackup : str([['TIPO,-,DATE,-,VAR\n'], ['TIPO,-,DATE,VAR\n'], ...])
		"""
		strBackup = [ ]
		for itens in ListBackup:
			strB = f"{itens[ 0 ]},-,{itens[ 1 ]},-,{itens[2]},-,{itens[ -1 ]}\n"
			if strB not in strBackup:
				strBackup.append([ strB.replace('\n\n', '') ])
		return strBackup

	def strB_to_writebackup(strBackup):
		"""
		convert strBackup to a writable variable to write in 'BACKUP.txt' file
		Args:
			strBackup: var to convert into a WriteBackup

		Returns: WriteBackup : str('TIPO,-,DATE,-,VAR\nTIPO,-,DATE,VAR\n...'
		"""
		WriteBackup = ""
		for line in strBackup:
			WriteBackup = WriteBackup.join(line)
		return WriteBackup.replace('\n\n', '')

	def strB_to_listbackup(strBackup):
		"""
		convert strBackup into a ListBackup
		Args:
			strBackup: string with lines separated on a lists from base of a 'BACKUP.txt' file.

		Returns: ListBackup : list([[tipo, data, contas], [tipo, data, var], ...)

		"""
		ListBackup = [ ]
		for line in strBackup:
			sep = str(line).strip().replace('["', '').replace(']"', '').replace('\n', '').replace('\\n', '\n').replace('"]', '').split(
				',-,')
			for pos, element in enumerate(sep):
				if pos == 0:
					tipo = element.strip().upper()
				elif pos == 1:
					data = element.strip()
				elif pos == 2:
					comment = element.strip().title()
				elif pos == 3:
					if tipo.strip().upper() == 'REG':
						ValuesToList = valuestolist(operation=2, obj=element)[ -1 ]
						item = valuestolist(operation=3, vtl=ValuesToList)[ 0 ][0]
					else:
						item = element.strip()
					ListBackup.append([ tipo, data, comment, item ])
		return ListBackup

	def capture_bc():
		"""Captura BACKUP.txt retornando ListBackup, e cria caso não exista"""
		if local is None:
			complete_archive = localizar_arquivo(criar=False, text=True, dir=dir, arquivo=arquivo, modo='r',
												 pandas=False, test_open=True)[ 2 ]
		else:
			from os.path import join
			complete_archive = join(local, arquivo)
		with open(complete_archive, 'r') as arq:
			lines = arq.readlines()
			strBackup = [ ]
			for line in lines:
				strBackup.append([ line ])
			ListBackup = strB_to_listbackup(strBackup)
		return ListBackup

	def format_bc():
		"""escreve em BACKUP.txt retornando WriteBackup, e cria caso não exista"""
		LB_antigo = capture_bc()
		if LB_antigo == ListBackup or LB_antigo[ -1 ] == ListBackup[ -1 ] and op == 'A':
			aviso = (F"Escrever em BACKUP.txt é inviável, pois o que deseja salvar, já está salvo no arquivo.")
			return None
		if local is None:
			complete_archive = localizar_arquivo(criar=True, text=False, dir=dir, arquivo=arquivo, modo='a',
												 pandas=False, test_open=True)[ 2 ]
		else:
			from os.path import join
			complete_archive = join(local, arquivo)
		# Converte ListBackup object em objetos de gravação
		strBackup = LB_to_strbackup(ListBackup)
		WriteBackup = strB_to_writebackup(strBackup)
		if op in [ '2', 'A', 'ADD' ]:
			adicionados = [ ]
			with open(complete_archive, 'a') as arq:
				for strB in strBackup:
					if strB not in adicionados:
						adicionados.append(strB)
						arq.write(strB[ 0 ])
		elif op in [ '3', 'F', 'FORMAT' ]:
			with open(complete_archive, 'w') as arq:
				arq.write(WriteBackup)
		return WriteBackup

	if op == '1' or op == 'C' or op == 'CAPTURE':  # Capturar backup:
		return capture_bc()
	elif op in [ '2', 'A', 'ADD', '3', 'F', 'FORMAT' ]:  # Salvar Backup
		return format_bc()


def convert_things_to_items(local=None, nome_arquivo='superreg.xlsx' ):
	"""
	captura a planilha 'things' do arquivo excel, transforma os dados capturdos em um dicionário
	Args:
		local: local onde o arquivo está
		nome_arquivo: nome do arquivo

	Returns: dict{ str(name_item): list[float(value_item), str(description), str(materials), str(category)] }
	"""
	if local is None:
		create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
			criar=False, text=False, arquivo=nome_arquivo, modo='rb', pandas=False, test_open=False)
		local = onde_ir
	else:
		complete_archive = path.join(local, nome_arquivo)
	# Pega o arquivo 'superreg.xlsx'
	from pandas import read_excel
	from numpy import nan
	with open(complete_archive, mode='rb') as arquivo:
		df = read_excel(arquivo, sheet_name='things', header=0).replace(nan, 'none')  # , colunas=[ '', 'SECTION', 'CLASSE', 'PERSON', 'MONEY', 'EXP', 'WORKS',"FIGHTS", "HUNTS", "MATCHES", "PARASITES_MURDERED", "MISSIONS", "LEVEL", "PATENT" ]
		colunas_atuais = list(read_excel(arquivo, sheet_name='things', nrows=0).columns.values.tolist())
		ValuesToList = df.values.tolist()
	# Converte para uso:
	items = valuestolist(operation=4, vtl=ValuesToList)[ 0 ]
	return items


def convert_items_to_things(items,
						   nome_arquivo=f'{complete_dir}/superreg.xlsx',
						   colunas=[ 'NAME', "VALUE", "DESCRIPTION", "MATERIALS", "CATEGORY"], verificar=False):
	"""
	Salva 'items' (dict usado como classe para operações do programa) num arquivo Excel(nome_arquivo), na planilha 'things'.
	Args:
		items: Objeto dicionário{'nome_item': float(valor_item)} a ser salvo no arquivo excel.
		nome_arquivo: nome do arquivo excel
		colunas: liste as colunas desejadas (evem condizer com Contas)
		verificar: Caso True, após o salvamento do objeto, o objeto é capturado do próprio arquivo com 'convert_xlsx_to_contas()' e é feita uma comparação se os objetos são iguais (esperado) ou diferentes (algo deu errado)

	Returns: desc = descrição do ocorrido

	"""
	desc = ''
	from pandas import DataFrame, ExcelWriter
	from numpy import nan
	# Converte para xlsx:
	if type(items) == type(dict()):
		operation = 5
	else:
		desc += f"\nAlerta de: {argv}\n> \nA variável 'contas' não está correta: {items}\nOperação cancelada."
		print(desc)
		return [ None, desc ]
	# Ajeita items:
	#for k, v in items.copy().items():
	#	items[str(k).strip().lower()] = items.pop(k)
	#	if str(v).strip().isnumeric() is False:
	#		v = 0
	#	v = float(v)
	#	items[k] = v
	# Converte e salva:
	ValuesToList = valuestolist(operation, obj=items)[ -1 ]
	df = DataFrame(ValuesToList, columns=colunas).replace(nan, 'none')
	print(F"\n Alerta de: {argv}:\n >	Planilha:\n{df}\n")
	with ExcelWriter(nome_arquivo, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
		df.to_excel(writer, sheet_name='things', engine='openpyxl')
	colunas_atuais = list(df.columns)
	if colunas_atuais != colunas:
		desc += f"\nAlerta de: {argv}\n>  \nHouve uma mudança nas colunas do arquivo. {colunas_atuais=}. Isto pode impactar em incompatibilidades em outras funções. Ajuste o arquivo, ou lembre-se de ajustar o parâmetro 'colunas' de cada função que as usa."
		print(desc)
	# Verifica se deu certo:
	if verificar is True:
		def verificar():
			items2 = convert_things_to_items(nome_arquivo=nome_arquivo)
			nonlocal desc
			nonlocal items
			if items == items2:
				desc += f'\nAlerta de: {argv}\n> \nArquivo foi atualizado com sucesso.'
				print(desc)
			else:
				desc += f"\nAlerta de: {argv}\n> \nO arquivo não foi atualizado corretamente."
				print(desc)
				print(F"\n Alerta de: {argv}:\n >{items=}\n{items2=}\n Iguais?: {items==items2=}")
			return desc
		desc += verificar()
	return desc


def convert_works_to_employmap(local=None, nome_arquivo='superreg.xlsx', see=False ):
	"""
	captura a planilha 'things' do arquivo excel, transforma os dados capturdos em um dicionário
	Args:
		local: local onde o arquivo está
		nome_arquivo: nome do arquivo

	Returns: dict{ str(name_item): list[float(value_item), str(description), str(materials), str(category)] }
	"""
	if local is None:
		create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
			criar=False, text=False, arquivo=nome_arquivo, modo='rb', pandas=False, test_open=False)
		local = onde_ir
	else:
		complete_archive = path.join(local, nome_arquivo)
	# Pega o arquivo 'superreg.xlsx'
	from pandas import read_excel
	from numpy import nan
	with open(complete_archive, mode='rb') as arquivo:
		df = read_excel(arquivo, sheet_name='works', header=0).replace(nan, 'none')  # , colunas=[ '', 'SECTION', 'CLASSE', 'PERSON', 'MONEY', 'EXP', 'WORKS',"FIGHTS", "HUNTS", "MATCHES", "PARASITES_MURDERED", "MISSIONS", "LEVEL", "PATENT" ]
		colunas_atuais = list(read_excel(arquivo, sheet_name='works', nrows=0).columns.values.tolist())
		ValuesToList = df.values.tolist()
	if see:
		print(f'\nAlerta de: {argv}\n> Arquivo:\n',df)
	# Converte para uso:
	employmap = valuestolist(operation='vtl-emp', vtl=ValuesToList)[ 0 ]
	return employmap


def convert_employmap_to_works(employmap,
						   nome_arquivo=f'{complete_dir}/superreg.xlsx',
						   colunas=[ "LABEL", "OFFICE"], verificar=False):
	"""
	Salva 'employmap' (dict usado como classe para operações do programa) num arquivo Excel(nome_arquivo), na planilha 'things'.
	Args:
		employmap: Objeto dicionário{'nome_item': float(valor_item)} a ser salvo no arquivo excel.
		nome_arquivo: nome do arquivo excel
		colunas: liste as colunas desejadas (evem condizer com Contas)
		verificar: Caso True, após o salvamento do objeto, o objeto é capturado do próprio arquivo com 'convert_xlsx_to_contas()' e é feita uma comparação se os objetos são iguais (esperado) ou diferentes (algo deu errado)

	Returns: desc = descrição do ocorrido

	"""
	desc = ''
	from pandas import DataFrame, ExcelWriter
	from numpy import nan
	# Converte para xlsx:
	if type(employmap) == type(dict()):
		operation = 'emp-vtl'
	else:
		desc += f"\nAlerta de: {argv}\n> \nA variável 'employmap' não está correta: {employmap}.\nOperação cancelada."
		print(desc)
		return [ None, desc ]
	# Ajeita items:
	#for k, v in items.copy().items():
	#	items[str(k).strip().lower()] = items.pop(k)
	#	if str(v).strip().isnumeric() is False:
	#		v = 0
	#	v = float(v)
	#	items[k] = v
	# Converte e salva:
	ValuesToList = valuestolist(operation, obj=employmap)[ -1 ]
	df = DataFrame(ValuesToList, columns=colunas).replace(nan, 'none')
	print(F"\n Alerta de: {argv}:\n >	Planilha:\n{df}\n")
	with ExcelWriter(nome_arquivo, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
		df.to_excel(writer, sheet_name='works', engine='openpyxl')
	colunas_atuais = list(df.columns)
	if colunas_atuais != colunas:
		desc += f"\nAlerta de: {argv}\n>  \nHouve uma mudança nas colunas do arquivo. {colunas_atuais=}. Isto pode impactar em incompatibilidades em outras funções. Ajuste o arquivo, ou lembre-se de ajustar o parâmetro 'colunas' de cada função que as usa."
		print(desc)
	# Verifica se deu certo:
	if verificar is True:
		def verificar():
			employmap2 = convert_works_to_employmap(nome_arquivo=nome_arquivo, see=True)
			nonlocal desc
			nonlocal employmap
			if employmap == employmap2:
				desc += f'\nAlerta de: {argv}\n> \nArquivo foi atualizado com sucesso.'
				print(desc)
			else:
				desc += f"\nAlerta de: {argv}\n> \nO arquivo não foi atualizado corretamente."
				print(desc)
				print(F"\n Alerta de: {argv}:\n >{employmap=}\n{employmap2=}\n Iguais?: {employmap==employmap2=}")
			return desc
		desc += verificar()
	return desc

#print(convert_employmap_to_works(verificar=True, employmap={'none':'pobre-plebeu-miserável','~': 'time-devs', '€': 'elite', '±': 'med', '+': 'treinador', '☆': 'time-iluminati', '≈': 'lider', '=': 'reinante', '≠': 'eterno', '•': 'anbu', 'r¬': 'recrutador', 'l¬': 'lojista', 'd¬': 'divulgador', 'f¬': 'ferreiro', 'b¬': 'banqueiro', 'g‹': 'guia-missões', 's‹': 'supervisor', 'j‹': 'juíz', 'i‹': 'interpretador', 'm‹': 'mentor', '°°°': 'administrador', '°': 'staff', '¤': 'casado', '@': 'fan', 'ຊ': 'time-yamata'}))
#print('>', convert_items_to_things(verificar=True, items={'none': [0.0, 'none', 'none', 'none'], 'kunai': [10.0, 'none', 'none', 'none'], 'kunai_curva': [10.0, 'none', 'none', 'none'], 'shuriken': [10.0, 'none', 'none', 'none'], 'senbons': [10.0, 'none', 'none', 'none'], 'makibishi': [10.0, 'none', 'none', 'none'], 'raihashis': [10.0, 'none', 'none', 'none'], 'flecha_comum-curta(1_lote_2uni)': [10.0, 'none', 'none', 'none'], 'pena_para_escrita': [10.0, 'none', 'none', 'none'], 'vidraça_com_tinta_para_pena': [10.0, 'none', 'none', 'none'], 'hip_pouchbolsa': [50.0, 'none', 'none', 'none'], 'soprador_com_sabão': [50.0, 'none', 'none', 'none'], 'selo_explosivo': [50.0, 'none', 'none', 'none'], 'bomba_de_luz': [50.0, 'none', 'none', 'none'], 'bomba_de_fumaça': [50.0, 'none', 'none', 'none'], 'bomba_de_fumaça_mineral': [100.0, 'none', 'none', 'none'], 'fios_de_aço(1m)': [50.0, 'none', 'none', 'none'], 'guisos': [50.0, 'none', 'none', 'none'], 'pássaro_mecânico': [50.0, 'none', 'none', 'none'], 'pergaminho': [100.0, 'none', 'none', 'none'], 'fuuma_shuriken': [100.0, 'none', 'none', 'none'], 'shuriken_gigante': [100.0, 'none', 'none', 'none'], 'bomba_de_gelo': [100.0, 'none', 'none', 'none'], 'dardo_de_injeção(5_uni)': [100.0, 'none', 'none', 'none'], 'antídoto': [100.0, 'none', 'none', 'none'], 'flecha_grande(1_lote_2uni)': [100.0, 'none', 'none', 'none'], 'bomba_de_pimenta': [100.0, 'none', 'none', 'none'], 'tampões_de_ouvido': [250.0, 'none', 'none', 'none'], 'pano_de_selamento': [300.0, 'none', 'none', 'none'], 'kusari-fundo': [300.0, 'none', 'none', 'none'], 'shuriken_quadrada': [300.0, 'none', 'none', 'none'], 'mangual': [300.0, 'none', 'none', 'none'], 'ataduras(1m)': [300.0, 'none', 'none', 'none'], 'pergaminho_com_tinta_e_caneta': [400.0, 'none', 'none', 'none'], 'pinças_de_tesoura': [400.0, 'none', 'none', 'none'], 'nunchaku': [500.0, 'none', 'none', 'none'], 'katana_simples': [500.0, 'none', 'none', 'none'], 'bõ': [500.0, 'none', 'none', 'none'], 'arco': [500.0, 'none', 'none', 'none'], 'pesos_de_treinamento': [500.0, 'none', 'none', 'none'], 'rádio_comunicador_(3uni)': [500.0, 'none', 'none', 'none'], 'kusarigama': [500.0, 'none', 'none', 'none'], 'tanto': [500.0, 'none', 'none', 'none'], 'danko': [500.0, 'none', 'none', 'none'], 'esfera_explosiva': [500.0, 'none', 'none', 'none'], 'bola_de_selos_explosivos': [500.0, 'none', 'none', 'none'], 'corrente_do_bastão_de_vento': [500.0, 'none', 'none', 'none'], 'atana_mediana': [1000.0, 'none', 'none', 'none'], 'lâminas_deunai': [1000.0, 'none', 'none', 'none'], 'guarda_chuva': [1000.0, 'none', 'none', 'none'], 'braceletes_de_ferro': [1000.0, 'none', 'none', 'none'], 'boneco_de_metal': [1000.0, 'none', 'none', 'none'], 'armadura_de_chakra(protetora)': [1000.0, 'none', 'none', 'none'], 'cartões_de_informações_ninja': [1200.0, 'none', 'none', 'none'], 'etiqueta_de_selamento': [1300.0, 'none', 'none', 'none'], 'catapulta_de_shuriken_gigante': [1500.0, 'none', 'none', 'none'], 'balista': [1500.0, 'none', 'none', 'none'], 'braceletes_de_selamento': [2000.0, 'none', 'none', 'none'], 'espada_retrátil': [2000.0, 'none', 'none', 'none'], 'alto_falante_ressonante_de_eco': [2000.0, 'none', 'none', 'none'], 'foice': [2000.0, 'none', 'none', 'none'], 'lançador_de_agulhas': [2000.0, 'none', 'none', 'none'], 'johyo': [2000.0, 'none', 'none', 'none'], 'tekkõkagi': [2000.0, 'none', 'none', 'none'], 'braço_de_cabo_retrátil': [2000.0, 'none', 'none', 'none'], 'garra_de_lâmina_tripla_aprimorada': [2000.0, 'none', 'none', 'none'], 'armadura_de_batalha_shinobi': [2000.0, 'none', 'none', 'none'], 'manoplas_de_metal': [2000.0, 'none', 'none', 'none'], 'lâminas_de_chakra_de_konoha': [2000.0, 'none', 'none', 'none'], 'canhão_elétrico': [2000.0, 'none', 'none', 'none'], 'hidro-bomba_(2_uni)': [2000.0, 'none', 'none', 'none'], 'serra_circula_de_marionete': [2000.0, 'none', 'none', 'none'], 'bastão_resistente': [2500.0, 'none', 'none', 'none'], 'katana_resistente': [3000.0, 'none', 'none', 'none'], 'yodai_sensu': [3000.0, 'none', 'none', 'none'], 'lançador_de_pulso': [3000.0, 'none', 'none', 'none'], 'jidanda': [3000.0, 'none', 'none', 'none'], 'atirador_de_dardos_de_injeção': [3000.0, 'none', 'none', 'none'], 'escudo_retrátil': [3000.0, 'none', 'none', 'none'], 'corte_da_lua': [3000.0, 'none', 'none', 'none'], 'hyotan': [4000.0, 'none', 'none', 'none'], 'katana_super_resistente': [5000.0, 'none', 'none', 'none'], 'ocarina': [5000.0, 'none', 'none', 'none'], 'braço_de_perfuração_mecânica': [5000.0, 'none', 'none', 'none'], 'canhão_da_cabeça_de_leão': [5000.0, 'none', 'none', 'none'], 'canhão_de_bomba_de_chakra': [5000.0, 'none', 'none', 'none'], 'chaves_de_braços_verdantes': [5000.0, 'none', 'none', 'none'], 'traje_de_lodo': [10000.0, 'none', 'none', 'none'], 'lançador_de_shurikens': [10000.0, 'none', 'none', 'none'], 'lançador_de_kunai_portátil': [10000.0, 'none', 'none', 'none'], 'dispositivo_de_rompimento_de_chakra': [15000.0, 'none', 'none', 'none'], 'tsuru000ame': [80000.0, 'none', 'none', 'none'], 'armadura_de_chakra_(absorve)': [100000.0, 'none', 'none', 'none'], 'tobishachimaru': [200000.0, 'none', 'none', 'none'], '2045': [400000.0, 'none', 'none', 'none'], 'marionete_de_madeira_vermelha': [90000.0, 'none', 'none', 'none'], 'marionete_formiga_negra': [100000.0, 'none', 'none', 'none'], 'marionete_salamandra': [120000.0, 'none', 'none', 'none'], 'marionete_veloz': [145000.0, 'none', 'none', 'none'], 'marionete_golem': [150000.0, 'none', 'none', 'none'], 'marionete_guardiã': [140000.0, 'none', 'none', 'none'], 'marionete_guardiã_gigante': [160000.0, 'none', 'none', 'none'], 'marionete_abelha_rainha': [195000.0, 'none', 'none', 'none'], 'marionete_base': [240000.0, 'none', 'none', 'none'], 'marionete_escorpião': [280000.0, 'none', 'none', 'none'], 'marionete_automatizada': [300000.0, 'none', 'none', 'none'], 'marionete_mestresuprema': [400000.0, 'none', 'none', 'none'], 'kiba_(espadas_do_trovão)': [500000.0, 'none', 'none', 'none'], 'kusanagi_(espada_serpente)': [600000.0, 'none', 'none', 'none'], 'shibuki(respingo)': [500000.0, 'none', 'none', 'none'], 'nuibari_(grande_agulha)': [350000.0, 'none', 'none', 'none'], 'kabutowari_(rachadora_de_elmos)': [600000.0, 'none', 'none', 'none'], 'kuribiribocho_(lâmina_do_executor)': [600000.0, 'none', 'none', 'none'], 'hiramekarei_(espadas_gêmeas)': [800000.0, 'none', 'none', 'none'], 'gunbai_(arranjo_do_exército)': [600000.0, 'none', 'none', 'none'], 'gamatasu': [600000.0, 'none', 'none', 'none'], 'gamaken': [600000.0, 'none', 'none', 'none'], 'gamahiro': [600000.0, 'none', 'none', 'none'], 'gamariki': [600000.0, 'none', 'none', 'none'], 'gama': [600000.0, 'none', 'none', 'none'], 'gamagoro': [600000.0, 'none', 'none', 'none'], 'gamaken2': [600000.0, 'none', 'none', 'none'], 'gamamaru': [600000.0, 'none', 'none', 'none'], 'gamariki2': [600000.0, 'none', 'none', 'none'], 'gamatatsu': [600000.0, 'none', 'none', 'none'], 'gekomatsu': [600000.0, 'none', 'none', 'none'], 'gerotora': [600000.0, 'none', 'none', 'none'], 'osuke': [600000.0, 'none', 'none', 'none'], 'shima': [600000.0, 'none', 'none', 'none'], 'gamakichi': [600000.0, 'none', 'none', 'none'], 'ikari_wa_hebi_cobras_raivosas': [500000.0, 'none', 'none', 'none'], 'jay_ermida': [600000.0, 'none', 'none', 'none'], 'kyodaijya': [600000.0, 'none', 'none', 'none'], 'aoda': [600000.0, 'none', 'none', 'none'], 'serpentes_de_três_cabeças': [700000.0, 'none', 'none', 'none'], 'yamata_cobra_de_várias_cabeças': [800000.0, 'none', 'none', 'none'], 'aliança_fajulta': [10.0, 'none', 'none', 'none'], 'buquê_de_flores_simples': [10.0, 'none', 'none', 'none'], 'papel_de_presente_simples': [10.0, 'none', 'none', 'none'], 'vestido_fajulto': [50.0, 'none', 'none', 'none'], 'terno_fajulto': [50.0, 'none', 'none', 'none'], 'papel_de_presente': [50.0, 'none', 'none', 'none'], 'aliança_de_namoro': [50.0, 'none', 'none', 'none'], 'aliança_de_noivado': [100.0, 'none', 'none', 'none'], 'buquê_de_flores': [100.0, 'none', 'none', 'none'], 'vestido': [500.0, 'none', 'none', 'none'], 'terno': [500.0, 'none', 'none', 'none'], 'buquê_de_flores_de_luxo': [500.0, 'none', 'none', 'none'], 'aliança_de_casamento': [1000.0, 'none', 'none', 'none'], 'vestido_de_casamento': [1000.0, 'none', 'none', 'none'], 'terno_para_cerimônias': [1000.0, 'none', 'none', 'none'], 'tratamento_médico': [1000.0, 'none', 'none', 'none'], 'aliança_de_diamante': [2500.0, 'none', 'none', 'none'], 'certidão_de_responsabilidade_para_ter_pets': [5000.0, 'none', 'none', 'none'], 'transplante_oficial': [20000.0, 'none', 'none', 'none'], 'casa_comum': [40000.0, 'none', 'none', 'none'], 'casa_com_cerquinhas_brancas': [65000.0, 'none', 'none', 'none'], 'casa_gótica': [65000.0, 'none', 'none', 'none'], 'mansão': [80000.0, 'none', 'none', 'none'], 'terreno_para_casa': [80000.0, 'none', 'none', 'none'], 'terreno_geral': [90000.0, 'none', 'none', 'none'], 'seguro_eterno': [90000.0, 'none', 'none', 'none'], 'espingarda': [9000.0, 'none', 'none', 'none'], 'carabina': [9000.0, 'none', 'none', 'none'], 'metralhadora': [40000.0, 'none', 'none', 'none'], 'submetralhadora': [12000.0, 'none', 'none', 'none'], 'fuzil_de_assalto': [20000.0, 'none', 'none', 'none'], 'rifle_sniper': [25000.0, 'none', 'none', 'none'], 'revólver': [8000.0, 'none', 'none', 'none'], 'pistola': [6000.0, 'none', 'none', 'none'], 'taser': [5000.0, 'none', 'none', 'none'], 'stun_gun': [4000.0, 'none', 'none', 'none'], 'eletrodos_para_taser': [500.0, 'none', 'none', 'none'], 'bateria_para_taser_e_stun_gun': [900.0, 'none', 'none', 'none'], 'tripé': [1000.0, 'none', 'none', 'none'], 'silenciador': [30000.0, 'none', 'none', 'none'], 'munição(12_uni)': [5000.0, 'none', 'none', 'none'], 'extensor_de_mira': [1000.0, 'none', 'none', 'none'], 'binóculo_20x50': [1000.0, 'none', 'none', 'none'], 'kit_manutenção_de_armas': [1000.0, 'none', 'none', 'none'], 'colete_a_prova_de_balas': [1000.0, 'none', 'none', 'none'], 'coldre': [30.0, 'none', 'none', 'none'], 'algema_ultra_forte': [850.0, 'none', 'none', 'none'], 'kit_primeiros_socorros': [700.0, 'none', 'none', 'none'], 'combustível_para_fogo_1l': [600.0, 'none', 'none', 'none'], 'bússola': [500.0, 'none', 'none', 'none'], 'sinalizador': [500.0, 'none', 'none', 'none'], 'corda_de_alpinismo': [400.0, 'none', 'none', 'none'], 'luz_química': [50.0, 'none', 'none', 'none'], 'capacete_com_proteção_facial': [350.0, 'none', 'none', 'none'], 'amolador_de_facas': [300.0, 'none', 'none', 'none'], 'pá': [200.0, 'none', 'none', 'none'], 'picareta': [200.0, 'none', 'none', 'none'], 'canivete': [170.0, 'none', 'none', 'none'], 'soco_inglês': [170.0, 'none', 'none', 'none'], 'capacete_tático': [170.0, 'none', 'none', 'none'], 'esqueiro_zippo': [50.0, 'none', 'none', 'none'], 'ponteiro_a_laser_quente': [60.0, 'none', 'none', 'none'], 'grimório fascínios elementais (lvl1)': [1.0, 'none', 'none', 'none'], 'grimório da classe (lvl1)': [1.0, 'none', 'none', 'none'], 'grimório fascínios chave': [1.0, 'none', 'none', 'none'], 'grimório fascínios elementais (lvl2)': [2.0, 'none', 'none', 'none'], 'grimório fascínios da classe (lvl2)': [2.0, 'none', 'none', 'none'], 'grimório fascínios elementais (lvl3)': [3.0, 'none', 'none', 'none'], 'grimório fascínios da classe (lvl3)': [3.0, 'none', 'none', 'none'], 'bijuu': [100.0, 'none', 'none', 'none']}))
#print(convert_contas_to_xlsx(contas={'reino da folha': {'inuzuka': {'meeh inu': [0, 0, 0, 0, 0, 0, 0, 0, 0, 'maxin']}}}, verificar=True))
#print(convert_things_to_items())