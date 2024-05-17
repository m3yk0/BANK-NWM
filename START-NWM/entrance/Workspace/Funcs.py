
"""

FUNCS == ARQUIVO QUE MANUSEIA O OBJETO `REGISTRO`
"""


# Global:
import os
from os import system as osys
import sys
import datetime

# Imports Bib. padroes:
# Imports Bib. terceiros:
# Imports Bib. Local:
from entrance.Workspace import controles
from entrance.historico import log  
global contas, backups, data_reg, historico, reinantes, valor_mundial, valor_guardado, lideres, dic_reg, avisos, i, log, start, leis, Rank
from entrance.Store_fold import store
from entrance.Workspace.Intercal import values_fc, pib_real_fc

storevar = store.contas, store.contratos, store.propriedades, store.classes_c2, store.backups, store.Rank, store.data_reg, store.dic_reg, \
        store.avisos, store.reinantes, store.leis, store.lideres


# Func. de confirmação
#   O QUE MUDAR AQUI, MOUDE EM INTERCALL
def confirm(text="[S/N]: "):
    """

    –> Função para fácilitar confirmação de decisões (retorna resultados lógicos, valida a entrada
    do usuário, categoriza o que foi digitado)
    Args:
        text: Texto a ser mostrado na tela

    Returns: Bool(True if user input a válid confirmation else False)

    """
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


# Func de alternariva
def alternativa(i):
    """

    _summary_

    Args:
        i (_type_): _description_

    Returns:
        _type_: _description_
    """
    log.append("construindo função 'alternativa'...")
    try:
        end: None = None
        print(f"\n", "-=" * 15, end="-\n")
        print("-" * 5, f"SELECIONADO: {i}.", "-" * 5)
        print(f"Confirma?")
        conf_alternative = confirm()
        if conf_alternative is True:
            if end is None:
                return None
            if end is True:
                print(f"Operação concluída.")
                print(f"\n", "-=" * 15, end="-\n")
                z = end = True
                return True
            elif end is False:
                z = end = False
                return False
        else:
            print(f"Operação cancelada.")
            print(f"\n", "-=" * 15, end="-\n")
            z = end = False
            return False
    except:
        print(f"Erro. Reporte o erro.")
        return False
     

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


# Func de monitoramento de programa
def run(mod=None):
    log.append("obtendo função 'run'...")
    start = True
    if mod == 6:
        print(f"LOG DO SISTEMA: ")
        for total, operation in enumerate(log):
            print(f"{total + 1} operações realizadas -–> {operation}")
        total += 1
        if total == 4:
            print(f"Todas operações básicas foram realizadas com sucesso")
        elif total == 10:
            print(f"Todas operações foram realizadas com sucesso.")
        else:
            print(f".")
        # -- FLAG --#
        del total
    else:
        pass
    # se programa for
    version = str(sys.version)  # versão python
    vers = version[0: 5]
    vers = f"""{vers}"""
    sis_operativo = str(os.name)
    # Checa Sistema Operacional:
    if sis_operativo == "posix":
        # ver_dt = str(osys("pip freeze | grep [DateTime]"))
        # ver_dt = ver_dt.split()
        # print(">>>>", ver_dt, "<<<<<<<<")
        pass
    elif sis_operativo == "nt":
        versao_1 = osys('pip freeze | findstr [DateTime]')
    else:
        pass
    # Checa versão python:
    if vers == "3.9.7":
        pass
    else:
        print(f"Sua versão do python é: {vers}")
        print(
            f"O programa 'Bank-Meeh', foi contruído com a versão python 3.9.7. "
            f"Por favor, para impedir erros, procure usar versões igual ou acima da tal citada.")
        '''
        #os.mkdir("src")
        diretorio_atual = str(os.getcwd())
        print(f"""{diretorio_atual}
        {os.system('cp -R ~ //Banco ~ src')}
            """) 
            '''


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
                break
            dias = int(input(f"Em quantos dias quer realizar a operação?: "))
            if dias <= -1:
                print(f"Usado valor negativo. Operação cancelada.")
                return False
                break
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
                    break
                minutos = int(
                    input(f"Em quantos minutos quer realizar a operação?: "))
                if minutos <= -1:
                    print(f"Usado valor negativo. Operação cancelada.")
                    return False
                    break
                segundos = int(
                    input(f"Em quantos segundos quer realizar a operação?: "))
                if segundos <= -1:
                    print(f"Usado valor negativo. Operação cancelada.")
                    return False
                    break
        except ValueError:
            print(f"Valor incorreto. Operação cancelada.")
            break
            return False
        if (meses+dias+horas+segundos+minutos) == 0:
            print(
                f"Você não pode programar algo para daqui há 0 instantes. Operação cancelada.")
            break
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


