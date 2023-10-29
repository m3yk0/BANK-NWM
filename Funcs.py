# Imports Bib. padroes:
import datetime
import sys
from os import system as osys
import os
from typing import List, Union, Dict
# Imports Bib. terceiros:
# Imports Bib. Local:
from controles import contas, backups, data_reg, historico, reinantes, valor_mundial, valor_guardado, lideres, dic_reg, avisos, i, log, start, all_persons, all_sections
    
global contas, backups, data_reg, historico, reinantes, valor_mundial, valor_guardado, lideres, dic_reg, avisos, i, log, start


# Func. de confirmação
def confirm():
        log.append("construindo função 'confirm'...")
        try:
            confirmation: str = str(input("[S/N]: ")).strip().upper()
        except:
            print(f"Erro. Confirmação taxada como negativa.")
            return False
        confirms = ["S", "SIM", "Y", "YES", "AFIRMATIVO", "CLARO", "EXATO", "SS", "POSITIVO", "TRUE", "1"]
        negacoes = ["N", "NAO", "NÃO", "NN", "NEGATIVO", "SAIR", "CANCELAR", "FALSO", "FALSE", "-1", "0"]
        if confirmation in confirms:
            print(f"Confirmado operação com sucesso.\n")
            return True
        elif confirmation in negacoes:
            print(f"Operação negada com sucesso.\n")
            return False
        else:
            print(f"Opção inválida. Confirmação taxada como negativa.\n")
            return False


# Func de alternariva
def alternativa(i):
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

#Func. de botar plural
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
    	if mod == 0: #Upper
    			letra = letra.upper()
    	elif mod == 1:
    		letra = letra.lower()
    	return letra
global letra
    	
# ver data
def atual_data() -> object:
        log.append("obtendo data atual...")
        data = str(datetime.date.today())
        ano, mes, dia = data[0:4], data[5:7], data[8:]
        hr = str(datetime.datetime.now())[11:19]
        data_atual = f"{dia}/{mes}/{ano}-{hr}"
        del hr, ano, mes, data
        return data_atual
atual_data()
global data_atual, data
    
    	
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
    	
#Func. de botar zero atrás.
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
global zero_


#Func. de definir data
def programar_data():
        log.append("construindo função 'programar_data'...")
        while True:
            #--- Delcaração de Vars. ---#
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
            #--- Código: ---#
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
                if (meses+dias) > 0: #Só define horário caso não deja definido dias.
                	horas = 0
                	minutos = 0
                	segundos = 0
                	min_novo, h_novo, s_novo = 0, 0, 0
                else:
                      horas = int(input(f"Em quantas horas quer realizar a operação?: "))
                      if horas <= -1:
                      	print(f"Usado valor negativo. Operação cancelada.")
                      	return False
                      	break
                      minutos = int(input(f"Em quantos minutos quer realizar a operação?: "))
                      if minutos <= -1:
                      	print(f"Usado valor negativo. Operação cancelada.")
                      	return False
                      	break
                      segundos = int(input(f"Em quantos segundos quer realizar a operação?: "))
                      if segundos <= -1:
                      	print(f"Usado valor negativo. Operação cancelada.")
                      	return False
                      	break
            except ValueError:
                print(f"Valor incorreto. Operação cancelada.")
                break
                return False
            if (meses+dias+horas+segundos+minutos) == 0:
               	 print(f"Você não pode programar algo para daqui há 0 instantes. Operação cancelada.")
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
	                		meses +=1
	                	if meses >= 13:
	                		meses -= 12
	                		anos += 1
	                print(f"\nA operação ocorrerá daqui há: {dias} dia{plural(dias, 1)}, {meses} {'meses' if meses != 1 else 'mês'} e {anos} ano{plural(anos, 1)}. E {zero(horas)}{horas}:{zero(minutos)}{minutos}:{zero(segundos)}{segundos} horas (h:m:s).")
	                print(f"\nData e hora atual: {d_atual}/{mes_atual}/{a_atual} (d/m/a). {zero(h_atual)}{h_atual}:{zero(min_atual)}{min_atual}:{zero(s_atual)}{s_atual} (h:m:s). \nA OPERAÇÃO OCORRERÁ EM: ", end="")
	                # Descobre que dia do calendário os valores darão:
	                d_novo += dias
	                mes_novo += meses
	                a_novo += anos
	                s_novo += segundos
	                min_novo += minutos
	                h_novo += horas
	                for n in range(0, (d_novo + mes_novo +a_novo + s_novo + min_novo + h_novo)):
	                	if s_atual >= 60:
	                		s_novo -= 60
	                		min_novo += 1
	                	if min_novo >= 60:
	                		min_novo -= 60
	                		h_novo += 1
	                	if h_novo >= 24:
	                		h_novo -=24
	                		d_novo  += 1
	                	if d_novo >= 32:
	                		d_novo -=32
	                		mes_novo += 1
	                	if mes_novo >= 13:
	                		mes_novo -= 13
	                		a_novo += 1
	                #verifica ultimo dia do mes:
	                info_data = calendar.monthrange(a_novo, mes_novo)[1]
	                ultimo_d_do_mes = int(str(info_data))
	                # retira dias até estar de acordo com o último dia do mês.
	                for n in range(0, d_novo):
	                	if d_novo > ultimo_d_do_mes:
	                		d_novo -= 1
	                #Valida a data
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

