# BANCO 3!!!!
# Encoding: UTF-8
# Fazer um sistema bancádrio p RPG completo
# Possibilidade de compra de store.itens
# iguslmente salvar/mostrar store.itens e patrimonio dos guri
# Uma I.A (Assistente virtual) irá ajudar o guri tb.

versao = '3.0.0'
__author__ = "Software m3yk0"
__copyright__ = "Copyright (C) 2023 N.W.M_OFC"
__license__ = "Public Domain"
__version__ = "3.0.0"


def main():
    from entrance.Store_fold import store
    #global store.contas, backups, data_reg, historico, store.reinantes, valor_mundial, valor_guardado, lideres, dic_reg, avisos, i, start, conclusoes, log, leis, Rank, stderr, ItemNotFoundInstore.itensError, FindItem
    storevar = store.contas, store.contratos, store.propriedades, store.classes_c2, store.backups, store.Rank, store.data_reg, store.dic_reg, \
        store.avisos, store.reinantes, store.leis, store.lideres
    print("\nBem-vindo ao programa Meeh World: Bank!\n")
    # Imports Bib. padroes:
    import time
    from sys import stderr
    # Imports Bib. terceiros:
    # Imports Bib. Local:

    from controles import PIB_real, i, log, start, vms, ems, all_class, moneypersec, totcontpersec, bolsa, bolsapersec, \
        valor_guardado, tesouro, feepersec, ipcapersec, \
        ETF, PIB_Per_Capita_persec, historico

    from Funcs import run, atual_data, alternativa, \
        confirm, prevent, money_func, iterar, recort, backups_fc, values_fc, \
        regselect_fc, magnatas_fc, secoes_func, classes_func, select_account_fc, hist_fc, sectsee_fc, give_fc

    log.append("módulos importados...")

    """arqbank_json = open("arqbank.json", 'a')
    arqbank_json.writelines(f"{backups=}")
    arq_read = open("arqbank.json", 'r')
    arq_read = arq_read.readlines()
    print("\n",arq_read, "\n")"""

    log.append("Carregando menu...")
    run()
    # Mostra menu:
    operacoes = ["None"]
    while True:
        print("\n~~~~ World Meeh: Bank! ~~~\n")
        print(f"\n ~~~ Program Version: {versao} ~~~\n")
        print("\n"
              "    Qual área do programa deseja entrar?:\n"
              "    0- Sair"
              "\n    1- Visualizar registro bancário\n    2- Magnatas\n    3- VMS (Checar taxas, valores, tributos e ajustes) \n    4- Processar card bancário\n"
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
              "    10- Rank de pontos, feitos em ON e store.itens"
              "    ...- CDI, PIB_real, Juros, RH, parcelas...")
        try:
            print(F"   > O ultimo comando digitado foi: {operacoes[-1]}")
            try:
                print(f"    Descrição do ocorrido: {historico[-1][1]}")
            except IndexError:
                print(F"    Histórico ainda inacessivel.")
            escolha = float(input("    > Escolha: "))
            operacoes.append(escolha)
            i = escolha
            log.append(f"Foi digitado no menu, opção {i}")
        except ValueError:
            print(f"Erro. Use um valor numérico.")
            time.sleep(1)
            continue
        finally:
            print('\n')

        # REALIZA BLOQUEIO DE OPERACOES:
        if start is True:
            # pega data e indice de dic_reg
            data = str()
            for data, index in dic_reg.items():
                data = data
            # Caso dic_reg (registro atual) esteja vazio:
            z = True
            if dic_reg[data].__len__() < 1:
                print(f"REGISTRO SEM REINOS! Operações bloqueadas:")
                # Bloqueio de operações caso dic_reg vazio:
                bloq = [2, 4.1, 4.2, 4.3, 4.4, 4.5, 3.6, 4.8, 4.9, 4.10, 4.11, 4.12]
                print(f"{iterar(bloq)}\n ESCOLHA OPÇÃO DE ADICIONAR NOVA SEÇÃO PARA DESBLOQUEAR (4.7)!")
                z = False
            # Caso registro sem classes:
            if all_class.__len__() < 1:
                print(f"REGISTRO SEM CLASSES!\n Operações Bloqueadas:")
                bloq = [2, 4.1, 4.2, 4.3, 4.4, 4.5, 4.8, 4.9, 4.10, 4.11, 4.12]
                print(f"{iterar(bloq)}\n ESCOLHA OPÇÃO DE ADICIONAR NOVA SEÇÃO PARA DESBLOQUEAR! (4.9)")
                z = False
            if all_persons.__len__() < 1:
                print(f"REGISTRO SEM CONTAS!\n Operações Bloqueadas:")
                bloq = [2, 4.2, 4.3, 4.4, 4.5, 4.10, 4.11, 4.12]
                print(f"{iterar(bloq)}\n ESCOLHA OPÇÃO DE ADICIONAR NOVA SEÇÃO PARA DESBLOQUEAR! (4.1)")
                z = False
            if z == True:
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
                desc = ''
                print(f"\n(SELECIONADO: VISUALIZAR ALGUM REGISTRO (e seus avisos))\n")
                global regist, registro, var_selecionada, data_select, b_r
                data_atual = atual_data()
                # --- Código ---#
                # -- Checa se há registros antigos --#
                reg_select = regselect_fc()
                if reg_select is None:
                    print(f"Houve um erro com a func. regselect_fc(). Registro não pode ser mostrado.")
                    end = False
                    desc = "regselect_fc() Retornou NONE"
                elif reg_select is not None:
                    caiu_em, b_r, data_select = reg_select
                    b_r = b_r[data_select]
                    # --- Mostra o registro ---#
                    values_a = values_fc()
                    values = values_a
                    if values is not None:
                        vms, ems, meta_selic, pvms, all_persons, tot_pvms, tot_fee, all_sections, all_class, moneypersec, \
                        feepersec, totcontpersec, bolsa, PIB_Per_Capita_persec, PIB_Per_Capita, IPCA, ipcapersec, bolsapersec, \
                        tesouro, tesouropersec, vpms, PIB_Nominal, PIB_Nominal_persec, ETF, ETF_persec, accontsdict = values
                        TBF = meta_selic - vms
                        mag = magnatas_fc()
                        if mag is not None:
                            lismag = mag[ 0 ]
                            cont = 0
                            # Verifica se DIC_REG está certo:
                            datas = str()
                            for datas, reg in dic_reg.items():
                                print(f"Datas de dic_reg: {datas}")
                                datas = datas
                            '''try:
								dic_reg[ data_select ]
							except KeyError:
								print(f"Houve um problema KEYERROR.\nA váriavel {dic_reg = }\n Não pode acessar a key {data_select = }")
								time.sleep(3)
								data_select = datas
								continue'''
                            print(f"\n",
                                  f".    ╔╦════•  •✠• ❀•✠ • •═══╦╗\n",
                                  f"       *Registro Bancário Mundial*\n",
                                  f"    ╚╩════• •✠• ❀ •✠ • •═══╩╝ \n\n",
                                  f"*Staffs (novos e antigos):*\n	Meyko Ivory,\n	Meeh Inu,\n	Susumo Tsuki,\n 	Naomi Uzuki,\n	Yu Zuky,\n	Chaos Akaguma,\n 	Naruko Namikaze,\n 	Yang Uchiha,\n	Rimawari Hyuuga,\n	Isa Akaguma")
                            for c, item in enumerate(b_r):
                                for secao, classes_lis in item.items():
                                    if c == 0:
                                        print( f"""\n	━━━━━━━━━  ✠  ━━━━━━━━━\n""",
                                            f"""*Contas em conjunto/NPCs:*\n""",
                                            f"""*PVMS das contas em conjunto:* {money_func(moneypersec[ secao ])}$ \n""",
                                            f"""*Taxa Selic das contas em conjunto:*  {money_func(moneypersec[ secao ] - PIB_Per_Capita_persec[ secao ])}\n""",
                                            F"""*PIB_Per_Capita:* {money_func(PIB_real / totcontpersec[ secao ])}\n""",
                                            F"""*IPCA:* {money_func(ipcapersec[ secao ])}% _({'some +IPCA% em suas compras (inflação)' if feepersec[ secao ] < 0 else 'diminua -IPCA% em suas compras (deflação)'})_\n""",
                                            F"""*BOLSA da seção:* {money_func(bolsapersec[ secao ])}\n""", sep='– ')
                                        for num, classes_dict in enumerate(classes_lis):
                                            for classe, contas_lis in classes_dict.items():
                                                print(f"""	*{classe.upper()}:*""")
                                                for n, account_dict in enumerate(contas_lis):
                                                    for name, valores in account_dict.items():
                                                        print(f"\n - {name.title()}: ", end="")
                                                        for index, val in enumerate(valores):
                                                            print(f" {money_func(val)}{'$ / ' if (index % 2) == 0 else 'EXP'}",end="")
                                                if n == contas_lis.__len__() - 1:
                                                    print(f"""\n		━━━━━━━━━  ✠  ━━━━━━━━━\n""")
                                    else:
                                        if dic_reg[ data_select ][ c ][secao ].__len__() >= 1:  # Somente caso Seção tenha classes, printa ela.
                                            print(f"""*●-  -=- {secao.upper()} -=-    -●*\n""",
                                                  f""" ፧⠂ *PVMS do Reino:* {money_func(moneypersec[ secao ])}$\n""",
                                                  """ ፧⠂ *Taxa Selic do Reino:* {}\n""".format(
                                                      money_func(
                                                          moneypersec[ secao ] - PIB_Per_Capita_persec[ secao ])),
                                                  F""" ፧⠂ *IPCA:* {money_func(ipcapersec[ secao ])}% _({'Taxa Selic negativa: some +IPCA% em suas compras (inflação)' if feepersec[ secao ] < 0 else 'Taxa selic positiva: diminua -IPCA% em suas compras (deflação)'})_\n""",
                                                  #""" ፧⠂ *PIB_Per_Capita:* {}\n""".format(f"{money_func(PIB_real / totcontpersec[ secao ])}" if totcontpersec[secao ] > 0 else f"{money_func(00)}"),
                                                  """ ፧⠂ *PIB Nominal Per Capita:* {}\n""".format(f"{money_func(PIB_Nominal_persec[ secao ])}"),
                                                  F""" ፧⠂ *BOLSA da seção:* {money_func(bolsapersec[ secao ])} \n""",
                                                  f""" ፧⠂ *Reinante:* {prevent(store.reinantes, secao)}\n""",
                                                  f""" ፧⠂ *Leis:* {'Barradas' if prevent(store.reinantes, secao) == 'None' else 'Ativas'}\n""",
                                                  f""" ፧⠂ *Classes:* {iterar(prevent(classes_c2, secao)) if prevent(classes_c2, secao) != 'None' else 'None'}\n""",
                                                  F""" ፧⠂ *Total de contas:* {totcontpersec[ secao ]}\n""",
                                                  f"""	━━━━━━━━━━  ✠  ━━━━━━━━━━\n""")
                                            for num, classes_dict in enumerate(classes_lis):
                                                for classe, contas_lis in classes_dict.items():
                                                    if dic_reg[ data_select ][ c ][ secao ][ num ][ classe ].__len__() >= 1:  # Somente caso classe tenha contas, printa ela.
                                                        print(f"""*Classe: {classe.title()}*\n""",
                                                              f"""*Líder:* {prevent(lideres, classe).title()}""")
                                                        for n, account_dict in enumerate(contas_lis):
                                                            for name, valores in account_dict.items():
                                                                cont += 1
                                                                print(f"\n - {name.title()}: ", end="")
                                                                for index, val in enumerate(valores):
                                                                    print(f" {money_func(val)}{'$ / ' if (index % 2) == 0 else 'EXP'}",
                                                                        end="")
                                                        if n == contas_lis.__len__() - 1:
                                                            print(f"""\n		━━━━━━━━━  ✠  ━━━━━━━━━\n""")
                                                    else:
                                                        print("")
                            print(
                                f"\n– *VMS🌐:* {money_func(vms)}",
                                f"– *META SELIC💰:* {money_func(meta_selic)}",
                                f"– *EMS✨:* {money_func(ems)}",
                                f"– *TBF🪙:*' {money_func(TBF)}",
                                F"– *PIB_real💎:* {money_func(PIB_real)}",
                                f"– *PIB Per Capita:* *{money_func(PIB_Per_Capita)}*\n"
                                f"– *PIB Nominal:* *{money_func(PIB_Nominal)}*\n"
                                F"– *BOLSA DE VALORES📊:* {money_func(bolsa)}\n"
                                F"— *PIB_Per_Capita Mundial⚖️:* {money_func(PIB_real / all_persons.__len__())}\n"
                                F"– *ETF:* *{money_func(ETF)}*"
                                f"\n\n   ~-=-|~ *MAGNATAS*: ~|-=-~",
                                "– {}\n".format(iterar(recort(lismag, 4), ', \n- ')),
                                f"\n*VERIFICAÇÕES:*",
                                f"_¬   Soma de todos PVMS: {money_func(tot_pvms)}_ _{'é igual ao VMS.' if tot_pvms == vms else f'ATENÇÃO: Não é igual ao VMS. Isso significa que este registro não está valido! Diferença: {vms - tot_pvms}'}_",
                                f"¬   _Soma de todas as taxas: {money_func(tot_fee, 2)}_ ",
                                f"¬   _VMS + META SELIC SEMPRE ser == {money_func(valor_guardado)}. Total: {money_func(vms + meta_selic)}._ {'' if (vms + meta_selic) == valor_guardado else f'_ATENÇÃO: O resultado não é o valor guardado.. Este registro está dado como inválido._'}",
                                f"¬   _Diferença entre VMS e META SELIC: {money_func(meta_selic - vms)} (TBF)_",
                                F"¬  _Total de IPCA: {money_func(IPCA)}_"
                                f"\n\n        ~-=-|~ *NOTAS:* ~|-=-~",
                                f"– PVMS = Parte do Valor Mundial Situado: quanto uma certa seção representa do VMS;",
                              F"- EMS = Total de EXP;",
                              F"- VMS = Total de grana em mãos;",
                              F"- META SELIC = Dinheiro guardado no banco;",
                              F"- TAXA SELIC = cálculo da diferença entre o que seu reino tem VPMS - o que seu reino deveria ter PIB_Per_Capita",
                              F"- PIB_real = soma dos preços de todos os store.itens (original/Bruto); ",
                              F"- IPCA = Medidor de inflação e deflação de cada reino. Valor positivo = muito dinheiro circulação (deflação), valor negativo = pouco dinheiro em mãos e store.itens caros (inflação) Pode ser definida também como a porcentagem da taxa selic;",
                              F"- TBF= Tributo básico financeiro: Variação do valor entre o VMS e M.Selic; ",
                              F"- Bolsa de Valores: Soma de todas as dívidas;",
                              F"- PIB_Per_Capita = (PIB_real ÷ contas) Calcula PIB_real por quantia de contas de cada seção (é dada como a meta de tributo que cada seção deveria alcançar);",
                              F"- PIB_Nominal = PIB_Per_capita com a diferença da inflação",
                              F"– ETF = Echange Trade Fund - Fundo de Índice comercial: Diferença entre PIB_Real (sem inflação) Para o PIB nominal (PIB com inflação)\n",
                                f"– Total de seções: {b_r.__len__()}",
                                f"– Total de classes ativas: {all_class.__len__()}",
                                f"– Total de contas: {all_persons.__len__()}\n\n", sep='\n')
                            print(f"\nAVISOS:\n Para o registro: {data_select}:\n aviso de atualização: {avisos[ 0 ][ 'avisos de atualizacoes' ][ f'{data_select}' ]}")
                            # MOSTRA VARIAVEL "CONTAS" ATUAL:
                            print(F"\n\n\n CONTAS: \n\n\n store.contas = [")
                            c_sec_ = b_r.__len__()
                            for dic_sec_ in b_r:
                                for reino_, lis_clas_ in dic_sec_.items():
                                    print("    {", f"'{reino_}': [")
                                    c_sec_ -= 1
                                    c_clas_ = lis_clas_.__len__()
                                    for dic_clas_ in lis_clas_:
                                        for clas_, lis_users_ in dic_clas_.items():
                                            print('	{', F" '{clas_}': [")
                                            for c_user_, dic_user_ in enumerate(lis_users_):
                                                print(F"        ", dic_user_, end="")
                                                if c_user_ < lis_users_.__len__() - 1:
                                                    print(",")
                                                else:
                                                    print("", end="")
                                            c_clas_ -= 1
                                            print("\n	]}", end="")
                                            if c_clas_ >= 1:
                                                print(",")
                                            elif c_clas_ <= 0:
                                                print("")
                                    if c_sec_ > 0:
                                        print("    ]},")
                                    elif c_sec_ <= 0:
                                        print("    ]}\n]\n")
                            # MOSTRA VÁRIAVEL "classes_c2" ATUAL:
                            print(f"\nCLASSES_C2:\n{classes_c2=}")
                            # MOSTRA VÁRIAVEL "lideres"
                            print(f"\nLIDERES:\n{lideres=}")
                            # MOSTRA VÁRIAVEL "leis":
                            print(f"\nLEIS: \n {leis=}")
                            # MOSTRA VÁRIAVEL "store.reinantes" ATUAL:
                            print(f"\nstore.reinantes: \n { store.reinantes=}")
                            try:
                                print(f"Aviso geral: {avisos[ 1 ][ 'avisos gerais' ][ f'{data_select}' ]}")
                            except KeyError:
                                print(f'Sem aviso geral para o registro selecionado.')
                                print(f"Aviso geral: {avisos[ 1 ][ 'avisos gerais' ][ f'11/07/2023-02:09:01' ]}")
                            desc = "desc: O registro foi visto."
                        else:
                            print(f"Houve um erro com a func. magnatas(). Registro não pode ser mostrado.")
                            desc = 'magnatas_fc() Retornou NONE'
                    else:
                        print(f"Houve um erro com a func. values_fc(). Registro não pode ser mostrado.")
                        desc = 'values_fc() Retornou NONE'
                        end = False
                # -- flag --#
                end = z = True
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([f"Concluído funcão {escolha}, para o registro {b_r}, as {data_atual}",
                                  desc,
                                  f"Finalização: {end}: {finalizacao}"])


        # VER MAGNATA:
        if escolha == 2:
            z = alternativa(i)
            while z is None:
                desc = ''
                data_atual = atual_data()
                print(f"\n(SELECIONADO: VER RANK DE MAGNATAS)\n")
                mag = magnatas_fc()
                sort_money, sort_exp = mag[0], mag[1]
                if mag is None:
                    print(f"Função retornou erro. Operação cancelada. ")
                    desc = 'magnatas_fc() Retornou NONE'
                    end = False
                else:
                    cont = 0
                    # --- Mostra os resultados ---#
                    # MAGNATA MONEY
                    print(f"""\nlista de riqueza monetária (maior para menor): \n""")
                    for name, grana in sort_money.items():
                        name = name.title()
                        grana = round(grana, 2)
                        if cont == 0:
                            print(f"{cont + 1}: {name} (MAGNATA) —> grana: {grana}$")
                        else:
                            print(f"{cont + 1}: {name} —> grana: {grana}$")
                        cont += 1
                    # MAGNATA EXP
                    print(f"""\nlista de riqueza EXP (maior para menor):\n""")
                    cont = 0
                    for name, exp in sort_exp.items():
                        name = name.title()
                        grana = round(grana, 2)
                        if cont == 0:
                            print(f"{cont + 1}: {name} (MAGNATA) —> EXP: {exp}$")
                        else:
                            print(f"{cont + 1}: {name} —> EXP: {exp}$")
                        cont += 1
                    desc = "desc: Foi checado os magnatas."
                    end = True
                # -- flag --#
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha}, para o registro {b_r}, as {data_atual}",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }"])
                break


        # ===> CHECAR VMS:
        if escolha == 3:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: CHECAR VMS)\n")
                data_atual = atual_data()
                # --- Código ---#
                # --- criação de vars ---
                # -- Checa se há registros antigos --#
                values_a = values_fc()
                values = values_a
                if values is not None:
                    vms, ems, meta_selic, pvms, all_persons, tot_pvms, tot_fee, all_sections, all_class, moneypersec, \
                    feepersec, totcontpersec, bolsa, PIB_Per_Capita_persec, PIB_Per_Capita, IPCA, ipcapersec, bolsapersec, \
                    tesouro, tesouropersec, vpms, PIB_Nominal, PIB_Nominal_persec, ETF, ETF_persec, accontsdict = values
                    TBF = meta_selic - vms
                elif values is None:
                    print(f"erro na operação 'values_fc'. Operação cancelada.")
                    desc = 'values_fc() Retornou NONE'
                    end = None
                if backups["contas"].__len__() >= 2:
                    print(f"\nHá registros antigos salvos. Você pode selecionar qual registro salvo deseja ver...\n")
                    # Seleciona qual registro quer ver
                    regist = registros()
                    if regist is not None:
                        reg_selecionado, data_selecionada, registro = regist[0], regist[1], regist[2]
                        caiu_em = 'antigo'
                        b_r = registro
                    elif regist is None:
                        print(f"Não foi possível selecionar o registro. Operação cancelada.")
                        desc = 'registros() Retornou NONE'
                        end = False
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
                    print(f"\n. {'*CHECAGEM DE VALORES*':^52}.\n")
                    print(f""" 
                        {'NOTAS:':^52}
                            
                        - TBF == Tributo Básico Financeiro: resume a diferença entre VMS e o Meta Selic
                                        (Cálculo: {vms=} *-* {tesouro=} *=* TBF{vms - tesouro})
                                        
                        - IPCA == Índice de preços ao consumidor amplo: indica de forma direta a Deflação e inflação na variação dos preços de store.itens e recebimentos (cada reino tem seu próprio IPCA). É basicamente o Taxa Selic em porcentagem de 100.000 Quando IPCA 
                                        (Cálculo IPCA Mundial: ({vms=} *-* {ETF=}) *÷* 100.000 *=* IPCA mundial {(vms - ETF) / 100000}
                                        Cálculo IPCA de cada seção: PVMS1 - ETF1 = IPCA da seção 1)
                                        
                        - VMS == Valor Mundial Situado _( ~shinobi~ )_ : Indica qual é a soma total do saldo de todas as contas registradas não negativadas. Ele aumenta quando as contas estão ricas, e abaixa quando pobres. Ele não pode ser negativado igualmente ao PVMS, pois significaria uma sociedade com dívidas além do viável retido no banco (tesouro). 
                                        (Cálculo: conta1 *+* conta2 *+* ...  *=* {vms})
                                        
                        - EMS == EXP (Experience) Mundial Situado: indica qual é a soma total de EXP de todas as contas registradas sem EXP negativado. 
                                        (Cálculo: exp_conta1 *+* exp_conta2 ... *=* {ems})
                                        
                        - TESOURO == Indica qual é o valor monetário total que está reservado no Banco, que pode ser usado. O Tesouro não deve ser negativo, pois, isso significaria injeção de dinheiro. Ele é fundado através do PIB_real, e diminui quando uma conta recebe dinheiro, e aumenta quando alguém perde dinheiro (devolve ao banco). 
                                        (Cálculo: {PIB_real=} *-* {vms=} *=* Tesouro {tesouro}) 
                                        
                        - PIB_real == Produto Interno Bruto: Situa qual é o preço final de todos os bens oferecidos (iterados no cálculo: /store.itens). 
                                            (Calculo: valor_item1 *+* valor_item2 ... *=* PIB_real {PIB_real} )
                                        
                        - PIB_Per_Capita: Excange Trade Fund - Fundo de Índice: É usado como uma Meta (fator de pretensão) financeira, que se resume ao PVMS que cada reino deveria ter para a conta bancária de todos os índios tenham a mesma capacidade de riqueza. Ele é medido com o PIB_real e é dividido tal valor dentre o total de contas cadastradas no registro. 
                                        (Cálculo PIB_Per_Capita mundial: {PIB_real=} *÷* tot.Contas_registradas *=* PIB_Per_Capita {PIB_real / all_persons.__len__()} 
                                        Cálculo PIB_Per_Capita por seção: {PIB_real=} *÷* tot.Contas_seção1 *=* PIB_Per_Capita da seção1)
                                    
                        - BOLSA DE VALORES == Índice que situa qual é a dívida total das contas registradas. 
                                        (Cálculo Bolsa Mundial: saldo_conta_negativada1 *-* saldo_conta_negativada2 ...  *=* Bolsa de valores {bolsa})
                                        
                        - TAXA SELIC == Taxa indicativa de quanto, em valor bruto, é a diferença entre o VMS (e PVMS de cada seção) entre o que cada seção têm de saldo, - o que deveria ter de saldo (PIB_Per_Capita) 
                                        (Calculo Taxa Selic Mundial: {vms=} *-* {ETF} *=* {money_func(vms - ETF)} )
                                    
                        {'TRIBUTOS:':^52}
                                        
                                    ¬ *TBF Mundial:* {money_func(TBF)} 
                                    ¬ *IPCA Mundial:* {money_func(IPCA)} 
                                    ¬ *VMS:* {money_func(vms)} 
                                    ¬ *EMS:* {money_func(ems)} 
                                    ¬ *META SELIC:* {money_func(tesouro)} 
                                    ¬ *PIB_real:* {money_func(PIB_real)}
                                    ¬ *PIB_Per_Capita:* {money_func(ETF)} 
                                    ¬ *BOLSA DE VALORES mundial:* {money_func(bolsa)}\n
                                            """)
                    for data, reg in b_r.items():
                        for sec_dic in reg:
                            for sec, lis_cla in sec_dic.items():
                                print(f"\n*°{sec.upper():~^28}°*\n"
                                f"-	*contas da seção:* {totcontpersec[sec ]}\n",
                                F"-	*PVMS da seção:* {money_func(moneypersec[sec])}\n"
                                f"-	*Taxa Selic da seção:* {money_func(feepersec[sec])}\n"
                                F"-	*IPCA da seção:* {money_func(ipcapersec[sec])}%\n"
                                F"-	*PIB_Per_Capita da seção:* {money_func(PIB_Per_Capita_persec[sec])}\n"
                                F"-	*TAXA DE TRANSFERÊNCIA:* Valor da movimentação ÷ 100\n"
                                F"-	*ITENS:* {money_func(ipcapersec[sec])}% {'mais caros' if ipcapersec[sec] < 0 else 'mais baratos'}\n"
                                f"-	*RECEBIMENTOS:* {money_func(ipcapersec[sec])}% {'menores' if ipcapersec[sec] < 0 else 'maiores'}\n"
                                F"-	*BOLSA de valores da seção:* {money_func(bolsapersec[sec])}\n")
                                for cla_dic in lis_cla:
                                    for classe, cont_lis in cla_dic.items():
                                        for cont_dic in cont_lis:
                                            for name, val in cont_dic.items():
                                                pass
                    desc = "desc: valores checados."
                    end = True
                    """# --- Realiza operação de analise da função ---#
                    # Calcula a inflação
                    # --- Deleta as var usadas ---
                    # Caso não possa ser visto:"""
                elif caiu_em in "none":
                    print(f"\nErro. O registro a ser visto não pôde ser definido, tente novamente.\n")
                    end = False
                    desc = 'Houve um erro na var "caiu_em".'
                # -- flag --#
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha}, para o registro {b_r}, as {data_atual}",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" ])
                del caiu_em, b_r
                break


        # CADASTRAR NOVO INDIVIDUO:
        if escolha == 4.1:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: CADASTRAR NOVO INDIVÍDUO)\n")
                data_atual = atual_data()
                print(f"~ Escolha seção e classe onde a nova conta ficará! ~")
                sc = classes_func()
                hi =""
                passe = True
                if sc is not None:
                    classe_select, classe_value, secao_selected, secao_value, contas_da_classe, data_reg, reg_classe = sc
                    print( dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select])
                    nome_novo = input(str(f" Nome do indivíduo (não precisa escrever classe): ")).title().strip() + f" {classe_select.title().strip()}"
                    print(f"Agora cite o saldo de {nome_novo}...")
                    give = give_fc("all")
                    if give is not None:
                        din, exp = give
                    else:
                        print(f"Não foi possível resgatar os valores pela func. Give_fc(). Operação cancelada.")
                        passe = False
                    if nome_novo == "":
                        print(f"O nome não pode estar em branco. Operação cancelada.")
                        passe = False
                    elif nome_novo in all_persons:
                        print(f"ATENÇÃO: O nome {nome_novo}, já está registrado no registro bancário. Operação cancelada.")
                        passe = False
                        """#DEFINE O VALOR GANHO PELO REI E LíDER
                        if None is not prevent(store.reinantes, secao_selected) != str(None):
                         print(f"O Reinante de {nome_novo} irá receber pelo indivíduo?") 
                         conf_rei = confirm() 
                         if conf_rei is True:
                            nome_rei = store.reinantes[secao_selected]
                            #pega classe do rei:
                            c_cla = 0
                            rei_value = 0
                            for data, lis_sects in dic_reg.items():
                                for dic_sects in lis_sects:
                                    for sec, lis_cla in dic_sects.items():
                                        for dic_cla in lis_cla:
                                            c_cla += 1
                                            for cla, lis_conts in dic_cla.items():
                                                for name_dic in lis_conts:
                                                    for nomes, saldo in name_dic.items():
                                                        if (str(nomes[1:-1]).lower().strip() == str(nome_rei).lower().strip()[1:-1]) == True :
                                                            cla_name_rei = cla
                                                            saldo_rei = saldo
                                                            cla_lis_rei = c_cla + 1
                                                            rei_value += 1
                                                            nome_rei = nomes
                                                            print(cla_name_rei, cla_lis_rei, rei_value, "@@@@")
                                                            break
                                                        else:
                                                            rei_value += 1
                                                            
                                                        
                            din_rei = round(float(input (f"Quantos $ {nome_rei} irá receber?: ")), 2)
                            if din_rei > tesouro:
                                print(f" ATENÇÃO: O saldo ultrapassa o valor de {tesouro} guardado no banco. Operação cancelada.")
                                passe = false
                            else: 
                                print(f"Rei de {secao_selected}, {nome_rei} recebeu {din_rei} por entrar novo indivíduo em seu reino.")
                            print( dic_reg[data_select][secao_value][secao_selected][cla_lis_rei]) 
                                hi = f"Rei {nome_rei} recebeu {din_rei}"
                                passe = True
                         elif conf_rei is False or conf_rei is None:
                            passe = True"""
                    if passe is False:
                        end = False
                        desc = 'Houve um erro durante o processo.'
                    else:
                        print(
                            f"Conta a ser registrada:\n nome: {nome_novo}\nSaldo: {din}$ / {exp}EXP. Na seção: {secao_selected} e classe {classe_select}. \nConfirma?")
                        conf = confirm()
                        if conf is True:
                            print("Certo. Vá ao menu e digite 7 para atualizar.")
                            nova_conta = {nome_novo: [din, exp]}
                            #---- Salva nova conta ----#
                            all_persons.append(nome_novo)
                            dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select].append(nova_conta)
                            desc = f"desc: Cadastrado novo indivíduo ({nome_novo} com saldo de {din}$/{exp}EXP)."
                            end = True
                        else:
                            print(f"Operação cancelada.")
                            desc = 'Confirmação da operacão foi negada.'
                            end = None
                elif sc is None:
                    print(f"Reino e Classe pertencente não pôde ser escolhida. Operação cancelada.")
                    desc = 'classes_func() Retornous NONE'
                    end = False
                # -- flag --#
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" + hi])
                #del din, exp, passe, sc, conf, hi
                break

        # EXCLUIR CONTA:
        if escolha == 4.2:
            print(f"~ Excluir Conta ~")
            z = alternativa(i)
            if z is None:
                desc = ''
                print(f"\n(SELECIONADO: EXCLUIR INDIVÍDUO)\n")
                # try:
                data_atual = atual_data()
                pp = select_account_fc()
                if pp is None:
                    print(F" Não foi possível selecionar o indivíduo. Operação cancelada.")
                    end = False
                    desc = 'account_fc() retornou NONE'
                else:
                    reg_person, lis_br, name, pp_value = pp[0], pp[1], pp[2], pp[3]
                    date, i_sec, sect, i_cla, classe, i_con, name = lis_br[0], lis_br[1], lis_br[2], lis_br[3], lis_br[4], \
                    lis_br[5], lis_br[6]
                    id = all_persons.index(name)
                # -- Confirma conta selecionada:
                print(f"Deseja excluir a conta: {dic_reg[date][i_sec][sect][i_cla][classe][i_con]} ?")
                confirm_cont = confirm()
                if confirm_cont is True:
                    del dic_reg[date][i_sec][sect][i_cla][classe][i_con]
                    del all_persons[id]
                    print(f"Registro: {iterar(dic_reg)}")
                    print(f"Certo, para declarar opção como definitiva, vá em opção 7.")
                    desc = f"Foi excluído a conta {name}"
                    end = True
                else:
                    desc = 'Confirmação da operacão foi negada.'
                    print(f"Operação cancelada.")
                    end = False
                # -- flag --#
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }"])
                # --- Deleta as var usadas ---#
                del name, date, i_sec, i_cla, classe, i_con, pp, reg_person, lis_br, pp_value
                continue


        # TRANSF. ENTRE CONTAS
        if escolha == 4.3:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: TRANSFERÊNCIA BANCÁRIA)\n")
                data_atual = atual_data()
                # -- seleciona individuos --#
                #    global indiv, di, nome_guri, data_reg
                print(f"Escolha a conta que realizará o depósito...")
                time.sleep(1.5)
                pp1 = select_account_fc()
                if pp1 is None:
                    print(F" Não foi possível selecionar o indivíduo. Operação cancelada.")
                    z = end = False
                    del pp1
                else:
                    reg_person1, lis_br1, nome1, pp_value1 = pp1
                    date1, i_sec1, sect1, i_cla1, classe1, i_con1, name1 = lis_br1
                    print(f"{name1.title()} irá transferir dinheiro para... ESCOLHA A CONTA CREDITADA:")
                    time.sleep(1.5)
                    pp2 = select_account_fc()
                    if pp2 is None:
                        print(F" Não foi possível selecionar o indivíduo. Operação cancelada.")
                        z = end = False
                        del pp2, reg_person1, lis_br1, nome1, pp_value1, date1, i_sec1, sect1, i_cla1, classe1, i_con1, name1
                    elif pp2 is not None:
                        reg_person2, lis_br2, nome2, pp_value2 = pp2
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
                            del pp2, reg_person1, lis_br1, nome1, pp_value1, date1, i_sec1, sect1, i_cla1, classe1, i_con1, name1, reg_person2, lis_br2, nome2, pp_value2, date2, i_sec2, sect2, i_cla2, classe2, i_con2, name2
                            continue
                        elif money1 <= 0:
                            print(f"Usuário a transferir dinheiro, não pode estar com a conta negativada nem zerada.")
                            print(f"Operação cancelada.")
                            print(f"\n", "-=" * 15, end="-\n")
                            z = end = False
                            del pp2, reg_person1, lis_br1, nome1, pp_value1, date1, i_sec1, sect1, i_cla1, classe1, i_con1, name1, reg_person2, lis_br2, nome2, pp_value2, date2, i_sec2, sect2, i_cla2, classe2, i_con2, name2
                        else:
                            # -- Decide valor a ser desabonado --#
                            try:
                                movido = round(float(input(f"Quantos reais deseja mover? {nome1} tem {money1}R$ disponíveis: ")), 2)
                                print(f" < {movido} > ")
                            except ValueError:
                                print(f"Valores inválidos. Operação cancelada.")
                                z = end = False
                            finally:
                                desc = 'Sem movimentação'
                            # -- Valida valor --#
                            if movido > money1:
                                print(f"O dinheiro movido excede o dinheiro disponível do saldo do credor. Operação cancelada.")
                                end = False
                                del pp2, reg_person1, lis_br1, nome1, pp_value1, date1, i_sec1, sect1, i_cla1, classe1, i_con1, name1, reg_person2, lis_br2, nome2, pp_value2, date2, i_sec2, sect2, i_cla2, classe2, i_con2, name2
                            elif movido == 0:
                                print(f"Você não pode transferir 0R$.")
                                print(f"Operação cancelada.")
                                print(f"\n", "-=" * 15, end="-\n")
                                end = False
                                del pp2, reg_person1, lis_br1, nome1, pp_value1, date1, i_sec1, sect1, i_cla1, classe1, i_con1, name1, reg_person2, lis_br2, nome2, pp_value2, date2, i_sec2, sect2, i_cla2, classe2, i_con2, name2
                                # -- confirma --#
                            else:
                                saldo_movido = round(dic_reg[date1][i_sec1][sect1][i_cla1][classe1][i_con1][name1][0] - movido, 2)
                                saldo_recebido = round(dic_reg[date2][i_sec2][sect2][i_cla2][classe2][i_con2][name2][0] + movido, 2)
                                print(
                                    f"A conta de {nome1}, então ficará com: {saldo_movido}R$\n"
                                    f"e {nome2}, ficará com: {saldo_recebido}R$.\n"
                                    f"confirma?")
                                conf = confirm()
                                if conf is True:
                                    dic_reg[date1][i_sec1][sect1][i_cla1][classe1][i_con1][name1][0] = saldo_movido
                                    dic_reg[date2][i_sec2][sect2][i_cla2][classe2][i_con2][name2][0] = saldo_recebido
                                    print(f"O registro ficará: {dic_reg}. Escolha opcão 7 para validar.")
                                    print(f"Operação concluida.")
                                    desc = f"Transferência de {movido} por {nome1} para {nome2}."
                                    print(f"\n", "-=" * 15, end="-\n")
                                    end = True
                                elif conf is False:
                                    desc = 'Confirmação da operacão foi negada.'
                                    print(f"Operação cancelada.")
                                    print(f"\n", "-=" * 15, end="-\n")
                                    del pp2, reg_person1, lis_br1, nome1, pp_value1, date1, i_sec1, sect1, i_cla1, classe1, i_con1, name1, reg_person2, lis_br2, nome2, pp_value2, date2, i_sec2, sect2, i_cla2, classe2, i_con2, name2, saldo_movido, saldo_recebido, conf
                                    end = None
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append(
                     [f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break


        # DESABONAR:
        if escolha == 4.4:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: DESABONAR CONTA DE INDIVÍDUO)\n")
                data_atual = atual_data()
                pp = select_account_fc()
                if pp is not None:
                    reg_person, lis_br, name, pp_value = pp
                    data, i_sec, sect, i_cla, classe, i_con, name = lis_br
                    # -- Decide valor a ser desabonado --#
                    try:
                        money = round(float(input(f"Quantos reais deseja retirar? (Máximo = {money_func(PIB_real) = }): ")), 2)
                        exp = round(float(input(f"Quantos EXP deseja retirar?: ")), 1)
                        print(f"{money} / {exp}")
                    except ValueError:
                        print(f"Valor numérico incorreto. Operacao cancelada.")
                        end = False
                        continue
                    # -- valida valor --#
                    if (money + exp) == 0:
                        print(f"Você não pode retirar 0$ e 0EXP.")
                        print(f"Operação cancelada.")
                        print(f"\n", "-=" * 15, end="-\n")
                        desc = f'Houve tentativa de retirar {exp} EXP / {money} RYO.'
                        end = False
                        del reg_person, lis_br, pp_value, data, i_sec, sect, i_cla, classe, i_con, name, money, exp
                    elif money > PIB_real:
                        print(f"Você não pode retirar mais que o PIB de um indivíduo, pois não haveria como o mesmo recuperar dinheiro.")
                        desc = f"H"
                    else:
                        # -- confirmação --#
                        grana_ryo = round(
                            dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 0 ] - money, 2)
                        grana_exp = round(
                            dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 1 ] - exp, 1)
                        print(
                            f"A conta de {name}, então ficará com saldo de: {grana_ryo}R$ e "
                            f"{grana_exp} EXP. confirma? ")
                        conf = confirm()
                        if conf is True:
                            # assert isinstance(data_reg, object)
                            dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 0 ] = grana_ryo
                            dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 1 ] = grana_exp
                            print(f"Registro ficará: {dic_reg}. Escolha opção 7 para salvar como novo registro.")
                            desc = f"Retirado {money}$ e {exp}EXP de {name}"
                            del reg_person, lis_br, pp_value, data, i_sec, sect, i_cla, classe, i_con, name, money, exp
                            z = end = True
                        # --- Deleta as var usadas ---#
                        else:
                            print(f"Operação cancelada.")
                            print(f"\n", "-=" * 15, end="-\n")
                            del reg_person, lis_br, pp_value, data, i_sec, sect, i_cla, classe, i_con, name, money, exp
                            end = z = False
                elif pp is None:
                    print(f"Houve um erro ao selecionar conta a ser desabonada. Operação cancelada.")
                    end = False
                    del pp
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append(
                    [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break


        # PAGAR
        if escolha == 4.5:
            z = alternativa(i)
            while z is None:
                desc = ''
                data_atual = atual_data()
                print(f"Escolha a conta a ser creditada.")
                pp = select_account_fc()
                if pp is not None:
                    reg_person, lis_br, name, pp_value = pp
                    data, i_sec, sect, i_cla, classe, i_con, name = lis_br
                    # -- Decide valor a ser abonado --#
                    try:
                        money = round(float(input(f"Quantos reais deseja somar? (máximo = {valor_guardado - vms}): ")), 2)
                        exp = round(float(input(f"Quantos EXP deseja somar?: ")), 1)
                    except ValueError:
                        print(f"Valor numérico incorreto. Tente novamente.")
                        end = False
                        continue
                    # -- valida valor --#
                    if (money + exp) <= 0:
                        print(f"Você não pode somar 0$ e 0EXP.")
                        print(f"Operação cancelada.")
                        print(f"\n", "-=" * 15, end="-\n")
                        desc = f'Houve tentativa de somar {money} e {exp} (que são menores ou iguais a zero). '
                        end = False
                    elif money > (valor_guardado - vms):
                        print(f"ATENÇÃO: O dineiro a ser retirado do banco para depósito em conta, ULTRAPASSA em"
                              f" {money_func(money - (valor_guardado - vms))}$ o Valor guardado dísponível no banco de"
                              f" {money_func(valor_guardado - vms)}. Operação cancelada.")
                        desc = f'Houve tentativa de somar {money} que ultrapassa em {money_func(money - (valor_guardado - vms))}$ o valor disponível ({money_func(valor_guardado - vms)}). '
                        end = False
                    elif money < 0 or exp < 0:
                        print(F"O valor a ser creditado deve ser positivo. Para retirada de valores, escolha outra opção. Tente novamente.")
                        desc = f'Houve tentativa de somar {money} e {exp} (que são menores ou iguais a zero). '
                        end = False
                    # --- Segue inflação ---#
                    else:
                        # -- confirmação --#
                        saldo_ryo = round(dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 0 ] + money, 2)
                        saldo_exp = round(dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 1 ] + exp, 1)
                        print(f"A conta de {name}, então ficará com: {saldo_ryo}R$ e "
                            f"{saldo_exp} EXP. confirma? ")
                        conf = confirm()
                        if conf is True:
                            # assert isinstance(data_reg, object)
                            dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 0 ] = saldo_ryo
                            dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 1 ] = saldo_exp
                            print(f"Registro ficará: {dic_reg}. Escolha opção 7 para salvar como novo registro.")
                            desc = f"Adicionado {money}$ e {exp}EXP para {name}"
                            del reg_person, lis_br, pp_value, data, i_sec, sect, i_cla, classe, i_con, name, pp, money, exp
                            end = True
                        # --- Deleta as var usadas ---#
                        else:
                            print(f"Operação cancelada.")
                            print(f"\n", "-=" * 15, end="-\n")
                            desc = 'Confirmação de continuidade foi negada.'
                            del reg_person, lis_br, pp_value, data, i_sec, sect, i_cla, classe, i_con, name, pp, money, exp
                            end = False
                elif pp is None:
                    print(f"Não foi possível selecionar indivíduo. Operação cancelada.")
                    desc = 'account_fc() Retornou NONE'
                    end = False
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append(
                    [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break

        # CRIAR CLASSE:
        if 46 == i or escolha == 4.6:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: CADASTRAR NOVA CLASSE)\n")
                time.sleep(2)
                data_atual = atual_data()
                print(f"~ Escolha seção cujo a nova classe ficará! ~")
                sc = secoes_func()
                allc = values_fc()
                all_class = allc[8]
                print(f"{all_class = }")
                if sc is not None:
                    all_secoes, classes_por_secao, secao_value, secao_selected, data_reg, classes_list, secao_reg, persons_sec, clas_person, dic_sec = sc
                    #print('Classe:', dic_reg[data_reg][secao_value][secao_selected])
                    nome_novo = str(input("Nome da classe nova: ")).lower().strip()
                    if nome_novo == "":
                        print(f"O nome da classe não pode estar em branco. Operação cancelada.")
                        del nome_novo
                        end = False
                    elif nome_novo in all_class:
                        print(f"ATENÇÃO: Esta classe parece já existir. Tente outros nomes. Operação cancelada.")
                        del nome_novo
                        end = False
                    else:
                        print(f"Classe a ser cadastrada: {nome_novo}\nReino Pertencente: {secao_selected}. \nConfirma?")
                        conf = confirm()
                        if conf is True:
                            print("Certo. Vá ao menu e digite 7 para atualizar.")
                            nova_conta = {nome_novo: []}
                            classes_c2[secao_selected].append(nome_novo)
                            print(f"{classes_c2=}")
                            # Salva nova classe:
                            dic_reg[data_reg][secao_value][secao_selected].append(nova_conta)
                            desc = f"Cadastrado nova classe ({nome_novo} em {secao_selected})."
                            del nome_novo
                            z = end = True
                        else:
                            print(f"Operação cancelada.")
                            del nome_novo
                            end = False
                elif sc is None:
                    print(f"Reino pertencente não pôde ser escolhida. Operação cancelada.")
                    end = False
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append(
                    [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break


        # CRIAR NOVA SEÇÃO:
        if 47 == i or escolha == 4.7:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: CADASTRAR NOVA SEÇÃO)\n")
                data_atual = atual_data()
                if data_atual is not None:
                    sectsee_fc()
                    nome_novo = str(input("\nNome da seção nova: ")).lower().strip()
                    if nome_novo == "":
                        print(f"O nome da seção não pode estar em branco. Operação cancelada.")
                        del nome_novo
                        end = False
                    else:
                        print(f"Seção a ser cadastrada: {nome_novo}. \nConfirma?")
                        conf = confirm()
                        if conf is True:
                            print("Certo. BOTE ALGUMA CLASSE NESTA SEÇÃO PARA EVITAR ERROS! Vá ao menu e digite 7 para atualizar.")
                            nova_conta = {nome_novo: []}
                            # Salva nova secao:
                            dic_reg[data_reg].append(nova_conta)
                            classes_c2[nome_novo] = []
                            sectsee_fc()
                            desc = f"Cadastrado nova seção ({nome_novo})."
                            del nome_novo
                            end = True
                        else:
                            print(f"Operação cancelada.")
                            del nome_novo
                            end = True
                elif sc is None:
                    print(f"Reino pertencente não pôde ser escolhida. Operação cancelada.")
                    end = False
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append(
                    [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break

        # REMOVER SEÇÃO:
        if 48 == i or escolha == 4.8:
            z = alternativa(i)
            while z is None:
                desc =''
                print(f"\n(SELECIONADO: REMOVER SEÇÃO)\n")
                data_atual = atual_data()
                print(f"Escolha a seção a ser removida...")
                sec = secoes_func()
                if sec is not None:
                    all_secoes, classes_por_secao, secao_value, secao_selected, data_reg, classes_list, secao_reg, persons_sec, clas_person, dic_sec = sec
                    print(f"Você irá excluir a seção {secao_selected}, e juntamente, todas as classes e contas possiveis pertencentes a tal seção. Você confirma?")
                    conf = confirm()
                    if conf is True:
                        # remove secao:
                        print(f"\nClasses da seção: {classes_por_secao[secao_selected]}")
                        saldo_recuperado = 0
                        dividas_perdidas = 0
                        exp_perdido = 0
                        classes_perdidas = []
                        pessoas_removidas = 0
                        for sec, lis_conts in dic_reg[data_reg][secao_value].items():
                            for i in lis_conts:
                                for classe, dic_conts in i.items():
                                    print(f"    > CLASSE {classe.upper()} EXCLUÍDA: ")
                                    classes_perdidas.append(classe.lower())
                                    for cnt in dic_conts:
                                        for nome, saldo in cnt.items():
                                            print(f"- Excluído conta: {nome} com saldo de: {saldo}")
                                            pessoas_removidas += 1
                                            for cont, value in enumerate(saldo):
                                                if cont % 2 == 0:
                                                    if value > 0:
                                                        saldo_recuperado += value
                                                    else:
                                                        dividas_perdidas -= value
                                                else:
                                                    if value > 0:
                                                        exp_perdido += value
                        print(F"\nSALDO RECUPERADO: {saldo_recuperado} \n DIVIDAS PERDIDAS: {dividas_perdidas} \n EXP PERDIDO: {exp_perdido}\n QUANTIA DE CLASSES REMOVIDAS: {classes_perdidas.__len__()}\n QUANTIA DE CONTAS REMOVIDAS: {pessoas_removidas}")
                        #print(f"Saldo da conta: {dic_reg[data_reg][secao_value][secao_selected]}")
                        del dic_reg[data_reg][secao_value]
                        print(f"EXCLUÍDO: {classes_c2[secao_selected] = }")
                        del classes_c2[secao_selected]
                        for cla in classes_perdidas:
                            print(F"REMOVIDO da váriavel: {lideres[cla] = } registro de líder da classe {cla}")
                            del lideres[cla]
                        sectsee_fc()
                        print(f"{secao_selected} foi removido com sucesso. Use a opção 7 para salvar esta operação.")
                        desc = f"Removida a seção ({secao_selected})."
                        end = True
                    elif conf is False:
                        print(f"Operação cancelada.")
                        desc = 'Confirmação da operacão foi negada.'
                        end = False
                elif sec is None:
                    print(f"Seção não pôde ser escolhida. Operação cancelada.")
                    desc = 'secoes_func() Retornou NONE'
                    end = False
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break

        '''# REMOVER CLASSE:
        if 49 == escolha or escolha == 4.9:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: REMOVER CLASSE)\n")
                time.sleep(2)
                data_atual = atual_data()
                print(f"~ Escolha a classe a ser removida ! ~")
                sc = classes_func()
                if sc is not None:
                    classe_select, classe_value, secao_selected, secao_value, contas_da_classe, data_reg, reg_classe = sc
                    print(F"\nDeseja excluir a classe {classe_select.upper()} da seção {secao_selected.upper()} com todas suas possíveis contas e registro de líderes de tal?\n")
                    conf = confirm()
                    if conf == True:
                        keys_clas_dicreg = dic_reg[ data_reg ][ secao_value ][ secao_selected ][ classe_value ].keys()
                        if classe_select.lower() in keys_clas_dicreg:
                            print(F"Excluído do registro bancário a classe: {classe_select.upper()}")
                            saldo_recuperado = 0
                            dividas_perdidas = 0
                            exp_perdido = 0
                            for lis_cont in dic_reg[ data_reg ][ secao_value ][ secao_selected ][ classe_value ][
                                classe_select ]:
                                for nome, saldo in lis_cont.items():
                                    print(f"    -> Excluído: {nome} com saldo de: {saldo}")
                                    for cont, value in enumerate(saldo):
                                        if cont % 2 == 0:
                                            if value > 0:
                                                saldo_recuperado += value
                                            else:
                                                dividas_perdidas -= value
                                        else:
                                            if value > 0:
                                                exp_perdido += value
                            print(F"\nSALDO RECUPERADO: {saldo_recuperado} \n DIVIDAS PERDIDAS: {dividas_perdidas} \n EXP PERDIDO: {exp_perdido}\n")
                            if classe_select.lower() in classes_c2[ secao_selected ]:
                                ind = classes_c2[ secao_selected ].index(classe_select.lower())
                                print(f"Exluído: {classes_c2[secao_selected][ind] = } (Classe desvinculada da seção {secao_selected})")
                                clas_lideres = lideres.keys()
                                if classe_select.lower() in clas_lideres:
                                    print(F"Excluído registro de líder {lideres[ classe_select ]} da classe {classe_select}.")
                                    del lideres[ classe_select ]
                                    print("")
                                    print(f"Operação concluída. Digite 7 para validar.")
                                    print(f"\n", "-=" * 15, end="-\n")
                                    desc = f"Foi removida a classe {classe_select} de dic_reg, lideres, e classes_c2"
                                    end = True
                                else:
                                    print(F"A classe não estava na var 'lideres'. Tente novamente.")
                                    end = False
                                    desc = f"Não foi encontrada a classe {classe_select} em {lideres = }."
                            else:
                                print(F"A classe pode ainda não ter sido desvindulada do Reino.")
                                end = False
                                desc = f"Não foi encontrada a classe {classe_select} em {classes_c2 = }."
                        else:
                            print(F"Erro. Não foi possível excluír a classe selecionada. Operação cancelada.")
                            end = False
                            desc = f"Não foi encontrada a classe {classe_select} em {dic_reg[ data_reg ][ secao_value ][ secao_selected ][ classe_value ] = }."
                    elif conf is False:
                        print(f"Operação cancelada.")
                        desc = 'Confirmação da operacão foi negada.'
                        end = False
                elif sc is None:
                    end = False
                    desc = 'classes_func() Retornou NONE'
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append(
                    [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break

        # DEFINIR NOVO LÍDER:
        if escolha == 4.10 or 410 == escolha:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: REMOVER CLASSE)\n")
                time.sleep(2)
                data_atual = atual_data()

            # -- flag --#
            if desc == '':
                desc = 'None'
            if end == True:
                finalizacao = 'Operação bem-sucedida.'
            elif end == False:
                finalizacao = 'Operação interrompida ou falha.'
            elif end == None:
                finalizacao = 'Operação em aberto ou não conclusiva.'
            historico.append(
                [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                  desc,
                  f"Finalização: {end = }: {finalizacao = }" ])
            # --- Deleta as var usadas ---#
            break


        # DEFINIR NOVO REI:
        if escolha == 4.11 or 411 == escolha:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: REMOVER CLASSE)\n")
                time.sleep(2)
                data_atual = atual_data()

            # -- flag --#
            if desc == '':
                desc = 'None'
            if end == True:
                finalizacao = 'Operação bem-sucedida.'
            elif end == False:
                finalizacao = 'Operação interrompida ou falha.'
            elif end == None:
                finalizacao = 'Operação em aberto ou não conclusiva.'
            historico.append(
                [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                  desc,
                  f"Finalização: {end = }: {finalizacao = }" ])
            # --- Deleta as var usadas ---#
            break

        # REMOVER LÍDER:
        if escolha == 4.12 or 412 == escolha:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: REMOVER CLASSE)\n")
                time.sleep(2)
                data_atual = atual_data()

            # -- flag --#
            if desc == '':
                desc = 'None'
            if end == True:
                finalizacao = 'Operação bem-sucedida.'
            elif end == False:
                finalizacao = 'Operação interrompida ou falha.'
            elif end == None:
                finalizacao = 'Operação em aberto ou não conclusiva.'
            historico.append(
                [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                  desc,
                  f"Finalização: {end = }: {finalizacao = }" ])
            # --- Deleta as var usadas ---#
            break

        # REMOVER REI:
        if escolha == 4.13 or 413 == escolha:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: REMOVER CLASSE)\n")
                time.sleep(2)
                data_atual = atual_data()

            # -- flag --#
            if desc == '':
                desc = 'None'
            if end == True:
                finalizacao = 'Operação bem-sucedida.'
            elif end == False:
                finalizacao = 'Operação interrompida ou falha.'
            elif end == None:
                finalizacao = 'Operação em aberto ou não conclusiva.'
            historico.append(
                [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                  desc,
                  f"Finalização: {end = }: {finalizacao = }" ])
            # --- Deleta as var usadas ---#
            break

        # DEFINIR LEI POR REINO:
        if escolha == 4.14 or 414 == escolha:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: REMOVER CLASSE)\n")
                time.sleep(2)
                data_atual = atual_data()

            # -- flag --#
            if desc == '':
                desc = 'None'
            if end == True:
                finalizacao = 'Operação bem-sucedida.'
            elif end == False:
                finalizacao = 'Operação interrompida ou falha.'
            elif end == None:
                finalizacao = 'Operação em aberto ou não conclusiva.'
            historico.append(
                [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                  desc,
                  f"Finalização: {end = }: {finalizacao = }" ])
            # --- Deleta as var usadas ---#
            break'''

        # MUDAR NOMES E SELOS:
        if escolha == 4.15 or 415 == escolha:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: MUDAR NOMES E SELOS)\n")
                time.sleep(2)
                data_atual = atual_data()
                print(F"Escolha a conta a ser creditada... ")
                sc = select_account_fc()
                if sc is not None:
                    reg_person, lis_br, name, pp_value = sc
                    data_reg, secao_value, secao_selected, classe_value, classe_select, name_value, name_select = lis_br
                    print(f"{dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select] = }")
                    saldo = dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select][name_value][name_select]
                    print(f'O nome "{name_select} será atualizado para qual nome? (Escreva a classe também): ')
                    nome_novo = str(input(F"")).strip().title()
                    if nome_novo == "":
                        print(f"O nome novo não pode estar vazio. Operação cancelada.")
                        end = False
                        desc = f"Houve tentativa de mudar um nome para Null (sem nome/vazio)"
                    else:
                        print(f"Na classe {classe_select.upper()} da seção {secao_selected.upper()}..."
                              f"\nVoce deseja mesmo mudar o nome da conta {name_select} com saldo {saldo} para {nome_novo},"
                              f" mantendo este na mesma classe, seção e com mesmo saldo?: \n(Confirme Atualização de nome)")
                        conf = confirm()
                        if conf == True:
                            del dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select][name_value]
                            dic_reg[ data_reg ][ secao_value ][ secao_selected ][ classe_value ][ classe_select ].append({nome_novo: saldo})
                            val_reinantes = store.reinantes.values()
                            if name_select.title() in val_reinantes:
                                store.reinantes[secao_selected ] = nome_novo
                                print(f"Váriavel Reinantes teve o nome do rei atualizado:\n { store.reinantes = }")
                            val_lideres = lideres.values()
                            if name_select.title() in val_lideres:
                                lideres[classe_select.lower()] = nome_novo
                                print(f"Váriavel 'lideres' teve o nome do lider da classe {classe_select} atualizado:\n {lideres = }")
                            print(F"Operação bem-sucedida. Use opção 7 para validar.", "-="*15)
                            desc = f'O nome de {name_select} mudou para {nome_novo}'
                            end = True
                        elif conf == False:
                            desc = 'Confirmação da operacão foi negada.'
                            print(f"Operação cancelada.")
                            end = False
                else:
                    print(f"Não foi possível selecionar indivíduo. Operação cancelada.")
                    desc = 'account_fc() Retornou NONE'
                    end = False
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append(
                    [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                z = True
                break

        # PAGAR VÁRIOS
        if 416 == escolha or escolha == 4.16:
            print(F"PAGAMENTO EM MASSA")
            z = alternativa(i)
            while z is None:
                desc = ''
                end = passe = None
                data_atual = atual_data()
                print(f"Escolha a conta a ser creditada.")
                values = values_fc()
                if values is not None:
                    dic_person = {}
                    nomes = []
                    saldos = []
                    datas = []
                    val_sects = []
                    sects_select = []
                    val_clas = []
                    clas_select = []
                    val_pps = []
                    pps_select = []
                    lis_ppvalues = []
                    c = 0
                    while True:
                        pp = select_account_fc()
                        if pp is not None:
                            dic_person[c] = pp
                            nomes.append(dic_person[c][-2])
                            c += 1
                            # Vê se não têm contas repetidas:
                            for k, lis in dic_person.items(): # para cada conjunto de dados de cada indivíduo, k=int(index)
                                pass
                            lis_ppvalues.append(lis[-1])
                            if c >= 2: # Caso já tenha dois selecionados, pergunta se quer continuar:
                                print(F"\n Deseja adicionar outra conta? você já selecionou {c}, sendo: {iterar(nomes)}, com os números: {lis_ppvalues} \n")
                                conf = confirm()
                                if conf is False:
                                    break
                            else:
                                print(F"{c = }")
                            lis_ppvalues.sort()
                            passe = True
                            for i in range(1, len(lis_ppvalues)):
                                if lis_ppvalues[ i ] == lis_ppvalues[ i - 1 ]:
                                    repetido = lis_ppvalues[i]
                                    print(F"{repetido = }")
                                    passe = False
                                    break
                            if passe is False:
                                del nomes[-1]
                                del lis_ppvalues[-1]
                                del dic_person[c]
                                print(F"\nHÁ CONTAS DUPLICADAS. Selecione contas diferentes. Tente novamente.\n")
                        elif pp is None:
                            print(F"Tente novamente.")
                    tot_person = c # int(input(F"Quantas pessoas ao todo você irá pagar? (1 - "))
                    """for c in range(0, tot_person):
                        pp = account_fc()
                        dic_person[c] = pp"""
                    if None not in dic_person.values():
                        print(F"Deseja abonar: ")
                        for k, lis in dic_person.items(): # para cada conjunto de dados de cada indivíduo, k=int(index)
                            print(f"{k = }, {lis = }")
                            lis_ppvalues.append(lis[-1])
                            for c, i in enumerate(lis):
                                print(F"{c = }, {i = }")
                                ty = type(i)
                                if c == 1:
                                    for n, val in enumerate(i):
                                        print(f"{n = }, {val = }")
                                        if n == 0:
                                            datas.append(val)
                                        elif n == 1:
                                            val_sects.append(val)
                                        elif n == 2:
                                            sects_select.append(val)
                                        elif n == 3:
                                            val_clas.append(val)
                                        elif n == 4:
                                            clas_select.append(val)
                                        elif n == 5:
                                            val_pps.append(val)
                                        else:
                                            pps_select.append(val)
                                if ty is type(dict()):
                                    for nome, saldo in i.items():
                                        saldos.append(saldo)
                        if passe is True:
                            try:
                                money = bruto = round(float(input(f"Quantos reais deseja somar para TODOS? (máximo = {round((valor_guardado - vms) / tot_person, 2)}): ")), 2)
                                exp = round(float(input(f"Quantos EXP deseja somar para TODOS?: ")), 1)
                                print(F"Você deseja aderir a flutuação financeira de cada seção ao débito? (Aplicar inflação aos valores) ")
                                inflacao = confirm("        [S/N]: ")
                            except ValueError:
                                print(f"Valor numérico incorreto. Tente novamente.")
                                end = False
                            print(F"Você confirma o crédito de {money} Ryos e {exp} EXP, em um total de {money_func(money*tot_person)}$, Para: ")
                            ryos_novo = []
                            exps_novo = []
                            for c in range(0, tot_person):
                                money = bruto
                                sc = values_fc()
                                if sc is not None: # FAZ A INFLAÇÃO:
                                    print(F">   {pps_select[ c ].title()}")
                                    print(F"Com saldo de {saldos[ c ]}", end=' ')

                                    if inflacao is True:
                                        print(f"(% negativo == inflação (menos abono), % positivo == deflação (aumento do abono)")
                                        ipcapersec = sc[ 16 ]
                                        sect = sects_select[ c ]
                                        name = pps_select[ c ]
                                        mod = ipcapersec[ sect ]
                                        porcent = round(mod / 100, 2)
                                        liquido = money * porcent
                                        if mod < 0: # Inflação:
                                            money += liquido
                                        elif mod > 0: # Deflação:
                                            money -= mod
                                        a = saldos[ c ][ 0 ] + money
                                        b = saldos[ c ][ 1 ] + exp
                                        ryos_novo.append(a)
                                        exps_novo.append(b)
                                        print(F"para ter o saldo de {ryos_novo[ c ]} e {exps_novo[ c ]} EXP (com inflação de: {porcent} ({mod}%) (diferença: {liquido}))")
                                    else:
                                        a = saldos[ c ][ 0 ] + money
                                        b = saldos[ c ][ 1 ] + exp
                                        ryos_novo.append(a)
                                        exps_novo.append(b)
                                        print(F"para ter o saldo de {ryos_novo[ c ]} e {exps_novo[ c ]} EXP")
                            conf = confirm()
                            if conf is True:
                                if (money + exp) <= 0:
                                    print(f"Você não pode somar 0$ e 0EXP.")
                                    print(f"Operação cancelada.")
                                    print(f"\n", "-=" * 15, end="-\n")
                                    desc = f'Houve tentativa de somar {money} e {exp} (que são menores ou iguais a zero). '
                                    end = False
                                elif (money * tot_person) > (valor_guardado - vms):
                                    print(
                                        f"ATENÇÃO: O dineiro a ser retirado do banco para depósito em conta, ULTRAPASSA em"
                                        f" {money_func(money - (valor_guardado - vms))}$ o Valor guardado dísponível no banco de"
                                        f" {money_func(valor_guardado - vms)}. Operação cancelada.")
                                    desc = f'Houve tentativa de somar {money} que ultrapassa em {money_func(money - (valor_guardado - vms))}$ o valor disponível ({money_func(valor_guardado - vms)}). '
                                    end = False
                                elif money < 0 or exp < 0:
                                    print(
                                        F"O valor a ser creditado deve ser positivo. Para retirada de valores, escolha outra opção. Tente novamente.")
                                    desc = f'Houve tentativa de somar {money} e {exp} (que são menores ou iguais a zero). '
                                    end = False
                                # --- Segue inflação ---#
                                else:
                                    # -- confirmação --#
                                    for i in range(0, tot_person):
                                        money = bruto
                                        sc = values_fc()
                                        if sc is not None:
                                            ipcapersec = sc[16]
                                            data = datas[i]
                                            i_sec = val_sects[i]
                                            sect = sects_select[i]
                                            i_cla = val_clas[i]
                                            classe = clas_select[i]
                                            i_con = val_pps[i]
                                            name = pps_select[i]
                                            mod = ipcapersec[ sect ]
                                            print(F"{mod = }, {sect = }, {name = }, {ipcapersec = }")
                                            if inflacao is True:
                                                porcent = round(mod / 100, 2)
                                                liquido = money * porcent
                                                if mod > 0:  # Inflação:
                                                    money += liquido
                                                elif mod < 0:  # Deflação:
                                                    money -= mod
                                            saldo_ryo = round(dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 0 ] + money, 2)
                                            saldo_exp = round(dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 1 ] + exp, 1)
                                            dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 0 ] = saldo_ryo
                                            dic_reg[ data ][ i_sec ][ sect ][ i_cla ][ classe ][ i_con ][ name ][ 1 ] = saldo_exp
                                        elif sc is None:
                                            print(f"Não foi possível obter valores de acordo com inflação. Operação cancelada.")
                                            desc = 'values_fc() Retornou NONE'
                                            end = False
                                            break
                                    if end is not False:
                                        print(f"Registro ficará: {dic_reg}. Escolha opção 7 para salvar como novo registro.")
                                        desc = f"Adicionado {money}$ e {exp}EXP para {pps_select}"
                                        end = True
                            elif conf is None or conf is False:
                                print(f"Operação cancelada.")
                                print(f"\n", "-=" * 15, end="-\n")
                                desc = 'Confirmação de continuidade foi negada.'
                                end = False
                        elif passe is False:
                            print(F"HÁ CONTAS DUPLICADAS. Selecione contas diferentes. Operação cancelada.")
                            end = False
                            desc = 'Foi selecionado contas iguais.'
                    elif pp is None:
                        print(f"Não foi possível selecionar indivíduo. Operação cancelada.")
                        desc = 'account_fc() Retornou NONE'
                        end = False
                elif values is None:
                    print(f"Não foi possivel realizar operação.")
                    end = False
                    desc = 'values_fc() Retornou NONE'
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append(
                    [ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                      desc,
                      f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break


        # DEFINIR REGISTRO ANTIGO COMO ATUAL
        if escolha == 5:
            z = alternativa(i)
            while z is None:
                desc = ''
                data_atual = atual_data()
                # –– CÓDIGO: ––#
                print(f"SELECIONADO: DEFINIR REGISTRO")
                data_atual = atual_data()
                if backups["contas"].__len__() <= 1:
                    print(f"Não há registros antigos salvos. Operação cancelada.")
                    desc = 'Não foi visto mais que um registro em backups["contas"]. Sem registro para ser selecionado.'
                    end = True
                elif backups["contas"].__len__() >= 2:
                    print(f"Selecione a data do registro a ser restaurada...")
                    b = backups_fc("contas")
                    contas_new, es, es2, data_select = b
                    dic_reg = {data_select: contas_new}
                    print(f"O registro número {reg_selecionado} do backup de registros, foi selecionado como registro atual (dic_reg, store.contas), com sucesso. \n"
                        f"Aqui está o registro atual: {dic_reg}\n")
                    desc = "um registro antigo virou o registro atual."
                    end = True
                # -- FLAG --#
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                del registro, reg_selecionado, data_selecionada
                break

        # VER HISTÓRICO DE PEDIDOS
        if escolha == 6:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: HÍSTÓRICO DE PEDIDOS)\n")
                data_atual = atual_data()
                historic = hist_fc()
                logs = run(6)
                desc = 'O código foi analisado.'
                end = True
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break

        # REGISTRAR BACKUP NOVO
        if escolha == 7:
            z = alternativa(i)
            while z is None:
                # SALVA COM MÓDULO PANDAS:
                registroDF.to_csv("backup_registro.csv")
                registroDF.read_csv("backup_registro.csv")
                desc = ''
                print(f"\n(SELECIONADO: ATUALIZAR BACKUPS)\n")
                # --- Código ---#
                ultimo_registro = {}
                ultimo_liders = []
                ultimo_storereinantes = []
                ultimo_avisos = []
                ultimo_leis = []
                data_ultimo_registro = None
                data_atual = atual_data()
                len_storecontas = backups["contas"].__len__()
                len_liders = backups["lideres"].__len__()
                len_reis = backups["reinantes"].__len__()
                len_avi = backups["avisos"].__len__()
                len_leis = backups["leis"].__len__()
                len_rank = backups["Rank"].__len__()
                len_propriedades = backups['propriedades'].__len__()
                len_contratos = backups['contratos'].__len__()
                len_backups = backups.__len__()
                print(f"\nHá {len_backups} categorias de variáveis salvas em backups. Sendo:"
                      f"\ncontas: tendo {len_contas} datas salvas;"
                      f"\nlíderes: tendo {len_liders} pontos salvos."
                      f"\nreinantes: tendo {len_reis} pontos de revuperação guardados;"
                      f"\navisos: tendo {len_avi} datas de avisos guardados;"
                      f"\ne leis: {len_leis};"
                      f"\nRanks: tendo {len_rank} datas de Ranks de feitos em ON guardados."
                      f"\ncontratos: tendo {len_contratos} datas de registro dos contratos salvos"
                      f"\npropriedades: tendo {len_propriedades} datas de registro de store.itens dos ladinos, salvos.")
                # Salva o registro atual em var diferente, e salva o penúltimo registro do programa.
                while True:
                    ultimo_leis = leis.copy()
                    ultimo_avisos = avisos.copy()
                    ultimo_storereinantes = store.reinantes.copy()
                    ultimo_registro = store.contas.copy()
                    ultimo_liders = lideres.copy()
                    ultimo_Rank = Rank.copy()
                    ultimo_propriedades = propriedades.copy()
                    ultimo_contratos = contratos.copy()
                    for data, contas in dic_reg.items():
                        data_ultimo_registro = data
                        break
                        '''if contas is not ultimo_registro or data is not data_ultimo_registro:
                            data_ultimo_registro = data
                            break
                        else:
                            print(f"O REGISTRO: \n{store.contas}\nOU\n{data}\nJÁ ESTÁ ITERADO NO BACKUP!")
                            break'''
                    break
                print(f"\nREGISTRO ANTIGO: {dic_reg}\nVAR: LIDERES: {lideres}\nVAR store.reinantes: {store.reinantes}\nVAR AVISOS: {avisos}\nVAR leis: {leis}.")
                print(f"\nALTERE AS VARIÁVEIS (Pressione enter sem digitar nada para deixar como está).")
                # -- Salva registro novo no backup --#
                backups["contas"].update({data_atual: ultimo_registro.copy()})
                backups["lideres"].update({data_atual: ultimo_liders.copy()})
                backups["reinantes"].update({data_atual: ultimo_storereinantes.copy()})
                backups["avisos"].update({data_atual: ultimo_avisos.copy()})
                backups["leis"].update({data_atual: ultimo_leis.copy()})
                backups["Rank"].update({data_atual: ultimo_Rank.copy()})
                backups['propriedades'].update({data_atual: ultimo_propriedades.copy()})
                backups["contratos"].update({data_atual: ultimo_contratos.copy()})
                # Define registro e váriaveis atuais:
                del dic_reg
                dic_reg = dict()
                dic_reg[f"{data_atual}"] = ultimo_registro.copy()
                # -- salva o registro novo --#
                print(f"\nNovo registro salvo com sucesso.\n",
                      "Estas são as váriaveis salvas: {}\n".format(iterar(backups, f',\n')))
                print(backups)
                # -- Mostra Backup de registros --
                categories = {}
                cont = 0
                for category, dados in backups.items():
                    for dates, values in dados.items():
                        categories[category] = [dates]
                        print(f"\n {cont} – {category.upper()} >> data: {dates}.\n	 Conteúdo: {values}\n")
                        cont += 1
                # --- COMEMTARIO SOBRE REGISTRO NOVO ---#
                desc = str(input(f"\nDescrição da atualização (adicionados, valores, remoção, etc): "))
                avisos[0]['avisos de atualizacoes'][f'{data_atual}'] = f"{desc}"
                print(f"\nO aviso do registro novo, foi: {avisos[0]['avisos de atualizacoes'][f'{data_atual}']}")
                # --- FLAG --- #
                desc = "registro atualizado."
                z = end = True
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break


        # DECLARAR AVISOS:
        if escolha == 8:
            z = alternativa(i)
            while z is None:
                print(f"\n(SELECIONADO: DEFINIR AVISO GERAL)\n")
                # --- Código ---#
                data_atual = atual_data()
                caiu_em = "none"
                # -- Checa se há registros antigos --#
                if backups['contas'].__len__() >= 2:
                    print(f"\nHá registros antigos salvos. Você pode selecionar qual registro salvo deseja definir um aviso...\n")
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
                    end = True
                    regist = atual_data()
                    data_atual = regist[1]
                    desc = f"Definido um aviso."
                # Caso não possa ser visto:
                elif caiu_em in "none":
                    print(f"\nErro. O registro a ser visto não pôde ser definido, tente novamente.\n")
                    desc = "A var caiu_em Retornou em NONE"
                    del caiu_em, b_r
                    end = False
                # Caso retorne algo diferente de 'none, antigo ou novo':
                else:
                    print(f"Erro desconhecido. Programa finalizado.")
                    exit()
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break

        # PROGRAMAR DESABONANÇA:
        if escolha == 9:
            z = alternativa(i)
            while z is None:
                desc = ''
                print(f"\n(SELECIONADO: Programar desconto de conta)\n")
                # --- Definições de Vars. ---#
                # --- Código ---#
                print(f"Selecione qual indivíduo irá ter desabonança automática: ")
                a = select_account_fc()
                if pp is None:
                    print(F" Não foi possível selecionar o indivíduo. Operação cancelada.")
                    desc = "A func account_fc() Retornou NONE"
                    end = False
                else:
                    reg_person, lis_br, name, pp_value = a
                    print(f"Quantos R$ serão retirados por parcela, da conta {name}?: ")
                    money = float(input("> "))
                    money = round(money, 2)
                    print(f"Você deseja selecionar um dia no calendário[1], ou programar um intervalo de tempo?[2]")
                    esc = str(input(f"> ")).upper().strip()[0]
                    if esc == "1":
                        pass
                    elif esc == "2":
                        pass
                        if conf is True:
                            pass
                        else:
                            print(f"Operação cancelada.")
                            z = end = False
                            break
                    else:
                        print(f"Valor incorreto. Por favor, digite 1 ou 2. Operação cancelada.")
                        end = False
                        desc = f"Foi digitado um valor errado em uma escolha."
                    # -- flag --#
                    print("Foi desabonado com sucesso a parcela {n} de {n}, da conta {tal}. Registro: {reg}")
                    print(f"Operação concluída. Digite 7 para validar.")
                    print(f"\n", "-=" * 15, end="-\n")
                    # -- Deleta as var usadas --#
                    del data_atual
                    z = end = True
                    regist = atual_data()
                    data_atual = regist[1]
                    desc = f"Retirado n valor automaticamente da conta tal."
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break



        # FEITOS EM ON E ITENS:
        if escolha == 10:
            z = alternativa(i)
            while z is None:
                desc = ''
                data_atual = atual_data()
                print(f"\n(SELECIONADO: RANK DE FEITOS EM ON)\n")
                # --- Definições de Vars. ---#
                # --- Código ---#
                # -- flag --#
                cont_loop2 = cont_loop1 = total = Nível_Considerado = 0
                print(
                    f".   ~┏─━─━─━─━─━∞♟️∞━─━─━─━─━─┓~",
                    f"```-=❢=-``` *RANK DE FEITOS EM ON* ```-=❢=-```",
                    f"    ~┗─━─━─━─━─━∞♟️∞━─━─━─━─━─┛~\n",
                    f"> _Em ordem de 'chegada' - {data_atual}_\n"
                    f'      °==========° """ °==========°"', sep='\n', end='\n\n')
                for name, ranks in Rank.items():
                    cont_loop1 += 1
                    print(F"\n-> {cont_loop1} - {name.title()}: ", end='\n〖')
                    cont_loop2 = 0
                    Nível_Considerado = 0 #Sempre que muda de pessoa, nível considerado reseta
                    for feito, qtia in ranks.items():
                        cont_loop2 += 1
                        print(f" ```{qtia} {feito} ``` ", end='/')
                        total += qtia
                        for c in range(1, qtia+1):
                            if feito == 'Lutas': # A cada 4 lutas = +1 nivel
                                if c % 4 == 0:
                                    Nível_Considerado += 1
                            elif feito == "Partidas":
                                if c % 4 == 0:
                                    Nível_Considerado += 1
                            elif feito == "Caça":
                                if c % 2 == 0:
                                    Nível_Considerado += 1
                            elif feito == "Missões":
                                Nível_Considerado += 1
                        if cont_loop2 == 4:
                            print(f" *({total})* 〗")
                            total = 0
                    print(f"- Nível Considerado: ", end='')
                    if Nível_Considerado <= 5:
                        print(f"{Nível_Considerado}/Noumin")
                    elif Nível_Considerado <= 10:
                        print(f"{int(Nível_Considerado/2)}/Workin")
                    else:
                        if Nível_Considerado >= 6 and Nível_Considerado < 100:
                            Nível_Considerado = 5
                            print(f"{int(Nível_Considerado/3)}/Maxin")
                        elif Nível_Considerado <= 150: # Entre 100 e 150
                            print(f"01/SÁBIO *SENNIN* ")
                        elif Nível_Considerado <= 200: # Entre 151 e 200:
                            print(f"02/SÁBIO *SENNIN* ")
                        elif Nível_Considerado <= 300: # Entre 201 e 300:
                            print(f"03/SÁBIO *SENNIN* ")
                        elif Nível_Considerado <= 400: # Entre 301 e 400:
                            print(f" *01/SUPREMO* ")
                        elif Nível_Considerado <= 600: # Entre 401 e 500:
                            print(f" *02/SUPREMO* ")
                        elif Nível_Considerado > 999:
                            print(f" *SUPREMO SÁBIO ABSOLUTO - PATENTE MÁXIMA* ")
                print(f"\n\n_(apenas lutas/caça/partidas/missões, válidas e processadas no grupo Banco, são contadas)_",
                    f"_Lutas contadas de 1/1/22 a 27/01/2023 - (espaço perdido) + 20/02/2024 -> hoje_",
                    f"_caças contadas de 4/4/22 a 27/01/2023 - (espaço perdido) + 20/02/2024 -> hoje_",
                    f"_partidas contadas de 27/7/22 a 27/01/2023 - (espaço perdido) + 20/02/2024 -> hoje_",
                    f"_missões contadas de 17/4/22 a 27/01/2023 - (espaço perdido) + 20/02/2024 -> hoje_",
                    f"_Ou seja,, começaram dia X/2022, pararam dia Y/2023, e contagem voltou então dia N/2024 até hoje (ano de 2023 perdido. 2022 sem garantias também)_",
                    F"A CADA 4 lutas = +1 lvl, 4 Partidas = +1lvl, 2 Caças = +1lvl, 1 Missão = +1lvl. A CADA 6 Níveis UP de Patente",
                    f"PATENTES POR NÍVEIS: 0 - 5: NOUMIN, 6 - 10: WORKIN, 11 - 100: MAXIN; 101 - 150: SENNIN, 150 - 200: SÁBIO SENNIN, 201 - 300: SENNIN SUPREMO, 400 = SUPREMO, 600 = SÁBIO SUPREMO, 1.000 = SUPREMO SÁBIO ABSOLUTO "
                    , sep='\n', end='\n.\n')
                print(f"\n{Rank = }\n")
                print(f"Operação concluída. Digite 7 para validar.")
                print(f"\n", "-=" * 15, end="-\n")
                desc = f"Foi visto o Rank de Feitos em ON"
                end = True
                # -- Deleta as var usadas --#
                # -- flag --#
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                break

 # FEITOS EM ON E ITENS:
        if escolha == 11:
            z = alternativa(i)
            while z is None:
                desc = ''
                end = None
                data_atual = atual_data()
                print(f"\n(SELECIONADO: REGISTRO DE ITENS E CONTRATOS\n")
                patrimonio_total = patrimonio_pp = 0
                patrimonio_sec = {}
                dic_patrimonios_pp = {}
                for nome, dic_store.itens in propriedades.items():
                    cont_store.itens = 0
                    print(f"{dic_patrimonios_pp = }")
                    print(F"\n{nome.upper()}:")
                    tot_store.itens = sum(dic_store.itens.values())
                    for item, qtia in dic_store.itens.items():
                        cont_store.itens += qtia
                        print(f"{cont_store.itens = }, {tot_store.itens = }")
                        print(F"{qtia} {item.title()}, ", end=' ')
                        # Estima o património:
                        if item.title() in store.itens.keys():
                            preço = store.itens[item.title() ]
                            patrimonio_total += store.itens[item.title() ] * qtia
                            patrimonio_pp += store.itens[item.title() ] * qtia
                            for data, reg in dic_reg.items():
                                for i_sec, lis_sec in enumerate(reg):
                                    for sec, dic_sec in lis_sec.items():
                                        for section, lis_cla in lis_sec.items():
                                            for dic_cla in lis_cla:
                                                for classe, lis_pp in dic_cla.items():
                                                    for dic_pp in lis_pp:
                                                        for name, saldo in dic_pp.items():
                                                            if nome == name:
                                                                conta = dic_reg[data][i_sec]
                                                                secao_do_guri = sec
                                                                print(F"Localizado, {conta = }\n")
                                        if cont_store.itens is tot_store.itens-1:
                                            print(F"Adicionado em dic_patrimonios")
                                            if secao_do_guri == sec:
                                                dic_patrimonios_pp[nome] = patrimonio_pp
                                                try:
                                                    patrimonio_sec[sec] += patrimonio_pp
                                                except:
                                                    patrimonio_sec[ sec ] = patrimonio_pp
                                                finally:
                                                    print(F"{patrimonio_sec = } {nome = } {patrimonio_pp = }")
                                            else:
                                                pass
                                        else:
                                            print(F"Não adicionado em dic_patrimonis: {cont_store.itens = }, {tot_store.itens-1 = }")
                        else:
                            print(F"Item n listed")
                            try:
                                raise InterruptedError(F"Item não listado")
                            except InterruptedError as mensagem:
                                print(F"\n\nATENÇÃO: O ITEM {item} NÃO FOI LISTADO NA VÁRIAVEL DE ITENS. CORRIJA!", mensagem, file=stderr)
                                print('\n')
                            finally:
                                atent = str(input(f"Confirme que irá corrigir."))
                                end = False
                                desc = f"O item {item} de {nome} não foi localizado na variável store.itens. Corrija."
                            break
                    if nome not in dic_patrimonios_pp.keys():
                        print(F"Erro")
                    print(f"\n*TOTAL:* {tot_store.itens} store.itens/propriedades, com *PATRIMÓNIO:* bruto estimado em {patrimonio_pp}.")
                    patrimonio_pp = 0
                    if nome in 'Yamata':
                        input(F"!@#!@#!@#!#@#!@#!@#@!#@!#@!#@!#@!#!@#!@#@!#@!#!@#!@#!")
                print(F"\n\n*Patrimonio Mundial: {patrimonio_total} Ryos*\n{patrimonio_sec = }\n{dic_patrimonios_pp = }")
                if desc == '':
                    desc = 'None'
                if end == True:
                    finalizacao = 'Operação bem-sucedida.'
                elif end == False:
                    finalizacao = 'Operação interrompida ou falha.'
                elif end == None:
                    finalizacao = 'Operação em aberto ou não conclusiva.'
                historico.append([ f"Concluído funcão {escolha = }, para o registro {dic_reg}, as {data_atual = }",
                                   desc,
                                   f"Finalização: {end = }: {finalizacao = }" ])
                # --- Deleta as var usadas ---#
                z = end
                break


if __name__ == "__main__":
    main()
