import os.path as path
from typing import List, Any

dir = 'START-NWM/mobile-nwm'
complete_dir = path.abspath(path.expanduser(path.expandvars(dir)))
print(complete_dir)

def criar_arquivo(local='START-NWM/mobile-nwm', nome_arquivo='registro.xlsx', colunas=[ '', 'REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ], mini_data=[['reino da folha', 'inu', 'meeh', 0, 0]], pandas=False):
	"""
	Usado para ocorrencia de <create_file==True> para tentar criar o arquivo faltante
	Returns:
		create_file # create_file bool.
			If True == o arquivo <nome_arquivo> precisa ser criado.
			False == <nome_arquivo> já joi criado no <patch_atual>

	"""
	from pandas import DataFrame
	create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(criar=False, text=False, dir=local, arquivo=nome_arquivo, modo='w', pandas=pandas, test_open=True)
	if create_file is True and correspondencia in patch_atual:
		if pandas is True:
			# Crie o arquivo e Insere dados básicos:
			df = DataFrame(data=mini_data, columns=colunas)
			df.to_excel(nome_arquivo)
			arquivo_retornado = localizar_arquivo()[ -1 ]
			create_file = False
			print(f"Arquivo criado com pandas.df.toexcel")
		else:
			try:
				open(complete_archive, 'a')
				create_file = False
			except:
				create_file = True
		if arquivo_retornado is None:
			print('ATENÇÃO: Não conseguimos construir o arquivo: {nome_arquivo} no diretório atual \n',
				  f'({patch_atual}). O programa pode não funcionar corretamente.')
	elif create_file is True and correspondencia not in patch_atual:
		print('É necessário encontrar ou criar o diretório {patch_esperado}. ')
	return create_file


def localizar_arquivo(criar=False, text=False, dir='START-NWM/mobile-nwm', arquivo='registro.xlsx', modo='rb', pandas=False, test_open=True):
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
	onde_ir = path.join(onde_ir[0: find], correspondencia)
	if correspondencia not in patch_atual:
		chdir(onde_ir)
		patch_atual = getcwd()
	complete_archive = path.join(onde_ir, arquivo)
	#print(f"\n{complete_archive=}\n{onde_ir=}\n{correspondencia=}\n{patch_atual=}")
	def abrir():
		if correspondencia in patch_atual:
			try:
				if pandas is False:
					arquivo_retornado = open(complete_archive, modo)
				if pandas is True:
					arquivo_retornado = read_excel(complete_archive, header=0)
				create_file = False
				if text:
					print(F"\n Alerta de: {sys.argv}:\n > Arquivo {arquivo} encontrado e aberto.\n")
			except FileNotFoundError as msg:
				if text is True:
					print(f"\n Alerta de: {sys.argv}:\n > O arquivo {arquivo} de registro não foi localizado.")
					if criar:
						print(" iremos criar um 'em branco'...\n")
						create_file = criar_arquivo(local=onde_ir, nome_arquivo=arquivo, pandas=pandas)
					else:
						create_file = True
		else:
			if text is True:
				print(f"O diretório atual não é o diretório esperado para correr o script manuseio.py corretamente.")  # MSG
				print(f"Diretório atual: {patch_atual}\n Diretório esperado: {onde_ir}")  # INFO
				print(f"Tente encontrar ou então criar o diretório esperado, alocar o arquivo 'manuseio.py' para criar 'registro.xlsx'.")  # SOLUTION
				print(f"Este erro pode ser evitado caso siga o código do github. Caso esteja realmente seguindo o "
					  f"código do github sem quaisquer mudanças e esteja vendo este erro, crie um 'issue'.")  # COMMENT
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
		create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(criar=False, text=False, dir='START-NWM/mobile-nwm', arquivo='registro.xlsx', modo='rb', pandas=False, test_open=True)
	# Captura do registro bancário:
	for tentativa in range(1, 4):
		print(f"{tentativa=}")
		if tentativa == 1:
			create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
				criar=False, text=False, dir=local, arquivo=arquivo, modo=modo,
				pandas=pandas, test_open=False)

			if create_file is False:
				break
		elif tentativa == 2:
			create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
				criar=True, text=True, dir=local, arquivo=arquivo, modo=modo,
				pandas=pandas, test_open=True)
		else:
			if arquivo=='registro.xlsx':
				# Tenta ultima vez no modo básico:
				funcionamento_basico = True
				colunas = [ 'REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ]
				create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(criar=True, text=True, dir=dir, arquivo='registro.xlsx', modo='w', pandas=False, test_open=True)
				if create_file is True:
					c_file = criar_arquivo()
					if c_file is True:
						print(f"Não foi possivel continuar o programa pois houve problemas na captura do registro.")
						# exit & break
				print(f"Conseguimos tratar problemas de inicialização nivel 1 do programa e botamos o script em modo básico.")
				return None
			elif arquivo=="BACKUP.txt":
				create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(criar=True, text=True, dir=dir, arquivo='BACKUP.txt', modo='w', pandas=False, test_open=True)
	return [create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado ]


def valuestolist(operation=None, df=False, contas={'reino da folha': {'inu': {'meeh': [ 0, 0 ]}}}, vtl=['reino da folha', 'inu', 'meeh', 0, 0]):
	"""

	Args:
		operation: int
			1 = convert contas to ValuesToList
			2 = convert str(contas) to ValuesToList
			3 = convert ValuesToList to contas
		contas: dict() | str(dict()) to pack on list var 'ValuesToList' if operation==2|3
		vtl: list() to unpack into a dict var 'contas', if operation==1

	Returns: [contas:dict, vtl:list/ValuesToList]

	"""
	if operation == 1:
		"""contas to VTL"""
		ValuesToList = [ ]
		c = 0
		for reino, classes in contas.items():
			for classe, person in classes.items():
				for name, saldo in person.items():
					money = saldo[ 0 ]
					exp = saldo[ 1 ]
					ValuesToList.append(
						[ str(reino).lower().strip(), str(classe).lower().strip(), str(name).lower().strip(),
						  str(money).lower().strip(), str(exp).lower().strip() ])
					c += 1
	elif operation == 2:
		"""string(contas) to VTL"""
		contas = str(contas)
		contas = contas.replace('{', '').replace('}', '').replace('[', '').replace('"', '').replace(
			"'", "").replace(']', '').replace(': ', ':').strip()
		ValuesToList = contas.split(':')
		if ',' in ValuesToList[-1]:
			saldo = ValuesToList[ -1 ].replace(' ', '').split(',')
			ValuesToList[ -1 ] = saldo[ 0 ]
			ValuesToList.append(saldo[ -1 ])
	elif operation == 3:
		"""VTL to contas"""
		# Converte para uso:
		reinos = dict(dict(dict()))
		reinos_alocados = [ ]
		classes_alocadas: list[ Any ] = [ ]
		for cont, line in enumerate(vtl):
			if type(line[ 0 ]) == type(int()):
				reino = str(line[ 1 ]).lower().strip()
				classe = str(line[ 2 ]).lower().strip()
				pp = str(line[ 3 ]).lower().strip()
				money = str(line[ 4 ]).lower().strip()
				exp = str(line[ 5 ]).lower().strip()
			else:
				reino, classe, pp, money, exp = line
				reino, classe, pp = [ reino.lower(), classe.lower(), pp.lower() ]
			if cont == 0:
				reinos_alocados.append(reino)
				reinos[ reino ] = {classe: {pp: [ money, exp ]}}
				classes_alocadas.append(classe)
			else:
				if reino not in reinos_alocados:
					reinos_alocados.append(reino)
					reinos[ reino ] = {classe: {pp: [ money, exp ]}}
					classes_alocadas.append(classe)
				else:  # Caso reino já alocado:
					if classe not in classes_alocadas:
						reinos[ reino ][ classe ] = {pp: [ money, exp ]}
						classes_alocadas.append(classe)
					else:
						reinos[ reino ][ classe ][ pp ] = [ money, exp ]
			contas = reinos
	else:
		print(F"argumento 'operation', inválido.")
	return [contas, vtl]



def convet_xlsx_to_contas(local=None, nome_arquivo=None, modo='rb'):
	if local is None:
		if nome_arquivo is None:
			nome_arquivo='registro.xlsx'
		create_file, patch_atual, complete_archive, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(
			criar=False, text=False, arquivo=nome_arquivo, modo='rb',
			pandas=False, test_open=False)
		local = onde_ir
	else:
		complete_archive = os.path.join(local, nome_arquivo)
	# Pega o arquivo 'registro.xlsx'
	from pandas import read_excel
	with open(complete_archive, modo) as arquivo:
		df = read_excel(arquivo, header=0)  # , colunas=['REINO', "CLASSE", "PERSON", "MONEY", "EXP"]
		colunas_atuais = list(read_excel(arquivo, nrows=0).columns.values.tolist())
		ValuesToList = df.values.tolist()
	# Converte para uso:
	reinos = dict(dict(dict()))
	reinos_alocados = []
	classes_alocadas: list[Any] = []
	for cont, line in enumerate(ValuesToList):
		if type(line[ 0 ]) == type(int()):
			reino = str(line[ 1 ]).lower().strip()
			classe = str(line[ 2 ]).lower().strip()
			pp = str(line[ 3]).lower().strip()
			money = str(line[4]).lower().strip()
			exp = str(line[5]).lower().strip()
		else:
			reino, classe, pp, money, exp = line
			reino, classe, pp = [reino.lower(), classe.lower(), pp.lower()]
		if cont == 0:
			reinos_alocados.append(reino)
			reinos[ reino ] = {classe: {pp: [ money, exp ]}}
			classes_alocadas.append(classe)
		else:
			if reino not in reinos_alocados:
				reinos_alocados.append(reino)
				reinos[ reino ] = {classe: {pp: [ money, exp ]}}
				classes_alocadas.append(classe)
			else:  # Caso reino já alocado:
				if classe not in classes_alocadas:
					reinos[ reino ][ classe ] = {pp: [ money, exp ]}
					classes_alocadas.append(classe)
				else:
					reinos[ reino ][ classe ][ pp ] = [ money, exp ]
	return reinos


def convert_contas_to_xlsx(contas={'reino da folha': {'inu': {'meeh': [ 0, 0 ]}}}, modo='w', nome_arquivo=f'{complete_dir}/registro.xlsx',
						   colunas=['REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ], verificar=False):
	"""
	Salva 'Contas' (dict usado como classe para operações o programa) em um arquivo Excel
	Args:
		contas: Objeto a ser salvo
		modo:
		nome_arquivo: nome do arquivo excel
		colunas: liste as colunas desejadas (evem condizer com Contas)
		verificar: Caso True, após o salvamento do objeto, o objeto é capturado do próprio arquivo com 'convert_xlsx_to_contas()' e é feita uma comparação se os objetos são iguais (esperado) ou diferentes (algo deu errado)

	Returns: None

	"""
	from pandas import DataFrame, ExcelWriter
	# Converte para xlsx:
	if type(contas) == type(str()):
		operation = 2
	elif type(contas) == type(dict()):
		operation = 3
	else:
		print(F"A variáel 'contas' não está correta.")
		return None
	ValuesToList = valuestolist(operation, contas=contas)[-1]
	df = DataFrame(ValuesToList, columns=colunas)
	print(f"{df=}")
	# Salva:
	a = writer = ExcelWriter(nome_arquivo)
	b = df.to_excel(writer)
	colunas_atuais = list(df.columns)
	if colunas_atuais != colunas:
		print(f"Houve uma mudança nas colunas do arquivo: {colunas_atuais=}. Isto pode impactar em incompatibilidades "
			  "em outras funções. Ajuste o arquivo, ou lembre-se de ajustar o parâmetro 'colunas' de cada função que as usa.")
	c = writer.close()
	# Verifica se deu certo:
	if verificar is True:
		def verificar():
			contas2 = convet_xlsx_to_contas(nome_arquivo=nome_arquivo)
			if contas2 == contas:
				print(f"Arquivo foi atualizado com sucesso.")
			else:
				print(f"O arquivo não foi atualizado corretamente.")
				print(f"{contas=}\n{contas2=}\n Iguais?: {contas==contas2=}")
				'''import xlsxwriter
				workbook = xlsxwriter.Workbook(nome_arquivo)
				print(workbook.worksheets())
				worksheet = workbook.add_worksheet()
				print(workbook.worksheets())
				for row_num, row_data in enumerate(ValuesToList):
					for col_num, col_data in enumerate(row_data):
						worksheet.write(row_num, col_num, col_data)
				workbook.close()'''
		verificar()



def manuseio_backup(operation=None, local=None, arquivo='BACKUP.txt', ListBackup=[['REG', '22/05/2024-14:00:01', {'none': {'none': {'none': ['none', 'none']}}}]]):
	"""

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
	def LB_to_strbackup(ListBackup:list=ListBackup):
		"""
		Convert ListBackup to strBackup for write this str in a 'BACKUP.txt' file
		Args:
			ListBackup: list var to convert

		Returns: strBackup : str([['TIPO,-,DATE,-,VAR\n'], ['TIPO,-,DATE,VAR\n'], ...])
		"""
		strBackup = []
		for itens in ListBackup:
			strB = f"{itens[0]},-,{itens[1]},-,{itens[-1]}\n"
			if strB not in strBackup:
				strBackup.append([strB.replace('\n\n', '')])
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
			print(f"{line=}")
			WriteBackup = WriteBackup.join(line)
		return WriteBackup.replace('\n\n', '')

	def strB_to_listbackup(strBackup):
		"""
		convert strBackup into a ListBackup
		Args:
			strBackup: string with lines separated on a lists from base of a 'BACKUP.txt' file.

		Returns: ListBackup : list([[tipo, data, contas], [tipo, data, var], ...)

		"""
		ListBackup = []
		for line in strBackup:
			sep = str(line).strip().replace('["', '').replace(']"', '').replace('\n', '').replace('\\n', '\n').split(',-,')
			for pos, element in enumerate(sep):
				if pos == 0:
					tipo = element.strip().upper()
				if pos == 1:
					data = element.strip()
				if pos == 2:

					if tipo.strip().upper() == 'REG':
						ValuesToList = valuestolist(operation=2, contas=element)[ -1 ]
						item = valuestolist(operation=1, vtl=ValuesToList)[ 0 ]
					else:
						item = element.strip()
					ListBackup.append([ tipo, data, item ])
					print(item)
				print(f"strB_to_listbackup - {ListBackup = }")
		return ListBackup

	def capture_bc():
		"""Captura BACKUP.txt retornando ListBackup, e cria caso não exista"""
		if local is None:
			complete_archive = localizar_arquivo(criar=False, text=True, dir=dir,
												 arquivo=arquivo, modo='r', pandas=False, test_open=True)[ 2 ]
		else:
			from os.path import join
			complete_archive = join(local, arquivo)
		ListBackup = [ ]
		with open(complete_archive, 'r') as arq:
			lines = arq.readlines()
			strBackup = [ ]
			for line in lines:
				strBackup.append([ line ])
			ListBackup = strB_to_listbackup(strBackup)
			print(f"{ListBackup = }")
		return ListBackup

	def format_bc():
		"""escreve em BACKUP.txt retornando WriteBackup, e cria caso não exista"""
		LB_antigo = capture_bc()
		if LB_antigo == ListBackup or LB_antigo[ -1 ] == ListBackup[ -1 ] and op == 'A':
			aviso = (F"Escrever em BACKUP.txt é inviável, pois o que deseja salvar, já está salvo no arquivo.")
			return None
		if local is None:
			complete_archive = localizar_arquivo(criar=True, text=False, dir=dir,
												 arquivo=arquivo, modo='a',pandas=False, test_open=True)[2]
		else:
			from os.path import join
			complete_archive = join(local, arquivo)
		# Converte ListBackup object em objetos de gravação
		strBackup = LB_to_strbackup(ListBackup)
		WriteBackup = strB_to_writebackup(strBackup)
		print(f"{strBackup=}\n{WriteBackup=}\n{ListBackup=}\n{LB_antigo = }")
		if op in ['2', 'A', 'ADD']:
			adicionados = []
			with open(complete_archive, 'a') as arq:
				for strB in strBackup:
					if strB not in adicionados:
						adicionados.append(strB)
						arq.write(strB[0])
		elif op in ['3', 'F', 'FORMAT']:
			with open(complete_archive, 'w') as arq:
				arq.write(WriteBackup)
		return WriteBackup

	if op == '1' or op == 'C' or op == 'CAPTURE': # Capturar backup:
		return capture_bc()
	elif op in ['2', 'A', 'ADD', '3', 'F', 'FORMAT']: # Salvar Backup
		return format_bc()


bp = manuseio_backup(operation='c')
print(f"{bp=}")


"""

	import xlsxwriter
	workbook = xlsxwriter.Workbook('registroS.xlsx')
	print(workbook.worksheets())
	worksheet = workbook.add_worksheet()
	print(workbook.worksheets())
	for row_num, row_data in enumerate(ValuesToList):
		for col_num, col_data in enumerate(row_data):
			worksheet.write(row_num, col_num, col_data)
	workbook.close()

	# creating an ExcelWriter object
	with ExcelWriter(nome_arquivo) as arq:
		#searchs: df[df['PERSON']] == 'klas inu' OR df.iloc[df['PERSON'].searchsorted('klas inu')]
		arquivo = df.to_excel(arq)
	df = [df, arq]
	return [ arquivo, df, ValuesToList ]
	
	try:
		try:
			with open(nome_arquivo, mode=modo) as arq:
				arquivo = df.to_excel(arq)
			return [ arquivo, df, ValuesToList ]
		except Exception as msg:
			print(msg)
	except:
		print(f"Tentativa 2")
	try:
		try:
			from pandas import ExcelWriter
			exl = ExcelWriter(nome_arquivo)
			arquivo = df.to_excel(exl)
			exl.close()
		except Exception as msg:
			print(msg)
	except:
		print(f"Tentativa 3")
	try:
		from pandas import ExcelWriter
		# creating an ExcelWriter object
		with ExcelWriter(nome_arquivo) as writer:
			# writing to the 'Employee' sheet
			df.to_excel(writer, sheet_name='Employee', index=False)
	except:
		pass"""

'''

class Manuseio():

	def __int__(self, colunas=None, nome_arquivo=None):
		if funcionamento_basico is True:
			colunas = [ 'REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ]
			nome_arquivo = 'registro.xlsx'
		else:
			colunas = [ 'REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ]
			nome_arquivo = 'super-registro.xlsx'


	def localizar_arquivo(self, text=False):
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
		create_file = None  # True = precisa criar o diretorio/arquivo, False = não precisa, já existe.
		patch_esperado = correspondencia = '/START-NWM/entrance/registro'
		onde_ir = os.path.dirname(os.path.abspath('registro/' + nome_arquivo))
		patch_atual = os.getcwd()
		arquivo_retornado = None
		if patch_esperado in onde_ir:
			patch_esperado = onde_ir
		if correspondencia in patch_atual:
			try:
				arquivo_retornado = open(nome_arquivo, 'rb')
				create_file = False
			except FileNotFoundError as msg:
				if text is True:
					print(f"O arquivo de registro não foi localizado, iremos criar um 'em branco'...")
				create_file = True
		else:
			if text is True:
				print(f"O diretório atual não é o diretório esperado para correr o script manuseio.py corretamente.")  # MSG
				print(f"Diretório atual: {patch_atual}\n Diretório esperado: {patch_esperado}")  # INFO
				print(f"Tente encontrar ou então criar o diretório esperado, alocar o arquivo 'manuseio.py'")  # SOLUTION
				print(f"Este erro pode ser evitado caso siga o código do github. Caso esteja realmente seguindo o código do github sem quaisquer mudanças e esteja vendo este erro, crie um 'issue'.")  # COMMENT
			create_file = True
		return [ create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado ]


	def criar_arquivo(self):
		create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo()
		# print(f"ATUAL: {patch_atual}\nONDE_IR {onde_ir}")
		if create_file is True and correspondencia in patch_atual:
			# Crie o arquivo e Insere dados básicos:
			df = pd.DataFrame(data=[ [ 'Folha', 'Inu', 'Meeh', 0, 0 ] ], columns=colunas)
			df.to_excel(nome_arquivo)
			arquivo_retornado = localizar_arquivo()[ -1 ]
			create_file = False
			if arquivo_retornado is None:
				print(f'ATENÇÃO: Não conseguimos construir o arquivo: {nome_arquivo} no diretório atual ({patch_atual}). O programa pode então não funcionar corretamente.')
		elif create_file is True and correspondencia not in patch_atual:
			print(f'É necessário encontrar ou criar o diretório {patch_esperado}. ')
		return create_file


	def obter_arquivo(self):
		# Captura do registro bancário:
		for tentativa in range(1, 4):
			print(f"{tentativa=}")
			if tentativa == 1:
				create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(text=True)
				if create_file is False:
					break
			elif tentativa == 2:
				create_file = criar_arquivo()
				if create_file is False:
					create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo()
					break
			else:
				#Tenta ultima vez no modo básico:
				funcionamento_basico = True
				colunas = [ 'REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ]
				nome_arquivo = 'registro.xlsx'
				create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo(text=True)
				if create_file is True:
					c_file = criar_arquivo()
					if c_file is True:
						print(f"Não foi possivel continuar o programa pois houve problemas na captura do registro.")
						# exit & break
				print(f"Conseguimos tratar problemas de inicialização nivel 1 do programa e botamos o script em modo básico.")
				return None
				#breakpoint()
				break
		arquivo_retornado = arquivo_retornado
		create_file = create_file
		return arquivo_retornado if create_file is False else None


	def convet_xlsx_to_contas(self):
		if obter_arquivo() is None:
			print(f"Código tentará continuar mesmo com problemas.")
		# Pega o arquivo 'registro.xlsx'
		with open(nome_arquivo, 'rb') as arquivo:
			df = pd.read_excel(arquivo, header=0)
			colunas_atuais = list(pd.read_excel(arquivo, nrows=0).columns.values.tolist())
			ValuesToList = df.values.tolist()
		# Converte para uso:
		reinos = {}
		for line in ValuesToList:
			reino = line[ 0 ]
			classe = line[ 1 ]
			pp = line[ 2 ]
			money = line[ 3 ]
			exp = line[ 4 ]
			if reino == 'Folha':
				if classe == 'Ivory':
					reinos[ 'Folha' ] = {'Ivory': {pp: [ money, exp ]}}
				if classe == 'Tsuki':
					reinos[ 'Folha' ].update({'Tsuki': {pp: [ money, exp ]}})
			if reino == 'Chuva':
				if classe == 'Runbon':
					reinos[ 'Chuva' ] = {"Runbon": {pp: [ money, exp ]}}
		contas = reinos
		return reinos


	def convert_contas_to_xlsx(self, contas={'Folha': {'Inu': {'Meeh': [0, 0]}}}):
		# Converte para xlsx:
		ValuesToList = [ ]
		for reino, classes in contas.items():
			for classe, person in classes.items():
				for name, saldo in person.items():
					money = saldo[ 0 ]
					exp = saldo[ 1 ]
					ValuesToList.append([ reino, classe, name, money, exp ])
		# print(ValuesToList)
		df = pd.DataFrame(ValuesToList, columns=colunas)
		arquivo = df.to_excel(nome_arquivo)
		arquivo = arquivo
		contas_df = df
		ValuesToList = ValuesToList
		return [arquivo, df, ValuesToList]

Manusear = Manuseio
Manusear()
Manusear().obter_arquivo()
'''
