# To V4.6.2 >> v4.3 of this code
import Historico
import Usages
from Funcs import atual_data



# None = confirmações habilitadas no programa
# False = todas confirmações do programa são imediatamente taxadas como negativas
# True = todas confirmações do programa são imediatamente taxadas como Positivas

# Pega o registro bancário (var contas)
from manuseio import convet_xlsx_to_contas, localizar_arquivo

nome_arquivo = \
	localizar_arquivo(criar=True, text=False, dir='START-NWM/mobile-nwm_V5', arquivo='superreg.xlsx', modo='rb',
					  pandas=False, test_open=True)[ 2 ]
contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo, modo='rb')[0]


def main():
	from Funcs import confirm
	from Metadados_banco import version
	operacoes = [ "None" ]  # Mostra o histórico de operações
	log = [ ]  # guarda o histórico de escolhas
	loops = 0  # conta quantos loops While True está
	desc = ''  # Var de captura de descrições dos resultados das operações
	retorno = None
	global contas
	contas_local = contas
	global nome_arquivo
	escolhas = [  # Especifica as operações e escolhas disponíveis.
		[ "0", "00", "/EXIT", "", "SAIR" ],
		# 0. escolhas[0][0] = num, escolhas[0][1] = num2, escolhas[0][2] = cmd, escolhas[0][3] = parametros, escolhas[0][4] == description
		[ "1", "01", "/SEE", "", "VER REGISTRO" ],  # 1
		[ "2", "02", "/ADD_CO", "-Section -Classe -Name -Money -Exp", "ADICIONAR CONTA" ],  # 2
		[ "3", "03", "/DEL_CO", "-Name", "DELETAR CONTA" ],  # 3
		[ "4", "04", "/TRANSF", "-Name -Section -Classe -Money -Name2 -Section2 -Classe2",
		  "TRANSFERÊNCIA BANCÁRIA ENTRE CONTAS" ],  # 4
		[ "5", "05", "/DES_CO", "-Name -Money -Exp", "DESABONAR CONTA" ],  # 5
		[ "6", "06", "/SOMA_CO", "-Name -Classe -Section -Money -Exp", "ABONAR CONTA" ],  # 6
		[ "7", "07", "/ADD_CLA", "-Sect -Classe", "ADICIONAR NOVA CLASSE" ],  # 7
		[ "8", "08", "/FV_CO", "-Quantia", "FORMATAR SALDO DE MÚLTIPLAS CONTAS " ],  # 8
		[ "9", "09", "/ADD_SEC", "-Sect", "ADICIONAR SEÇÃO" ],  # 9
		[ "10", "010", "/OK", "", "SALVAR REGISTRO" ],  # 10
		[ "11", "011", "/DEL_CLA", "-Class -Sect", "DELETAR CLASSE" ],  # 11
		[ "12", '012', '/VER_VARS', "", "VER VARIÁVEIS" ],  # 12
		[ "13", "013", "/SEL_REG", "-data", 'SELECIONAR REGISTRO BANCÁRIO DE BACKUP' ],
		['14', 'feitos', '/feitos', '', 'RANK DE FEITOS EM ON'],

		[ "-2", '-02', '/AUTO_SAVE', '-Bool', "ATIVAR/DESATIVAR SALVAMENTO AUTOMÁTICO (padrão == False)" ],  # -2
		[ "-1", "/?", "/HELP", "-Comando", "VER AJUDA" ] ]  # -1

	save = False  # Expressa se o salvamento automático de operações está Ativado (True) ou desligado (False)

	def run(i=None, command=None, escolhas=escolhas, contas_param=contas):
		classe = section = name = name2 = money = exp = quantia = section2 = classe2 = CMD = None
		if type(command) == type(str()):
			print(f"Processando linha de comando...")
			cmds = command.lower().strip().replace('=', ' ').replace('  ', ' ').replace('-cmd ', '-comando ').replace(
				'-b ', '-bool ').replace('-b save', '-bool True ').replace('-cla ', '-classe ').replace(
				'-qtia ', '-quantia ').replace('-class ', '-classe ').replace('-ryo ', '-money ').replace(
				'-reino_', '-sect reino_').split(' ')
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
			CMD = get_option_value(option='-comando')
		else:
			print(F"Processando comando único...")

		nonlocal save
		i = str(i).upper().strip()
		if i == '':
			return None
		print(f"RUN: {i}")
		if i in escolhas[ -1 ]:
			print(f'{CMD = }')
			Usages.Help(cmd=CMD)
			retorno = [ None, "Foi vista a ajuda." ]
		elif i in escolhas[ -2 ]:
			desc = F"\nO save automático está {'ligado' if save else 'desligado'}. "
			print(desc)
			if confirm(f"Você escolheu: --DEFINIR SAVE AUTOMÁTICO--. Confirma? \nstr(S/N) >>> ") is False:
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
			if confirm(f"Você escolheu: --VER REGISTRO--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			Usages.ver_contas(tipo_do_registro='Completo', contas=contas_param, nome_arquivo=nome_arquivo, vars=False)
			desc = "O registro foi visto."
			retorno = [ None, desc ]
		elif i in escolhas[ 2 ]:
			if confirm(f"Você escolheu:  -- CADASTRAR CONTA NOVA--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.cadastrar_conta(contas=contas_param, nome_arquivo=nome_arquivo, save_in_archive=save,
											 section=section, cla=classe, grana=money, EXP=exp, name=name)
			if type(retorno) == type(list()):
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
				desc = retorno[ 1 ]
		elif i in escolhas[ 3 ]:
			if confirm(f"Você escolheu:  --REMOVER CONTA--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.remover_conta(contas=contas_param, nome_arquivo=nome_arquivo, save_in_archive=save, name=name,
										   classe=classe, section=section)
			if type(retorno) == type(list()):
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
				desc = retorno[ 1 ]
		elif i in escolhas[ 4 ]:
			if confirm(f"Você escolheu:  --TRANSFERÊNCIA ENTRE CONTAS--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.transferencia(contas=contas_param, nome_arquivo=nome_arquivo, save_in_archive=save,
										   name=name, classe=classe, section=section,
										   name2=name2, classe2=classe2, section2=section2, movido=money)
			if type(retorno) == type(list()):
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
				desc = retorno[ 1 ]
		elif i in escolhas[ 5 ]:
			if confirm(f"Você escolheu:  --DESABONAR CONTA--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.descontar(contas=contas_param, nome_arquivo=nome_arquivo, save_in_archive=save, name=name,
									   classe=classe, section=section, dinheiro=money, exp=exp)
			if type(retorno) == type(list()):
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
		elif i in escolhas[ 6 ]:
			if confirm(f"Você escolheu:  --ABONAR CONTA--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.abonar(nome_arquivo=nome_arquivo, contas=contas_param, save_in_archive=save, name=name,
									classe=classe, section=section)
			if type(retorno) == type(list()):
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
				desc = retorno[ 1 ]
		elif i in escolhas[ 7 ]:
			if confirm(f"Você escolheu:  --CRIAR NOVA CLASSE--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.add_classe(nome_arquivo=nome_arquivo, contas=contas_param, save_in_archive=save,
										secao_selected=section, nome_novo=classe)
			if type(retorno) == type(list()):
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
				desc = retorno[ 1 ]
		elif i in escolhas[ 8 ]:
			if confirm(
					f"Você escolheu:  --FORMATAR SALDO DE MÚLTIPLOS INDIVÍDUOS--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.formatar_contas(nome_arquivo=nome_arquivo, contas=contas_param, save_in_archive=save,
											 vezes=quantia)
			if type(retorno) == type(list()):
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
				desc = retorno[ 1 ]
		elif i in escolhas[ 9 ]:
			if confirm(f"Você escolheu:  --ADICIONAR NOVA SEÇÃO--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.add_section(nome_arquivo=nome_arquivo, contas=contas_param, save_in_archive=save,
										 nome_novo=section)
			if type(retorno) == type(list()):
				"""contas_param, desc = retorno[ 0:2 ]
				desc = desc + f'\n  --Data atual: {data_atual}'"""
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
				desc = retorno[ 1 ]
		elif i in escolhas[ 10 ]:
			if confirm(f"Você escolheu:  --SALVAR REGITRO--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.save_backup(contas=contas_param)
			retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
		elif i in escolhas[ 11 ]:
			if confirm(f"Você escolheu:  --DELETAR CLASSE--. Confirma? \nstr(S/N) >>> ") is False:
				return None
			retorno = Usages.remover_classe(classe=classe, section=section, nome_arquivo=nome_arquivo, contas=contas_param,
											save_in_archive=save)
			if type(retorno) == type(list()):
				retorno[ 1 ] += f'\n  --Data atual: {data_atual}'
				desc = retorno[ 1 ]
		elif i in escolhas[ 12 ]:
			if confirm(f"Você escolheu:  --VER VARIÁVEIS-. Confirma? \n[S/N] >>> ") is False:
				return None
			retorno = Usages.ver_contas(tipo_do_registro="S", nome_arquivo=nome_arquivo, contas=contas_param, vars=True)
			retorno = [ retorno, f'As variáveis foram vistas. --Data atual: {data_atual}  --Contas: {contas_param}' ]
		elif i in escolhas[ 13 ]:
			if confirm(f"Você escolheu:  --SELECIONAR REGISTRO-. Confirma? \n[S/N] >>> ") is False:
				return None
			retorno = Usages.select_backup()
			global contas
			contas = convet_xlsx_to_contas(nome_arquivo=nome_arquivo, modo='rb')[0]
		elif i in escolhas[14]:
			if confirm(f"Você escolheu:  --VER RANK DE FEITOS EM ON-. Confirma? \n[S/N] >>> ") is False:
				return None
			retorno = Usages.feitosemon()
		else:
			print(f"Comando {i} inválido. Tente novamente. ")
			return None
		return retorno

	def alt(escolha, contas_=contas):
		escolha = escolha.strip().lower()
		if '/' in escolha and "-" in escolha:
			i, *args = escolha.split()
			i = i.upper().strip()
			if i in alternativas:
				return run(contas_param=contas_, command=escolha)
			else:
				print(f">> Comando '{i}' inválido. Tente novamente. ")
				return None
		else:
			i, *args = escolha.split(' ')
			return run(i, contas_param=contas_)

	while True:
		bad_escolhas = [ ]
		loops += 1
		# Recolhe alternativas inviáveis:
		qtia_sects = [ ]
		qtia_cla = [ ]
		qtia_nomes = [ ]
		for sect, classes in contas_local.items():
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
				qtia_sects.__len__() < 1 or qtia_nomes.__len__() < 1 or qtia_cla.__len__() < 1 ] is True:
				bad_escolhas.append(esco)
		if qtia_cla.__len__() >= 1:
			try:
				find = bad_escolhas.index(escolhas[ 11 ])
				del bad_escolhas[ find ]
			except ValueError:
				pass
		if bad_escolhas.__len__() >= 1:
			print(
				f" Registro sem classe, oontas ou seções. Adicione com /ADD_SECT, /ADD_CLA, /ADD_CO. \n Registro: {contas_local}\n")
		data_atual = atual_data()
		print(f"\n\n~~~~ World Meeh: Bank! ~~~\n\n~~~ Program Version: {version} - Mobile Version~~~\n\nQual área do programa deseja entrar? Escolhas disponíveis:\n")
		alternativas = [ ]  # escolhas[n][0:3]
		# imprime escolhas:
		for item in escolhas:
			if item not in bad_escolhas:
				print(f"  ¬ {item[ 0 ]:^5} | {item[ 2 ]} {item[ -2 ]} -> \n	   {item[ -1 ]};")
			else:
				print(f"BLOQUEADO:  ¬  {item[ 0 ]:^5} | {item[ 2 ]} {item[ -2 ]};")
			for pos, alte in enumerate(item):
				if alte != '' and pos < 4:
					alternativas.append(alte.strip().upper())  # Salva alternativas escolha[0:3] (num, num, cmd)
		print(f"\nNOTAS:\n1-(Escolha o número ou digite o comando como /OPERAÇÃO -parametro)\n2-(-Name == Nome da "
			  f"conta + Classe. Ex: /SOMA_CO -Name meeh_inu -Classe inu -Sect reino_da_folha -Money 347)\n3-(Use $ na "
			  f"linha de comando para forcar acesso mesmo em opções bloqueadas (cuidado)).\n 4- {'(Você está manuseando um arquivo não salvo)' if Usages.validar(contas=contas_local, nome_arquivo=nome_arquivo) is True else '(A variável contas_param atual está salva)'}\n\nMenu {loops} ",
			  end="")
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
			if escolha in es and '$' not in escolha:
				passe = False
				print(f" Você selecionou uma escolha bloquada. Tente novamente. ")
				break
		if passe is False:
			continue
		escolha = escolha.replace('$', '')
		operacoes.append(escolha)
		i = escolha
		log.append(f"Foi digitado no menu, comando: {i}")

		def init(escolha, _contas=contas):
			if "&&" in escolha:
				commas = escolha.split('&&')
				for cmd in commas:
					cmd = cmd.strip()
					if "/" in cmd and "-" in cmd:  # Caso seja comando com argumentos:
						retorno = alt(escolha, contas_=_contas)
				# /ADD_CLA /ADD_CLA -reino da folha -inu && 12
			else:
				if '/' in escolha and "-" in escolha:
					retorno = alt(escolha, contas_=_contas)
				else:
					retorno = alt(i, contas_=_contas)
			return retorno

		#try:
		retorno = init(escolha, _contas=contas_local)


		if type(retorno) == type(list()):
			try:
				desc = retorno[ 1 ]
				if desc != '':
					Historico.historico.append(desc)
				if type(retorno[0]) == type(dict()):
					contas = retorno[0]
					print("Var local {contas_local} atualizada.")
			except IndexError:
				desc = ''
		print(f"{retorno=}")

		print(data_atual)



if __name__ == "__main__":
	main()
