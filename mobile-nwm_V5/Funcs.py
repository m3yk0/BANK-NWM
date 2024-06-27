"""
To v (4.6.1 of Bank-Mobile), V 5 of this code
FUNCS == ARQUIVO QUE MANUSEIA O OBJETO `REGISTRO`
"""

# ver 05/02/2024: add "função zero2", de Intercal.

# Global:
import datetime

# Imports Bib. padroes:
# Imports Bib. terceiros:
# Imports Bib. Local:
#import controles
from Historico import log  # all_persons, all_sections, PIB_real, totcontpersec, bolsa, PIB_Per_Capita_persec, PIB_Per_Capita, IPCA, ipcapersec, feepersec, tot_fee, tesouro, TBF, leis, Rank, contratos, propriedades
global contas, backups, data_reg, historico, reinantes, valor_mundial, valor_guardado, lideres, dic_reg, avisos, i, log, start, leis, Rank
from Intercal import values_fc, pib_real_fc


# Func. de confirmação
#   O QUE MUDAR AQUI, MOUDE EM INTERCALL
def confirm(text="\n[S/N]: "):
    """

    –> Função para fácilitar confirmação de decisões (retorna resultados lógicos, valida a entrada
    do usuário, categoriza o que foi digitado)
    Args:
        text: Texto a ser mostrado na tela

    Returns: Bool(True if user input a válid confirmation else False)

    """
    # Caso 'desconfirm' seja setado em diferente de None, então todas as confirmações do programa serão desacatadas e definidas com o valor de desconfirm
    from controles import desconfirm
    if desconfirm is not None and desconfirm is True or desconfirm is False:
        print(text)
        return desconfirm
    else:
        while True:
            log.append("construindo função 'confirm'...")
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


# Func de alternariva - retirada

# Func. de botar plural
def plural(algo, mod=0):
    log.append("construindo função 'plural'...")
    if algo > 1:
        letra = 'S'
    elif algo == 0:
        letra = 'S'
    elif algo < -1:
        letra = 'S'
    else:
        letra = ''
    if mod == 0:  # Upper
        letra = letra.upper()
    elif mod == 1:
        letra = letra.lower()
    return letra


# ver data

def atual_data() -> object:
    log.append("obtendo data atual...")
    data = str(datetime.date.today())
    ano, mes, dia = data[0:4], data[5:7], data[8:]
    hr = str(datetime.datetime.now())[11:19]
    data_atual = f"{dia}/{mes}/{ano}-{hr}"
    del hr, ano, mes, data
    return data_atual

global data_atual
data_atual = atual_data()


# Func  'run(mod)' de monitoramento de programa - Retirado


# Func. de botar zero atrás.
# ISTO ESTÁ LIGADO A INTERCAL.PY. SE ATUALIZAR AQUI, TAMBÉM ATUALIZE LÁ
global zero_


def zero(algo):
    log.append("construindo função 'zero()'...")
    algo = str(algo)
    v = algo.__len__()
    if v > 1:
        zero_ = ''
    elif v == 1:
        zero_ = 0
    else:
        zero_ = ""
    return zero_


# Func. de botar zero a direita. Use somente INT
# ISTO ESTÁ LIGADO A FUNC.PY. SE ATUALIZAR AQUI, TAMBÉM ATUALIZE LÁ
global zero2


def zero2(algo):
    log.append("construindo função 'zero2()'...")
    tipo = str(type(algo))
    algo = str(algo)
    v = algo.__len__()
    zero_ = algo[0]
    # zero_ = int(algo[0])
    for c in range(1, v):
        zero_ += "0"
    if int is tipo:
        zero_ = int(zero_)
    else:
        print("ERRO 'FUNC ZERO2(), Por favor, bote INT como parâmetro.")
    return zero_