# Func. de converter valor em forma mometária
# ISTO ESTÁ LIGADO A INTERCAL.PY. SE ATUALIZAR AQUI, TAMBÉM ATUALIZE LÁ
def money_func(din, f=2):
    """Formata valor em preço que pode ser lido por usuário (str)"""
    # Criação de vars:
    lis = []
    cont = 3
    # Tira decimal:
    din2 = int(din)
    # Cria str do valor total sem decimal:
    dinstr = str(din2)
    # Cria str do valor só decimal:
    decimal = str(round(din, f))
    try:
        a = decimal.index(".")
        decimal = decimal[a:]
    except ValueError:
        a = -1
        decimal = "0"
    # Substitui ponto por virgula no decimal:
    decimal = decimal.replace(".", ",")
    # Caso valor negativo, rerira o "menos":
    if din < 0:
        dinstr = dinstr[1:]
    # Vê quantas caracteres tem dinstr:
    len_din = dinstr.__len__()
    # Caso o número nessecite de separação de milhares (seja maior que 999):
    if din > 999 or din < -999:
        dinstr = "#" + dinstr
        for c, v in enumerate(dinstr[-1:0:-1]):
            lis.append(f"{v}")
            cont -= 1
            if cont == 0:
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
        # Garante que não tenha mais nem menos que uma vírgula:
        tipo = str(type(din))
        if "float" not in tipo:
            final = formatado + f",{decimal}"
        else:
            final = formatado + decimal
        qtia_virgulas = final.count(",")
        if qtia_virgulas > 1:
            final = final.replace(",", "a", qtia_virgulas)
        # garante que quantia de decimais seja igual a f:
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
        # Retorna o valor formatado
        if din < 0:
            final = "-" + final  # caso seja abaixo de zero, bota o traço de negativo
            return final  # + f"{decimal}"
        else:  # caso seja positivo, não bota o sinal de negativo.
            return final  # + f"{decimal}"
    # caso não precise de separação de milhar:
    else:
        if din < 0:
            dinstr = "-" + dinstr
        return dinstr  # + f"{decimal}"


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



