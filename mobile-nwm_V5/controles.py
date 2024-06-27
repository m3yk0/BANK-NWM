"""
V 5 (Mobile bank), v 7 of this code
Package 'mobile-nwm' > controles.py
controles.store.contas
controles.backup
DEPENDÊNCIAS:
	mobile-nwm/Intercal.py
	mobile-nwm/


"""
# CONTROLES 2!!!!!*****
# Encoding: UTF-8
'entrance.registro'
# Bibs Padrões (/usr/local/bin/python3.9)

# Bibs locais (/Desktop/START-NWM)
from Intercal import zero2
from manuseio import convert_things_to_items, convet_xlsx_to_contas

Itens = convert_things_to_items()
Contas = convet_xlsx_to_contas()[0]

desconfirm = None

'''
global PIB_real, i, log, start, vms, ems, all_class, moneypersec, totpvms, pvms, totcontpersec, accounts, accountsdict, \
	bolsa, bolsapersec, tesouropersec, valor_mundial, valor_guardado, tesouro, meta_selic, feepersec, tot_fee, ipcapersec, \
	ipca, PIB_Nominal_persec, PIB_Nominal, ETF, ETF_persec, PIB_Per_Capita_persec, PIB_Per_Capita, historico'''


# CONTROLES = ARQUIVO QUE OBTÉM DADOS DOS OBJETOS `REGISTRO` E `ITENS`:


def pib_real_fc(itens=Itens, change=True):
	"""
    Define PIB_REAL, TBF e arruma ITENS:
    criado: 06/04/2024
    """
	# Define o PIB_real
	# Contabiliza o PIB real (Diferente do PIB Per Capita, que considera a quantia de indivíduos,
	PIB_real = 0
	# que seria o PIB_Per_Capita, e diferente do PIB Nominal, que considera a inflação)
	if change is False:
		itens = itens.copy()  # Não muda a variável 'itens' de instância caso 'change==false'
	old_itens = itens.copy()
	new_itens = itens
	for k, v in old_itens.items():  # Para cada chave e valor presente em "store.itens":
		k_novo = k.title().replace('_', ' ').strip()
		new_itens[ k_novo ] = new_itens.pop(k)
		#print(k, v, PIB_real, end=',-, ')
		if type(v) == type(list()):
			if str(v[0]).replace('.', '').isnumeric() is False: # v[0] = value_item
				value = 0
			value = float(v[0])  # Transforma o valor em INT
		else:
			if str(v).replace('.', '').isnumeric():
				value = float(v)
			else:
				value = 0
		PIB_real += value  # itera em PIB_real
		new_itens[ k_novo ] = value  # E salva o valor antes "str", como "INT" no dicionário de store.itens do RPG.
	# Arredonda o valor de PIB_real para ter somente zeros e o número inicial
	PIB_real = int(zero2(PIB_real))
	"""DEFINE TBF DE ACORDO COM PIB_REAL:"""
	# =====- AQUI em [0: 6] VOCÊ DEFINE QUANTOS ZEROS TERÁ A FRAÇÃO DE TBF para os cálculos do IPCA, Taxa, etc. -=======#
	TBF = int(str(zero2(PIB_real))[ 0:8 ])  # Transforma "TBF" # Padrão = [0:6]
	# em variável INT com o primeiro número do PIB_real e x quantias de zeros atrás para formatação de fração quando for realizar alguma divisão "VMS ÷ TBF" como VMS%×Nx (N = número PIB_real, x = qtia. De zeros)
	return [ PIB_real, TBF, old_itens, new_itens ]

#print(pib_real_fc(itens=Itens))

# VERIFICAÇÃO:
# Todos que estão em 'store.contas', devem também estar em 'store.propriedades', 'store.contratos' e 'store.Rank':

def list_persons_fc(registro):
	all_persons = []
	for dic_cla in registro.values():
		for conts in dic_cla.values():
			for name in conts.keys():
				if name != 'none':
					all_persons.append(name)  # Bota nome do guri em lista de nomes
	return all_persons


