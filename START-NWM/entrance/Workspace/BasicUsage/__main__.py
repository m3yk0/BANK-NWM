from entrance import funcionamento_basico
from entrance import historico
from entrance.Workspace.BasicUsage import Usages

nome_arquivo = "registro\registro.xlsx"

def main():
	if funcionamento_basico is True:
		operacoes = [ "None" ]
		log = []
		while True:
			print("\n~~~~ World Meeh: Bank! ~~~\n")
			print(f"\n ~~~ Program Version: {0+0} ~~~\n")
			print("\n"
				  "    Qual área do programa deseja entrar?:\n"
				  "    0- Sair"
				  "\n    1- Visualizar registro bancário\n"
				' 		1.1 - Mostrar todas as variáveis "importantes".'
				  "    2- Magnatas (Excluído no modo básico)\n "
				  "   3- VMS (Checar taxas, valores, tributos e ajustes) \n "
				  "   4- Processar card bancário\n"
				  "        4.1- Adicionar conta\n"
				  "        4.2- Remover conta\n"
				  "        4.3- Transferência\n"
				  "        4.4- Descontar\n"
				  "        4.5- Pagar\n"
				  "		4.6- Adicionar nova classe\n"
				  "		4.7- Adicionar nova seção\n"
				  "		4.8- Remover seção\n"
				  "		4.9- Remover classe\n"
				  "		4.10- Definir Líder\n"
				  "		4.11- Definir Rei\n"
				  "		4.12- Definir Leis em reinos\n"
				  "     4.15- Mudar Nomes das contas\n"
				  "    5- Definir registro antigo como principal\n"
				  "    6- Ver histórico de operações\n"
				  "    7- Atualizar registro\n"
				  "    8- Avisos\n"
				  "    9- Bonança por Cargo"
				  "    10- Rank de pontos, feitos em ON e store.itens ( Excluido no modo básico)"
				  "    ...- CDI, PIB_real, Juros, RH, parcelas...")
			try:
				print(F"   > O ultimo comando digitado foi: {operacoes[ -1 ]}")
				try:
					print(f"    Descrição do ocorrido: {historico[ -1 ][ 1 ]}")
				except IndexError:
					print(F"    Histórico ainda inacessivel.")
				escolha = float(input("    > Escolha: "))
				operacoes.append(escolha)
				i = escolha
				log.append(f"Foi digitado no menu, opção {i}")
			except ValueError:
				print(f"Erro. Use um valor numérico.")
				continue
			finally:
				print('\n')

			if i == 0:
				Usages.sair()
			elif i == 1:
				Usages.ver_contas(tipo_do_registro='Escolher', nome_arquivo=nome_arquivo)
			elif i == 4.1:
				Usages.cadastrar_pandasdf(salve_in_archive=False)
			elif i == 4.2:
				Usages.remover_conta(
 salve_in_archive=False)
			elif i == 4.3:
				Usages.transferencia(salve_in_archive=False)

if __name__ == "__main__":
	main()