#Func. de impedir erro de index ou chaves 
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
			
#Func. de impedir erro de index ou chaves 
def tryline(cod):
	log.append("construindo função 'tryline'...")
	try:
		return cod
	except KeyError:
			return None
			
			
#Func. de converter valor em forma mometária
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


#func. de iterar numa só linha.
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
	
	
#Func. de recortar qualquer container.
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
	

#transformar valor em decimal:
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
	
	

#Func de valores
def values_fc():
	log.append("construindo função 'values_fc'...")
	vms = 0
	ems = 0
	all_sections = []
	all_class = []
	all_persons = []
	moneypersec = {} 	#money per sections (grana por seções == PVMS de cada seção)
	tot_vpms = vpms = 0
	feepersec = {} 	#Fee per sections (taxa por seções) == Taxa Selic de cada seção)
	tot_fee = 0 	#total fee (taxas totais) == soma de todas taxa selic
	#Define VMS, all_sections, all_persons, all_class, tot_pvms, moneypersec	
	for i in contas:
		for sec, clas_lis in i.items():
			all_sections.append(sec)
			vpms = 0
			for clas_dic in clas_lis:
				for classe, accounts_lis in clas_dic.items():
					all_class.append(classe)
					for cont in accounts_lis:
						for name, values_lis in cont.items():
							all_persons.append(name)
							for pos, val in enumerate(values_lis):
								if pos == 0: #ryo
									if val > 0:
										vms += val
										vpms  += val
										tot_vpms += val
								else: #exp:
									ems += val
			moneypersec[sec] = vpms
	#Define taxa selic de cada seção:
	for sect, val in moneypersec.items():
		feepersec[sect] = (vms * decim_fc(val))
		if vms != 0 and val != 0:
			tot_fee += (val / vms * 100)
	tot_fee = round(tot_fee, 4)
	meta_selic = valor_guardado - vms
	#Printa tudo:
	"""print(f"\n registro a ser visto: ATUAL: {dic_reg}\n \n--- VMS (Todo dinheiro do mundo: {vms} ---\n \n--- META SELIC (vms - valor_guardado_no_banco): {meta_selic } ---\n \n--- EMS (todo exp do mundo): {ems} ---\n \n--- PVMS (total de valor que cada seção tem, (taxa selic = quanto % a seção representa do VMS)) {vpms} ---\n \n --- Total de contas cadastradas: {all_persons.__len__()}\n \n --- Total de Categorias: {all_class.__len__()} ---\n \n --- Total de Seções: {all_sections.__len__()} ---\n"
                 f"\n 	VERIFICAÇÕES:"
                 f"\n > Soma de todos PVMS SEMPRE deve ser igual ao VMS mundial. (Result: Soma: {tot_vpms} VMS: {vms}. É igual?: {'SIM' if tot_vpms == vms else 'NÃO'})"
                 f"\n > Somas de todas as taxas ser = 100: soma: {tot_fee} (result: {tot_fee}. É == 100?: {'SIM' if tot_fee == 100 else 'NÃO'})"
                 f"\n > Meta Selic + VMS, SEMPRE deve ser == {valor_guardado} (result: {meta_selic+vms}. É igual?: {'SIM' if (meta_selic + vms) == valor_guardado else 'NÃO'})")"""
	pvms = vpms
	return [vms, ems, meta_selic, pvms, all_persons, tot_vpms, tot_fee, all_sections, all_class, moneypersec, feepersec]


