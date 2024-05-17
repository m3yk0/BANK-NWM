from typing import List, Any


def localizar_arquivo(text=False, nome_arquivo=nome_arquivo, modo='rb', pandas=False):
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
	from os import path, getcwd
	from pandas import read_excel
	create_file = None  # True = precisa criar o diretorio/arquivo, False = não precisa, já existe.
	patch_esperado = correspondencia = '/START-NWM/entrance/registro'
	onde_ir = path.dirname(path.abspath('registro/' + arquivo))
	patch_atual = getcwd()
	arquivo_retornado = None
	if patch_esperado in onde_ir:
		patch_esperado = onde_ir
	if correspondencia in patch_atual:
		try:
			if pandas is False:
				arquivo_retornado = open(arquivo, modo)
			if pandas is True:
				arquivo_retornado = read_excel(arquivo, header=0)
			create_file = False
		except FileNotFoundError as msg:
			if text is True:
				print(f"O arquivo de registro não foi localizado, iremos criar um 'em branco'...")
			create_file = True
	else:
		if text is True:
			print(f"O diretório atual não é o diretório esperado para correr o script manuseio.py corretamente.")  # MSG
			print(f"Diretório atual: {patch_atual}\n Diretório esperado: {onde_ir}")  # INFO
			print(f"Tente encontrar ou então criar o diretório esperado, alocar o arquivo 'manuseio.py'")  # SOLUTION
			print(f"Este erro pode ser evitado caso siga o código do github. Caso esteja realmente seguindo o "
				  f"código do github sem quaisquer mudanças e esteja vendo este erro, crie um 'issue'.")  # COMMENT
		create_file = True
	return [ create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado ]


def criar_arquivo(nome_arquivo=nome_arquivo, colunas=[ '', 'REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ]):
	"""
	Usado para ocorrencia de <create_file==True> para tentar criar o arquivo faltante
	Returns:

	"""
	from pandas import DataFrame
	create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo()
	# print(f"ATUAL: {patch_atual}\nONDE_IR {onde_ir}")
	if create_file is True and correspondencia in patch_atual:
		# Crie o arquivo e Insere dados básicos:
		df = DataFrame(data=[['Folha', 'Inu', 'Meeh', 0, 0]], columns=colunas)
		df.to_excel(nome_arquivo)
		arquivo_retornado = localizar_arquivo()[ -1 ]
		create_file = False
		if arquivo_retornado is None:
			print('ATENÇÃO: Não conseguimos construir o arquivo: {nome_arquivo} no diretório atual ',
				  f'({patch_atual}). O programa pode então não funcionar corretamente.')
	elif create_file is True and correspondencia not in patch_atual:
		print('É necessário encontrar ou criar o diretório {patch_esperado}. ')
	return create_file


def obter_registro(arquivo=nome_arquivo, modo='rb', pandas=False):
	"""

	Args:
		arquivo: str - nome do arquivo
		modo: str - Util apenas caso 'pandas=False', modo ['r', 'rb', 'a', 'w', ...]
		pandas: Bool - False == Obter registro via comando 'open' do python. True == obter registro via comando 'pandas.read_excel()'

	Returns: arquivo <None==Não obteu o arquivo. <Class

	"""
	# Captura do registro bancário:
	for tentativa in range(1, 4):
		print(f"{tentativa=}")
		if tentativa == 1:
			create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo \
				(text=True, arquivo=arquivo, modo=modo, pandas=pandas)
			if create_file is False:
				break
		elif tentativa == 2:
			create_file = criar_arquivo()
			if create_file is False:
				create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo \
					(arquivo=arquivo, modo=modo, pandas=pandas)
				break
		else:
			# Tenta ultima vez no modo básico:
			funcionamento_basico = True
			colunas = [ 'REINO', 'CLASSE', 'PERSON', 'MONEY', 'EXP' ]
			nome_arquivo = 'registro.xlsx'
			create_file, patch_atual, patch_esperado, correspondencia, onde_ir, arquivo_retornado = localizar_arquivo \
				(text=True, arquivo=nome_arquivo, modo='rb', pandas=False)
			if create_file is True:
				c_file = criar_arquivo()
				if c_file is True:
					print(f"Não foi possivel continuar o programa pois houve problemas na captura do registro.")
					# exit & break
			print(f"Conseguimos tratar problemas de inicialização nivel 1 do programa e botamos o script em modo básico.")
			return None
			# breakpoint()
			break
	return arquivo_retornado if create_file is False else None


def convet_xlsx_to_contas(nome_arquivo=nome_arquivo, modo='rb'):
	# Pega o arquivo 'registro.xlsx'
	from pandas import read_excel
	with open(nome_arquivo, modo) as arquivo:
		df = read_excel(arquivo, header=0)  # , colunas=['REINO', "CLASSE", "PERSON", "MONEY", "EXP"]
		colunas_atuais = list(read_excel(arquivo, nrows=0).columns.values.tolist())
		ValuesToList = df.values.tolist()
	# Converte para uso:
	reinos = dict(dict(dict()))
	reinos_alocados = []
	classes_alocadas: list[Any] = []
	for cont, line in enumerate(ValuesToList):
		if type(line[ 0 ]) == type(int()):
			reino = line[ 1 ].lower()
			classe = line[ 2 ].lower()
			pp = line[ 3 ].lower()
			money = line[ 4 ]
			exp = line[ 5 ]
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


def convert_contas_to_xlsx(contas={'reino da folha': {'inu': {'meeh': [ 0, 0 ]}}}, modo='w', nome_arquivo=nome_arquivo,
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
	ValuesToList = [ ]
	c = 0
	for reino, classes in contas.items():
		for classe, person in classes.items():
			for name, saldo in person.items():
				money = saldo[0]
				exp = saldo[1]
				ValuesToList.append([reino.lower(), classe.lower(), name.lower(), money, exp ])
				c += 1
	df = DataFrame(ValuesToList, columns=colunas)
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
				print(f"{contas=}\n{contas2=}") 
				import xlsxwriter
				workbook = xlsxwriter.Workbook(nome_arquivo)
				print(workbook.worksheets())
				worksheet = workbook.add_worksheet()
				print(workbook.worksheets())
				for row_num, row_data in enumerate(ValuesToList):
					for col_num, col_data in enumerate(row_data):
						worksheet.write(row_num, col_num, col_data)
				workbook.close()
		verificar()