# Func. de definir data
def programar_data():
    log.append("construindo função 'programar_data'...")
    while True:
        # --- Delcaração de Vars. ---#
        import calendar
        a = calendar.weekheader(5)
        data_atual = atual_data()
        d_atual = int(data_atual[0:2])
        mes_atual = int(data_atual[3:5])
        a_atual = int(data_atual[6:10])
        min_atual = int(data_atual[11:13])
        h_atual = int(data_atual[14:16])
        s_atual = int(data_atual[17:19])
        d_novo, mes_novo, a_novo, min_novo, h_novo, s_novo = d_atual, mes_atual, a_atual, min_atual, h_atual, s_atual
        # --- Código: ---#
        try:
            meses = int(input(f"Em quantos meses quer realizar a operação?: "))
            if meses <= -1:
                print(f"Usado valor negativo. Operação cancelada.")
                return False
            dias = int(input(f"Em quantos dias quer realizar a operação?: "))
            if dias <= -1:
                print(f"Usado valor negativo. Operação cancelada.")
                return False
            # Só define horário caso não deja definido dias.
            if (meses+dias) > 0:
                horas = 0
                minutos = 0
                segundos = 0
                min_novo, h_novo, s_novo = 0, 0, 0
            else:
                horas = int(
                    input(f"Em quantas horas quer realizar a operação?: "))
                if horas <= -1:
                    print(f"Usado valor negativo. Operação cancelada.")
                    return False
                minutos = int(
                    input(f"Em quantos minutos quer realizar a operação?: "))
                if minutos <= -1:
                    print(f"Usado valor negativo. Operação cancelada.")
                    return False
                segundos = int(
                    input(f"Em quantos segundos quer realizar a operação?: "))
                if segundos <= -1:
                    print(f"Usado valor negativo. Operação cancelada.")
                    return False
        except ValueError:
            print(f"Valor incorreto. Operação cancelada.")
            return False
        if (meses+dias+horas+segundos+minutos) == 0:
            print(
                f"Você não pode programar algo para daqui há 0 instantes. Operação cancelada.")
            return False
        else:
            min = minutos*60
            hr = horas*3600
            d = dias*86400
            mes = meses * 2628002
            total_em_seg = min+hr+d+mes
            print(f"Tempo em segundos: {total_em_seg}", end="")
            # padroniza os valores:
            for n in range(0, (horas+minutos+segundos)):
                if segundos >= 60:
                    segundos -= 60
                    minutos += 1
                if minutos >= 60:
                    minutos -= 60
                    horas += 1
            anos = 0
            for n in range(0, (meses+dias+horas)):
                if horas >= 24:
                    horas -= 24
                    dias += 1
                if dias >= 32:
                    dias -= 31
                    meses += 1
                if meses >= 13:
                    meses -= 12
                    anos += 1
            print(
                f"\nA operação ocorrerá daqui há: {dias} dia{plural(dias, 1)}, {meses} {'meses' if meses != 1 else 'mês'} e {anos} ano{plural(anos, 1)}. E {zero(horas)}{horas}:{zero(minutos)}{minutos}:{zero(segundos)}{segundos} horas (h:m:s).")
            print(
                f"\nData e hora atual: {d_atual}/{mes_atual}/{a_atual} (d/m/a). {zero(h_atual)}{h_atual}:{zero(min_atual)}{min_atual}:{zero(s_atual)}{s_atual} (h:m:s). \nA OPERAÇÃO OCORRERÁ EM: ", end="")
            # Descobre que dia do calendário os valores darão:
            d_novo += dias
            mes_novo += meses
            a_novo += anos
            s_novo += segundos
            min_novo += minutos
            h_novo += horas
            for n in range(0, (d_novo + mes_novo + a_novo + s_novo + min_novo + h_novo)):
                if s_atual >= 60:
                    s_novo -= 60
                    min_novo += 1
                if min_novo >= 60:
                    min_novo -= 60
                    h_novo += 1
                if h_novo >= 24:
                    h_novo -= 24
                    d_novo += 1
                if d_novo >= 32:
                    d_novo -= 32
                    mes_novo += 1
                if mes_novo >= 13:
                    mes_novo -= 13
                    a_novo += 1
            # verifica ultimo dia do mes:
            info_data = calendar.monthrange(a_novo, mes_novo)[1]
            ultimo_d_do_mes = int(str(info_data))
            # retira dias até estar de acordo com o último dia do mês.
            for n in range(0, d_novo):
                if d_novo > ultimo_d_do_mes:
                    d_novo -= 1
            # Valida a data
            data_nova = f"{zero(d_novo)}{d_novo}/{zero(mes_novo)}{mes_novo}/{a_novo}-{zero(h_novo)}{h_novo}:{zero(min_novo)}{min_novo}:{zero(s_novo)}{s_novo}"
            if data_atual == data_nova:
                print(f"Houve um erro pelo lado do servidor. A data agendada se tornou a mesma que a data atual, desculpe. Operação cancelada. Tente novamente mais tarde")
                return False
                break
            elif d_novo < d_atual and mes_novo == mes_atual and a_novo == a_atual:
                print(f"Desculpe. Houve um erro pelo lado de nosso sistema. A data agendada acabou retornando um valor menor que a data de hoje. Operação cancelada. Tente novamente mais tarde.")
                return False
                break
            elif data_atual != data_nova:
                print(f"{data_nova}. Confirma?: ")
                conf = confirm()
                if conf == True:
                    return data_nova
                    break
                else:
                    print(f"Operação cancelada.")
                    programar_data()
                    break