# func. Mostra Backup Registros:
def backups_fc(var=str(None), date=str(None)) -> object:
        log.append("construindo função 'backups_fc'...")
        while True:
            passe = None
            guardados = []
            for variavel, content in backups.items():
	            	guardados.append(variavel)
            print(guardados)
            #Caso instância var não definida:
            if var == str(None):
	            # Mostra registros:
	            print(f"Itens guardados no backup: ")
	            for cont, variavel in enumerate(guardados):
	            	print(f"{'':^5}    {'-':-^25}")
	            	print(f"[{cont:^5}]: ¦ {variavel:^20} ", end=" ¦\n")
	            print(f"{'':^5}    {'-':-^25}")
	            es = str(input(f"Qual dos itens quer resgatar? (escreva o nome) ")).lower().strip()
	            if es not in guardados:
		            	print(f"Nome inválido. Tente novamente")
		            	passe = False
	            else:
		            	passe = True
		        #caso verificações conote False como erro: reinicia
	            if passe == False:
	             	continue
            #caso instância var definida:
            if var != str(None):
	            es = str(var)
	            passe = True
            if passe == True:
	            cont = 0
	            cont_data = dict()
	            dts = []
	            conts = []
	            #Caso instância date definida:
	            if date != str(None):
		            #-- Mostra Datas Salvas p. escolher --#
		            for Data, arquiv in backups[f"{es}"].items():
					                 	dts.append(Data)
					                 	cont_data[cont] = Data
					                 	conts.append(cont)
					                 	if Data == date:
					                 		break
					                 	cont += 1
		            es2 = cont
		            conf = True
		        #Caso instância date não definida:
	            elif date == str(None):
	                print(f"Você selecionou a variável: {es}. para ser restaurada. \nEscolha qual das datas salvas será o ponto de recuperação...\n	Pontos de restauração disponíveis:")
	                for Data, arquiv in backups[f"{es}"].items():
			                 	print(f"{cont} > {Data = } ")
			                 	cont_data[cont] = Data
			                 	dts.append(Data)
			                 	conts.append(cont)
			                 	cont += 1
	                conts = tuple(conts)
	                dts = tuple(dts)
	                es2 = cont = int(input(f"Escolha o número: "))
	            #-- Valida escolha --#
	            if es2 in conts:
	            	es2 = dts[es2]
	            	if var == str(None) and date == str(None):
	            		print(f"Você selecionou: {es} com data: {cont_data[cont]}. Confirma?")
	            		conf = confirm()
	            	else:
	            		conf = True
	            	if conf is True:
			                 		if es == 'contas':
			                 			contas = backups[es][es2]
			                 			if var == str(None) and date == str(None):
			                 				print(f"Deseja também importar os avisos, líderes, reinantes e valor_guardado deste registro? [S/N]")
			                 				decision = confirm()
			                 			else:
			                 				decision = True
			                 			if decision == True:
			                 				global avisos_2, lideres_2, reinantes_2, valor_mundial_2
			                 				avisos_2 = backups_fc('avisos', es2)
			                 				avisos = avisos_2[0]
			                 				lideres_2 = backups_fc('lideres', es2)
			                 				lideres = lideres_2[0]
			                 				reinantes_2 = backups_fc('reinantes', es2)
			                 				reinantes = reinantes_2[0]
			                 				valor_mundial_2 = backups_fc('valor_mundial', es2)
			                 				valor_mundial = valor_mundial_2[0]
			                 		elif es == 'lideres':
			                 			lideres = backups[es][es2]
			                 		elif es == 'reinantes':
			                 			 reinantes = backups[es][es2]
			                 		elif es == 'avisos':
			                 			avisos = backups[es][es2]
			                 		elif es == 'valor_mundial':
			                 			valor_mundial = backups[es][es2]
			                 		else:
			                 			print(f"Não foi indexado no código, a variável selecionada. Por favor, faça a correção.")
			                 			break
			                 		#--- Flag ---#
			                 		if var != str(None) and date != str(None):
			                 			print("Backup selecionado com sucesso.")
			                 		return [backups[es][es2], es, es2, dts[es2]]
			                 		break
	            	elif conf is False:
			                 			print(f"Operação cancelada.")
			                 			return None
			                 			break
	            elif es2 not in conts:
	            	print(f"Não foi possível localizar o ponto de restauração. Operação cancelada.")
	            	return None
	            	break
