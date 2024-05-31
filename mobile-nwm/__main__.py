# To V4.6.1 >> v4 of this code
import Historico
import Usages
from Funcs import atual_data

desconfirm = None


# None = confirmações habilitadas no programa
# False = todas confirmações do programa são imediatamente taxadas como negativas
# True = todas confirmações do programa são imediatamente taxadas como Positivas


def main():
	from Funcs import confirm
	from Metadados_banco import version
	operacoes = [ "None" ]
	log = [ ]
	loops = 0
	desc = ''
	escolhas = [
		[ "0", "00", "/EXIT", "", "SAIR" ],
		# 0. escolhas[0][0] = num, escolhas[0][1] = num2, escolhas[0][2] = cmd, escolhas[0][3] = parametros, escolhas[0][4] == description
		[ "1", "01", "/SEE", "", "VER REGISTRO" ],  # 1
		[ "2", "02", "/ADD_CO", "-Section -Classe -Name -Money -Exp", "ADICIONAR CONTA" ],  # 2
		[ "3", "03", "/DEL_CO", "-Name", "DELETAR CONTA" ],  # 3
		[ "4", "04", "/TRANSF", "-Name -Section -Classe -Money -Name2 -Section2 -Classe2", "TRANSFERÊNCIA BANCÁRIA ENTRE CONTAS" ],  # 4
		[ "5", "05", "/DES_CO", "-Name -Money -Exp", "DESABONAR CONTA" ],  # 5
		[ "6", "06", "/SOMA_CO", "-Name -Classe -Section -Money -Exp", "ABONAR CONTA" ],  # 6
		[ "7", "07", "/ADD_CLA", "-Sect -Classe", "ADICIONAR NOVA CLASSE" ],  # 7
		[ "8", "08", "/FV_CO", "-Quantia", "FORMATAR SALDO DE MÚLTIPLAS CONTAS " ],  # 8
		[ "9", "09", "/ADD_SEC", "-Sect", "ADICIONAR SEÇÃO" ],  # 9
		[ "10", "010", "/OK", "", "SALVAR REGISTRO" ],  # 10
		[ "11", "011", "/DEL_CLA", "-Class -Sect", "DELETAR CLASSE" ],  # 11
		[ "12", '012', '/VER_VARS', "", "VER VARIÁVEIS" ],  # 12

		[ "-2", '-02', '/AUTO_SAVE', '-Bool', "ATIVAR/DESATIVAR SALVAMENTO AUTOMÁTICO (padrão == False)" ],  # -2
		[ "-1", "/?", "/HELP", "-Comando", "VER AJUDA" ] ]  # -1

	# Pega o registro bancário (var contas)
	from manuseio import convet_xlsx_to_contas, localizar_arquivo
	nome_arquivo = \
		localizar_arquivo(criar=True, text=False, dir='START-NWM/mobile-nwm', arquivo='registro.xlsx',
						  modo='rb', pandas=False, test_open=True)[ 2 ]
	contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo, modo='rb')

	def printalt(alternativas):
		for e in alternativas:
			print(e, end=" | ")
		print("\n")

	save = False

	def run(i=None, command=None, escolhas=escolhas, contas=contas):
		classe = section = name = name2 = money = exp = quantia = section2 = classe2 = CMD = None
		if type(command) == type(str()):
			cmds = command.lower().strip().replace('=', ' ').replace('  ', '').split(' ')
			i, *args = cmds
			def get_option_value(cmds=cmds, option=None):
				if option in cmds:
					return cmds[ cmds.index(option) + 1 ].replace('_', ' ')
				return None

			section = get_option_value(cmds, '-sect')
			classe = get_option_value(cmds, '-classe')
			name = get_option_value(cmds, '-name')
			money = get_option_value(cmds, '-money')
			exp = get_option_value(cmds, '-exp')
			name2 = get_option_value(cmds, '-name1')
			section2 = get_option_value(cmds, '-name2')
			classe2 = get_option_value(option='-classe2')
			quantia = get_option_value(option='-quantia')
			CMD = get_option_value(option='/')

		nonlocal save
		i = str(i).upper().strip()
		print(f"RUN: {i = }")
		if i in escolhas[ -1 ]:
			Usages.help(cmd=CMD)
			retorno = [ None, "Foi vista a ajuda." ]
		elif i in escolhas[ -2 ]:
			desc = F"\nO save automático está {'ligado' if save else 'desligado'}. "
			print(desc)
			if confirm(f"Você escolheu: --DEFINIR SAVE AUTOMÁTICO--. Confirma? \nS/N] >>> ") is False:
				return None
			if confirm("Digite 1 para salvar automaticamente todas as operações daqui para frente, digite 0 " \
					   "para não salvar automáticamente (use comando /OK para salvar manualmente).\n [0/1] >>> "):
				save = True
			else:
				save = False
			desc = F"\nO save automático está {'ligado' if save else 'desligado'}. "
			retorno = [ save, desc ]
		elif i in escolhas[ 0 ]:
			Usages.sair()
		elif i in escolhas[ 1 ]:
			if confirm(f"Você escolheu: --VER REGISTRO--. Confirma? \nS/N] >>> ") is False:
				return None
			Usages.ver_contas(tipo_do_registro='Completo', contas=contas, nome_arquivo=nome_arquivo, vars=True)
			desc = "O registro foi visto."
			retorno = [ None, desc ]
		elif i in escolhas[ 2 ]:
			if confirm(f"Você escolheu:  -- CADASTRAR CONTA NOVA--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.cadastrar_conta(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=save,
											 section=section, cla=classe, grana=money, EXP=exp, name=name)
			if retorno is not None:
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 3 ]:
			if confirm(f"Você escolheu:  --REMOVER CONTA--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.remover_conta(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=save, name=name,
										   classe=classe, section=section)
			if retorno is not None:
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 4 ]:
			if confirm(f"Você escolheu:  --TRANSFERÊNCIA ENTRE CONTAS--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.transferencia(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=save,
										   name=name, classe=classe, section=section,
										   name2=name2, classe2=classe2, section2=section2, movido=money)
			if retorno is not None:
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 5 ]:
			if confirm(f"Você escolheu:  --DESABONAR CONTA--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.descontar(contas=contas, nome_arquivo=nome_arquivo, save_in_archive=save, name=name,
									   classe=classe, section=section, dinheiro=money, exp=exp)
			if retorno is not None:
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 6 ]:
			if confirm(f"Você escolheu:  --ABONAR CONTA--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.abonar(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=save, name=name,
									classe=classe, section=section)
			if retorno is not None:
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 7 ]:
			if confirm(f"Você escolheu:  --CRIAR NOVA CLASSE--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.add_classe(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=save,
										secao_selected=section, nome_novo=classe)
			if retorno is not None:
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 8 ]:
			if confirm(f"Você escolheu:  --FORMATAR SALDO DE MÚLTIPLOS INDIVÍDUOS--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.formatar_contas(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=save,
											 vezes=quantia)
			if retorno is not None:
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 9 ]:
			if confirm(f"Você escolheu:  --ADICIONAR NOVA SEÇÃO--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.add_section(nome_arquivo=nome_arquivo, contas=contas, save_in_archive=save,
										 nome_novo=section)
			if retorno is not None:
				"""contas, desc = retorno[ 0:2 ]
				desc = desc + f' --Data atual: {data_atual}'"""
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 10 ]:
			if confirm(f"Você escolheu:  --SALVAR REGITRO--. Confirma? \nS/N] >>> ") is False:
				return None
			from manuseio import convert_contas_to_xlsx
			retorno = convert_contas_to_xlsx(contas=contas, nome_arquivo=nome_arquivo, verificar=True)
			comment = str(input("Digite um comentário do registro atual a ser salvo (Não precisa de data): "))
			if retorno is not None:
				print(f" salvo {nome_arquivo}\n - com sucesso.")
				from manuseio import manuseio_backup
				ListBackup = [ [ "REG", data_atual, comment, contas ] ]
				manuseio_backup(operation="ADD", arquivo='BACKUP.txt', ListBackup=ListBackup)
				desc = 'REGISTRO SALVO.'
			Historico.contas_antigas.append([ data_atual, contas ])
		elif i in escolhas[ 11 ]:
			if confirm(f"Você escolheu:  --DELETAR CLASSE--. Confirma? \nS/N] >>> ") is False:
				return None
			retorno = Usages.remover_classe(classe=classe, section=section, nome_arquivo=nome_arquivo, contas=contas,
											save_in_archive=save)
			if retorno is not None:
				retorno[ 1 ] += f' --Data atual: {data_atual}'
		elif i in escolhas[ 12 ]:
			if confirm(f"Você escolheu:  --VER VARIÁVEIS-. Confirma? \n[S/N] >>> ") is False:
				return None
			retorno = Usages.ver_contas(tipo_do_registro="S", nome_arquivo=nome_arquivo, contas=contas, vars=True)
			retorno = [ retorno, f'As variáveis foram vistas. --Data atual: {data_atual}  --Contas: {contas}' ]

		else:
			print(f"Comando {i} inválido. Tente novamente. ")
			return None
		return retorno

	def alt(escolha, contas=contas):
		escolha = escolha.strip().lower()
		if '/' in escolha and "-" in escolha:
			i, *args = escolha.split()
			i = i.upper().strip()
			if i in alternativas:
				return run(contas=contas, command=escolha)
			else:
				print(f">> Comando '{i}' inválido. Tente novamente. ")
				return None
		else:
			i, *args = escolha.split(' ')
			return run(i, contas=contas)


	while True:
		bad_escolhas = [ ]
		loops += 1
		# Recolhe alternativas inviáveis:
		qtia_sects = [ ]
		qtia_cla = [ ]
		qtia_nomes = [ ]
		for sect, classes in contas.items():
			if sect.strip().lower() != 'none':
				qtia_sects.append(sect)
				for classe, nomes in classes.items():
					if classe.strip().lower() != 'none':
						qtia_cla.append(classe)
						for nome, saldo in nomes.items():
							if nome.strip().lower() != 'none':
								qtia_nomes.append(nome)
		for pos, esco in enumerate(escolhas):
			if pos in [ 1, 3, 4, 5, 6, 8, 11 ] and [
				qtia_sects.__len__() < 1 or qtia_nomes.__len__() < 1 or qtia_cla.__len__() < 1 ]:
				bad_escolhas.append(esco)
		if qtia_cla.__len__() >= 1:
			try:
				find = bad_escolhas.index(escolhas[ 11 ])
				del bad_escolhas[ find ]
			except ValueError:
				pass
		if bad_escolhas.__len__() >= 1:
			print(
				f" Registro sem classe, oontas ou seções. Adicione com /ADD_SECT, /ADD_CLA, /ADD_CO. \n Registro: {contas}")
		data_atual = atual_data()
		print(
			f"\n\n~~~~ World Meeh: Bank! ~~~\n\n~~~ Program Version: {version} - Mobile Version~~~\n\nQual área do programa deseja entrar? Escolhas disponíveis:\n")
		alternativas = [ ]  # escolhas[n][0:3]
		# imprime escolhas:
		for item in escolhas:
			if item not in bad_escolhas:
				print(f"  ¬ {item[ 0 ]:^5} | {item[ 2 ]} {item[ -2 ]} -> \n	   {item[ -1 ]}")
			else:
				print(f"BLOQUEADO:  ¬  {item[ 0 ]:^5} | {item[ 2 ]} {item[ -2 ]}")
			for pos, alte in enumerate(item):
				if alte != '' and pos < 4:
					alternativas.append(alte.strip().upper())  # Salva alternativas escolha[0:3] (num, num, cmd)
		print(f"\n(Escolha o número ou digite o comando como /OPERAÇÃO -parametro)\n(-Name == Nome da conta + Classe."
			  f" Ex: /SOMA_CO -Name meeh_inu -Classe inu -Sect reino_da_folha -Money 347)\nMenu {loops} ", end="")
		try:  # Mostra comandos anteriores
			print(f" > O ultimo comando digitado foi: {operacoes[ -1 ]}")
			print(f"    Descrição do ocorrido: {Historico.historico[ -1 ]}")
		except IndexError:
			print(F"    Histórico ainda inacessivel.")
		# Faz escolha e armazena ela:
		escolha = str(input("\n    > Escolha >>> ")).strip().upper()
		passe = True
		# Verifica se escolha é válida:
		for es in bad_escolhas:
			if escolha in es:
				passe = False
				print(f" Você selecionou uma escolha bloquada. Tente novamente. ")
				break
		if passe is False:
			continue
		operacoes.append(escolha)
		i = escolha
		log.append(f"Foi digitado no menu, comando: {i}")

		if "&&" in escolha:
			commas = escolha.split('&&')
			for cmd in commas:
				cmd = cmd.strip()
				if "/" in cmd and "-" in cmd:  # Caso seja comando com argumentos:
					alt(escolha, contas=contas)


		# /ADD_CLA /ADD_CLA -reino da folha -inu && 12
		else:
			if '/' in escolha and "-" in escolha:
				alt(escolha)
			else:
				alt(i)


		if desc != '':
			Historico.historico.append(desc)
		print(data_atual)


if __name__ == "__main__":
	main()

