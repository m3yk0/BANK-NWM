# Numinous def


# Será um conversor da nova éra do rpg
#att 29/6/23 10:41

import os


def main():
	print("Conversor éra antiga para nova.\n"
	"Observações:\n"
	"1-Digite @ e enter para sinalizar o final do texto.\n"
	"2- Os paragrafos (pulo de linha) podem ser afetados após a conversão.\n"
	"3- Você pode digitar '¶' em seu texto aonde deseja deixar os paragrafos.\n"
	"4- locais com 2 caracteres de espaço em branco,também são comvertidas em paragrafo (pull de linha)"
	"\n Insira seu texto: \n"
	">>>   ")
	
	text = Line=""
	while True:
	    x=input()
	    Line=Line+" "+x
	    if "@" in x:
	        break
		
	new1 = Line.replace("dojutsu", "Ornous").replace("Habilidades" or "Jutsus" or "habilidades" or "jutsus", "Grimório", 1)
	new2 = new1.replace("hijutsu", "Harinous").replace("HIJITSU", "HARINOUS").replace("hijutsu", "Harinous").replace("hokage" or "Hokage", "Rei").replace("kage" or "Kage", "Líder").replace("hokage" and "HOKAGE" and "Hokage", "Rei").replace("kage" and "Kage" and "KAGE", "Líder")
	new3 = new2.replace("ninja", "ladino").replace("NINJA", "LADINO").replace("ninja", "ladino")
	new4 = new3.replace("Hidden jutsu","Harinous").replace("HIDDEN JUTSU", "HARINOUS").replace("Hidden jutsu","Harinous").replace("clã","Classe").replace("CLÃ", "CLASSE").replace("CLAN", "CLASSE").replace("clan", "Classe").replace("clã","Classe")
	new5 = new4.replace("chakra","nespiritus / numinosidade", 2)
	new6 = new5.replace("selos de mão", "feitio").replace("SELOS DE MÃO", "FEITIOS DE MÃO").replace("selos de mão", "feitio")
	new7 = new6.replace("Tenketsus","Pontos Numinous corporal").replace("TENKETSUS", "pontos de Numinous corporais").replace("Tenketsus","pontos de Numinosidade corporal")		
	new8 = new7.replace("suiton","Vandus")
	new9 = new8.replace("katon","Brandus")
	new10 = new9.replace("doton","Jordus")
	new11 = new10.replace("raiton","Rayus")
	#-=-
	new12 = new11.replace("gennin","Noumin").replace("genjutsu", "Genjutsu").replace("Genjutsu","hipinose").replace("GENJUTSU", "HIPNOSE")
	new13 = new12.replace("chunnin","Workin")
	new14 = new13.replace("jounnin","Maxin")
	new15 = new13.replace("kkg","Ker").replace("/j", "/f").replace("-n", "-N").replace("-C", "-W")
	new16 = new15.replace("kekkei genkai","Kerinous").replace("KEKKEI GENKAI", "KERINOUS")
	new17 = new16.replace("Hijutsu","Harinous").replace("HIJUTSU", "HARINOUS")
	# Title 
	new18 = new17.replace("Clã","Classe").replace("CLÃ", "CLASSE").replace("seu classe" or "Seu Classe" or "seu Classe" or "SEU CLASSE", "sua Classe")
	new19 = new18.replace("Chakra","numinous").replace("CHAKRA", "NESPIRITUS")
	new20 = new19.replace("Selos de Mão","feitio")
	new21 = new20.replace("tenketsus","pontos de nespiritus")
	new22 = new21.replace("Suiton","Vandus")
	new23 = new22.replace("Katon","Brandus")
	new24 = new23.replace("Doton","Jordus")
	new25 = new24.replace("Raiton","Rayus")
	#-=-
	new26 = new25.replace("Gennin","Noumin")
	new27 = new26.replace("Chunnin","Workin")
	new28 = new27.replace( "Jounnin", "Maxin")
	new29 = new28.replace("Kkg","Ker")
	new30 = new29.replace("Kekkei Genkai","Kerinous")
	new31 = new30.replace("Jutsu","Fascinio").replace("JUTSU", "FASCÍNIO")
	new32 = new31.replace("jutsu","fascinio")
	new33 = new32.replace("shinobi", "Ladino")
	new34 = new33.replace("Shinobi", "Ladino")	
	# clãs
	new35 = new34.replace("Senju", "Ivory").replace("SENJU", "IVORY").replace("tsuchigumo", "Hakai").replace("Tsuchigumo", "Hakai").replace("TSUCHIGUMO", "HAKAI")
	new36 = new35.replace("Hyuuga", "Tsuki").replace("HYUUGA", "TSUKI").replace("kaguya", "Akaguma").replace("Kaguya", "Akaguma").replace("KAGUYA", "AKAGUMA")
	new37 = new36.replace("Uchiha", "Zuky").replace("UCHIHA", "ZUKY")
	new38 = new37.replace( "Uzumaki", "Uzuki").replace("UZUMAKI", "UZUKI")
	new39 = new38.replace( "Akatsuki", "Kieta").replace("Aburame", "Mushi").replace("sarutobi", "Yoso").replace("Sarutobi", "Yoso").replace("SARUTOBI", "YOSO").replace("zuka", "").replace("ZUKA", "").replace("tsuchigumo", "Hakai").replace("Tsuchigumo", "Hakai").replace("TSUCHIGUMO", "HAKAI").replace("Yuki", "Kori").replace("yuki", "kori").replace("YUKI", "KORI").replace( "Akatsuki", "Kieta").replace("AKATSUKI", "KIETA")
	new40 = new39.replace( "Aldeia", "Reino")
	lis = ("a reino", "a Reino", "A reino", "A REINO", "o Reino", "sua reino", "sua Reino", "sua REINO", "suo reino", "uo Reino", "UO REINO", "uo Reino", "uo reino") 
	for element in lis:
		if element[0:1] in "a ":
			troca = "o Reino"
		elif "su" in element in "uo":
			troca = "seu Reino"
			if element.isupper() == True:
				troca.upper()
		new40 = new40.replace(element, troca)
	new41 = new40.replace("Vila oculta", "Reino oculto").replace("VILA OCULTA", "REINO")
	new42 = new41.replace("¶", "\n")
	new43 = new42.replace("o classe", "a classe")
	new44 = new43.replace("O Classe", "A Classe").replace("O CLASSE", "A CLASSE").replace("O Classe", "A Classe").replace("O CLASSE", "A CLASSE").replace("seu classe", "Sua classe").replace("seu Classe", "sua Classe").replace("seu CLASSE", "SUA CLASSE").replace("Seu Classe", "sua Classe")
	new000= new44.replace("o Classe", "a classe")
	new45 = new000.replace("o classe", "a classe").replace("O CLASSE", "A CLASSE")
	new46 = new45.replace("  ", "\n")
	new47 = new46.replace("Ninja", "ladino").replace("NINJA", "LADINO")
	new48 = new47 = new46.replace("Ninja", "ladino").replace("NINJA", "LADINO")
	new49 = new48.replace("taifascinio", "taijutsu").replace("TAIFASCINIO", "TAIJUTSU").replace("hokage", "Rei").replace("Hokage", "Rei").replace("kage", "Líder").replace("Kage", "Líder").replace("HOKAGE", "REI").replace("Hokage", "Rei").replace( "KAGE", "LÍDER").replace("so reino", "seu Reino").replace("so Reino", "seu Reino").replace("ALDEIA", "REINO").replace("Uma reino", "um Reino").replace("Uma Reino", "um reino").replace("sua reino", "seu Reino").replace("Sua Reino", "seu Reino").replace("Sua Reino", "Seu Reino").replace("seu classe", "sua Classe").replace("classe", "Classe").replace("reino", "Reino").replace("A Reino", "O Reino").replace("a Reino", "o Reino").replace("O Classe", "A classe").replace("o Classe", "a classe").replace("suo Reino", "seu Reino")	
	# titled dnv
	new50 = new49.replace("senju", "Ivory").replace("nara", "Kurai")
	new51 = new50.replace("hyuuga", "Tsuki").replace("Kazekage", "Sanzu").replace("kazekage", "Sanzu")
	new52 = new51.replace("uchiha", "Zuky").replace("HATAKE", "SHIRO").replace("hatake", "Shiro")
	new53 = new52.replace( "uzumaki", "Uzuki")
	new54 = new53.replace( "akatsuki", "Kieta").replace("aburame","Mushi").replace("Kaguya", "Akaguma").replace("kaguya", "Akaguma").replace("KAGUYA", "AKAGUMA").replace("Hatake", "Shiro").replace("kami", "Runbon").replace("Kami", "Runbon").replace("KAMI", "RUNBON").replace("ABURAME", "MUSHI").replace("Aburame","Mushi").replace("hoshigaki", "Same").replace("Hoshigaki", "Same").replace("HOSHIGAKI", "SAME").replace("tsurugi", "Anomalise").replace("Tsurugi","Anomalise").replace("TSURUGI","ANOMALISES")
	new55 = new54.replace( "aldeia", "Reino")
	new56 = new55.replace("vila", "Reino").replace("Vila", "Reino")
	new57 = new56.replace("   ", "\t")
	new58 = new57.replace("sharingan", "Ornous-Zuky").replace("SHARINGAN", "ZUKYNOUSS")
	new59 = new58.replace("Sharingan", "Ornous-Zuky")
	new60= new59.replace("byakugan", "Ornous-Tsuki").replace("BYAKUGAN", "TSUKINOUS")
	new61 = new60.replace("o classe", "a classe")
	new62 = new61.replace("...  ", "… \n")
	new63 = new62.replace("ninja", "ladino")
	new64 = new63.replace("dofascinio", "Ornous")
	new65 = new64.replace("Taifascinio", "taijutsu")
	new66 = new65.replace("Byakugan", "Ornous-Tsuki")
	new67 = new66.replace("Ninfascinio", "Tática-espiritual-ladino")
	new68 = new67.replace("ninjutsu", "tática-espiritual-ladino")
	new69 = new68.replace("ascinio", "ascínio")
	new70 = new69.replace("ninpou", "Feitiço secreto (ninpou)", 2)
	new71 = new70.replace("ninpou", "feitiço secreto")	
	if new70.count("rnous-Tsuki") >= 3:
		new71.replace("rnous-Tsuki", "rn-Tsuknous")
	if new70.count("rnous-tsuki") >=3:
		new71.replace("rnous-tsuki", "rn-Tsuknous")
	if new70.count("rnous-Zuky") >=3:
		new71.replace("rnous-Zuky", "rn-Zuknous")
	new72 = new71.replace("Ninpou", "Feitiço Secreto").replace("ninpou", "conjuração secreta")	
	new73 = new72.replace("senfascínio", "senjutsu") #msm coisa cm shurikenjutsu, bojutsu, etc	
	new74 = new73.replace("shurikenfascínio", "arte das facas")	
	#upper
	new75 = new74.replace("GENNIN", "NOUMINN")
	new76 = new75.replace("CHUNNIN", "WORKINN")
	new77 = new76.replace("JOUNNIN", "MAXINN").replace("Jou", "Max").replace("JOU", "MAX").replace("jou", "Max").replace("chu ", "Workinn ").replace("Chu ", "Workinn ").replace("C ", "W " ).replace("ge ", "Noumin ").replace("Ge ", "Noumin ")
	new78 = new77.replace("JUTSU", "FASCÍNIO").replace("G ", "N ") 
	new79 = new78.replace("Shurikenfascínio", "Shurikenjutsu")
	new80 = new79.replace("fuuton", "Vindus")
	new81 = new80.replace("Fuuton", "Vindus")
	new82 = new81.replace("jounnin", "Maxinn")	
	new83 = new82.replace("ladino (ladino)", "ladino")
	new84 = new83.replace("Ladino (ladino)", "ladino")
	new85 = new84.replace("ladino (Ladino)", "ladino")
	new86 = new85.replace("Ladino (Ladino)", "ladino")	
	new87 = new86.replace("descrição:", "\nDescrição:\n")
	new88 = new87.replace("Descrição", "\nDescrição:\n")
	new89 = new88.replace(":", ":\n")
	new90 = new89.replace("nota:", "\nNota:").replace("Nota:","\nNota:")
	new91 = new90.replace("genfascínio", "Genjutsu/hipinose sensorial")
	new92 = new91.replace("Genfascínio", "Hipinose sensorial")
	new93 = new92.replace("konbijutsu" or "konbifascínio", "técnica de combate em conjunto")	
	new94 = new93.replace("no fascínio", "fascínio")
	new95 = new94.replace("chakra", "numinous").replace("CHAKRA", "NESPIRITUS")
	new96 = new95.replace("no Fascínil", "no Fascínio")
	new97 = new96.replace("no sato", "*<<REINO>>*")
	new98 = new97.replace("No sato", "*<<REINO>>*")
	new99 = new98.replace("no Sato", "*<<REINO>>*")	
	new100 = new99.replace("vila", "reino")
	new101= new100.replace("vila Oculta", "Reino Oculto")
	new102 = new101.replace("Vila Oculta", "Reino oculto")	
	new103 = new102.replace("Líder Bunshin","Replica Expressiva")
	new104 = new103.replace("Líder bunshin", "Replica Expressiva")
	new105 = new104.replace("Líder bunshin", "Replica Expressiva").replace("LÍDER BUNSHIN", "RÉPLICA EXPRESSIVA")	
	new106 = new105.replace("bijuu", "Besta Espiritual (bijuu)", 3)
	new107 = new106.replace("Bijuu", "Besta espiritual").replace("BIJUU", "BESTA ESPIRITUAL")
	#.replace("1.", "\n1.").replace("2." or "\n\n2.", "\n2.").replace("3." or "\n\n3.", "\n3.").replace("4." or "\n\n4.", "\n4.").replace("5." or "\n\n5.", "\n5.").replace("6." or "\n\n6.", "\n6.").replace("7." or "\n\n7.", "\n7.").replace("8." or "\n\n8.", "\n8.").replace("9." or "\n\n9.", "\n9.").replace("0." or "\n\n0." ,"\n0.")
	new108 = new107.replace("konohagakure" or "Konohagakure", "Reino da Folha").replace("otogakure" or "Otogakure", "Reino do Som").replace("amegakure" or "Amegakure", "Reino da Chuva" ).replace("Sunagakure" or "sunagakure", "Reino da Areia").replace("kirigakure" or "Kirigakure", "Reino da Névoa").replace("KONOHAGAKURE", "REINO DA FOLHA").replace("OTOGAKURE", "REINO DO SOM").replace("AMEGAKURE", "REINO DA CHUVA").replace("KIRIGAKURE", "REINO DA NÉVOA").replace("SUNAGAKURE", "REINO DA AREIA").replace("algum classe", "alguma classe").replace( "Algum Classe", "Alguma classe").replace("Algum classe", "Alguma Classe").replace("algum Classe", "Alguma classe").replace("Kage", "Líder").replace("do seu classe", "da sua classe").replace("do seu Classe", "da sua Classe").replace("do Seu Classe", "da sua classe").replace("do teu classe", "da tua classe").replace( "do teu Classe", "da tua classe").replace( "do Teu Classe", "de tua classe").replace("no seu classe", "em sua classe").replace("no seu Classe", "em sua classe").replace("no Seu classe", "em sua classe").replace("noulo", "gelo").replace("Hyōton", "Noulo").replace("hyōton", "Noulo").replace("Hyouton", "Noulo").replace("hyouton", "Noulo").replace("Hyoton", "Noulo").replace("hyoton", "Noulo").replace("axnnin", "axinn").replace("noural", "geral").replace("Noural", "Geral").replace("oummin", "ouminn").replace("onnoular", "ongelar").replace("nouladas", "geladas").replace("Nouladas", "geladas").replace("connoulado", "congelado").replace("lonnou", "longe").replace("NOUMMIN", "NOUMINN").replace("MAXXIN", "MAXIN").replace("clone", "Replica").replace("g=", "N=").replace("c=", "W=").replace("j=", "M=").replace("byakugan", "Ornous Tsuki").replace("sharingan", "Ornous Zuky").replace("etc,", "etc.,").replace("Kage bunshin", "Réplica").replace("kage bunshin", "Réplica Expressiva").replace("Líder shuriken", "Replica shuriken").replace("Líder Shuriken", "Replica shuriken").replace("BUNSHIN", "Réplica Expressiva")
	new109 = new108.replace(".)", "). ").replace(") ", "), " ).replace(")\n", ").\n").replace(">", ">, ").replace("-", "–").replace("vc" or "Vc" or "VC", "você").replace(" q ", " que ").replace(" Q ", " Que ").replace("qnd" or "Qnd", "quando").replace("att ", "att.: ").replace("etc ", "etc. ").replace("rpg", "RPG").replace("RPG ", "RPG. ").replace("nn", "não").replace("nwm", "N.W.M").replace("n.w.m","N.W.M").replace(" p ", " para ").replace("noulo", "gelo").replace("Líders", "Líderes").replace("Konoha", "Reino da folha").replace("fzr", "fazer").replace(" p ", "para").replace("msm", "mesmo").replace("tb", "também").replace("tbm", "também").replace("gp", "Grupo")
	
	
	nwm = new109
	
	ctz = input("\confirma?. ")
	print(f"resp: {ctz}\n")
	
	# LIMPA A TELA:
	#os.system("clear")
	#os.system('clear')os.system("clear")os.system("clear")
	#print("\x1b[2J") 
	
	print(f'''\nAqui está seu texto convertido a nova éra:\n''')
	
	print("-="*30 + "-")
	
	print(nwm)
	
	print("-="*30 + "-")


