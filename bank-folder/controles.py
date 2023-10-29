
from Intercal import decim_fc

global contas, backup_registros, data_reg, historico, reinantes, valor_mundial, valor_guardado, lideres, dic_reg, avisos, i, log, start

i = 0
log = list()
start = True
					
contas =  [
 	{"contas em conjunto/NPC": [ 
 		{"times": [ 
 			  {"devs~": [180980.0, 1.0]},
    	  	 {"iluminati": [0.0, 0.0]},
    	  	 {"yamata": [90000.0, 0.0]}
 		]}, 
 		{"npcs": [ 
 			{"Okyem Kurai": [2500.0, 0.0]},
    		 {"Chaos Kurai": [2500.0, 0.0]},
   	 	 {"Yu Hokori": [2500.0, 0.0]} ]}
 	]},
	 {"reino da folha": [ 
	 	{"tsuki": [
	 			{"Susumo Tsuki": [420073.00, 393.0] },
	    		{"Mahina Tsuki": [59694.00, 64.5]},
	    		{"Norushige Tsuki": [30.0, 5.0]} 
	   ]},
	 	{"inu": [ {"Meeh Inu": [847.00, 847.0]} ] },
	 	{"ivory": [ 
	 				{"Meyko Ivory": [1319420.0, 1239.0]},
	    			{"Meyko Ivory 2045 - (1.710.466, 956,5)": [0.0, 0.0]},
	    			{"Leandro Ivory": [-17500.0, -25.0]},
	   		 	{"Broca Ivory": [-970.0, -1.0]},
	  		  	{"Alackbaki Ivory": [970.0, 1.0]},
	    			{"Zaraky Ivory": [3524.0, 11.5]} 
	    ] },
	 	{"zuky": [
	 			   {"Yu Zuky": [346992.0, 157.5]},
	  		  	{"Dexter Zuky": [0.0, 5.0]},
	    			{"Sora Zuky": [230.0, 8.0]},
	   		 	{"Mika Zuky": [30.0, 5.0]},
			    	{"Ryle Zuky": [23.0, 5.0]}
	    ] }, 
	    {"shiro": [ {"Tioo Shiro": [24.0, 5.0] } ] },
	 	{"uzuki": [ {"Naomi Uzuki": [1130646.0, 780.5]}
	 	 ] }
	 ]},
	 {"reino da chuva": [ 
		 {"runbon": [
		 	 {"Shi Runbon": [3000.0, 6.0] },
    		{"Arlokis Runbon": [0.0, 5.0] },
  	  	{"Shinobu Rubon": [0.0, 5.0]}
		  ] },
	 	 {"senko": [ 
	 		 {"Korin Senko": [24.0, 5.0]}
	 	 ] }, 
	 	 {"kurai": [
	 	 	{"Maja Kurai": [10000.0, 10.0]}
	 	 ] }
	 ]},
	 {"reino do som": [ 
		  {"akaguma": [ 
		 	 {"Chaos Kaguya Akaguma": [638868.0, 512.0] }, 
  	  	 {"Ishikawa Akaguma": [39790.00, 65.5] }
		   ] },
	 	 {"yoso": [ 
	 	   	{"Ki Yoso": [0.00, 5.0]},
  	 	 	{"Sophia Yoso": [0.0, 5.0]}
	 	   ] }, 
	 	 {"terepasu": [ 
	 	 	{"Dante Sparda Terepasu": [0.00, 5.0]} 
	 	 ] }
	 ]},
	 {"reino da nevoa": [ 
	 	{"kori": [ {"Hrymir Kori": [-1000.0, -1.0] } ] }
	 ]}
 ]


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
	tot_fee += (val / vms * 100)

tot_fee = round(tot_fee, 4)

valor_mundial = valor_guardado = 8500000 # Valor mundial é como se fosse o PIB. É o total do valor que pode cair em mãos.

meta_selic = (valor_mundial - vms)

classes_c2 = [
{"contas em conjunto/NPC": ["times", "npcs"],
"reino da folha": ["tsuki", "inu", "ivory", "zuky", "uzuki", "shiro"], 
"reino do som": ["akaguma", "yoso", 'terepasu', 'kokyo'],
"reino da chuva": ["kieta", 'runbon', 'senko', 'kurai'],
"reino da nevoa": ['kori', "same", "shio"], 
"reino da areia": ["sanzu", "hokori", "mushi"]}]

data_reg = "11/07/2023-02:09:01"

dic_reg = {data_reg: contas}  # registro atual

avisos: list[dict[str]] = [{"avisos de atualizacoes":	 {data_reg: "None"}}, {"avisos gerais": {data_reg: "None"}}]  # Avisos[0 = Avisos de mudança[data]] [1 = Avisos gerais[data]

historico = list()  # histórico de funções usadas.

reinantes = {"reino da folha": "Meyko Ivory"}

leis = {"reino da folha": "Ativas"}