#Verifica e seleciona registros de pontos novos ou anteriores.
def regselect_fc(pos='antigo'):
    len_backup = backups['contas'].__len__()
    global regist, registro, var_selecionada, data_select, b_r
    if len_backup <= 1 or pos == 'novo':
                    print(f"\nVocê verá o registro atual.\n")
                    # Caso não tenha reg. antigo: b_r == registro atual
                    b_r = dic_reg
                    # Define a variavel data de b_r
                    for data, reg in b_r.items():
                        registro = reg
                    data_select= data
                    caiu_em = 'novo'
                    return [caiu_em, b_r, data_select]
    if len_backup >= 2:
                    print(f"\nHá registros antigos salvos. Você pode selecionar qual registro salvo deseja ver...\n")
                    # Seleciona qual registro quer ver
                    regist = backups_fc('contas')
                    registro, var_selecionada, data_select = regist[0], regist[1], regist[2]
                    caiu_em = 'antigo'
                    b_r = registro
                    return [caiu_em, b_r, data_select]
            	
            	
#Func. ver magnatas:
def magnatas_fc(see="antigo"):
        log.append("construindo função 'magnatas_fc()'...")
        global sort_money, sort_exp
        data_atual = atual_data()
        # -- Código --#
        sort_money = {}
        sort_exp = {}
        cont = 0
        magnatas_m = []
        b = regselect_fc(see)
        if b != None:
        	caiu_em, b_r, data_select = b
        	for data_reg, list_reinos in b_r.items():
                  for classes_reino in list_reinos:
                  	for secao, classes_lis in classes_reino.items():
                  		for id_of_classes, classe_dict in enumerate(classes_lis):
                  			for class_name, contas_lis in classe_dict.items():
                  				#class_name == nome da classe da seção
                  				for acount_in_class, acount_dict in enumerate(contas_lis):
                  					#acount_in_class == num (index) da conta (da classe)
                  					for nome, tributos in acount_dict.items():
                  					     for num, valor in enumerate(tributos):
                  					     	if (num % 2) == 0:  # money:
                  					     		sort_money[nome] = round(valor, 2)
                  					     	else:  # exp:
                  					     		sort_exp[nome] = round(valor, 1)
        	sort_money = dict(sorted(sort_money.items(), key=lambda x: x[1], reverse= True))  # lambda k:v = key: value [1] = select value
        	sort_exp = dict(sorted(sort_exp.items(), key=lambda x: x[1], reverse= True))
        	"""print(f"Retornado: SORT_MONEY: {sort_money}\n\n SORT_EXP: {sort_exp},\n\n")"""
        	return sort_money, sort_exp
        elif b == None:
            	print(f"Magnatas_fc(): Não foi possível selecionar o registro a ser visto de regselect_fc(). Operação cancelada.")
            	return None