global data_nova

# Func. de impedir erro de index ou chaves


def prevent(container, index):
    log.append("construindo função 'prevent'...")
    classe = container.__class__()
    if classe == dict():
        try:
            return container[index]
        except KeyError:
            return "None"
    elif classe == list():
        try:
            return container[index]
        except IndexError:
            return "None"

# Func. de impedir erro de index ou chaves


def tryline(cod):
    log.append("construindo função 'tryline'...")
    try:
        return cod
    except KeyError:
        return None



# func. de iterar numa só linha.
def iterar(container, sep=", "):
    log.append("construindo função 'iterar'...")
    a = ""
    cont = 0
    for i in container:
        i = str(i).title()
        cont += 1
        if cont == container.__len__():
            a = a + f"{i}."
        else:
            a = a + f"{i}{sep}"
    return a


# Func. de recortar qualquer container.
def recort(container, qtia):
    log.append("construindo função 'recort'...")
    a = []
    c = 0
    for i in container:
        i = str(i).title()
        c += 1
        if c == qtia:
            break
        else:
            a.append(i)
    return a


# transformar valor em decimal:
# ISTO ESTÁ LIGADO A INTERCAL.PY. SE ATUALIZAR AQUI, TAMBÉM ATUALIZE LÁ
def decim_fc(valglobal):
    log.append("construindo função 'decim_fc'...")
    __val__ = str(round(valglobal))
    zeros = "1"
    for c, v in enumerate(__val__):
        zeros = zeros + "0"
    zeros = int(zeros)
    __val__ = int(__val__)
    __new__ = __val__ / zeros
    return __new__


# Func. 'backups_fc()' retirada.

# Func 'regselect_fc()' retirada


# Func. ver magnatas:
def magnatas_fc(registro):
    """

    Args:
        registro: registro a ser baseado o cálculo
    Returns: list([lista_maiores_ricos_em_grana, maiores_ricos_em_exp)
    """
    # -- Código --#
    sort_money = {}
    sort_exp = {}
    for classes in registro.values():
        if classes != 'none':
            for person in classes.values():
                if person != 'none':
                    for nome, valores in person.items():
                        if nome != 'none':
                            for num, valor in enumerate(valores):
                                if num in [0, 1]:
                                    if valor != 'none':
                                        valor = float(valor)
                                        if (num % 2) == 0:  # money:
                                            sort_money[ nome ] = round(valor, 2)
                                        else:  # exp:
                                            sort_exp[ nome ] = round(valor, 1)
    sort_money = dict(sorted(sort_money.items(), key=lambda x: x[ 1 ], reverse=True))
    sort_exp = dict(sorted(sort_exp.items(), key=lambda x: x[ 1 ], reverse=True))
    return [sort_money, sort_exp]


# Func. que seleciona seções.
def secoes_func(registro):
    """
    Seleciona seção
    Args:
        registro: dict
    Returns:

    """
    log.append(f"construindo funcão 'secoes_func()'...")
    print(f" LISTAGEM DAS SESSÕES: ")
    num = 0
    classes_por_secao = {}
    dic_sec = {}
    for sect, classes in registro.items():
        if sect != 'none':
            num += 1
            print(f"\n> OPÇÃO: ~ {num}:  -=-=-=->  {sect.upper()}  <-=-=-=-\nCategorias desta seção:")
            for n, classe in enumerate(classes):
                if classe != 'none':
                    print(f"   |{classe.title()}", end='|')
            classes_por_secao[sect] = list(registro[sect].keys())
            dic_sec[sect] = registro[sect]
    # Seleciona reino:
    while True:
        secao_value = str( input(f"\nQual seção quer selecionar? 1 até {num}: "))
        if secao_value.isnumeric() is False:
           pass
        elif int(secao_value) > num or int(secao_value) < 0:
            pass
        else:
            break
        print(f"Você precisa digitar um valor numérico no intervalo de 1 a {num}. Tente novamente.")
    secao_value = int(secao_value) -1
    secao_selected = list(registro.keys())[secao_value]
    dic_sec = {secao_selected: dic_sec[secao_selected]}
    print(f"\n A seção selecionado foi: {secao_selected.title()}. Confirma? ")
    conf = confirm()
    if conf == True:
        del conf, num
        return [classes_por_secao, secao_value, secao_selected, dic_sec]
    else:
        print(f"Operação cancelada.")
        return None


