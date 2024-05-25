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
		escolhas = [
		["0", "00",  "/EXIT", "", "SAIR"], 
		["1", "01", "/SEE", "", "VER REGISTRO"] , 
		 ["4.1", "41", "/ADD_CO", "-Name -Money -Exp", "ADICIONAR CONTA"], 
		 ["4.2", "42",  "/DEL_CO", "-Name", "DELETAR CONTA"], 
		 ["4.3", "43", "/TRANSF", "-Name1 -Value -Name2", "TRANSFERÊNCIA BANCÁRIA ENTRE CONTAS"], 
		 ["4.4", "44", "/DES_CO", "-Name -Value", "DESABONAR CONTA"], 
		 ["4.5", "45", "/SOMA_CO", "-Name -Value", "ABONAR CONTA"], 
		 ["4.6", "46", "/ADD_CLA", "-Sect -Class", "ADICIONAR NOVA CLASSE"], 
		 ["4.7", "47", "/FV_CO", "", "FORMATAR SALDO DE MÚLTIPLAS CONTAS "], 
		 ["4.8", "48", "/ADD_SEC", "-Sect", "ADICIONAR SEÇÃO"], 
		 ["7", "07", "/OK", "", "SALVAR REGISTRO"],
		 
		 ["-1", "/?", "/HELP", "-Comando", "VER AJUDA"]]  
		bad_escolhas = []
		
		def printalt(alternativas):
			for e in alternativas:
				print(e, end=" | ")
			print("\n")
				
		while True:
			data_atual = atual_data()
			print(f"\n\n~~~~ World Meeh: Bank! ~~~\n\n~~~ Program Version: {4.5} - Mobile Version~~~\n\nQual área do programa deseja entrar? Escolhas disponíveis:\n")
			alternativas = [] 
			for item in escolhas: # imprime escolhas:
				if item not in bad_escolhas:
					print(f"  ¬ {item[0]:^5} | {item[2]} {item[-2]} -> \n	   {item[-1]}")
				for pos, alt in enumerate(item):
					if pos in [0, 1, 2] and alt not in alternativas:
						alternativas.append(alt)
			print(f"\n(Escolha o número ou digite o comando como /OPERAÇÃO -parametro)\n(-Name == Nome da conta + Classe. Ex: /SOMA CO -meeh inu -347)\nMenu {loops+1} ", end="") 
			try: # Mostra comandos anteriores
					print(f" > O ultimo comando digitado foi: {operacoes[ -1 ]}") 
					print(f"    Descrição do ocorrido: {Historico.historico[-1]}")
			except IndexError:
					print(F"    Histórico ainda inacessivel.")
			# Faz escolha e armazena ela:
			escolha = str(input("\n    > Escolha >>> ")).strip().upper()
			operacoes.append(escolha)
			i = escolha 
			log.append(f"Foi digitado no menu, comando: {i}")
			
			#Pega o registro bancário (var contas)
			if loops == 0:
				from manuseio import convet_xlsx_to_contas, localizar_arquivo
				nome_arquivo = localizar_arquivo(criar=True, text=False, dir='START-NWM/mobile-nwm', arquivo='registro.xlsx', modo='rb', pandas=False, test_open=True)[2]
				contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo, modo='rb')
			loops += 1
			
			if "/" in escolha and "-" in escolha:
				comma = escolha.split("-")
				cmd, *parametros = comma
				cmd = i = cmd.strip()
				if cmd not in alternativas:
					print(f" Erro. Verifique a sintaxe do comando.")
					print(" Ou use as alternativas comuns:")
					printalt(alternativas)
				print(f":{cmd}:","######", parametros)

			if i in escolhas[-1]:
				Usages.help()
			elif i in escolhas[0]:
				Usages.sair()
			elif i in escolhas[1]:
				if confirm(f"Você escolheu: --VER REGISTRO--. Confirma? \n[S/N] >>> "):
					Usages.ver_contas(tipo_do_registro='Completo', contas=contas, nome_arquivo=nome_arquivo)
			elif i in escolhas[2]:
				if confirm(f"Você escolheu:  -- CADASTRAR CONTA NOVA--. Confirma? \n[S/N] >>> "):
					retorno = Usages.cadastrar_pandasdf(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=True)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i in escolhas[3]:
				if confirm(f"Você escolheu:  --REMOVER CONTA--. Confirma? \n[S/N] >>> "):
					Usages.remover_conta(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=True)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i in escolhas[4]:
				if confirm(f"Você escolheu:  --TRANSFERÊNCIA ENTRE CONTAS--. Confirma? \n[S/N] >>> "):
					retorno = Usages.transferencia(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=True)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i in escolhas[5]:
				if confirm(f"Você escolheu:  --DESABONAR CONTA--. Confirma? \n[S/N] >>> "):
					retorno = Usages.descontar(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=True)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i in escolhas[6]:
				if confirm(f"Você escolheu:  --ABONAR CONTA--. Confirma? \n[S/N] >>> "):
					Usages.abonar(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=True)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i in escolhas[7]:
				if confirm(f"Você escolheu:  --CRIAR NOVA CLASSE--. Confirma? \n[S/N] >>> "):
					Usages.add_classe(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=True)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i in escolhas[8]:
				if confirm(f"Você escolheu:  --FORMATAR SALDO DE MÚLTIPLOS INDIVÍDUOS--. Confirma? \n[S/N] >>> "):
					retorno = Usages.formatar_contas(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=True)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i in escolhas[9]:
				if confirm(f"Você escolheu:  --ADICIONAR NOVA SEÇÃO--. Confirma? \n[S/N] >>> "):
					retorno = Usages.add_section(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=True)
					if retorno is not None:
						contas, desc = retorno[0:2]
						desc = desc + f' --Data atual: {data_atual}'
			elif i in escolhas[10]:
				if confirm(f"Você escolheu:  --SALVAR REGITRO--. Confirma? \n[S/N] >>> "):
					from manuseio import convert_contas_to_xlsx
					retorno = convert_contas_to_xlsx(contas=contas, nome_arquivo=nome_arquivo, verificar=True)
					if retorno is not None:
						print(f" salvo {nome_arquivo}\n - com sucesso.")
						from manuseio import manuseio_backup
						ListBackup = [["REG", data_atual, contas]]
						manuseio_backup(operation="ADD", arquivo='BACKUP.txt', ListBackup=ListBackup)
						desc = 'REGISTRO SALVO.'
					Historico.contas_antigas.append([data_atual, contas])
			if desc != '':
				Historico.historico.append(desc)
			print(data_atual)



if __name__ == "__main__":
	main()
	
	
				#es = str(input(F" Você deseja definir tddas as confirmações do programa como:\n0 - False\n1 - True\n [0/1] >>> "))
#				if confirm(f"Você deseja desativar a escolha de confirmações? Confirme: "):
#					if es == '0':
#						desconfirm = False
#					else:
#						desconfirm = True 