def values_fc(registro):
	"""DEFINE VMS, EMS, ALL_SECTIONS, ALL_CLASS, MONEYPERSEC{}, TOT_PVMS, PVMS, TOTCONTPERSEC, ACCOUNTS,
	ACCOUNTSDICT, BOLSA, BOLSAPERSEC, TESOUROPERSEC: """
	vms = 0
	ems = 0
	all_sections = list(registro.keys())
	all_class = [ ]
	tot_pvms = vpms = pvms = 0
	totcontpersec = {}
	acconts = 0
	accontsdict = {'negativos': 0, 'positivos': 0}
	bolsa = 0
	bolsapersec = {}
	tesouropersec = {}
	for sec, dic_cla in registro.items():
		vpms = pvms = 0  # PVMS reseta sempre que muda de seção
		bolsa2 = 0  # Bolsa reseta sempre que muda de seção
		if dic_cla != 'none' and sec != 'none':
			for cla, conts in dic_cla.items():
				if str(conts).lower().strip() != 'none' and str(cla).lower().strip() != 'none' and [
							conts.keys().__len__() == 1 and str(list(conts.keys())[0]) == 'none'] == [False]:
					all_class.append(cla)  # Soma todas as classes QUE TENHA PESSOAS, em uma lista
					for name, saldo in conts.items():
						if name != 'none' and saldo != 'none':
							acconts += 1  # total de contas soma +1
							for pos, val in enumerate(saldo):
								if str(val).replace('.', '').isnumeric():
									val = float(val)
									if pos == 0:  # ryo
										# Somente caso o saldo for positivo, ele é contabilizado para o VMS (tot_pvms), PVMS e soma de store.contas positivadas.
										if val > 0:
											vms += val
											vpms += val
											pvms += val
											tot_pvms += val
											accontsdict[ 'positivos' ] += 1
										elif val < 0:  # Caso o saldo do indivíduo for negativo:
											bolsa -= val  # A bolsa de valores mundial é contabilizada
											# A bolsa de valores da seção atual é contabilizada.
											bolsa2 -= val
											accontsdict[ 'negativos' ] += 1
									elif pos == 1:  # exp:
										ems += val
							totcontpersec[ sec ] = conts
						bolsapersec[ sec ] = round(bolsa2, 2)
						tesouropersec[ sec ] = round(vpms, 2)
	return [vms,ems, all_sections, all_class, tot_pvms, vpms, pvms, totcontpersec,
	acconts, accontsdict, bolsa, bolsapersec, tesouropersec]


#print(values_fc(Contas))

def totcontspersec_fc(registro, ignore_none=True):
	"""

	Args:
		registro: dict = var Contas
		ignore_none: Bool = True caso queira ignorar a contagem dos valores 'none', False caso queira que 'none' entre na contagem.
	Returns: dict = {section: [name1, name2, ...] # Dicionário com key da seção e Value é uma lista com o nome das contas pertecentes a tal seção.-
	"""
	totcontpersec = {}
	names = [ ]
	for sec, clas in registro.items():
		for conts in clas.values():
			for name in conts.keys():
				if ignore_none and name.lower().strip() != 'none':
					names.append(name)
				elif ignore_none is False:
					names.append(name)
		else:
			totcontpersec[sec] = names.copy()
			names.clear()
	del names
	return totcontpersec



def capta_fc(registro, itens=Itens):
	"""DEFINE PIB_PER_CAPITA_PERSEC E PIB_PER_CAPITA"""
	# calcula PIB_Per_Capita (atualizado para PIB_Per_Capita mundial ser == PIB_real)
	# define PIB_Per_Capita_persec
	all_persons = list_persons_fc(registro=Contas)
	person_persec = 0
	PIB_Per_Capita_persec = {} # PIB de cada seção
	PIB_Per_Capita = 0
	PIB_real = pib_real_fc(itens)[ 0 ]
	# novo:
	for sec, dic_cla in registro.items():
		if type(dic_cla) == type(dict()): # Caso classe exista:
			for conts in dic_cla.values():
				if type(conts) == type(dict()): # E caso tenha pessoas:
					for nome in conts.keys():
						if nome.strip().lower() != 'none': # E elas não sejam 'none':
							person_persec += 1
		else:
			PIB_Per_Capita_persec[sec] = 0

		if person_persec > 1: # Caso haja várias pessoas na seção:
			PIB_Per_Capita_persec[sec] = round(PIB_real / person_persec, 2)
		elif person_persec == 1 and all_persons.__len__() > 1: # Caso exista 1 pessoa na seção, mas várias pessoas no mundo
			PIB_Per_Capita_persec[sec] = round(PIB_real / all_persons.__len__())
		elif person_persec == 1 and all_persons.__len__() == 1: # Caso haja 1 pessoa no mundo, o justo seria não haver dinheiro.
			PIB_Per_Capita_persec[sec] = 0
		else:
			PIB_Per_Capita_persec[sec] = 1
		person_persec = 0
	# calcula PIB_Per_Capita mundial:
	for k, v in PIB_Per_Capita_persec.items():
		PIB_Per_Capita += v
	return [PIB_Per_Capita_persec, PIB_Per_Capita]

'''
def capta_fc(registro=store.contas.copy()):
	"""DEFINE PIB_PER_CAPITA_PERSEC E PIB_PER_CAPITA"""
	# calcula PIB_Per_Capita (atualizado para PIB_Per_Capita mundial ser == PIB_real)
	# define PIB_Per_Capita_persec
	all_persons = list_persons_fc(registro=Contas)
	PIB_Per_Capita_persec = {}
	PIB_Per_Capita = 0
	PIB_real = pib_real_fc()[ 0 ]
	# novo:
	for sec, dic_cla in registro.items():
		if dic_cla != 'none':
			for conts in dic_cla.values():
				if conts != 'none':
					acconts = conts.__len__()
					if acconts > 1:
						PIB_Per_Capita_persec[ sec ] = (PIB_real / acconts)
					else:
						PIB_Per_Capita_persec[ sec ] = round(PIB_real / all_persons.__len__(), 2)
	# calcula PIB_Per_Capita mundial:
	for k, v in PIB_Per_Capita_persec.items():
		PIB_Per_Capita += v
	return [PIB_Per_Capita_persec, PIB_Per_Capita]
'''


