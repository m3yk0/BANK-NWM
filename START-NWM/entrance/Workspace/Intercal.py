#Intercalação entre FUNCS e CONTROLES para evitar ImportError Name Circle dependence.
from entrance.Store_fold.store import contas, itens



def pib_real_fc(Itens=itens, change=True):
	from entrance.Workspace.controles import pib_real_fc
	return pib_real_fc(Itens=itens, change=True)

def values_fc(registro=contas.copy()):
	from entrance.Workspace.controles import values_fc
	return values_fc(registro=contas.copy())

def capta_fc(registro=contas.copy()):
	from entrance.Workspace.controles import capta_fc
	return capta_fc(registro=contas.copy())
			 
			 

#transformar valor em decimal:
# ISTO ESTÁ LIGADO A FUNC.PY. SE ATUALIZAR AQUI, TAMBÉM ATUALIZE LÁ
def decim_fc(valglobal):
	from entrance.Workspace.Funcs import decim_fc
	return decim_fc(valglobal)
	
#Func. de converter valor em forma mometária
# ISTO ESTÁ LIGADO A FUNC.PY. SE ATUALIZAR AQUI, TAMBÉM ATUALIZE LÁ
def money_func(din, f=2):
	#Criação de vars:
	lis = []
	cont = 3
	#Tira decimal:
	din2 = int(din)
	# Cria str do valor total sem decimal:
	dinstr = str(din2)
	#Cria str do valor só decimal:
	decimal = str(round(din, f))
	try:
		a = decimal.index(".")
		decimal = decimal[a:]
	except ValueError:
		a = -1
		decimal = "0"
	#Substitui ponto por virgula no decimal:
	decimal = decimal.replace(".", ",")
	#Caso valor negativo, rerira o "menos":
	if din < 0:
		dinstr = dinstr[1:]
	#Vê quantas caracteres tem dinstr:
	len_din = dinstr.__len__()
	#Caso o número nessecite de separação de milhares (seja maior que 999):
	if din > 999 or din < -999:
		dinstr = "#" + dinstr
		for c, v in enumerate(dinstr[-1:0:-1]):
				lis.append(f"{v}")
				cont -= 1
				if cont == 0 :
							 lis.append(".")
							 cont = 3
		if lis[-1] == ".":
			del lis[-1]
		try:
					virg = (lis.index(","))
					print(virg)
					if lis[virg-1] == ".":
						del lis[virg-1]
					elif lis[virg+1] == ".":
						del lis[virg+1]
		except:
			pass
		a = list(reversed(lis))
		formatado = "".join(a)
		#Garante que não tenha mais nem menos que uma vírgula:
		tipo = str(type(din)) 
		if "float" not in tipo:
			final = formatado + f",{decimal}"
		else: final = formatado + decimal
		qtia_virgulas = final.count(",")
		if qtia_virgulas > 1:
			final = final.replace(",","a", qtia_virgulas)
		#garante que quantia de decimais seja igual a f:
		decimal = final[final.index(","):]
		dinstr = final[0: final.index(",")]
		qtia_decimais = decimal.__len__() - 1
		while qtia_decimais < f:
			decimal += "0"
			qtia_decimais = decimal.__len__() - 1
		if f >= 1:
			final = dinstr + decimal
		else:
			final = dinstr
		#Retorna o valor formatado
		if din < 0: 
			final = "-" + final #caso seja abaixo de zero, bota o traço de negativo
			return final #+ f"{decimal}"
		else: #caso seja positivo, não bota o sinal de negativo. 
			return final #+ f"{decimal}"
	#caso não precise de separação de milhar:
	else:
			if din < 0:
				dinstr = "-" + dinstr
			return dinstr #+ f"{decimal}"

    	
#Func. de botar zero a direita. Use somente INT
# ISTO ESTÁ LIGADO A FUNC.PY. SE ATUALIZAR AQUI, TAMBÉM ATUALIZE LÁ
def zero2(algo):
    	tipo = type(algo)
    	algo = str(algo)
    	v = algo.__len__()
    	zero_ = algo[0]
    	#zero_ = int(algo[0]) 
    	for c in range(1, v):
    		zero_ += "0"
    	if int is tipo:
    		zero_ = int(zero_)
    	else:
    		print("ERRO 'FUNC ZERO2(), Por favor, bote INT como parâmetro.")
    	return zero_
global zero_


def confirm(text="[S/N]: "):
	"""

	–> Função para fácilitar confirmação de decisões (retorna resultados lógicos, valida a entrada
	do usuário, categoriza o que foi digitado)
	Args:
		text: Texto a ser mostrado na tela

	Returns: Bool(True if user input a válid confirmation else False)

	"""
	while True:
		try:
			confirmation: str = str(input(text)).strip().upper()
		except:
			print(f"\nErro. Confirmação taxada como negativa.\n")
			return False
		confirms = ["S", "SIM", "Y", "YES", "AFIRMATIVO",
					"CLARO", "EXATO", "SS", "POSITIVO", "TRUE", "1", "TRUE"]
		negacoes = ["N", "NAO", "NÃO", "NN", "NEGATIVO",
					"SAIR", "CANCELAR", "FALSO", "FALSE", "-1", "0", "2", "FALSE"]
		if confirmation in confirms:
			print(f"\nConfirmado operação com sucesso.\n")
			return True
		elif confirmation in negacoes:
			print(f"\nOperação negada com sucesso.\n")
			return False
		else:
			print(f"\nOpção inválida. Tente novamente.\n")
			continue


def preço(text=""):
	"""

	–> Transforma texto em INT, removendo o que não for numérico.
	:text: texto a ser convertido em INT
	:Returns: integer (text)
	"""
	text = text.strip().lower()
	lis = 'a b c d e f g h i j k l m n o p q r s t u v w x y z ! @ # $ % ¨ & * ( ) _ + " { ` } ˆ < > : ? , . ; / ] ˜ [ ´ - = § ∏ | ≤ ≥ … ° ~ º ´ ª – § ¬ ¢ / ® € ŧ ← ↓ → þ ´ ª · º æ ß ð ∆ ħ ʝ ĸ ł · Ω ≈ ʋ ∫ '.lower().split(' ')
	for e in lis:
		text = text.replace(e, '')
	text = text.replace(' ', '').replace("'", "").strip()
	if text == "":
		text = 0
	return int(text)