# func. Mostra Backup Registros:
def backups_fc(var=str(None), date=str(None)) -> object:
    """:var == Key/Nome da váriavel a ser vista
    date == Data que váriavel foi salva/ data do conteúdo."""
    log.append("construindo função 'backups_fc'...")
    while True:
        escolha1 = str(None)
        escolha2 = str(None)
        # Sempre que 'passe == None' então código continua. Caso passe == False, caí em erro. Caso passe == True, programa continua a rodar/passar.
        passe = None
        # Armazena o nome (Key) das váriaveis guardadas que podem serem usadas no programa.
        guardados = []
        for variavel, content in backups.items():
            guardados.append(variavel)
        # Caso instância var não definida:
        if var == str(None):
            # Mostra registros/ Faz selecionar alguma váriavel para ser recuperada/ ver seu backup:
            print(f"Itens guardados no backup: ")
            for cont, variavel in enumerate(guardados):
                print(f"{'':^5}    {'-':-^25}")
                print(f"[{cont:^5}]: ¦ {variavel:^20} ", end=" ¦\n")
            print(f"{'':^5}    {'-':-^25}")
            escolha1 = str(input(f"Qual dos itens quer resgatar? (escreva o nome) ")).lower(
            ).strip()  # escolha1 = str(substituto de 'var') em backup_fc(var)
            if escolha1 not in guardados:
                print(f"Nome inválido. Tente novamente")
                passe = False
            else:
                passe = True
            # caso verificações conote False como erro: reinicia
            if passe == False:
                continue
        # caso instância var definida (escolha1 desnecessária):
        if var != str(None):
            escolha1 = str(var)
            passe = True
        if passe == True:
            cont = 0
            cont_data = dict()
            dates = []
            list_dates = []
            # Caso instância date definida:
            if date != str(None):
                # -- Verifica se 'date' corresponde a uma data guardada existente: --#
                for Data, arquiv in backups[f"{escolha1}"].items():
                    dates.append(Data)
                    cont_data[cont] = Data
                    list_dates.append(cont)
                    if Data == date:
                        # print(f'Passadas: {cont} - Arquivo de referência: {escolha1.upper()}. Data desejada correspondente: {Data}')
                        break
                    cont += 1
                # Caso não seja encontrado 'date':
                if date not in dates:
                    print(f"A data {date} não foi encontrada.")
                    passe = False
                escolha2 = cont
                conf = True
            # Caso instância date não definida:
            elif date == str(None):
                print(
                    f"Você selecionou a variável: {escolha1}. para ser restaurada. \nescolha1 qual das datas salvas será o ponto de recuperação...\n        Pontos de restauração disponíveis:")
                for Data, arquiv in backups[f"{escolha1}"].items():
                    print(f"{cont} > {Data=} ")
                    cont_data[cont] = Data
                    dates.append(Data)
                    list_dates.append(cont)
                    cont += 1
                list_dates = tuple(list_dates)
                dates = tuple(dates)
                escolha2 = cont = int(input(f"escolha1 o número: "))
            # -- Valida escolha1 --#
            if escolha2 in list_dates:
                escolha2 = dates[escolha2]
                print(escolha2)
                if var == str(None) and date == str(None):
                    print(
                        f"Você selecionou: {escolha1} com data: {cont_data[cont]}. Confirma?")
                    conf = confirm()
                else:
                    conf = True
                if conf is True:
                    if escolha1 == 'store.contas':
                        passe = True
                        store.contas = backups[escolha1 ][escolha2 ]
                        print(f"A VÁRIAVEL 'CONTAS', ACABA DE SER ATUALIZADA!")
                        if var == str(None) and date == str(None):
                            print(
                                f"Deseja também importar os avisos, líderes, reinantes e leis deste registro? [S/N]")
                            decision = confirm()
                        else:
                            decision = passe = True
                        if decision == True:
                            passe = True
                            global avisos_2, lideres_2, reinantes_2, leis_2
                            avisos_2 = backups_fc('avisos', escolha2)
                            avisos = avisos_2[-1]
                            lideres_2 = backups_fc('lideres', escolha2)
                            lideres = lideres_2[-1]
                            reinantes_2 = backups_fc('reinantes', escolha2)
                            reinantes = reinantes_2[-1]
                            leis_2 = backups_fc('leis', escolha2)
                            leis = leis_2[-1]
                            passe = True
                        else:
                            print(
                                f" houve um erro em backup_fc()... (Parada de erro 1)")
                            pass
                    elif escolha1 == 'lideres':
                        lideres = backups[escolha1][escolha2]
                    elif escolha1 == 'reinantes':
                        reinantes = backups[escolha1][escolha2]
                    elif escolha1 == 'avisos':
                        avisos = backups[escolha1][escolha2]
                    elif escolha1 == 'leis':
                        leis = backups[escolha1][escolha2]
                    elif escolha1 == 'Rank':
                        Rank = backups[escolha1][escolha2]
                    elif escolha1 == 'propriedades':
                        propriedades = backups[escolha1][escolha2]
                    elif escolha1 == 'contratos':
                        contratos = backups[escolha1][escolha2]
                    else:
                        print(
                            f"Não foi indexado no código, a variável selecionada. Por favor, faça a correção.")
                        break
                    # --- Flag ---#
                    if var != str(None) and date != str(None) or passe == True:
                        print("Backup selecionado foi feito com sucesso.")
                        """print(f"Retornado: {escolha1 = },\n {escolha2 = }, \n{dates = }.")"""
                        return [escolha1, escolha2, dates]
                        break
                    if escolha1 != str(None) != escolha2:
                        print(f"Backup destinado feito com sucesso.")
                        return [escolha1, escolha2, dates]
                        break
                elif conf is False:
                    print(f"Operação cancelada.")
                    return None
                    break
            elif escolha2 not in list_dates:
                print(
                    f"Não foi possível localizar o ponto de restauração. Operação cancelada.")
                return None
                break


# Verifica e seleciona registros de pontos novos ou anteriores.
def regselect_fc(pos='antigo'):
    log.append("construindo função 'regselect_fc()'...")
    len_backup = backups['store.contas'].__len__()
    data_atual = atual_data()
    global regist, registro, var_selecionada, data_select, b_r, escolha1, escolha2, dates
    if len_backup <= 1 or pos == 'novo':
        print(f"\nVocê verá o registro atual.\n")
        # Caso não tenha reg. antigo: b_r == registro atual
        b_r = dic_reg
        # Define a variavel data de b_r
        for data, reg in b_r.items():
            registro = reg
            data_select = data
        caiu_em = 'novo'
        print(F"\n\nVERÁS REGIRSTRO NOVO\n")
        return [caiu_em, b_r, data_select]
    if len_backup >= 2:
        print(f"\nHá registros antigos salvos. Você pode selecionar qual registro salvo deseja ver...\n")
        # Seleciona qual registro quer ver
        regist = backups_fc('store.contas')
        escolha1, escolha2, dates = regist
        registro, var_selecionada, data_select = backups[escolha1], escolha1, escolha2
        caiu_em = 'antigo'
        b_r = registro
        print(F"\n\nVERÁS REGISTRO ANTIGO\n")
        historico.append([f"Concluído regselect_fc, o registro escolhido foi: {b_r}, com data {escolha1} ás {data_atual}",
                          "desc: O registro foi visto."])
        return [caiu_em, b_r, data_select]