# VER SEÇOES:
def sectsee_fc():
    print(f"SEÇÕES CADASTRADAS:")
    c = 0
    for date, sect_dict in dic_reg.items():
        if date != 'none' != sect_dict:
            for sect_lis in sect_dict:
                if sect_lis != 'none':
                    for i, sect in enumerate(sect_lis):
                        if sect != 'none':
                            print(f"\n- {c} > ¦ {sect.upper():.^30} ¦")
                            c += 1


# func. que  mostra classes (categorias).
def classes_func(registro):
    log.append("construindo função 'classes_func'...")
    # -- código --#
    print(f"\nVocê selecionará primeiro a seção, em seguida a classe...\n")
    secao_var = secoes_func(registro=registro)
    if secao_var is None:
        print(f" Seção não pôde ser selecionado. Operação cancelada.")
        return None
    classes_por_secao, secao_value, secao_selected, dic_sec= secao_var
    print(f"\n LISTAGEM CATEGORIAS/CLASSES DE {secao_selected.upper()}:")
    cont = 0
    for n, classes in enumerate(classes_por_secao[secao_selected]):
        print(f"\nOPÇÃO {n+1}: --> {classes.upper()}", end="")
        cont += 1
    # Seleciona classe:
    while True:
        try:
            classe_value = int(input(f"\n (1 a {cont}). Classe número: ")) - 1
        except ValueError:
            print(f"\nValor incorreto. Favor digitar um número adequado a circunstância. Tente novamente.")
        if classe_value <= n and classe_value >= 0:
            break
        print(f"\n Usuário não encontrado, tente novamente.")
    classe_select = classes_por_secao[secao_selected][classe_value]
    contas_da_classe = dic_sec[secao_selected][classe_select]
    print( f"Você selecionou: {classe_select.title()}, da seção: {secao_selected.title()}. Confirma?")
    conf = confirm()
    if conf == True:
        print(f"Seleção de classe bem-sucedida.")
        reg_classe = registro[secao_selected][classe_select]
        return [classe_select, classe_value, secao_selected, secao_value, contas_da_classe, reg_classe]
    print(f"Erro.")
    return None


# func. que seleciona contas em seleção manual de reino e classs.
def contas_func():
    while True:
        log.append("construindo funcão 'contas_func'...")
        print(f"\nSELECIONE O REINO, EM SEGUIDA A CLASSE PARA ESCOLHER UM INDIVÍDUO!\n")
        # -- criação de vars --#
        class_var = classes_func()
        nomes = []
        n = 0
        if class_var != None:
            classe_select, classe_value, secao_selected, secao_value, contas_da_classe, data_reg = class_var[
                0], class_var[1], class_var[2], class_var[3], class_var[4], class_var[5]
            print(dic_reg[data_reg])
            # --- Código ---#
            print(f"\nSelecionado seção e categoria com sucesso. Agora escolha1 qual conta desta categoria você deseja selecionar...\n")
            for n, contas in enumerate(contas_da_classe):
                if contas != 'none':
                    for conta, valores in contas.items():
                        if conta != 'none':
                            print(f"{n} -> Nome: {conta.title()}. Saldo: {valores}")
                            nomes.append(conta)
            # realiza escolha1:
            try:
                indiv_value = int(input(f"(0 a {n}). Conta número: "))
            except ValueError:
                print(f"Por favor, use um INT valor numérico inteiro.")
                continue
            # valida escolha1:
            if indiv_value < 0 or indiv_value > n:
                print(f"Indivíduo não encontrado. Por favor, tente novamente.")
                continue
            else:
                indiv_select = nomes[indiv_value]
                saldo_indiv = dic_reg[data_reg][secao_value][secao_selected][classe_value][classe_select][indiv_value][indiv_select]
                print(f"Você escolheu {indiv_select.title()}, com a conta: {saldo_indiv}. Confirma?: ")
                conf = confirm()
                if conf == True:
                    print(f"Selecionada conta com sucesso.")
                    """print(f"Retornado: data_reg: {data_reg}\n	secao_value: {secao_value}\n	secao_selected: {secao_selected}\n	classe_value: {classe_value}\n	classe_select: {classe_select}\n	indiv_value: {indiv_value},\n	indiv_select: {indiv_select}\n	saldo_indiv: {saldo_indiv} ")"""
                    return [data_reg, secao_value, secao_selected, classe_value, classe_select, indiv_value, indiv_select, saldo_indiv]
                    break
                else:
                    print(f"Operação cancelada.")
                    return None
                    break
        else:
            print(f"Não foi possível selecionar a classe ou o reino. Tente novamente.")
            continue

