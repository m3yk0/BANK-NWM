# Fazer um sistema bancádrio p RPG completo
# Possibilidade de compra de itens
# iguslmente salvar/mostrar itens e patrimonio dos guri
# Uma I.A (Assistente virtual) irá ajudar o guri tb.

versao = '1.0.0'
__author__ = "Software m3yk0"
__copyright__ = "Copyright (C) 2023 N.W.M_OFC"
__license__ = "Public Domain"
__version__ = "1.0.0"

"""
READ-ME:
    Versão: {versao}
    v 1.2.3 = controles: adicionado classes dentro de cada seção.
    v 1.2.1 = código "Funcs", separado do código "Banco". Uso por import
    v 1.2.0 = código "controles" separado do codigo "Banco" (uso por import)
    v 1.1.9 = var mundial lideres
    v 1.1.8 = var mundial reinantes
    v 1.1.7 = data_reg virou var global
    v 1.1.6 = Operação numero 3 desligada.
    v 1.1.5 = Ao invés de reinos, as contas são separadas pelo nome "seções".
    v 1.1.4 = def valores adicionado taxa silic
    v 1.1.3 = def valores adicionado meta silic
    v 1.1.2 = def individuos e registros reformados
    v 1.1.1 = def reinos
    v 1.1.0 = Adicionado "reinos" em contas
    v 1.0.0 = Escolher registro antigo, como um principal (ctrl+z)
    v 0.2.9 = Agora não é mais possível um indivíduo negativado, realziar transferências bancárias.
    v 0.2.8 = Bug de seleção de indivpiduos, corrigido
    v 0.2.7 = Melhorias (nomes, váriaveis, contas.copy, etc)
    v 0.2.6 = Corrigido bugs de Backup
    v 0.2.5 = Melhorias (money de INT foi para FLOAT (2 casas) e EXP 1 casa), nome de vars mudados para sem acentos, algumas instruções PEP8 seguidas.
    v 0.2.4 = Corrigido bugs na operacao 3
    v 0.2.3 = Bloqueio de operacoes
    v 0.2.2 = def confirm()
    v 0.2.1 = def ver registros antigos
    v 0.2.0 = histórico de funções escolhidas pelo usuário
    v 0.1.9 = Func. individuos()
    v 0.1.8 = corrigindo func 'alternativa()'
    v 0.1.7 = correção de bugs
    v 0.1.6 = voltado base 0.1.4 + incrementos de função 'alternativa()' em cada funcao 
    v 0.1.5 = cada alternativa = funcão
    v 0.1.4 = correção de português
    -
    v 0.1.1 = Opção 6 foi fechada (opc 1 já cumpria tal funcão)
    v 0.1.2 = programa aninhado em def main() 
    v 0.1.3 = def confirm_input()

    vars. constantes são em MAIUSCULO
    vars. function em minusculo
    classes em Titled (sem underlines)
    >>> Todo código de operação é separado em 2 comentários:
    #-- CÓDIGO --# == área do código
    #-- FLAG --# == área da finalização bem-sucedida do código.
        Em flag, sempre deve haver:
        del váriaveis usadas na operação
        end = z = True == representa que a operação foi finalizada 
        # end = TRUE == finalizado com sucesso
        # end = FALSE == finalizado com falha entre a operação
        # end = NONE = Operação em estado aberto/não finalizada.
        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                                      "desc: DESCRIÇÃO DA FUNÇÃO."])
"""

"""
    BUGS N RESOLVIDOS:

    > Ao clicar 4.5, em.seguida errar a opcão, mas, outrora, selecionar individuo correto, vem um erro
    > O mesmo para 4.4

"""

"""
# armazenando o caminho do arquivo de módulos na variável file_path
file_local = datetime.__file__
# armazenando o diretório (caminho do adquivo) na variável dir
dir = os.path.dirname(file_local)
print(dir)

def mod(tool):
    import os
    try:
        import tool
        mod = True
        print(f"{tool} instalado.")
    except ImportError:
        mod = False
        print(f" {tool} NÃO instalado. Aguarde...")
    if mod is False:
        a = os.system(f'pip install {tool}')
        print("Instalamos para você.\n", a )
        import datetime
    else:
        pass
"""

"""    def salvar(filename, info):
        file = open('{}.csv'.format(filename),'a',encoding='UTF-8')
        file.write(info+'\n')
        file.close()

    lis = [{"Meyko": [10.0, 1000.0]}]
    salvar(lis, lis)

    def ler(filename):
        file = open('{}.csv'.format(filename),'r', encoding='UTF-8')
        return file.read()
"""

"""
AJUSTES RESTANTES:
    1 > Correção de bugs
    2> Firmar versão do python e dos modulos usados (se estão iguais ou atualizadas ao que o programa foi baseado)
    3> Importar e exportar as var principais (dic_reg,backup registros)
    4>  Implementar o código em um backup automático (ou seja, automatizar o ajuste 3 citado acima, para que, sempre em algum momento do programa, salve o arquivo do relatório)
    5 > Talvez, manusear EXEL com este programa (ou faze-lo no exel quando estudado tal software)
    6 > divisão de clãs
    7 > Upar no Github
    8 > Usar no RPG!

"""