# Func. ver magnatas:
def magnatas_fc(registro=store.contas):
    """

    Args:
        registro: registro a ser baseado o cálculo
    Returns: list([lista_maiores_ricos_em_grana, maiores_ricos_em_exp)
    """
    # -- Código --#
    sort_money = {}
    sort_exp = {}
    for classes in registro.values():
        for person in classes.values():
            for nome, valores in person.items():
                for num, valor in enumerate(valores):
                    if (num % 2) == 0:  # money:
                        sort_money[ nome ] = round(valor, 2)
                    else:  # exp:
                        sort_exp[ nome ] = round(valor, 1)
    sort_money = dict(sorted(sort_money.items(), key=lambda x: x[ 1 ], reverse=True))
    sort_exp = dict(sorted(sort_exp.items(), key=lambda x: x[ 1 ], reverse=True))
    return [sort_money, sort_exp]



# Func. que seleciona seções.
def secoes_func(registro=store.contas):
    """

    Args:
        registro = dict
    Returns:

    """
    log.append(f"construindo funcão 'secoes_func()'...")
    print(f" LISTAGEM DAS SESSÕES: ")
    num = 0
    classes_por_secao = {}
    dic_sec = {}
    for sect, classes in registro.items():
        num += 1
        print(f"\n> OPÇÃO: ~ {num}:  -=-=-=->  {sect.upper()}  <-=-=-=-\nCategorias desta seção:")
        for n, classe in enumerate(classes):
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

    


# func. que  mostra classes (categorias).
def classes_func(registro=store.contas):
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
                for conta, valores in contas.items():
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
                print(
                    f"Você escolheu {indiv_select.title()}, com a conta: {saldo_indiv}. Confirma?: ")
                conf = confirm()
                if conf == True:
                    print(f"Selecionada conta com sucesso.")
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
def select_account_fc(contas=store.contas):
    log.append("construindo função 'account_fc'...")
    cont = 0
    ValuesToList = []
    for sect, classes in contas.items():
        print(f"    <~{sect.title()}~>")
        for classe, persons in classes.items():
            print(f"  -{classe.title()}-")
            for nome, saldo in persons.items():
                print(f" > Opção: {cont} - Nome: {nome.upper()}, Saldo: {saldo}")
                ValuesToList.append([cont, sect, classe, nome])
                cont +=1
    while True:
        num = int(input(f"Digite o número do indivíduo: "))
        if num > cont or num < 0:
            print(f"Por favor, selecione um valor entre o intervalo de 0 a {num}. Tente novamente.")
            continue
        break
    VTL_person = ValuesToList[num]
    name = VTL_person[-1]
    classe = VTL_person[-2]
    section = VTL_person[1]
    person = contas[section][classe][name]
    if confirm(f"Você selecionou {num} - {name} da seção {section} e classe {classe} com saldo {person}. \nConfirma? [S/N]: "):
        return [num, name, classe, section, person]


# Func. de ver histórico.
def hist_fc():
    log.append("construindo função 'hist'...")
    data_atual = atual_data()
    global conclusoes
    c = len(historico)
    conclusoes = "( "
    # Caso sem históricos:
    if c < 1:
        print(f"Ainda não há historico salvo.")
        z = end = False
        return None
    else:
        for n, operacoes in enumerate(historico):
            print("\n\n", n, ">", end=" ")
            for num, secao in enumerate(operacoes):
                print("\n", f"—", secao, end="")
                conclusoes += f"\n~ n° de precedência: {n + 1}°;" \
                    f"  identificação: {num}; conteúdo:     {secao}.   "
        conclusoes += "~)"
        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                          f"Histórico de operações visto."])
        print(f"\n\n----Esse foi o histórico. Para resetar, escolha1 opção 7.----")
        z = end = True
        return None


# VER SEÇOES:
def sectsee_fc():
    print(f"SEÇÕES CADASTRADAS:")
    c = 0
    for date, sect_dict in dic_reg.items():
        for sect_lis in sect_dict:
            for i, sect in enumerate(sect_lis):
                print(f"\n- {c} > ¦ {sect.upper():.^30} ¦")
                c += 1


# operação dar saldo
def give_fc(type="all",registro=store.contas):
    values_a = values_fc(registro)
    values = values_a
    if values is None:
        print(f"Houve um erro ao tentar obter 'intercal.values_fc()'")
        return None
    vms = values[0]
    pb = pib_real_fc()
    PIB_real, TBF = pb[0], pb[1]
    meta_selic = PIB_real - vms
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
            din = str(input(f"Dinheiro [0 - {meta_selic}]: "))
            exp = str(input("EXP: "))
            if (din+exp).replace(',', '').replace('.', '').isnumeric() is False:
                print(f"Insira valor numérico.")
                continue
            din = float(din)
            exp = float(exp)
        break
    if type == "money":
        return din
    elif type == "exp":
        return exp
    elif type == "all":
        return [din, exp]