#Func. que seleciona seções.
def secoes_func():
    	log.append(f"construindo funcão 'secoes_func()'...")
    	while True:
    	       global all_secoes, classes_por_secao, secao_value, secao_selected, data_reg, classes_list, secao_reg
    	       #-- declaração de vars. --#
    	       all_secoes = []
    	       classes_por_secao = []
    	       classes_list = []
    	       persons_sec = {}
    	       #-- código --#
    	       print(f" LISTAGEM DAS SESSÕES: ")
    	       for data_reg, list_secoes in dic_reg.items():
    	           for num, secoes in enumerate(list_secoes):
    	               for secao, classes  in secoes.items():
    	               	all_secoes.append(secao)
    	               	print(f"\nOPÇÃO: ~ {num}:  -=-=-=->  {secao.upper()}  <-=-=-=-")
    	               	print(f"Categorias desta seção:")
    	               	classes_por_secao.append([secao])
    	               	classes_list.append([secao])
    	               	for n, classe_dict in enumerate(classes):
                	   		classes_por_secao[num].append(classe_dict)
                	   		for cla, conts in classe_dict.items():
                	   			print(f" {n} - {cla.title()}")
                	   			classes_list[num].append(cla)
                	   			for names_dic in conts:
                	   				for names_lis in names_dic.items():
                	   					for name in names_lis:
                	   						persons_sec[secao] = name
    	       try:
    	           #Seleciona reino:
                   secao_value = int(input(f"\nQual seção quer selecionar? 0 até {num}: "))
    	       except ValueError:
    	           print(f"Erro de valor. Tente novamente")
    	           continue
    	       if secao_value > num or secao_value < 0:
    	       	print(f"Você não digitou um valor entre o intervalo 0 a {num}. Tente novamente.")
    	       	continue
    	       else: #caso tudo certo, código continua:
    	       	secao_selected = all_secoes[secao_value]
    	       	print(f"\n A seção selecionado foi: {secao_selected.title()}. Confirma? ")
    	       	secao_reg = dic_reg[data_reg][secao_value]
    	       	conf = confirm()
            	if conf == True:
            		"""print(f"Retornado: [all_secoes: {all_secoes},\n classes_por_secao, {classes_por_secao},\n secao_value: {secao_value},\n secao_selected: {secao_selected},\n data_reg: {data_reg},\n classes_list: {classes_list},\n secao_reg: {secao_reg}]")"""
            		del conf
            		return [all_secoes, classes_por_secao, secao_value, secao_selected, data_reg, classes_list, secao_reg, persons_sec]
            	else:
            		print(f"Operação cancelada.")
            		return None
            		break