lideres = {"tsuki": "Susumo Tsuki",
     "inu": "Meeh Inu", 
     "ivory": "Meyko ivory", 
     "zuky": "Yu Zuky", 
     "uzuki": "None", 
     "shiro": "None",
     "akaguma": "Chaos Kaguya",
     "terepasu": "None",
     "yoso": "None",
     "kokyu": "None", 
     "kieta": "None", 
     "runbon":"None", 
     "kurai":"None", 
     "senko":"None", 
     "kori":"None", 
     "same":"None", 
     "shio":"None"}
     
backups = {
"contas": 
	{"11/07/2023-02:09:01": (contas.copy())},
"lideres":  {"11/07/2023-02:09:01": (lideres.copy())},
"reinantes": {"11/07/2023-02:09:01": (reinantes.copy())},
"avisos": {"11/07/2023-02:09:01": (avisos.copy())},
"valor_mundial": {"11/07/2023-02:09:01": (valor_mundial)}
}


#Caso adicione mais categorias no backup, lembre-se de mudar a func backups_fc de Banco.py.


"""
list[
	dict(list[
		dict(list[]),
		dict(list[]) ] ),
	dict(list[
		dict(list[
			dict() ] ) ] ), 
	dict(list[	
		dict(list[
			dict() ] ) ] ),
	dict(list[
		dict(
			dict() ] ), 
	dict(list[
		dict() ] ) 
					]

contas = [ 
    {"contas em conjunto/NPC":
    	 [{"times": [
    	 	  {"devs~": [180980.0, 1.0]},
    	  	 {"iluminati": [0.0, 0.0]},
    	  	 {"yamata": [90000.0, 0.0]} ] },
    	 {"npcs": [
    		 {"Okyem Kurai": [2500.0, 0.0]},
    		 {"Chaos Kurai": [2500.0, 0.0]},
   	 	 {"Yu Hokori": [2500.0, 0.0]} ] }
    	] },
    {"reino da folha": 
	    [ {"tsuki": [
	    	 	{"Susumo Tsuki": [420073.00, 393.0] },
	    		{"Mahina Tsuki": [59694.00, 64.5]},
	    		{"Norushige Tsuki": [30.0, 5.0]} ] },
	 	{"inu": [
	 	  	{"Meeh Inu": [847.00, 847.0]} ] },
		{"ivory": [
	    	{"Meyko Ivory": [1319420.0, 1239.0]},
	    	{"Meyko Ivory 2045 - (1.710.466, 956,5)": [0.0, 0.0]},
	    	{"Leandro Ivory": [-17500.0, -25.0]},
	    	{"Broca Ivory": [-970.0, -1.0]},
	    	{"Alackbaki Ivory": [970.0, 1.0]},
	    	{"Zaraky Ivory": [3524.0, 11.5]} ] },
	    {"zuky": [
	    	{"Yu Zuky": [346992.0, 157.5]},
	    	{"Dexter Zuky": [0.0, 5.0]},
	    	{"Sora Zuky": [230.0, 8.0]},
	    	{"Mika Zuky": [30.0, 5.0]},
	    	{"Ryle Zuky": [23.0, 5.0]} ] },
	    {"uzuki": [
	    	{"Naomi Uzuki": [1130646.0, 780.5]} ] } ] },
    {"reino do som": 
  	  [ {"akaguma": [
  	  	{"Chaos Kaguya Akaguma": [638868.0, 512.0] }, 
  	  	 {"Ishikawa Akaguma": [39790.00, 65.5] } ] },
  	   {"yoso": [
    		{"Ki Yoso": [0.00, 5.0]},
  	  	{"Sophia Yoso": [0.0, 5.0]} ] },
 	   {"terepasu": [
    		{"Dante Sparda Terepasu": [0.00, 5.0]} ] } ] },
    {"reino da chuva": [
    	{"runbon": [
    		{"Shi Runbon": [3000.0, 6.0] },
    		{"Arlokis Runbon": [0.0, 5.0] },
  	  	{"Shinobu Rubon": [0.0, 5.0]} ] },
  	  {"senko": [
    		{"Korin Senko": [24.0, 5.0]}
    					 ] },
    	{"Kurai": [
    		{"Maja Kurai": [10000.0, 10.0]}
    ] } ] },
    {"reino da névoa": [
    	{"Kori":
    		[ {"Hrymir Kori": [-1000.0, -1.0] } ] } ] }
			 	 ]

"""

"""contsc2 = []
contsc2.append(secoes_c2)
print(contsc2, "###")
for n in range(0, secoes_c2.__len__()):
	print(n, ">", contsc2)
	contsc2[n].append(classes_c2[n])
	
print(contsc2, "@@@@@")
reg = []
for n, secao in enumerate(secoes_c):
	reg.append([secao])
	for num, classe in enumerate(classes_c):
		reg[n].append(classes_c)
	
for i in reg:
	print(i, "\n>")
print(reg)

for lis in contas:
	for secoes, classes in lis.items():
		#print("\n", secoes.upper())
		for conts in classes:
			for classe, indivs in conts.items():
				#print("----", classe, "----")
				for cc in indivs:
					for nome, valor in cc.items():
						#print(f"'{nome}', ", end="")
						pass
"""
