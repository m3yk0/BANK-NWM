from __init__ import funcionamento_basico
import Historico
import Usages
from Funcs import atual_data

desconfirm = None
# None = confirmações habilitadas no programa
# False = todas confirmações do programa são imediatamente taxadas como negativas
# True = todas confirmações do programa são imediatamente taxadas como Positivas


def main():
	from Funcs import confirm
	if funcionamento_basico is True:
		operacoes = [ "None" ]
		log = []
		loops = 0
		desc = ''
		while True:
			data_atual = atual_data()
			print("\n~~~~ World Meeh: Bank! ~~~\n")
			print(f"\n ~~~ Program Version: {0+0} ~~~\n")
			print("\n"
				  "    Qual área do programa deseja entrar?:\n"
				  "  	Negativo == configuração do programa\n"
				  "		-1 = Retirar todas as confirmações de escolha do programa (cuidado)"	
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
					print(f"    Descrição do ocorrido: {Historico.historico[-1]}")
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

			if loops == 0:
				from manuseio import convet_xlsx_to_contas, localizar_arquivo
				nome_arquivo = localizar_arquivo(criar=True, text=True, dir='START-NWM/mobile-nwm', arquivo='registro.xlsx', modo='rb', pandas=False, test_open=True)[2]
				contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo, modo='rb')
			loops += 1

			if i == -1:
				es = str(input(F" Você deseja definir tddas as confirmações do programa como:\n0 - False\n1 - True\n [0/1] >>> "))
				if confirm(f"Você deseja desativar a escolha de confirmações? Confirme: "):
					if es == '0':
						desconfirm = False
					else:
						desconfirm = True
			elif i == 0:
				Usages.sair()
			elif i == 1:
				if confirm(f"Você escolheu: --VER REGISTRO--. Confirma? \n[S/N] >>> "):
					Usages.ver_contas(tipo_do_registro='Completo', contas=contas, nome_arquivo=nome_arquivo)
			elif i == 4.1:
				if confirm(f"Você escolheu:  -- CADASTRAR CONTA NOVA--. Confirma? \n[S/N] >>> "):
					retorno = Usages.cadastrar_pandasdf(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=False)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i == 4.2:
				if confirm(f"Você escolheu:  --REMOVER CONTA--. Confirma? \n[S/N] >>> "):
					Usages.remover_conta(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=False)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i == 4.3:
				if confirm(f"Você escolheu:  --TRANSFERÊNCIA ENTRE CONTAS--. Confirma? \n[S/N] >>> "):
					retorno = Usages.transferencia(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=False)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i == 4.4 or i == 44:
				if confirm(f"Você escolheu:  --DESABONAR CONTA--. Confirma? \n[S/N] >>> "):
					retorno = Usages.descontar(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=False)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i == 4.5:
				if confirm(f"Você escolheu:  --ABONAR CONTA--. Confirma? \n[S/N] >>> "):
					Usages.abonar(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=False)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i == 4.6:
				if confirm(f"Você escolheu:  --CRIAR NOVA CLASSE--. Confirma? \n[S/N] >>> "):
					Usages.add_classe(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=False)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i == 4.7:
				if confirm(f"Você escolheu:  --FORMATAR SALDO DE MÚLTIPLOS INDIVÍDUOS--. Confirma? \n[S/N] >>> "):
					retorno = Usages.formatar_contas(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=False)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i == 4.8:
				if confirm(f"Você escolheu:  --ADICIONAR NOVA SEÇÃO--. Confirma? \n[S/N] >>> "):
					retorno = Usages.add_section(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=False)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i == 7:
				if confirm(f"Você escolheu:  --SALVAR REGITRO--. Confirma? \n[S/N] >>> "):
					from manuseio import convert_contas_to_xlsx
					retorno = convert_contas_to_xlsx(contas=contas, nome_arquivo=nome_arquivo, verificar=True)
					if retorno is not None:
						if Usages.verificar_presença(registro=nome_arquivo, oque_procurar=3, nome_pp='susumo'):
							print(f"Indivíduo salvo em {nome_arquivo}\n - com sucesso.")
						desc = 'REGISTRO SALVO.'

					Historico.contas_antigas.append([data_atual, contas])
			if desc != '':
				Historico.historico.append(desc)
			print(data_atual)



if __name__ == "__main__":
	main()