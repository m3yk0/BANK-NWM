from sys import stderr

import store
from Funcs import confirm

from Historico import log


class ItemNotFoundInItensError(Exception):
	"""DEFINE ERRO (ITEM NOT FOUND IN ITENS)"""
	pass


"""DEFINE FUNÇÃO PARA VALIDAR OS ITENS DA VÁRIAVEL `PROPRIEDADES`:"""

def alocar_item_manual(new_key, price=None):
	"""
	–> Aloca 'new_key' no dict store.itens com o valor 'price'
	Args:
		new_key: str(item novo a ser iterado)
		price: int(valor do item novo)
	Returns: None
	"""
	print(f"\nDeseja adicionar o item {new_key} à variável 'itens'? ")
	conf = confirm()
	if conf:
		if price is None:
			price = int(input(F"\nDigite o valor do item: "))
		store.itens[ new_key ] = price
	return f'Item {new_key} alocado em "store.itens" com valor de {price}.'

def find_one_item(Item, Itens=store.itens, alocar=False, price=None):
	"""

    –> checks the global variable: dict(store.itens) and validates the global variable: dict(store.propriedades)
    :param Item: optional argument (Emergency Delared: NoneType). If declared, you will see if the item exists in the variable dict(items)
    :param alocar: Caso encontre itens desanexados, True dá oportunidade de anexá-lo.
    :param price: Caso 'alocar' is True, menciona o preço a ser alocado.
    :return: BOOLTYPE False if Error (character has a property not listed under 'store.itens') else return True
    """
	# - - - Code - - -
	# Caso verificação seja de um item específico:
	if Item not in Itens.keys():
		try:
			raise ItemNotFoundInItensError(F"Item {Item} não encontrado em store.itens <")
		except ItemNotFoundInItensError as msg:
			print('\nItemNotFoundInItensError.itensError:', msg, file=stderr)
			retorno = False  # Falso = item não incluso em Itens
		finally:
			if alocar is True:
				alocar_item_manual(new_key=Item, price=price)
	else:
		retorno = True
	return retorno

def find_all_itens(Propriedades=store.propriedades, Itens=store.itens, alocar=False, stop=False):
	"""

	Args:
		Propriedades: objeto cujo os valores[key] devem estarem na variável itens
		Itens: objeto tipo dicionário que lista todos os itens[keys=nome, val=preço] que podem existir.
		alocar: bool
			Caso True, da a chance do usuário corrijir o erro, alocando o item novo no obj Itens
			caso False, deleta o item
		stop: Para o programa na primeira ocorrência ao invés continuar tratando os erros no objeto inteiro. False == continua

	Returns:
		list([bool, person, item]) == erro de item não localizado
			bool = False == Item do objeto 'Propriedades' não localizado com Items
			person = personagem de Propriedades que tem um item errado
			item = item não localizado em Itens
		None == não houve exeções.

	"""
	# Caso não seja de item especifico, então averigua toda a variável 'store.propriedades' com 'store.itens'
	retorno = None
	for pp, dic_store in Propriedades.copy().items():
		for item, value in dic_store.copy().items():
			old_key = item
			new_key = item.title().strip()
			Propriedades[ pp ][ new_key ] = Propriedades[ pp ].pop(old_key)
			if new_key not in Itens:
				try:
					raise ItemNotFoundInItensError(
						F"> Item '{new_key}' de Propriedades['{pp}'] não encontrado na variável de itens")
				except ItemNotFoundInItensError as msg:
					print('ItemNotFoundInItensError.itensError:', msg, file=stderr)
					retorno = [ False, pp, new_key ]  # False == Item não incluso em Itens
				finally:
					if alocar:
						alocar_item_manual(new_key=new_key, price=None)
					elif alocar is False:
						del Propriedades[ pp ][ new_key ]
					stop = True
					break
		if stop is True:
			break  # Para tudo, tratando apenas um item por vez.
	return retorno

"""TRATAMENTO DE `propriedades` """
flag = not None
c = 0
while flag is not None:
	c += 1
	flag = find_all_itens(Propriedades=store.propriedades, Itens=store.itens, alocar=False)
	if flag is not None:
		item, pp = flag[1], flag[-2]
		log.append(F"\n ({c} alteração em Propriedades): Item '{item}' de '{pp}' foi removido por não existir no objeto de Itens.")