# func. que  mostra classes (categorias).
def classes_func():
        log.append("construindo função 'classes_func'...")
        while True:
            #-- código --#
            print(f"\nVocê selecionará primeiro a seção, em seguida a classe...\n")
            secao_var = secoes_func()
            if secao_var != None:
	            all_secoes, classes_por_secao, secao_value, secao_selected, data_reg, classes_list = secao_var[0], secao_var[1], secao_var[2], secao_var[3], secao_var[4], secao_var[5]
	            print(f"\n LISTAGEM CATEGORIAS DE {secao_selected.upper()}:")
	            cont = 0
	            for n, classes in enumerate(classes_por_secao[secao_value]):
	            		if n != 0:
	            			for classe, contas_lis in classes.items():
	            				print(f"\nOPÇÃO {n}: --> {classe.upper()}", end="")
	            				cont += 1
	            #Seleciona classe:
	            try:
	            			classe_value = int(input(f"\n (1 a {cont}). Classe número: ")) - 1
	            except ValueError:
		            		print(f"\nValor incorreto. Favor digitar um número adequado a circunstância. Tente novamente.")
		            		continue
		            	# -- valida a escolha --#
	            if classe_value > (n) or classe_value < 0:
		                	print(f"\n Usuário não encontrado, tente novamente.")
		                	continue
	            else:
		            	   	classe_select = classes_list[secao_value][classe_value +1]
		            	   	contas_da_classe = classes_por_secao[secao_value][classe_value+1][classe_select]
		            	   	print(f"Você selecionou: {classe_select.title()}, da seção: {secao_selected.title()}. Confirma?")
		            	   	conf = confirm()
		            	   	if conf == True:
		            	   	   # count_selected = dic_reg[data_reg][0][secao_selected][indiv]
		            	   	    """print(f"Retornado:", f"classe_select' {classe_select}.\n secao_selected: {secao_selected}.\n classe_value: {classe_value}.\n secao_value: {secao_value}. \n contas_da_classe: {contas_da_classe}.\n")"""
		            	   	    print(f"Seleção de classe bem-sucedida.")
		            	   	    #dic_reg[data_reg][1]["reino da folha"][1]["inu"]
		            	   	    reg_classe = dic_reg[data_reg][secao_value][secao_selected][classe_value]
		            	   	    return [classe_select, classe_value, secao_selected, secao_value, contas_da_classe, data_reg, reg_classe]
		            	   	else:
		            	   		print(f"Operação cancelada.")
		            	   		return None
		            	   		break
            else: #caso reino_var == None:
            	print(f" Seção não pôde ser selecionado. Operação cancelada.")
            	return None


#func. que seleciona contas em seleção manual de reino e classs.
def contas_func():
     	while True:
	     	log.append("construindo funcão 'contas_func'...")
	     	print(f"\nSELECIONE O REINO, EM SEGUIDA A CLASSE PARA ESCOLHER UM INDIVÍDUO!\n")
	     	#-- criação de vars --#
	     	class_var = classes_func()
	     	nomes = []
	     	n = 0
	     	if class_var != None:
	     		classe_select, classe_value, secao_selected, secao_value, contas_da_classe, data_reg = class_var[0], class_var[1], class_var[2], class_var[3], class_var[4], class_var[5]
	     		print(dic_reg[data_reg])
	     		#--- Código ---#
	     		print(f"\nSelecionado seção e categoria com sucesso. Agora escolha qual conta desta categoria você deseja selecionar...\n")
	     		for n, contas in enumerate(contas_da_classe):
	     			for conta, valores in contas.items():
	     				print(f"{n} -> Nome: {conta.title()}. Saldo: {valores}")
	     				nomes.append(conta)
	     		#realiza escolha:
	     		try:
	     			indiv_value = int(input(f"(0 a {n}). Conta número: "))
	     		except ValueError:
	     			print(f"Por favor, use um INT valor numérico inteiro.")
	     			continue
	     		#valida escolha:
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
     			

#function for  person selection to automatic selection of section and class.
def account_fc():
	log.append("construindo função 'account_fc'...")
	while True:
		log.append('construíndo func. account_fc().')
		global i_sec, sect, i_cla, classe, i_con
		lis_br = []
		all_accounts = []
		cont = 0
		print(f"Reinos e classes a serem vistas:")
		#i_sec, sect, i_cla, classe, i_con = None
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
									lis_br.append([date, i_sec, sect, i_cla, classe, i_con, name])
		try:
			pp_value = int(input(f"Digite o número do indivíduo: "))
		except ValueError:
			print(f"Por favor, digite um valor numérico de 0 a {cont}. Tente novamente.")
			continue
		intervalo = [ i for i in range(0, cont)]
		if pp_value in intervalo:
			pp_select = all_accounts[pp_value]
			lis_br = lis_br[pp_value+1]
			data, i_sec, sect, i_cla, classe, i_con, name = lis_br[0], lis_br[1], lis_br[2], lis_br[3], lis_br[4], lis_br[5], lis_br[6]
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
			print(f"Não foi encontrado conta número {pp_value}. Tente novamente.")
			continue
		
			
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
            print(f"\n\n----Esse foi o histórico. Para resetar, escolha opção 7.----")
            z = end = True
            return None
            