def main():
    print("\nBem-vindo ao programa Meeh World: Bank!\n")
    # Imports Bib. padroes:
    import datetime
    import sys
    from os import system as osys
    import os
    from typing import List, Union, Dict
    import time
    # Imports Bib. terceiros:
    # Imports Bib. Local:
    	
    from controles import contas, backups, data_reg, historico, reinantes, valor_mundial, valor_guardado, lideres, dic_reg, avisos, i, start, log, classes_c2, vms, ems, meta_selic, tot_fee, tot_vpms, all_class, all_sections, all_persons
    
    from Funcs import programar_data, zero, run, atual_data, plural, alternativa, confirm, prevent, money_func, iterar, recort, backups_fc, values_fc, regselect_fc, magnatas_fc, secoes_func, classes_func, account_fc, hist_fc, sectsee_fc
    
    global contas, backups, data_reg, historico, reinantes, valor_mundial, valor_guardado, lideres, dic_reg, avisos, i, start, conclusoes, log
    log.append("módulos importados...")
    
    """arqbank_json = open("arqbank.json", 'a')
    arqbank_json.writelines(f"{backups=}")
    arq_read = open("arqbank.json", 'r')
    arq_read = arq_read.readlines()
    print("\n",arq_read, "\n")"""
   
                                 
                                 				
    log.append("Carregando menu...")
    run()
    # Mostra menu:
    while True:
        print("\n~~~~ World Meeh: Bank! ~~~\n")
        print(f"\n ~~~ Program Version: {versao} ~~~\n")
        print("\n"
              "    Qual área do programa deseja entrar?:\n"
              "    0- Sair"
              "\n    1- Visualizar registro bancário\n    2- Magnatas\n    3- VMS (checar valor mundano e valor barrado, e seus ajustes)\n    4- Processar card bancário\n"
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
              "    5- Definir registro antigo como principal\n"
              "    6- Ver histórico de operações\n"
              "    7- Atualizar registro\n"
              "    8- Avisos\n"
              "    ...- CDI, PIB, Juros, RH, parcelas...")
        try:
            escolha = float(input("    Escolha: "))
            i = escolha
            log.append(f"Foi digitado no menu, opção {i}")
        except ValueError:
            print(f"Erro. Use um valor numérico.")
            continue



        # REALIZA BLOQUEIO DE OPERACOES:
        if start is True:
            # pega data e indice de dic_reg
            for data, index in dic_reg.items():
                data = data
            # Caso dic_reg (registro atual) esteja vazio:
            if dic_reg[data].__len__() < 1:
                print(f"REGISTRO SEM REINOS! Operações bloqueadas:")
                # Bloqueio de operações caso dic_reg vazio:
                bloq = [2, 4.1, 4.2, 4.3, 4.4, 4.5, 3.6, 4.8, 4.9, 4.10, 4.11, 4.12]
                print(f"{iterar(bloq)}\n ESCOLHA OPÇÃO DE ADICIONAR NOVA SEÇÃO PARA DESBLOQUEAR (4.7)!")
            #Caso registro sem classes:
            elif all_class.__len__() < 1:
                print(f"REGISTRO SEM CLASSES!\n Operações Bloqueadas:")
                bloq = [2, 4.1, 4.2, 4.3, 4.4, 4.5, 4.8, 4.9, 4.10, 4.11, 4.12]
                print(f"{iterar(bloq)}\n ESCOLHA OPÇÃO DE ADICIONAR NOVA SEÇÃO PARA DESBLOQUEAR! (4.9)")
            elif all_persons.__len__() < 1:
                print(f"REGISTRO SEM CONTAS!\n Operações Bloqueadas:")
                bloq = [2, 4.2, 4.3, 4.4, 4.5, 4.10, 4.11, 4.12]
                print(f"{iterar(bloq)}\n ESCOLHA OPÇÃO DE ADICIONAR NOVA SEÇÃO PARA DESBLOQUEAR! (4.1)")
            else:
                print("~~ Todas operações estão disponíveis. ~~")
                bloq = []
            if i in bloq:
                    print(
                        f"Você escolheu uma opção bloqueada. Para desbloquear as tais, use a opcão recomendada de desbloqueio.")
                    continue


        # SAIR:
        if i == 0:
            z = alternativa(i)
            if z is None:
                print(f"Até logo!")
                print(f"\n", "-=" * 15, end="-\n")
                del z
                exit()

        # MOSTRAR REGISTROS:
        if i == 1:
            z = alternativa(i)
            if z is None:
                print(f"\n(SELECIONADO: VISUALIZAR ALGUM REGISTRO (e seus avisos))\n")
                global regist, registro, var_selecionada, data_select, b_r
                data_atual = atual_data()
                # --- Código ---#
                # -- Checa se há registros antigos --#
                reg_selct = regselect_fc()
                if reg_selct == None:
                	print(f"Houve um erro com a func. regselect_fc(). Registro não pode ser mostrado.")
                if reg_selct != None:
                    caiu_em, b_r, data_select = reg_selct[0], reg_selct[1], reg_selct[2]
                    b_r = b_r[data_select]
                    # --- Mostra o registro ---#
                    values_a = values_fc()
                    values = values_a
                    if values != None:
	                    vms, ems, meta_selic, pvms, all_indiv, all_pvms, all_taxas, tot_secoes, tot_class, moneypersec, feepersec = values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10]
                    else:
                    	print(f"Houve um erro com a func. values_fc(). Registro não pode ser mostrado.")
                    	z = end = False
                    	break
                    mag = magnatas_fc()
                    if mag != None:
                    	lismag = mag[0]
                    else:
                    	print(f"Houve um erro com a func. magnatas(). Registro não pode ser mostrado.")
                    cont = 0
                    print(f"\n"
                          f".    ╔╦════•  •✠• ❀•✠ • •═══╦╗\n"
                          f"    *Registro de todos os ladinos*\n"
                          f"    ╚╩════• •✠• ❀ •✠ • •═══╩╝ \n\n"
                          f"*Staffs (novos e antigos):*\n	Meyko Ivory,\n	Meeh Inu,\n	Susumo Tsuki,\n 	Naomi Uzuki,\n	Yu Zuky,\n	Chaos Akaguma,\n 	Naruko Namikaze,\n 	Yang Uchiha,\n	Rimawari Hyuuga,\n	Isa Akaguma\n"
                          f"	━━━━━━━━━━━ ✠ ━━━━━━━━━━\n"
                          f"– *VMS🌐:* {money_func(vms)}\n"
                          f"– *META SELIC💰:* {money_func(meta_selic)}\n"
                          f"– *EMS✨:* {money_func(ems)}\n"
                          f"– IPCA: {meta_selic - vms}"
                          f"\n*MAGNATAS*:\n"
                          "{}\n".format(iterar(recort(lismag, 4), ', \n')),
                          f"\n*VERIFICAÇÕES:*\n"
                          f"_¬   Soma de todos PVMS: {money_func(all_pvms)}_ _{'é igual ao VMS.' if all_pvms == vms else f'ATENÇÃO: Não é igual ao VMS. Isso significa que este registro não está valido! Diferença: {vms - all_pvms}'}_\n"
                          f"¬   _Soma de todas as taxas: {money_func(all_taxas, 2)}_ {'' if all_taxas == 100.0 else f'_ATENÇÃO: Soma das taxas não é igual a 100. Este registro está dado como inválido. Diferença: {100 - all_taxas}._'}\n"
                          f"¬   _VMS + META SELIC SEMPRE ser == {valor_guardado}. Total: {vms + (meta_selic)}._ {'' if (vms+(meta_selic)) == valor_guardado else f'_ATENÇÃO: O resultado não é o valor guardado.. Este registro está dado como inválido._'}\n"
                          f"¬   _Diferença entre VMS e META SELIC: {meta_selic - vms}_\n"
                          f"\n*NOTAS:*\n"
                          f"– EMS = Total de EXP; VMS = Total de grana em mãos; META SELIC = Dinheiro guardado no banco.\n"
                          f"– Total de seções: {b_r.__len__()}\n"
                          f"– Total de classes ativas: {tot_class.__len__()}\n"
                          f"– Total de contas: {all_indiv.__len__()}\n"
                          )
                    for c, item in enumerate(b_r):
                        for secao, classes_lis in item.items():
                        	if c == 0:
                        		print(
f"""\n		━━━━━━━━━━  ✠  ━━━━━━━━━━""",
	f"""*Contas em conjunto/NPCs:*
	*PVMS das contas em conjunto:* {money_func(moneypersec[secao])}$
	*Taxa Selic das contas em conjunto:*  {money_func(feepersec[secao])}%""")
                        		for num, classes_dict in enumerate(classes_lis):
                        			for classe, contas_lis in classes_dict.items():
                        				print(
f"""	*{classe.upper()}:*
	~_Cod: dic_reg[data_reg][{c}]['{secao}'][{num}]['{classe}']_~""")
                        				for n, account_dict in enumerate(contas_lis):
                        					for name, valores in account_dict.items():
	                        					print(f"\n ¬ ~_{cont}-{c}.{num}.{n}_~ - {name.title()}: ", end="")
	                        					for index, val in enumerate(valores):
	                        						print(f" {money_func(val)}{'$ / ' if (index % 2) == 0 else 'EXP'}", end="")
                        				if n == contas_lis.__len__() -1:
                        					print(
f"""\n		━━━━━━━━━━  ✠  ━━━━━━━━━━""")
                        	else:
                        		print(f"""
     *●-  -=- {secao.upper()} -=-    -●*
	*PVMS do Reino:* {money_func(moneypersec[secao])}$
	*Taxa Selic do Reino:* {money_func(feepersec[secao])}%
	Reinante: {prevent(reinantes, secao)}
	Leis: {'Barradas' if prevent(reinantes, secao) == 'None' else 'Ativas'}
	Classes: {iterar(prevent(classes_c2[0],secao)) if prevent(classes_c2[0], secao) != 'None' else 'None'}""",
f"""\n		━━━━━━━━━━  ✠  ━━━━━━━━━━""")
	                        	for num, classes_dict in enumerate(classes_lis):
                        			for classe, contas_lis in classes_dict.items():
                        				print(f"""
	*Classe: {classe.title()}*
	*Líder:* {prevent(lideres, classe).title()}
	~_Cod: dic_reg[data_reg][{c}]['{secao}'][{num}]['{classe}']_~ """)
                        				for n, account_dict in enumerate(contas_lis):
                        					for name, valores in account_dict.items():
                        						cont += 1
	                        					print(f"\n ¬ ~_{cont}-{c}.{num}.{n}_~  - {name.title()}: ", end="")
	                        					for index, val in enumerate(valores):
	                        						print(f" {money_func(val)}{'$ / ' if (index % 2) == 0 else 'EXP'}", end="")
                        				if n == contas_lis.__len__() -1:
                        					print(
f"""\n		━━━━━━━━━━  ✠  ━━━━━━━━━━""")
                    print(
	                        f"\nAVISOS:\n Para o registro: {data_select}:\n aviso de atualização: {avisos[0]['avisos de atualizacoes'][f'{data_select}']}")
                    try:
                        			print(f"Aviso geral: {avisos[1]['avisos gerais'][f'{data_select}']}")
                    except KeyError:
                        			print(f'Sem aviso geral para o registro selecionado.')
                        			print(f"Aviso geral: {avisos[1]['avisos gerais'][f'11/07/2023-02:09:01']}")
                    # -- flag --#
                    end = z = True
                    historico.append([f"Concluído funcão 1, para o registro {b_r}, as {data_atual}",
	                                      "desc: O registro foi visto."])
	                                      
	                                      
        # VER MAGNATA:
        if escolha == 2:
            z = alternativa(i)
            while z is None:
                data_atual = atual_data()
                print(f"\n(SELECIONADO: VER RANK DE MAGNATAS)\n")
                mag = magnatas_fc()
                sort_money, sort_exp = mag[0], mag[1]
                if mag == None:
                	print(f"Função retornou erro. Operação cancelada. ")
                	z = end = False
                	break
                else:
                    cont = 0
                    # --- Mostra os resultados ---#
                    # MAGNATA MONEY
                    print(f"""\nlista de riqueza monetária (maior para menor): \n""")
                    for name, grana in sort_money.items():
                     	name = name.title()
                     	grana = round(grana, 2)
                     	if cont == 0:
                       	 print(f"{cont+1}: {name} (MAGNATA) —> grana: {grana}$")
                     	else:
                    	    print(f"{cont+1}: {name} —> grana: {grana}$")
                     	cont += 1
                    # MAGNATA EXP
                    print(f"""\nlista de riqueza EXP (maior para menor):\n""")
                    cont = 0
                    for name, exp in sort_exp.items():
                    	name = name.title()
                    	grana = round(grana, 2)
                    	if cont == 0:
                        	print(f"{cont+1}: {name} (MAGNATA) —> EXP: {exp}$")
                    	else:
                        	print(f"{cont+1}: {name} —> EXP: {exp}$")
                    	cont += 1
                    z = end = True
                    historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
	                                  "desc: Foi checado os magnatas."])
	                                  

        # ===> CHECAR VMS:
        if escolha == 3:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: CHECAR VMS)\n")
                data_atual = atual_data()
                # --- Código ---#
                # --- criação de vars ---
                # -- Checa se há registros antigos --#
                if backup_registros[0].__len__() >= 2:
                    print(f"\nHá registros antigos salvos. Você pode selecionar qual registro salvo deseja ver...\n")
                    # Seleciona qual registro quer ver
                    regist = registros()
                    reg_selecionado, data_selecionada, registro = regist[0], regist[1], regist[2]
                    caiu_em = 'antigo'
                    b_r = registro
                else:
                    print(f"\nVocê verá o registro atual.\n")
                    # Caso não tenha reg. antigo: b_r == registro atual
                    b_r = dic_reg
                    # Define a variavel data de b_r
                    for data, reg in b_r.items():
                        registro = reg
                    data_selecionada = data
                    caiu_em = 'novo'
                # Verifica se registro pode ser visto:
                print(f"Data_selecionada: {data_selecionada}")
                print(f"FUNCÃO EM MANUTENÇÃO!")
                if caiu_em == 'novo' or caiu_em == 'antigo':
                    del caiu_em, b_r
                    z = end = False
                    break
                    """# --- Realiza operação de analise da função ---#
                    # Calcula a inflação
                    # --- Deleta as var usadas ---
                    # Caso não possa ser visto:"""
                elif caiu_em in "none":
                    print(f"\nErro. O registro a ser visto não pôde ser definido, tente novamente.\n")
                    del caiu_em, b_r
                    z = end = False
                    break


        # CADASTRAR NOVO INDIVIDUO:
        if escolha == 4.1:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: CADASTRAR NOVO INDIVÍDUO)\n")
                data_atual = atual_data()
                print(f"~ Escolha seção e classe onde a nova conta ficará! ~")
                sc = classes_func()
                if sc != None:
	                classe_select, classe_value, secao_selected, secao_value, contas_da_classe, data_reg, reg_classe = sc[0], sc[1], sc[2], sc[3], sc[4], sc[5], sc[6]
	                print( dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select])
	                try:
	                    nome_novo = str(input("Nome e classe da conta nova: ")).title().strip()
	                    din = float(input("Dinheiro: "))
	                    exp = float(input("EXP: "))
	                    exp = round(exp, 1)
	                    din = round(din, 2)
	                except ValueError:
	                    print(f"Valor incorreto. Operação cancelada!")
	                    z = end = False
	                    break
	                if nome_novo == "":
	                    print(f"O nome não pode estar em branco. Operação cancelada.")
	                    del nome_novo, din, exp
	                    z = end = False
	                    break
	                else:
	                    print(f"Conta a ser registrada:\n nome: {nome_novo}\nSaldo: {din}$ / {exp}EXP. Na seção: {secao_selected} e classe {classe_select}. \nConfirma?")
	                    conf = confirm()
	                    if conf is True:
	                        print("Certo. Vá ao menu e digite 7 para atualizar.")
	                        nova_conta = {nome_novo: [din, exp]}
	                        all_persons.appens(nome_novo)
	                        # Salva nova conta:
	                        dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select].append(nova_conta)
	                        print( dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select])
	                        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
	                                          f"Cadastrado novo indivíduo ({nome_novo} com saldo de {din}$/{exp}EXP)."])
	                        del nome_novo, din, exp
	                        z = end = True
	                    else:
	                        print(f"Operação cancelada.")
	                        del nome_novo, din, exp
	                        z = end = True
	                        break
                elif sc == None:
                	print(f"Reino e Classe pertencente não pôde ser escolhida. Operação cancelada.")
                	z = end = False
                	break


        # EXCLUIR CONTA:
        if escolha == 4.2:
            print(f"~ Excluir Conta ~")
            z = alternativa(i)
            if z is None:
                print(f"\n(SELECIONADO: EXCLUIR INDIVÍDUO)\n")
                # try:
                data_atual = atual_data()
                pp = account_fc()
                reg_person, lis_br, name, pp_value = pp[0], pp[1], pp[2], pp[3]
                date, i_sec, sect, i_cla, classe, i_con, name = lis_br[0], lis_br[1], lis_br[2], lis_br[3], lis_br[4], lis_br[5], lis_br[6]
                id = all_persons.index(name)
                # -- Confirma conta selecionada:
                print(f"Deseja excluir a conta: {dic_reg[date][i_sec][sect][i_cla][classe][i_con]} ?")
                confirm_cont = confirm()
                if confirm_cont is True:
                    del dic_reg[date][i_sec][sect][i_cla][classe][i_con]
                    del all_persons[id]
                    print(f"Registro: {iterar(dic_reg)}")
                    print(f"Certo, para declarar opção como definitiva, vá em opção 7.")
                    historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                                      f"Foi excluído a conta {name}"])
                    del name, date, i_sec, i_cla, classe, i_con, pp, reg_person, lis_br, pp_value
                    z = end = True
                else:
                    # --- Deleta as var usadas ---#
                    del name, date, i_sec, i_cla, classe, i_con, pp, reg_person, lis_br, pp_value
                    print(f"Operação cancelada.")
                    z = end = False
                    

        # TRANSF. ENTRE CONTAS
        if escolha == 4.3:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: TRANSFERÊNCIA BANCÁRIA)\n")
                data_atual = atual_data()
                # -- seleciona individuos --#
                #    global indiv, di, nome_guri, data_reg
                print(f"Escolha a conta que realizará o depósito...")
                time.sleep(1.5)
                pp1 = account_fc()
                reg_person1, lis_br1, nome1, pp_value1 = pp1
                date1, i_sec1, sect1, i_cla1, classe1, i_con1, name1 = lis_br1
                print(f"{name1.title()} irá transferir dinheiro para... ESCOLHA A CONTA CREDITADA:")
                time.sleep(1.5)
                pp2 = account_fc()
                reg_person2, lis_br2, nome2, pp_value2= pp2
                date2, i_sec2, sect2, i_cla2, classe2, i_con2, name2 = lis_br2
                print(f"{nome2.title()} receberá dinheiro de {nome1.title()}\n")
                # Captura saldo dos individuos
                money1 = dic_reg[date1][i_sec1][sect1][i_cla1][classe1][i_con1][name1][0]
                money2 = dic_reg[date2][i_sec2][sect2][i_cla2][classe2][i_con2][name2][0]
                print(money1, money2)
                # -- valida a escolha --#
                if nome1 == nome2:
                    print(f"Não é possivel transferir para a mesma conta. Operação cancelada")
                    print(f"\n", "-=" * 15, end="-\n")
                    z = end = False
                    continue
                elif money1 <= 0:
                    print(f"Usuário a transferir dinheiro, não pode estar com a conta negativada nem zerada.")
                    print(f"Operação cancelada.")
                    print(f"\n", "-=" * 15, end="-\n")
                    z = end = False
                    continue
                else:
                    # -- Decide valor a ser desabonado --#
                    try:
                        movido = float(input(
                            f"Quantos reais deseja mover? {nome1} tem {money1}R$ disponíveis: "))
                        movido = round(movido, 2)
                    except ValueError:
                        print(f"Valores inválidos. Operação cancelada.")
                        z = end = False
                    # -- Valida valor --#
                    if movido > money1:
                        print(f"O dinheiro movido excede o dinheiro disponível do saldo do credor.")
                        del movido
                        z = end = False
                    elif movido == 0:
                        print(f"Você não pode transferir 0R$.")
                        print(f"Operação cancelada.")
                        print(f"\n", "-=" * 15, end="-\n")
                        del movido
                        end = False
                        z = end = False
                    # -- confirma --#
                    else:
                        print(f"A conta de {nome1}, então ficará com: {dic_reg[date1][i_sec1][sect1][i_cla1][classe1][i_con1][name1][0] - movido}R$\n"
                              f"e {nome2}, ficará com: {dic_reg[date2][i_sec2][sect2][i_cla2][classe2][i_con2][name2][0] + movido}R$.\n"
                              f"confirma?")
                        conf = confirm()
                        if conf is True:
                            dic_reg[date1][i_sec1][sect1][i_cla1][classe1][i_con1][name1][0] -= movido
                            dic_reg[date2][i_sec2][sect2][i_cla2][classe2][i_con2][name2][0] += movido
                            print(f"O registro ficará: {dic_reg}. Escolha opcão 7 para validar.")
                            historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                                              f"Transferência de {movido} por {nome1} para {nome2}."])
                            print(f"Operação concluida.")
                            print(f"\n", "-=" * 15, end="-\n")
                            del movido
                            end = z = True
                        elif conf == False:
                            print(f"Operação cancelada.")
                            print(f"\n", "-=" * 15, end="-\n")
                            del movido
                            end = z = False


        # DESABONAR:
        if escolha == 4.4:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: DESABONAR CONTA DE INDIVÍDUO)\n")
                data_atual = atual_data()
                pp = account_fc()
                reg_person, lis_br, name, pp_value = pp
                data, i_sec, sect, i_cla, classe, i_con, name = lis_br
                # -- Decide valor a ser desabonado --#
                try:
                    money = float(input(f"Quantos reais deseja retirar?: "))
                    money = round(money, 2)
                    exp = float(input(f"Quantos EXP deseja retirar?: "))
                    exp = round(exp, 1)
                except ValueError:
                    print(f"Valor numérico incorreto. Operacao cancelada.")
                    z = end = False
                    break
                # -- valida valor --#
                if (money + exp) == 0:
                    print(f"Você não pode retirar 0$ e 0EXP.")
                    print(f"Operação cancelada.")
                    print(f"\n", "-=" * 15, end="-\n")
                    z = end = False
                    break
                else:
                    # -- confirmação --#
                    print(
                        f"A conta de {nome}, então ficará com: {dic_reg[data][i_sec][sect][i_cla][classe][i_con] [nome][0] - money}R$ e "
                        f"{dic_reg[data][i_sec][sect][i_cla][classe][i_con][nome][1] - exp} EXP. confirma? ")
                    conf = confirm()
                    if conf is True:
                        # assert isinstance(data_reg, object)
                        dic_reg[data][i_sec][sect][i_cla][classe][i_con][nome][0] -= money
                        dic_reg[data][i_sec][sect][i_cla][classe][i_con][nome][1] -= exp
                        print(f"Registro ficará: {dic_reg}. Escolha opção 7 para salvar como novo registro.")
                        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                                          f"Retirado {money}$ e {exp}EXP de {nome}"])
                        del money, exp
                        z = end = True
                    # --- Deleta as var usadas ---#
                    else:
                        print(f"Operação cancelada.")
                        print(f"\n", "-=" * 15, end="-\n")
                        del money, exp
                        end = z = False


        # PAGAR
        if escolha == 4.5:
            z = alternativa(i)
            while z is None:
                data_atual = atual_data()
                print(f"Escolha a conta a ser creditada.")  
                pp = account_fc()
                reg_person, lis_br, name, pp_value = pp
                data, i_sec, sect, i_cla, classe, i_con, name = lis_br
                # -- Decide valor a ser desabonado --#
                try:
                    money = float(input(f"Quantos reais deseja somar?: "))
                    money = round(money, 2)
                    exp = float(input(f"Quantos EXP deseja somar?: "))
                    exp = round(exp, 1)
                except ValueError:
                    print(f"Valor numérico incorreto. Operacão cancelada.")
                    z = end = False
                    break
                # -- valida valor --#
                if (money + exp) == 0:
                    print(f"Você não pode somar 0$ e 0EXP.")
                    print(f"Operação cancelada.")
                    print(f"\n", "-=" * 15, end="-\n")
                    z = end = False
                    break
                else:
                    # -- confirmação --#
                    print(
                        f"A conta de {name}, então ficará com: {dic_reg[data][i_sec][sect][i_cla][classe][i_con] [name][0] + money}R$ e "
                        f"{dic_reg[data][i_sec][sect][i_cla][classe][i_con][name][1] + exp} EXP. confirma? ")
                    conf = confirm()
                    if conf is True:
                        # assert isinstance(data_reg, object)
                        dic_reg[data][i_sec][sect][i_cla][classe][i_con][name][0] += money
                        dic_reg[data][i_sec][sect][i_cla][classe][i_con][name][1] += exp
                        print(f"Registro ficará: {dic_reg}. Escolha opção 7 para salvar como novo registro.")
                        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                                          f"Adicionado {money}$ e {exp}EXP para {name}"])
                        del money, exp
                        z = end = True
                    # --- Deleta as var usadas ---#
                    else:
                        print(f"Operação cancelada.")
                        print(f"\n", "-=" * 15, end="-\n")
                        del money, exp
                        end = z = False


        #CRIAR NOVA CLASSE:
        if 46 == i or escolha == 4.6:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: CADASTRAR NOVA CLASSE)\n")
                data_atual = atual_data()
                print(f"~ Escolha seção cujo a nova classe ficará! ~")
                sc = secoes_func()
                if sc != None:
	                all_secoes, classes_por_secao, secao_value, secao_selected, data_reg, classes_list, secao_reg = sc
	                print( dic_reg[data_reg][secao_value][secao_selected], "####")
	                nome_novo = str(input("Nome da classe nova: ")).lower().strip()
	                if nome_novo == "":
	                    print(f"O nome da classe não pode estar em branco. Operação cancelada.")
	                    del nome_novo
	                    z = end = False
	                    break
	                else:
	                    print(f"Classe a ser cadastrada: {nome_novo}\nReino Pertencente: {secao_selected}. \nConfirma?")
	                    conf = confirm()
	                    if conf is True:
	                        print("Certo. Vá ao menu e digite 7 para atualizar.")
	                        nova_conta = {nome_novo: [  ]}
	                        classes_c2[0][secao_selected] = [nome_novo]
	                        print(classes_c2, "@@@@@")
	                        # Salva nova classe:
	                        dic_reg[data_reg][secao_value][secao_selected].append(nova_conta)
	                        print( dic_reg[data_reg][secao_value][secao_selected])
	                        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
	                                          f"Cadastrado nova classe ({nome_novo} em {secao_selected})."])
	                        del nome_novo
	                        z = end = True
	                    else:
	                        print(f"Operação cancelada.")
	                        del nome_novo
	                        z = end = True
	                        break
                elif sc == None:
                	print(f"Reino pertencente não pôde ser escolhida. Operação cancelada.")
                	z = end = False
                	break
        	
        	
        	
        #CRIAR NOVA SEÇÃO:
        if 47 == i or escolha == 4.7:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: CADASTRAR NOVA SEÇÃO)\n")
                data_atual = atual_data()
                if data_atual != None:
	                sectsee_fc()
	                nome_novo = str(input("\nNome da seção nova: ")).lower().strip()
	                if nome_novo == "":
	                    print(f"O nome da seção não pode estar em branco. Operação cancelada.")
	                    del nome_novo
	                    z = end = False
	                    break
	                else:
	                    print(f"Seção a ser cadastrada: {nome_novo}. \nConfirma?")
	                    conf = confirm()
	                    if conf is True:
	                        print("Certo. BOTE ALGUMA CLASSE NESTA SEÇÃO PARA EVITAR ERROS! Vá ao menu e digite 7 para atualizar.")
	                        nova_conta = {nome_novo: [  ]}
	                        # Salva nova secao:
	                        dic_reg[data_reg].append(nova_conta)
	                        classes_c2.append(nova_conta)
	                        print( dic_reg[data_reg])
	                        sectsee_fc()
	                        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
	                                          f"Cadastrado nova seção ({nome_novo})."])
	                        del nome_novo
	                        z = end = True
	                    else:
	                        print(f"Operação cancelada.")
	                        del nome_novo
	                        z = end = True
	                        break
                elif sc == None:
                	print(f"Reino pertencente não pôde ser escolhida. Operação cancelada.")
                	z = end = False
                	break
        	
        #REMOVER SEÇÃO:
        if 48 == i or escolha == 4.8:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: REMOVER SEÇÃO)\n")
                data_atual = atual_data()
                print(f"Escolha a seção a ser removida...")
                sec = secoes_func()
                if sec != None:
	                all_secoes, classes_por_secao, secao_value, secao_selected, data_reg, classes_list, secao_reg, persons_sec = sec
	                print(f"Você irá excluir a seção {secao_selected}, e juntamente, todas as classes e contas possiveis pertencentes a tal seção. Você confirma?")
	                conf = confirm()
	                if conf == True:
	                        # remove secao:
	                        print(all_persons, "@@@@")
	                        print(f"Contas da seção: {persons_sec}")
	                        for name in persons_sec[secao_selected]:
	                        	if name in all_persons:
	                        		print(f"Conta deletada: {name}")
	                        		del all_persons[str(name)]
	                        del dic_reg[data_reg][secao_value]
	                        del classes_c2[0][secao_selected]
	                        
	                        print(dic_reg[data_reg], "< Registro\n", classes_c2, "< Classes_c2.")
	                        sectsee_fc()
	                        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
	                                          f"Removida a seção ({secao_selected})."])
	                        z = end = True
	                elif conf == False:
	                	print(f"Operação cancelada.")
	                	z = end = False
	                	break
                elif sec == None:
                	print(f"Seção não pôde ser escolhida. Operação cancelada.")
                	z = end = False
                	break
        	
               	
        #REMOVER CLASSE:
        
        #DEFINIR NOVO LÍDER:
        	
        #DEFINIR NOVO REI:
        	
        #REMOVER LÍDER:
        	
        #REMOVER REI:
        	
        #DEFINIR LEI POR REINO:
        	
        # DEFINIR REGISTRO ANTIGO COMO ATUAL
        if escolha == 5:
            z = alternativa(i)
            while z is None:
                data_atual = atual_data()
                # –– CÓDIGO: ––#
                print(f"SELECIONADO: DEFINIR REGISTRO")
                data_atual = atual_data()
                if backups["contas"].__len__() <= 1:
                	print(f"Não há registros antigos salvos. Operação cancelada.")
                	z = end = True
                	break
                elif backups["contas"].__len__() >= 2:
                	print(f"Selecione a data do registro a ser restaurada...")
                	b = backups_fc("contas")
                	contas_new, es, es2, data_select = b
                	dic_reg = {data_select: contas_new}
                	print(f"O registro número {reg_selecionado} do backup de registros, foi selecionado como registro atual (dic_reg, contas), com sucesso. \n"
                	f"Aqui está o registro atual: {dic_reg}\n")
                # -- FLAG --#
                z = end = True
                del registro, reg_selecionado, data_selecionada
                historico.append([f" Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                                  "um registro antigo virou o registro atual."])


        # VER HISTÓRICO DE PEDIDOS
        if escolha == 6:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: HÍSTÓRICO DE PEDIDOS)\n")
                data_atual = atual_data()
                historic = hist_fc()
                logs = run(6)
                break


        # REGISTRAR BACKUP NOVO
        if escolha == 7:
            z = alternativa(i)
            while z is None:
                    print(f"\n(SELECIONADO: ATUALIZAR BACKUPS)\n")
	                # --- Código ---#
                    data_atual = atual_data()
                    len_contas = backups["contas"].__len__()
                    len_liders = backups["lideres"].__len__()
                    len_reis = backups["reinantes"].__len__()
                    len_avi = backups["avisos"].__len__()
                    len_mundival= backups["valor_mundial"].__len__()
                    len_backups = backups.__len__()
                    print(f"\nHá {len_backups} categorias de variáveis salvas em backups. Sendo:"
	                f"\ncontas: tendo {len_contas} datas salvas;"
	                f"\nlíderes: tendo {len_liders} pontos salvos."
	                f"\nreinantes: tendo {len_reis} pontos de revuperação guardados;"
	                f"\navisos: tendo {len_avi} datas de avisos guardados;"
	                f"\ne valor_mundial: {len_mundival}.")
	                # Salva o registro atual em var diferente, e salva o penúltimo registro do programa.
                    for data, contas in dic_reg.items():
	                    ultimo_registro = contas.copy()
                    ultimo_liders = lideres.copy()
	                
                    data_ultimo_registro = data
                    print(f"\nREGISTRO ANTIGO: {dic_reg}\nVAR: LIDERES: {lideres}\nVAR REINANTES: {reinantes}\nVAR AVISOS: {avisos}\nVAR VALOR_MUNDIAL: {valor_mundial}.")
                    print(f"\nALTERE AS VARIÁVEIS (Pressione enter sem digitar nada para deixar como está).")
                    # -- Salva registro novo no backup --#
                    backups["contas"]= {data_atual: ultimo_registro.copy()}
                    """backups["lideres"] = {data_atual:
                    }
                    backups["reinantes"] = {data_atual:
                    }
                    backups["avisos"] = {data_atual:
                    }
                    backups["valor_mundial"] = {data_atual:
                    }"""
                # Define registro atual:
                    del dic_reg
                    dic_reg = dict()
                    dic_reg[f"{data_atual}"] = ultimo_registro.copy()
                # -- salva o registro novo --#
                    print(f"\nNovo registro salvo com sucesso.\n",
                "aqui está o backup de registros atualizado: {}\n".format(iterar(backups, ', \n\n')))
                    
                # -- Mostra Backup de registros --
                    categories = {}
                    for category, dados in backups.items():
                    	for dates, values in dados.items():
                    		categories[category] = [dates]
                    		print(f"\n {category.upper()} >> datas salvas: {dates}.\n	 Conteúdo: {values}\n")
                # --- COMEMTARIO SOBRE REGISTRO NOVO ---#
                    desc = str(input(f"\nDescrição da atualização (adicionados, valores, remoção, etc): "))
                    avisos[0]['avisos de atualizacoes'][f'{data_atual}'] = f"{desc}"
                    print(f"\nO aviso do registro novo, foi: {avisos[0]['avisos de atualizacoes'][f'{data_atual}']}")
                # --- FLAG --- #
                    historico.append(
                    [f" Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}", "registro atualizado."])
                    z = end = True

        # DECLARAR AVISOS:
        if escolha == 8:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: DEFINIR AVISO GERAL)\n")
                # --- Código ---#
                data_atual = atual_data()
                caiu_em = "none"
                # -- Checa se há registros antigos --#
                if backup_registros[0].__len__() >= 2:
                    print(
                        f"\nHá registros antigos salvos. Você pode selecionar qual registro salvo deseja definir um aviso...\n")
                    # Seleciona qual registro
                    regist = registros()
                    reg_selecionado, data_selecionada, registro = regist[0], regist[1], regist[2]
                    caiu_em = 'antigo'
                    b_r = registro
                else:
                    print(f"\nVocê verá o registro atual.\n")
                    # Caso não tenha reg. antigo: b_r == registro atual
                    b_r = dic_reg
                    # Define a variavel data de b_r
                    for data, reg in b_r.items():
                        registro = reg
                    data_selecionada = data
                    caiu_em = 'novo'
                # Verifica se registro pode ser visto:
                print(f"Data_selecionada: {data_selecionada}")
                if caiu_em == 'novo' or caiu_em == 'antigo':
                    # --- Sctript de aviso: ---#
                    print(f"Os avisos podem ser vistos escolhendo a opc 1.")
                    # --- Digita aviso ---#
                    print("DIGITE SEU AVISO.\n"
                          "Observações:\n"
                          "1-Digite @ e enter para sinalizar o final do texto.\n"
                          "2- Os paragrafos (pulo de linha) podem ser afetados após a conversão.\n"
                          "3- Você pode digitar '¶' em seu texto aonde deseja deixar os paragrafos.\n"
                          "4- locais com 2 caracteres de espaço em branco,também\n"
                          " são convertidas em paragrafo (pull de linha)\n"
                          "\n Insira seu texto: \n"
                          ">>>   ")
                    line = ""
                    while True:
                        x = input()
                        line = line + " " + x
                        if "@" in x:
                            break
                    comment = repr(line).strip()[1: -2]
                    # --- Aloca aviso em área correta ---#
                    avisos[1]['avisos gerais'][f'{data_selecionada}'] = f"{comment}"
                    print(avisos)
                    # -- flag --#
                    print(f"Foi definido com sucesso, um aviso para o registro datado como: {data_selecionada}."
                          f" Seu comentário foi: {avisos[1]['avisos gerais'][f'{data_selecionada}']}")
                    print(f"Operação concluída. Digite 7 para validar.")
                    print(f"\n", "-=" * 15, end="-\n")
                    # -- Deleta as var usadas --#
                    del line, x, data, comment, caiu_em
                    z = end = True
                    regist = atual_data()
                    data_atual = regist[1]
                    historico.append(
                        [f"Concluído funcão {i}, para o registro {dic_reg}, as {data_selecionada}",
                         f"Definido um aviso."])
                # Caso não possa ser visto:
                elif caiu_em in "none":
                    print(f"\nErro. O registro a ser visto não pôde ser definido, tente novamente.\n")
                    del caiu_em, b_r
                    z = end = False
                # Caso retorne algo diferente de 'none, antigo ou novo':
                else:
                    print(f"Erro desconhecido. Programa finalizado.")
                    exit()

        # PROGRAMAR DESABONANÇA:
        if escolha == 9:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: Programar desconto de conta)\n")
                # --- Definições de Vars. ---#
                #--- Código ---#
                print(f"Selecione qual indivíduo irá ter desabonança automática: ")
                a = individuos()
                print(f"Quantos R$ serão retirados por parcela, da conta {a}?: ")
                money = float(input("> "))
                money = round(money, 2)
                print(f"Você deseja selecionar um dia no calendário[1], ou programar um intervalo de tempo?[2]")
                esc = str(input(f"> ")).upper().strip()[0]
                if esc == "1":
                	pass
                elif esc == "2":
                	pass
	                if conf == True:
	                	pass
	                else:
	                	print(f"Operação cancelada.")
	                	z = end = False
	                	break
	                
                else:
                	print(f"Valor incorreto. Por favor, digite 1 ou 2. Operação cancelada.")
                	z = end = False
                	break
				# -- flag --#
                print("Foi desabonado com sucesso a parcela {n} de {n}, da conta {tal}. Registro: {reg}")
                print(f"Operação concluída. Digite 7 para validar.")
                print(f"\n", "-=" * 15, end="-\n")
                # -- Deleta as var usadas --#
                del data_atual
                z = end = True
                regist = atual_data()
                data_atual = regist[1]
                historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                         f"Retirado n valor automaticamente da conta tal."])

if __name__ == "__main__":
    main()