def Numinous(text=""):
	text = str(text)
	text = text.replace(".)", "). ").replace(") ", "), " ).replace(")\n", ").\n").replace(">", ">, ").replace("-", "–").replace("vc" or "Vc" or "VC", "você").replace(" q ", " que ").replace(" Q ", " Que ").replace("qnd" or "Qnd", "quando").replace("att ", "att.: ").replace("etc ", "etc. ").replace("rpg", "RPG").replace("RPG ", "RPG. ").replace("nn", "não").replace("nwm", "N.W.M").replace("n.w.m","N.W.M").replace(" p ", " para ").replace("noulo", "gelo").replace("Líders", "Líderes").replace("Konoha", "Reino da folha").replace("fzr", "fazer").replace(" p ", "para").replace("msm", "mesmo").replace("tb", "também").replace("tbm", "também").replace("gp", "Grupo").replace("dojutsu", "Ornous").replace("Habilidades" or "Jutsus" or "habilidades" or "jutsus", "Grimório", ).replace("hijutsu", "Harinous").replace("HIJITSU", "HARINOUS").replace("hijutsu", "Harinous").replace("hokage" or "Hokage", "Rei").replace("kage" or "Kage", "Líder").replace("hokage" and "HOKAGE" and "Hokage", "Rei").replace("kage" and "Kage" and "KAGE", "Líder").replace("ninja", "ladino").replace("NINJA", "LADINO").replace("ninja", "ladino").replace("Hidden jutsu","Harinous").replace("HIDDEN JUTSU", "HARINOUS").replace("Hidden jutsu","Harinous").replace("clã","Classe").replace("CLÃ", "CLASSE").replace("CLAN", "CLASSE").replace("clan", "Classe").replace("clã","Classe").replace("chakra","nespiritus / numinosidade", 2 ).replace("selos de mão", "feitio").replace("SELOS DE MÃO", "FEITIOS DE MÃO").replace("selos de mão", "feitio").replace("Tenketsus","Pontos Numinous corporal").replace("TENKETSUS", "pontos de Numinous corporais").replace("Tenketsus","pontos de Numinosidade corporal").replace("suiton","Vandus").replace("katon","Brandus").replace("doton","Jordus").replace("raiton","Rayus").replace("gennin","Noumin").replace("genjutsu", "Genjutsu").replace("Genjutsu","hipinose").replace("GENJUTSU", "HIPNOSE").replace("chunnin","Workin").replace("jounnin","Maxin").replace("kkg","Ker").replace("/j", "/f").replace("-n", "-N").replace("-C", "-W").replace("kekkei genkai","Kerinous").replace("KEKKEI GENKAI", "KERINOUS").replace("Hijutsu","Harinous").replace("HIJUTSU", "HARINOUS").replace("Clã","Classe").replace("CLÃ", "CLASSE").replace("seu classe" or "Seu Classe" or "seu Classe" or "SEU CLASSE", "sua Classe").replace("Chakra","numinous").replace("CHAKRA", "NESPIRITUS").replace("Selos de Mão","feitio").replace("tenketsus","pontos de nespiritus").replace("Suiton","Vandus").replace("Katon","Brandus").replace("Doton","Jordus").replace("Raiton","Rayus").replace("Gennin","Noumin").replace("Chunnin","Workin").replace( "Jounnin", "Maxin").replace("Kkg","Ker").replace("Kekkei Genkai","Kerinous").replace("Jutsu","Fascinio").replace("JUTSU", "FASCÍNIO").replace("jutsu","fascinio").replace("shinobi", "Ladino").replace("Shinobi", "Ladino").replace("Senju", "Ivory").replace("SENJU", "IVORY").replace("tsuchigumo", "Hakai").replace("Tsuchigumo", "Hakai").replace("TSUCHIGUMO", "HAKAI").replace("Hyuuga", "Tsuki").replace("HYUUGA", "TSUKI").replace("kaguya", "Akaguma").replace("Kaguya", "Akaguma").replace("KAGUYA", "AKAGUMA").replace("Uchiha", "Zuky").replace("UCHIHA", "ZUKY").replace( "Uzumaki", "Uzuki").replace("UZUMAKI", "UZUKI").replace( "Akatsuki", "Kieta").replace("Aburame", "Mushi").replace("sarutobi", "Yoso").replace("Sarutobi", "Yoso").replace("SARUTOBI", "YOSO").replace("zuka", "").replace("ZUKA", "").replace("tsuchigumo", "Hakai").replace("Tsuchigumo", "Hakai").replace("TSUCHIGUMO", "HAKAI").replace("Yuki", "Kori").replace("yuki", "kori").replace("YUKI", "KORI").replace( "Akatsuki", "Kieta").replace("AKATSUKI", "KIETA").replace( "Aldeia", "Reino").replace("Vila oculta", "Reino oculto").replace("VILA OCULTA", "REINO").replace("o classe", "a classe").replace("O Classe", "A Classe").replace("O CLASSE", "A CLASSE").replace("O Classe", "A Classe").replace("O CLASSE", "A CLASSE").replace("seu classe", "Sua classe").replace("seu Classe", "sua Classe").replace("seu CLASSE", "SUA CLASSE").replace("Seu Classe", "sua Classe").replace("o Classe", "a classe").replace("o classe", "a classe").replace("O CLASSE", "A CLASSE").replace("  ", "").replace("Ninja", "ladino").replace("NINJA", "LADINO").replace("Ninja", "ladino").replace("NINJA", "LADINO").replace("taifascinio", "taijutsu").replace("TAIFASCINIO", "TAIJUTSU").replace("hokage", "Rei").replace("Hokage", "Rei").replace("kage", "Líder").replace("Kage", "Líder").replace("HOKAGE", "REI").replace("Hokage", "Rei").replace( "KAGE", "LÍDER").replace("so reino", "seu Reino").replace("so Reino", "seu Reino").replace("ALDEIA", "REINO").replace("Uma reino", "um Reino").replace("Uma Reino", "um reino").replace("sua reino", "seu Reino").replace("Sua Reino", "seu Reino").replace("Sua Reino", "Seu Reino").replace("seu classe", "sua Classe").replace("classe", "Classe").replace("reino", "Reino").replace("A Reino", "O Reino").replace("a Reino", "o Reino").replace("O Classe", "A classe").replace("o Classe", "a classe").replace("suo Reino", "seu Reino").replace("senju", "Ivory").replace("nara", "Kurai").replace("hyuuga", "Tsuki").replace("Kazekage", "Sanzu").replace("kazekage", "Sanzu").replace("uchiha", "Zuky").replace("HATAKE", "SHIRO").replace("hatake", "Shiro").replace( "uzumaki", "Uzuki").replace( "akatsuki", "Kieta").replace("aburame","Mushi").replace("Kaguya", "Akaguma").replace("kaguya", "Akaguma").replace("KAGUYA", "AKAGUMA").replace("Hatake", "Shiro").replace("kami", "Runbon").replace("Kami", "Runbon").replace("KAMI", "RUNBON").replace("ABURAME", "MUSHI").replace("Aburame","Mushi").replace("hoshigaki", "Same").replace("Hoshigaki", "Same").replace("HOSHIGAKI", "SAME").replace("tsurugi", "Anomalise").replace("Tsurugi","Anomalise").replace("TSURUGI","ANOMALISES").replace( "aldeia", "Reino").replace("vila", "Reino").replace("Vila", "Reino").replace("   ", "      ").replace("sharingan", "Ornous-Zuky").replace("SHARINGAN", "ZUKYNOUSS").replace("Sharingan", "Ornous-Zuky").replace("byakugan", "Ornous-Tsuki").replace("BYAKUGAN", "TSUKINOUS").replace("o classe", "a classe").replace("...  ", "… ").replace("ninja", "ladino").replace("dofascinio", "Ornous").replace("Taifascinio", "taijutsu").replace("Byakugan", "Ornous-Tsuki").replace("Ninfascinio", "Tática-espiritual-ladino").replace("ninjutsu", "tática-espiritual-ladino").replace("ascinio", "ascínio").replace("ninpou", "Feitiço secreto (ninpou)", ).replace("ninpou", "feitiço secreto").replace("Ninpou", "Feitiço Secreto").replace("ninpou", "conjuração secreta").replace("senfascínio", "senjutsu").replace("shurikenfascínio", "arte das facas").replace("GENNIN", "NOUMINN").replace("CHUNNIN", "WORKINN").replace("JOUNNIN", "MAXINN").replace(" Jou", " Max").replace(" JOU", " MAX").replace(" jou", " Max").replace(" chu ", " Workinn ").replace(" Chu ", " Workinn ").replace(" C ", " W " ).replace(" ge ", " Noumin ").replace(" Ge ", " Noumin ").replace("JUTSU", "FASCÍNIO").replace(" G ", " N ").replace("Shurikenfascínio", "Shurikenjutsu").replace("fuuton", "Vindus").replace("Fuuton", "Vindus").replace("jounnin", "Maxinn").replace("ladino (ladino)", "ladino").replace("Ladino (ladino)", "ladino").replace("ladino (Ladino)", "ladino").replace("Ladino (Ladino)", "ladino").replace("descrição:", "\nDescrição:\n").replace("Descrição", "\nDescrição:\n").replace(":", ": ").replace("nota:", "\nNota:").replace("Nota:","\nNota:").replace("genfascínio", "Hipnose Sensorial").replace("Genfascínio", "Hipinose Sensorial").replace("konbijutsu" or "konbifascínio", "técnica de combate em conjunto").replace("no fascínio", "fascínio").replace("chakra", "numinous").replace("CHAKRA", "NESPIRITUS").replace("no Fascínil", "no Fascínio").replace("no sato", "*<<REINO>>*").replace("No sato", "*<<REINO>>*").replace("no Sato", "*<<REINO>>*").replace("vila", "reino").replace("vila Oculta", "Reino Oculto").replace("Vila Oculta", "Reino oculto").replace("Líder Bunshin","Replica Expressiva").replace("Líder bunshin", "Replica Expressiva").replace("Líder bunshin", "Replica Expressiva").replace("LÍDER BUNSHIN", "RÉPLICA EXPRESSIVA").replace("bijuu", "Besta Espiritual (bijuu)", 3).replace("Bijuu", "Besta espiritual").replace("BIJUU", "BESTA ESPIRITUAL").replace("konohagakure" or "Konohagakure", "Reino da Folha").replace("otogakure" or "Otogakure", "Reino do Som").replace("amegakure" or "Amegakure", "Reino da Chuva" ).replace("Sunagakure" or "sunagakure", "Reino da Areia").replace("kirigakure" or "Kirigakure", "Reino da Névoa").replace("KONOHAGAKURE", "REINO DA FOLHA").replace("OTOGAKURE", "REINO DO SOM").replace("AMEGAKURE", "REINO DA CHUVA").replace("KIRIGAKURE", "REINO DA NÉVOA").replace("SUNAGAKURE", "REINO DA AREIA").replace("algum classe", "alguma classe").replace( "Algum Classe", "Alguma classe").replace("Algum classe", "Alguma Classe").replace("algum Classe", "Alguma classe").replace("Kage", "Líder").replace("do seu classe", "da sua classe").replace("do seu Classe", "da sua Classe").replace("do Seu Classe", "da sua classe").replace("do teu classe", "da tua classe").replace( "do teu Classe", "da tua classe").replace( "do Teu Classe", "de tua classe").replace("no seu classe", "em sua classe").replace("no seu Classe", "em sua classe").replace("no Seu classe", "em sua classe").replace("noulo", "gelo").replace("Hyōton", "Noulo").replace("hyōton", "Noulo").replace("Hyouton", "Noulo").replace("hyouton", "Noulo").replace("Hyoton", "Noulo").replace("hyoton", "Noulo").replace("axnnin", "axinn").replace("noural", "geral").replace("Noural", "Geral").replace("oummin", "ouminn").replace("onnoular", "ongelar").replace("nouladas", "geladas").replace("Nouladas", "geladas").replace("connoulado", "congelado").replace("lonnou", "longe").replace("NOUMMIN", "NOUMINN").replace("MAXXIN", "MAXIN").replace("clone", "Replica").replace(" g=", " N=").replace(" c=", " W=").replace(" j=", " M=").replace("byakugan", "Ornous Tsuki").replace("sharingan", "Ornous Zuky").replace("etc,", "etc.,").replace("Kage bunshin", "Réplica").replace("kage bunshin", "Réplica Expressiva").replace("Líder shuriken", "Replica shuriken").replace("Líder Shuriken", "Replica shuriken").replace("BUNSHIN", "Réplica Expressiva").replace("  ", " ").replace("\n\n", "\n").replace("\nrição:","").replace("Nota", "\nNota").replace("\n\nNota", "\nNota").replace(" ao a ", " em razão a ").replace("\n: ", "").replace("_\nNota", "\n_Nota").replace("ninfascínio", "Conjuração Secreta")
	
	# correções de português:
	text = text.replace(" ir em ", " ir à ").replace("assim ", "assim, ").replace("Assim ", "Assim, ").replace(" ir na ", " ir à ").replace(" ir no ", " ir ao ")
	return text
 
 


if __name__ == "__main__":
	main()
	#A = Numinous(input(">> "))
	#print(A)
	exit()

