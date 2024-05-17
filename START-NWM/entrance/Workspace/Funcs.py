
"""

FUNCS == ARQUIVO QUE MANUSEIA O OBJETO `REGISTRO`
"""

# ver 05/02/2024: add "função zero2", de Intercal.

# Global:
import os
from os import system as osys
import sys
import datetime

# Imports Bib. padroes:
# Imports Bib. terceiros:
# Imports Bib. Local:
from entrance.Workspace import controles
from entrance.historico import log  # all_persons, all_sections, PIB_real, totcontpersec, bolsa, PIB_Per_Capita_persec, PIB_Per_Capita, IPCA, ipcapersec, feepersec, tot_fee, tesouro, TBF, leis, Rank, contratos, propriedades
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
                    f"Você selecionou a variável: {escolha1}. para ser restaurada. \nescolha1 qual das datas salvas será o ponto de recuperação...\n	Pontos de restauração disponíveis:")
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


'''
backups = {
    "store.contas":
        {"11/07/2023-02:09:01": (store.contas.copy()), "hoje": (store.contas.copy())
         },
    "lideres": {"11/07/2023-02:09:01": (lideres.copy()), "hoje": (lideres.copy())
                },
    "reinantes": {"11/07/2023-02:09:01": (reinantes.copy()), "hoje": (reinantes.copy())
                  },
    "avisos": {"11/07/2023-02:09:01": (avisos.copy()), "hoje": (avisos.copy())
               },
    "leis": {"11/07/2023-02:09:01": (leis.copy), "hoje": (leis.copy())
             }
    }
print(regselect_fc())'''

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

    """
        # -- declaração de vars. --#
        all_secoes = []
        classes_por_secao = {}
        classes_list = []
        persons_sec = {}
        clas_person = {}
        dic_sec = {}
        # -- código --#
          
               
            templis_cla = [ ]
            for n, classe_dict in enumerate(classes):
                for cla, conts in classe_dict.items():
                    templis_cla.append(cla)
                    classes_list.append(cla)
                    print(f" {n + 1} - {cla.title()}")
                    for names_dic in conts:
                        for names, saldo in names_dic.items():
                            templis_names.append(names)
                clas_person[ cla ] = templis_names
        persons_sec[ secao ] = templis_names
        classes_por_secao[ secao ] = templis_cla
        
        for data_reg, list_secoes in dic_reg.items():  # pega a data e var 'store.contas' do dicionário dic_reg
            # faz a numeração das seções de list_seções (lista com dicionários)
            for num, secoes in enumerate(list_secoes):
                for secao, classes in secoes.items():  # Separa o nome da seção e a lista de classes de tal seção
                    templis_names = []
                    dic_sec[secao] = classes
                    all_secoes.append(secao)
                    print(
                        f"\nOPÇÃO: ~ {num}:  -=-=-=->  {secao.upper()}  <-=-=-=-")
                    print(f"Categorias desta seção:")
                    templis_cla = []
                    for n, classe_dict in enumerate(classes):
                        for cla, conts in classe_dict.items():
                            templis_cla.append(cla)
                            classes_list.append(cla)
                            print(f" {n+1} - {cla.title()}")
                            for names_dic in conts:
                                for names, saldo in names_dic.items():
                                    templis_names.append(names)
                        clas_person[cla] = templis_names
                persons_sec[secao] = templis_names
                classes_por_secao[secao] = templis_cla
        try:
            # Seleciona reino:
            secao_value = int(
                input(f"\nQual seção quer selecionar? 0 até {num}: "))
        except ValueError:
            print(f"Erro de valor. Tente novamente")
            continue
        if secao_value > num or secao_value < 0:
            print(
                f"Você não digitou um valor entre o intervalo 0 a {num}. Tente novamente.")
            continue
        else:  # caso tudo certo, código continua:
            secao_selected = all_secoes[secao_value]
            print(
                f"\n A seção selecionado foi: {secao_selected.title()}. Confirma? ")
            secao_reg = dic_reg[data_reg][secao_value]
            dic_sec = dic_sec[secao_selected]
            # print(dic_sec)
            conf = confirm()
            if conf == True:
                #print(f"Retornado: [all_secoes: {all_secoes},\n classes_por_secao, {classes_por_secao},\n secao_value: {secao_value},\n secao_selected: {secao_selected},\n data_reg: {data_reg},\n classes_list: {classes_list},\n secao_reg: {secao_reg}]")
                del conf
                return [all_secoes, classes_por_secao, secao_value, secao_selected,
                        data_reg, classes_list, secao_reg, persons_sec, clas_person, dic_sec]
            else:
                print(f"Operação cancelada.")
                return None
                break"""


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

    """while True:
        global i_sec, sect, i_cla, classe, i_con
        lis_br = []
        all_accounts = []
        cont = 0
        print(f"Reinos e classes a serem vistas:")
        # i_sec, sect, i_cla, classe, i_con = None
        for date, item in dic_reg.items():
            lis_br.append([item])
            for i_sec, sections in enumerate(item):
                for sect, class_lis in sections.items():
                    print(f"\n{sect.upper()}")
                    for i_cla, class_dict in enumerate(class_lis):
                        for classe, conts_lis in class_dict.items():
                            print(f"\n{classe.title()}")
                            for i_con, conts_dict in enumerate(conts_lis):
                                all_accounts.append(conts_dict)
                                for name, values_lis in conts_dict.items():
                                    print(f"– {cont} > {name}: {values_lis}")
                                    cont += 1
                                    lis_br.append(
                                        [date, i_sec, sect, i_cla, classe, i_con, name])
        try:
            pp_value = int(input(f"Digite o número do indivíduo: "))
        except ValueError:
            print(
                f"Por favor, digite um valor numérico de 0 a {cont}. Tente novamente.")
            continue
        intervalo = [i for i in range(0, cont)]
        if pp_value in intervalo:
            pp_select = all_accounts[pp_value]
            lis_br = lis_br[pp_value+1]
            data, i_sec, sect, i_cla, classe, i_con, name = lis_br[0], lis_br[
                1], lis_br[2], lis_br[3], lis_br[4], lis_br[5], lis_br[6]
            reg_person = dic_reg[data][i_sec][sect][i_cla][classe][i_con]
            print(f"\nVocê selecionou {pp_value} - {pp_select}. Confirma?")
            conf = confirm()
            if conf == True:
                print(f"Conta selecionada com sucesso")
                return [reg_person, lis_br, name, pp_value]
            elif conf == False:
                print(f"Operação cancelada.")
                return None
        else:
            print(
                f"Não foi encontrado conta número {pp_value}. Tente novamente.")
            continue
"""

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