#VER SEÇOES:
def sectsee_fc():
	print(f"SEÇÕES CADASTRADAS:")
	c = 0
	for date, sect_dict in dic_reg.items():
	                	for sect_lis in sect_dict:
	                		for i, sect in enumerate(sect_lis):
	                			print(f"\n- {c} > ¦ {sect.upper():.^30} ¦")
	                			c += 1
	
"""# Func. De ver valores.
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
        tot_class = 0
        all_indiv = 0 #
        all_taxas = 0 #
        all_pvms = 0
        vpms = dict() #
        #Define VMS, meta_selic, all_exp, all_money, all_exp_list, all_money_list:
        for data_reg, list_reinos in dic_reg.items():
            for classes_reino in list_reinos:
                for secao, classes_lis in classes_reino.items():
                	#secao == str(nome da seção)
                	secao_valores.append([secao])
                	tot_secoes += 1
                	for id_of_classes, classe_dict in enumerate(classes_lis):
                		for class_name, contas_lis in classe_dict.items():
                			#class_name == nome da classe da seção
                			tot_class += 1
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
        meta_selic = valor_mundial - all_money
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
        					all_taxas += valor
        				else:
        					all_pvms += valor
        #all_taxas = round(all_taxas)
        #Printa tudo:
        print(f"\n registro a ser visto: ATUAL: {dic_reg}\n"
                 f"\n--- VMS (Todo dinheiro do mundo: {vms} ---\n",
                 f"\n--- META SELIC (vms - valor_guardado_no_banco): {meta_selic } ---\n",
                 f"\n--- EMS (todo exp do mundo): {ems} ---\n"
                 f"\n--- PVMS (total de valor que cada seção tem, (taxa selic = quanto % a seção representa do VMS)) {vpms} ---\n"
                 f"\n --- Total de contas cadastradas: {all_indiv}\n"
                 f"\n --- Total de Categorias: {tot_class} ---\n"
                 f"\n --- Total de Seções: {tot_secoes} ---\n"
                 f"\n 	VERIFICAÇÕES:"
                 f"\n > Soma de todos PVMS SEMPRE deve ser igual ao VMS mundial. (Result: Soma: {all_pvms} VMS: {vms}. É igual?: {'SIM' if all_pvms == vms else 'NÃO'})"
                 f"\n > Somas de todas as taxas ser = 100: soma: {all_taxas} (result: {all_taxas}. É == 100?: {'SIM' if all_taxas == 100 else 'NÃO'})"
                 f"\n > Meta Selic + VMS, SEMPRE deve ser == 8500000 (result: {meta_selic+vms}. É igual?: {'SIM' if (meta_selic + vms) == 8500000 else 'NÃO'})")
        pvms = vpms
        del all_money_list, all_exp_list, all_money,all_exp, secao_valores, cont,  secao_exp,  secao_money, lis_money,  lis_exp,  tot_money, tot_exp, vpms
        return [vms, ems, meta_selic, pvms, all_indiv, all_pvms, all_taxas, tot_secoes, tot_class]
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
	     		print(f"\nSelecionado seção e categoria com sucesso. Agora escolha qual conta desta categoria você deseja selecionar...\n")
	     		for n, contas in enumerate(contas_da_classe):
	     			for conta, valores in contas.items():
	     				print(f"{n} -> Nome: {conta.title()}. Saldo: {valores}")
	     				nomes.append(conta)
	     		#realiza escolha:
	     		try:
	     			indiv_value = int(input(f"(0 a {n}). Conta número: "))
	     		except ValueError:
	     			print(f"Por favor, use um INT valor numérico inteiro.")
	     			continue
	     		#valida escolha:
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
    
"""

    	