def fee_fc(registro, itens=Itens):
	"""DEFINE FEEPERSEC, TOT_FEE, IPAPERSEC, IPCA, PIB_NOMINAL_PERSEC, PIB_NOMINAL, ETF, ETF_PERSEC"""
	# Define taxa selic e IPCA de cada seção:
	# LEMBRESE DE SE ATUALIZAR AQUI, TB. ATUALIZAR EM FUNCS.PY DEF valores
	# Fee per sections (taxa por seções) == Taxa Selic de cada seção)
	feepersec = {}
	tot_fee = 0  # total fee (taxas totais) == soma de todas taxa selic
	# Define VMS, all_sections, all_persons, all_class, tot_pvms, moneypersec
	ipcapersec = {}
	IPCA = 0  # Contabiliza a soma de todos os IPCA
	PIB_Nominal_persec = {}
	PIB_Nominal = 0
	ETF = 0
	ETF_persec = {}
	var1 = values_fc(registro)
	moneypersec = tesouropersec = var1[-1]
	vms = var1[0]
	PIB_Per_Capita_persec = capta_fc(registro)[0]
	var2 = pib_real_fc(itens)
	PIB_real = var2[0]
	TBF = var2[1]
	# moneypersec = dict{Key=str(sect==Seção), Value=float(val== PVMS (valor positivo total em mãos da tal seção)}
	for sect, val in moneypersec.items():
		if val >= 0:  # Caso PVMS seja positivo e maior que zero
			# Cria uma taxa (mas não em porcentagem, sim em número real inteiro absoluto), baseada no valor que a seção tem, menos o que ela Deveria ter (Isto é o IPCA)
			#print(f"{val}, {PIB_Per_Capita_persec[sect]} = {PIB_Per_Capita_persec[sect]=}")
			taxa = val - PIB_Per_Capita_persec[ sect ]
			# E esta taxa é guardada na seção pertencente
			feepersec[ sect ] = round(taxa, 2)
			# Soma a taxa de desbalanço atual, formando o IPCA mundial
			tot_fee += (taxa / TBF)
			# Então cria o IPCA de cada seção, sendo a taxa dividída peo TBF(que seria a base de cálculo de quantos zeros seria necessário dividir a TAXA, para resultar em um númedo de até 3 casas decimáis (1 a 100)

			ipcapersec[ sect ] = round(taxa / TBF, 2)
			IPCA += taxa  # Soma a taxa de desbalanço atual, formando o IPCA mundial
			# PIB_Nominal_persec, é o PIB_Per_Capita (pib dividido por quantia de registrados), menos a taxa(que se refere ao o que todos têm- o que deveriam)
			PIB_Nominal_persec[ sect ] = PIB_Per_Capita_persec[ sect ] - round(taxa / TBF, 2)
			# PIB_Nominal Mundial então é a soma de todos os pib nominais das seções.
			PIB_Nominal += PIB_Nominal_persec[ sect ]
			# ETF_persec é a díferença do PIB com inflação para o PIB real sem inflação
			ETF_persec[ sect ] = ((PIB_Nominal_persec[ sect ] - PIB_real))
			# ETF Mundial é esta diferença contabilizando todas as seções juntas.
			ETF += ((PIB_Nominal_persec[ sect ] - PIB_real))
		else:  # Sempre que o PVMS for nulo ou negativo, ele é dado como zero.
			feepersec[ sect ] = 0
			ipcapersec[ sect ] = 0
		"""print(f"{sect=}", f"{money_func(moneypersec[sect])=}", f"{money_func(feepersec[sect])=}",
			  f"{money_func(ETF_persec[sect])=}", f"{money_func(ipcapersec[sect])=}",
			  f"{money_func(PIB_Nominal_persec[sect])=}", F"{money_func(PIB_Per_Capita_persec[sect])=}",
			  f"{money_func(PIB_real)=}", sep='\n')"""
	tot_fee = round(tot_fee, 4)
	"""DEFINE VALOR_MUNDIAL, VALOR_GUARDADO, TESOURO E META_SELIC"""
	# Valor mundial é como se fosse o PIB_real. É o total do valor que pode cair em mãos. Ele sempre será o valor do PIB_real.
	valor_mundial = valor_guardado = PIB_real
	tesouro = meta_selic = (valor_mundial -vms)
	return 	[feepersec, tot_fee, ipcapersec, IPCA, PIB_Nominal_persec, PIB_Nominal, ETF, ETF_persec, tesouro]

#print(fee_fc(registro=Contas))
# 1.200.300.400
# FIM PROGRAMA PRINCIPAL.