"""


RETIRADO 07/04/2024:


def pib_real_fc():
  
    Define PIB_REAL, TBF e arruma ITENS:
    criado: 06/04/2024
  
    # Define o PIB_real
    # Contabiliza o PIB real (Diferente do PIB Per Capita, que considera a quantia de indivíduos,
    PIB_real = 0
    # que seria o PIB_Per_Capita, e diferente do PIB Nominal, que considera a inflação)
    old_itens = store.itens.copy()
    new_itens = store.itens.copy()
    for k, v in old_itens.items():  # Para cada chave e valor presente em "store.itens":
        k_novo = k.title().replace('_', ' ').strip()
        new_itens[ k_novo ] = new_itens.pop(k)
        v = int(v)  # Transforma o valor em INT
        PIB_real += v  # E itera em PIB_real
        # E salva o valor antes "str", como "INT" no dicionário de store.itens do RPG.
        new_itens[ k_novo ] = int(v)
    # Arredonda o valor de PIB_real para ter somente zeros e o número inicial
    PIB_real = int(zero2(PIB_real))
    ""DEFINE TBF DE ACORDO COM PIB_REAL:""
    # =====- AQUI em [0: 6] VOCÊ DEFINE QUANTOS ZEROS TERÁ A FRAÇÃO DE TBF para os cálculos do IPCA, Taxa, etc. -=======#
    TBF = int(str(zero2(PIB_real))[ 0:6 ])  # Transforma "TBF"
    # em variável INT com o primeiro número do PIB_real e x quantias de zeros atrás para formatação de fração quando for realizar alguma divisão "VMS ÷ TBF" como VMS%×Nx (N = número PIB_real, x = qtia. De zeros)
    return  [PIB_real, TBF, old_itens, new_itens]


def all_names_fc(registro=store.contas):
    all_persons = []
    for dic_cla in registro.values():
        for conts in dic_cla.values():
            for name in conts.keys():
                all_persons.append(name)  # Bota nome do guri em lista de nomes
    return all_persons


def pibs_fc():
    ""DEFINE PIB_PER_CAPITA_PERSEC E PIB_PER_CAPITA""
    pib = pib_real_fc()  # Define PIB_real e TBF
    PIB_real, TBF = pib[ 0 ], pib[ 1 ]
    all_persons = all_names_fc()
    # calcula PIB_Per_Capita (atualizado para PIB_Per_Capita mundial ser == PIB_real)
    # define PIB_Per_Capita_persec
    PIB_Per_Capita_persec = {}
    PIB_Per_Capita = 0
    acconts = 0
    for sec, dic_cla in store.contas.items():
        for cla, conts in dic_cla.items():
            for cont in conts.items():
                acconts += 1
            if acconts > 1:
                PIB_Per_Capita_persec[ sec ] = (PIB_real / acconts)
            else:
                PIB_Per_Capita_persec[ sec ] = round(
                    PIB_real / all_persons.__len__(), 2)
            acconts = 0
    # calcula PIB_Per_Capita mundial:
    for k, v in PIB_Per_Capita_persec.items():
        PIB_Per_Capita += v
    return [PIB_Per_Capita, PIB_Per_Capita_persec, PIB_real, TBF]


# Func de capturar valores do registro (cópia do registro)
def values_fc(registro=store.contas.copy()):
    log.append("construindo função 'values_fc'...")
    vms = 0
    ems = 0
    all_sections = []
    all_class = []
    # money per sections (grana por seções == PVMS de cada seção)
    # VPMS == PVMS == Parte do Valor Mundial Situado. Cita o valor em mãos de tal parte/seção.
    tot_pvms = vpms = 0
    totcontpersec = {}
    acconts = 0
    accontsdict = {'negativos': 0, 'positivos': 0}
    bolsa = 0
    bolsapersec = {}
    tesouropersec = {}
    for sec, dic_cla in registro.items():  # i = dict{str(seção): dict(classes)}
        all_sections.append(sec)  # Adiciona a seção na lista que conta todas as seções.
        vpms = pvms = 0  # PVMS reseta sempre que muda de seção
        bolsa2 = 0  # Bolsa reseta sempre que muda de seção
        for cla, dic_conts in dic_cla.items():
            all_class.append(cla)  # Soma todas as classes em uma lista
            for name, saldo in dic_conts.items():
                acconts += 1  # total de contas soma +1
                for pos, val in enumerate(saldo):
                    if pos == 0:  # ryo
                        # Somente caso o saldo for positivo, ele é contabilizado para o VMS (tot_pvms), PVMS e soma de store.contas positivadas.
                        if val > 0:
                            vms += val
                            vpms += val
                            tot_pvms += val
                            accontsdict[ 'positivos' ] += 1
                        elif val < 0:  # Caso o saldo do indivíduo for negativo:
                            bolsa -= val  # A bolsa de valores mundial é contabilizada
                            # A bolsa de valores da seção atual é contabilizada.
                            bolsa2 -= val
                            accontsdict[ 'negativos' ] += 1
                    else:  # exp:
                        ems += val
            totcontpersec[ sec ] = acconts
        acconts = 0
        bolsapersec[ sec ] = round(bolsa2, 2)
        tesouropersec[ sec ] = round(vpms, 2)

    all_persons = all_names_fc()
    PIB_Per_Capita, PIB_Per_Capita_persec, PIB_real, TBF = pibs_fc()


    # Define taxa selic e IPCA de cada seção:
    # LEMBRESE DE SE ATUALIZAR AQUI, TB. ATUALIZAR EM CONTROLES.PY DEF valores
    # Fee per sections (taxa por seções) == Taxa Selic de cada seção)
    feepersec = {}
    tot_fee = 0  # total fee (taxas totais) == soma de todas taxa selic
    # Define VMS, all_sections, all_persons, all_class, tot_pvms, moneypersec
    ipcapersec = {}
    IPCA = 0  # Contabiliza a soma de todos os IPCA
    PIB_Nominal_persec = {}
    PIB_Nominal = 0
    ETF = 0
    ETF_persec = {}
    # moneypersec = dict{Key=str(sect==Seção), Value=float(val== PVMS (valor positivo total em mãos da tal seção)}
    for sect, val in moneypersec.items():
        if val >= 0:  # Caso PVMS seja positivo e maior que zero
            # Cria uma taxa (mas não em porcentagem, sim em número real inteiro absoluto), baseada no valor que a seção tem, menos o que ela Deveria ter (Isto é o IPCA)
            taxa = val - PIB_Per_Capita_persec[sect]
            # E esta taxa é guardada na seção pertencente
            feepersec[sect] = round(taxa, 2)
            # Soma a taxa de desbalanço atual, formando o IPCA mundial
            tot_fee += (taxa / TBF)
            # Então cria o IPCA de cada seção, sendo a taxa dividída peo TBF(que seria a base de cálculo de quantos zeros seria necessário dividir a TAXA, para resultar em um númedo de até 3 casas decimáis (1 a 100)
            ipcapersec[sect] = round(taxa / TBF, 2)
            IPCA += taxa  # Soma a taxa de desbalanço atual, formando o IPCA mundial
            # PIB_Nominal_persec, é o PIB_Per_Capita (pib dividido por quantia de registrados), menos a taxa(que se refere ao o que todos têm- o que deveriam)
            PIB_Nominal_persec[sect] = PIB_Per_Capita_persec[sect] - round(taxa / TBF, 2)
            # PIB_Nominal Mundial então é a soma de todos os pib nominais das seções.
            PIB_Nominal += PIB_Nominal_persec[sect]
            # ETF_persec é a díferença do PIB com inflação para o PIB real sem inflação
            ETF_persec[sect] = ((PIB_Nominal_persec[sect] - PIB_real))
            # ETF Mundial é esta diferença contabilizando todas as seções juntas.
            ETF += ((PIB_Nominal_persec[sect] - PIB_real))
        else:  # Sempre que o PVMS for nulo ou negativo, ele é dado como zero.
            feepersec[sect] = 0
            ipcapersec[sect] = 0
    tot_fee = round(tot_fee, 4)
    tesouro = meta_selic = PIB_real - vms
    pvms = vpms
    # Printa tudo:
    '''print(f"\n registro a ser visto: ATUAL: {dic_reg}\n \n--- VMS (Todo dinheiro do mundo: {vms} ---\n \n--- META SELIC (vms - valor_guardado_no_banco): {tesouro } ---\n \n--- EMS (todo exp do mundo): {ems} ---\n \n--- PVMS (total de valor que cada seção tem, (taxa selic = quanto % a seção representa do VMS)) {vpms} ---\n \n --- Total de store.contas cadastradas: {all_persons.__len__()}\n \n --- Total de Categorias: {all_class.__len__()} ---\n \n --- Total de Seções: {all_sections.__len__()} ---\n"
                 f"\n 	VERIFICAÇÕES:"
                 f"\n > Soma de todos PVMS SEMPRE deve ser igual ao VMS mundial. (Result: Soma: {tot_pvms} VMS: {vms}. É igual?: {'SIM' if tot_pvms == vms else 'NÃO'})"
                 f"\n > Somas de todas as taxas ser = 100: soma: {tot_fee} (result: {tot_fee}. É == 100?: {'SIM' if tot_fee == 100 else 'NÃO'})"
                 f"\n > Meta Selic + VMS, SEMPRE deve ser == {valor_guardado} (result: {tesouro+vms}. É igual?: {'SIM' if (tesouro + vms) == valor_guardado else 'NÃO'})", vms, ems, meta_selic, pvms, all_persons, tot_pvms, tot_fee, all_sections, all_class, moneypersec,
            feepersec, 	tottotcontpersec, bolsa, PIB_Per_Capita_persec, PIB_Per_Capita, IPCA, ipcapersec, bolsapersec,
            tesouro, tesouropersec, vpms, PIB_Nominal, PIB_Nominal_persec, ETF, ETF_persec, accontsdict)'''
    return [vms, ems, meta_selic, pvms, all_persons, tot_pvms, tot_fee, all_sections, all_class, moneypersec,
            feepersec, 	totcontpersec, bolsa, PIB_Per_Capita_persec, PIB_Per_Capita, IPCA, ipcapersec, bolsapersec,
            tesouro, tesouropersec, vpms, PIB_Nominal, PIB_Nominal_persec, ETF, ETF_persec, accontsdict]

values_fc()


RETIRADOS MAIS ANTIGAMENTE:




# Func. De ver valores.
    def valores_func(): 
        log.append("construindo função 'valores'...")
        all_money_list = []
        all_exp_list = []
        all_money = 0
        all_exp = 0
        secao_valores = [] # !
        tot_secoes= 0 #
        cont = 0
        secao_exp = dict() #
        secao_money = dict() #
        lis_money = []
        lis_exp = []
        tot_money = 0 
        tot_exp = 0 
        all_class = 0
        all_indiv = 0 #
        tot_fee = 0 #
        all_pvms = 0
        vpms = dict() #
        #Define VMS, tesouro, all_exp, all_money, all_exp_list, all_money_list:
        for data_reg, list_reinos in dic_reg.items():
            for classes_reino in list_reinos:
                for secao, classes_lis in classes_reino.items():
                    #secao == str(nome da seção)
                    secao_valores.append([secao])
                    tot_secoes += 1
                    for id_of_classes, classe_dict in enumerate(classes_lis):
                        for class_name, contas_lis in classe_dict.items():
                            #class_name == nome da classe da seção
                            all_class += 1
                            for acount_in_class, acount_dict in enumerate(contas_lis):
                                #acount_in_class == num (index) da conta (da classe)
                                for name, balance in acount_dict.items():
                                    #balance == saldo
                                    all_indiv += 1
                                    for indice, value in enumerate(balance):
                                        if value >= 0:
                                            secao_valores[tot_secoes -1].append(value)
                                        if (indice % 2) == 0: #money:
                                            all_money_list.append(value)
                                            all_money += value
                                        else: #exp
                                            all_exp_list.append(value)
                                            all_exp += value
        vms = all_money
        ems = all_exp
        tesouro = valor_mundial - all_money
        print(f"\n{secao_valores} @@@@@\n")
        #bota valores em lis_money e em lis_exp (separa reinos_valores por exp e money)
        for cont, lis in enumerate(secao_valores):
            for num, valor in enumerate(lis):
                #print(num, ">", valor, "###")
                if num != 0:
                    if (num % 2 ) == 0:
                        lis_exp[cont].append(valor)
                    else:
                        lis_money[cont].append(valor)
                else:
                    lis_exp.append([valor])
                    lis_money.append([valor])
        #cria PVMS de money de cada reino:
        for n in range(0, (lis_money.__len__())):
            temp_lis = []
            for n2 in range(0, lis_money[n].__len__()):
                if lis_money[n][n2].__class__() == float():
                    temp_lis.append(lis_money[n][n2])
            secao_money[f"secao{n+1}"] = temp_lis
        #cria PVMS de EXP de cada reino:
        for n in range(0, (lis_exp.__len__())):
            temp_lis = []
            for n2 in range(0, lis_exp[n].__len__()):
                if lis_exp[n][n2].__class__() == float():
                    temp_lis.append(lis_exp[n][n2])
            secao_exp[f"secao{n+1}"] = temp_lis
        #Cria valor absoluto PVMS de cada reino:
        for secao, lis_valores in secao_money.items():
            ryo = 0
            for num, money in enumerate(lis_valores):
                    tot_money += money
                    ryo += money
            print(secao, ">", ryo)
            vpms[f"{secao}"] = [{"pvms": ryo}, {"taxa selic": (ryo / vms * 100)}]
        #VERIFICAÇÕES:
        for secao, secoes in vpms.items():
            for n, var in enumerate(secoes):
                for categoria, valor in var.items():
                    if valor >= 0:
                        if categoria == "taxa selic":
                            tot_fee += valor
                        else:
                            all_pvms += valor
        #tot_fee = round(tot_fee)
        #Printa tudo:
        print(f"\n registro a ser visto: ATUAL: {dic_reg}\n"
                 f"\n--- VMS (Todo dinheiro do mundo: {vms} ---\n",
                 f"\n--- META SELIC (vms - valor_guardado_no_banco): {tesouro } ---\n",
                 f"\n--- EMS (todo exp do mundo): {ems} ---\n"
                 f"\n--- PVMS (total de valor que cada seção tem, (taxa selic = quanto % a seção representa do VMS)) {vpms} ---\n"
                 f"\n --- Total de contas cadastradas: {all_indiv}\n"
                 f"\n --- Total de Categorias: {all_class} ---\n"
                 f"\n --- Total de Seções: {tot_secoes} ---\n"
                 f"\n 	VERIFICAÇÕES:"
                 f"\n > Soma de todos PVMS SEMPRE deve ser igual ao VMS mundial. (Result: Soma: {all_pvms} VMS: {vms}. É igual?: {'SIM' if all_pvms == vms else 'NÃO'})"
                 f"\n > Somas de todas as taxas ser = 100: soma: {tot_fee} (result: {tot_fee}. É == 100?: {'SIM' if tot_fee == 100 else 'NÃO'})"
                 f"\n > Meta Selic + VMS, SEMPRE deve ser == 8500000 (result: {tesouro+vms}. É igual?: {'SIM' if (tesouro + vms) == 8500000 else 'NÃO'})")
        pvms = vpms
        del all_money_list, all_exp_list, all_money,all_exp, secao_valores, cont,  secao_exp,  secao_money, lis_money,  lis_exp,  tot_money, tot_exp, vpms
        return [vms, ems, tesouro, pvms, all_indiv, all_pvms, tot_fee, tot_secoes, all_class]
    valores_func()
    
    
    
      
                    
    #func. que seleciona contas
    def contas_func():
        while True:
            log.append("construindo funcão 'contas_func'...")
            print(f"\nSELECIONE O REINO, EM SEGUIDA A CLASSE PARA ESCOLHER UM INDIVÍDUO!\n")
            #-- criação de vars --#
            time.sleep(1)
            class_var = classes_func()
            nomes = []
            n = 0
            if class_var != None:
                classe_select, classe_value, secao_selected, secao_value, contas_da_classe, data_reg = class_var[0], class_var[1], class_var[2], class_var[3], class_var[4], class_var[5]
                print(dic_reg[data_reg])
                #--- Código ---#
                print(f"\nSelecionado seção e categoria com sucesso. Agora escolha1 qual conta desta categoria você deseja selecionar...\n")
                for n, contas in enumerate(contas_da_classe):
                    for conta, valores in contas.items():
                        print(f"{n} -> Nome: {conta.title()}. Saldo: {valores}")
                        nomes.append(conta)
                #realiza escolha1:
                try:
                    indiv_value = int(input(f"(0 a {n}). Conta número: "))
                except ValueError:
                    print(f"Por favor, use um INT valor numérico inteiro.")
                    continue
                #valida escolha1:
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
                        print(f"Retornado: data_reg: {data_reg}\n	secao_value: {secao_value}\n	secao_selected: {secao_selected}\n	classe_value: {classe_value}\n	classe_select: {classe_select}\n	indiv_value: {indiv_value},\n	indiv_select: {indiv_select}\n	saldo_indiv: {saldo_indiv} ")
                        return [data_reg, secao_value, secao_selected, classe_value, classe_select, indiv_value, indiv_select, saldo_indiv]
                        break
                    else:
                        print(f"Operação cancelada.")
                        return None
                        break
            else:
                print(f"Não foi possível selecionar a classe ou o reino. Tente novamente.")
                continue
    
    


def money_func(din, f=2):
    log.append("construindo função 'money_func'...")
    #Criação de vars:
    lis = []
    cont = 3
    #Tira decimal:
    din2 = int(din)
    # Cria str do valor total sem decimal:
    dinstr = str(din2)
    #Cria str do valor só decimal:
    decimal = str(round(din, f))
    try:
        a = decimal.index(".")
    except ValueError:
        a = -1
    decimal = decimal[a:]
    #Substitui ponto por virgula no decimal:
    decimal = decimal.replace(".", ",")
    #Caso valor negativo, rerira o "menos":
    if din < 0:
        dinstr = dinstr[1:]
    #Vê quantas caracteres tem dinstr:
    len_din = dinstr.__len__()
    #Caso o número nessecite de separação de milhares (seja maior que 999):
    if din > 999 or din < -999:
        dinstr = "%" + dinstr
        for c, v in enumerate(dinstr[-1:0:-1]):
                lis.append(f"{v}")
                cont -= 1
                if cont == 0 :
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
        if din < 0:
            formatado = "-" + formatado
            return formatado + decimal
        else:
            return formatado + decimal
    else:
            if din < 0:
                dinstr = "-" + dinstr
            return dinstr + decimal



VALORES DE 8/JAN/2024:
    
    
#Func de valores
def values_fc():
    log.append("construindo função 'values_fc'...")
    vms = 0
    ems = 0
    all_sections = []
    all_class = []
    all_persons = []
    moneypersec = {} 	#money per sections (grana por seções == PVMS de cada seção)
    tot_pvms = vpms = 0
    feepersec = {} 	#Fee per sections (taxa por seções) == Taxa Selic de cada seção)
    tot_fee = 0 	#total fee (taxas totais) == soma de todas taxa selic
    #Define VMS, all_sections, all_persons, all_class, tot_pvms, moneypersec
    totcontpersec = {}
    acconts = 0
    bolsa = 0
    PIB_Per_Capita_persec ={} 
    PIB_Per_Capita = 0
    feepersec = {} 
    tot_fee = 0
    ipcapersec = {} 
    IPCA = 0
    bolsapersec = {}
    for i in contas:
        for sec, clas_lis in i.items():
            all_sections.append(sec)
            vpms = 0
            bolsa2 = 0
            for clas_dic in clas_lis:
                for classe, accounts_lis in clas_dic.items():
                    all_class.append(classe)
                    for cont in accounts_lis:
                        for name, values_lis in cont.items():
                            all_persons.append(name)
                            acconts += 1
                            for pos, val in enumerate(values_lis):
                                if pos == 0: #ryo
                                    if val > 0:
                                        vms += val
                                        vpms  += val
                                        tot_pvms += val
                                    elif val < 0:
                                        bolsa -= val
                                        bolsa2 -= val
                                else: #exp:
                                    ems += val
            moneypersec[sec] = round(vpms, 2)
            totcontpersec[sec]  = acconts 
            bolsapersec[sec] = round(bolsa2, 2)
            acconts = 0
    #define PIB_Per_Capita_persec 
    for i in contas:
        for sec, clas_lis in i.items():
            for clas_dic in clas_lis:
                for classe, accounts_lis in clas_dic.items():
                    for cont in accounts_lis:
                        for name, values_lis in cont.items():
                            acconts += 1
            if acconts >= 2:
                PIB_Per_Capita_persec[sec] = round(PIB_real / acconts, 2) 
            elif acconts <= 1: 
                PIB_Per_Capita_persec[sec] = round(PIB_real / all_persons.__len__(), 2)
            acconts = 0 
    #Define taxa selic e IPCA de cada seção:
    for sect, val in moneypersec.items():
            if val >= 0:
                taxa = round(val - PIB_Per_Capita_persec[sect], 2)
                feepersec[sect] = (taxa)
                tot_fee += (taxa)
                ipcapersec[sect] = round(taxa / 100000, 2)
                IPCA += taxa
            else:
                feepersec[sect] = 0
                ipcapersec[sect] = 0
    tot_fee = round(tot_fee, 4)
    tesouro = valor_guardado - vms
    #calcula PIB_Per_Capita:
    for k, v in PIB_Per_Capita_persec.items():
        PIB_Per_Capita += v
    #Printa tudo:
    '''print(f"\n registro a ser visto: ATUAL: {dic_reg}\n \n--- VMS (Todo dinheiro do mundo: {vms} ---\n \n--- META SELIC (vms - valor_guardado_no_banco): {tesouro } ---\n \n--- EMS (todo exp do mundo): {ems} ---\n \n--- PVMS (total de valor que cada seção tem, (taxa selic = quanto % a seção representa do VMS)) {vpms} ---\n \n --- Total de contas cadastradas: {all_persons.__len__()}\n \n --- Total de Categorias: {all_class.__len__()} ---\n \n --- Total de Seções: {all_sections.__len__()} ---\n"
                 f"\n 	VERIFICAÇÕES:"
                 f"\n > Soma de todos PVMS SEMPRE deve ser igual ao VMS mundial. (Result: Soma: {tot_pvms} VMS: {vms}. É igual?: {'SIM' if tot_pvms == vms else 'NÃO'})"
                 f"\n > Somas de todas as taxas ser = 100: soma: {tot_fee} (result: {tot_fee}. É == 100?: {'SIM' if tot_fee == 100 else 'NÃO'})"
                 f"\n > Meta Selic + VMS, SEMPRE deve ser == {valor_guardado} (result: {tesouro+vms}. É igual?: {'SIM' if (tesouro + vms) == valor_guardado else 'NÃO'})")'''
    pvms = vpms
    return [vms, ems, tesouro, pvms, all_persons, tot_pvms, tot_fee, all_sections, all_class, moneypersec, feepersec, totcontpersec, bolsa, PIB_Per_Capita_persec, PIB_Per_Capita, IPCA, ipcapersec, bolsapersec]

#values_fc() 	


    
   . 
"""