# function for  person selection to automatic selection of section and class.
def select_account_fc(contas):
    log.append("construindo função 'account_fc'...")
    cont = 0
    ValuesToList = []
    for sect, classes in contas.items():
        if classes != 'none' and sect != 'none':
            print(f"    <~{sect.title()}~>")
            for classe, persons in classes.items():
                if classe != 'none' and persons != 'none':
                    print(f"  -{classe.title()}-")
                    for nome, saldo in persons.items():
                        if nome != 'none':
                            if saldo == 'none':
                                saldo = [0, 0]
                            print(f" > Opção: {cont} - Nome: {nome.upper()}, Saldo: {saldo}")
                            ValuesToList.append([cont, sect, classe, nome])
                            cont +=1
    while True:
        num = int(input(f"Digite o número do indivíduo (-1 para cancelar): "))
        if num >= cont or num < 0:
            print(f"Por favor, selecione um valor entre o intervalo de 0 a {cont-1}. Tente novamente.")
            continue
        elif num == -1:
            return None
        break
    VTL_person = ValuesToList[num]
    name = VTL_person[-1]
    classe = VTL_person[-2]
    section = VTL_person[1]
    person = contas[section][classe][name]
    if confirm(f"Você selecionou {num} - {name} da seção {section} e classe {classe} com saldo {person}. \nConfirma? [S/N]: "):
        return [num, name, classe, section, person]

# Func. de ver histórico retirada.

# operação dar saldo
def give_fc(registro, type="all"):
    values_a = values_fc(registro)
    values = values_a
    if values is None:
        print(f"Houve um erro ao tentar obter 'intercal.values_fc()'")
        return None
    vms = values[0]
    from manuseio import convert_things_to_items
    pb = pib_real_fc(Itens=convert_things_to_items())
    PIB_real, TBF = pb[0], pb[1]
    meta_selic = PIB_real -vms
    while True:
        if type == "money":
            din = round(float(input(f"Dinheiro [0 - {meta_selic}]: ")), 2)
            if din > meta_selic:
                print( f" ATENÇÃO: O saldo monetário ultrapassa o valor de {meta_selic} guardado no banco. Tente Novamente.")
                continue
            break
        if type == "exp":
            exp = round(float(input("EXP: ")), 1)
        else:
            din = str(input(f"Dinheiro [0 - {meta_selic}]: ")).strip().replace(',', '').replace('.', '')
            exp = str(input("EXP: ")).strip().replace(',', '').replace('.', '')
            if (din+exp).isnumeric() is False:
                print(f"Insira valor numérico.")
                continue
            din = float(din)
            exp = float(exp)
            if din > meta_selic:
                print( f" ATENÇÃO: O saldo monetário ultrapassa o valor de {meta_selic} guardado no banco. Tente Novamente.")
                continue
        break
    if type == "money":
        return din
    elif type == "exp":
        return exp
    elif type == "all":
        return [din, exp]


def employ_fc(registro, laddie=None, job=None, operation=None, employ_map=None):
    """

    Args:
        registro:
        laddie:
        job:
        operation: none | str
            '1' = 'Jobless' # Desempregar
            '2' = 'Give job' # Empregar
            '3' = 'Create Job' # Criar selo/cargo
            '4' = 'Replace Job' # Alterar selo/ cargo
            '5' = 'Delete Job'  # Deletar cargo
            '6' = 'List Jobs'  # Liste os empregos e cargos
        employ_map:

    Returns:

    """
    if employ_map is None:
        from manuseio import convert_works_to_employmap
        employ_map = convert_works_to_employmap()
    options = ['1', '2', '3', '4', '5', 'Jobless', 'Give Job', 'Create Job', 'Replace Job', 'Delete Job']

    def jobs(map=employ_map):
        num =0
        lis = []
        print()
        for k, v in map.items():
            print(f'{f" -> {num} - Selo: {k} ({v}) <- |":>45}', end='')
            num += 1
            if num % 2 == 0:
                print('')
            lis.append([k, v])
        while True:
            es = str(input(f"\nDigite o número [-1 para cancelar]: "))
            if es.isnumeric() or es == '-1':
                es = int(es)
                if es >= 0 and es <= num-1 or es == -1:
                    break
        if es == -1:
            selo = ''
            cargo = ''
        else:
            selo = lis[es][0]
            cargo = lis[es][1]
        return [es, selo, cargo]

    def give_job(job=job):
        # Seleciona indivíduo:
        if laddie is None or str(laddie).strip() == '':
            print(f"Primeiramente, selecione o indivíduo a receber um novo emprego")
            num, name, classe, section, person = select_account_fc(registro)
        # Seleciona emprego:
        if job is None:
            job = jobs()
            es, selo, cargo = job
        works = registro[ section ][ classe ][ name ][ 2 ]
        cargos = [ e.strip().title() for e in works.split(',') ]
        selos = [ ]
        for e in employ_map.keys():
            if e in name:
                selos.append(e)
        print(cargos)
        # valida escolha:
        if cargo in cargos or selo in selos:
            desc = f'\nO indivíduo: {name}, já tem o emprego {cargo}. Operação cancelada.'
            print(desc)
            return desc
        # Concretiza operação:
        cargos.append(cargo.lower())
        works = ','.join(cargos)
        registro[ section ][ classe ][ name ][ 2 ] = works
        info = registro[ section ][ classe ][ name ]
        del registro[ section ][ classe ][ name ]
        registro[ section ][ classe ][ f"{selo}{name}" ] = info
        print(job, laddie, works, registro)
        return f"Contas alterada. {name} chama-se '{selo}{name}' (adição de selo), e contém agora o cargo {cargo}."

    operation = str(operation).strip().title()
    if operation in ['1', 'Jobless', "unworking"]:
        pass
    elif operation in ['2', 'Give Job', "Give"]:
        return give_job(job=job)
    elif operation in ['3', 'Create Job', "Create"]:
        pass
    elif operation in ['4', 'Change Job', "Replace Job", "Rep", "Change"]:
        pass
    elif operation in ['5', 'Delete Job', 'Del']:
        pass
    elif operation in ['6', 'List Jobs', 'List']:
        return jobs(map=employ_map)
    else:
        while operation not in options:
            operation = input(f""" Selecione o que desejas fazer:
            1 = 'Jobless' # Desempregar
            2 = 'Give job' # Empregar
            3 = 'Create Job' # Criar selo/cargo
            4 = 'Replace Job' # Alterar selo/ cargo
            5 = 'Delete Job'  # Deletar cargo
            6 = 'List jobs'  # Listar empregos\n>>> """).strip().title()
        operation = str(operation).strip().title()
        employ_fc(registro, laddie, job, operation, employ_map)


def select_persons_with_work(registro, employ_map=None, filter='pobre-plebeu-miserável'):
    if employ_map is None:
        from manuseio import convert_works_to_employmap
        employ_map = convert_works_to_employmap()
    options = ['1', '2', '3', '4', '5', 'Jobless', 'Give Job', 'Create Job', 'Replace Job', 'Delete Job']

    sel = []
    cont = 0
    for sect, classes in registro.items():
        for cla, persons in classes.items():
            for name, data in persons.items():
                cont += 1
                for pos, element in enumerate(data):
                    if element == filter:
                        print(name, element)
                        sel.append([sect, cla, name, data, cont])

from manuseio import convet_xlsx_to_contas
select_persons_with_work(convet_xlsx_to_contas()[0])
#print(employ_fc(registro=convet_xlsx_to_contas()[0], operation='List'))

