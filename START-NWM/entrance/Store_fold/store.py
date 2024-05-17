# Encoding:  UTF-8
# From NWM-SISTEM
"""_summary_
    /qitens, /r1, /r2 <...>, etc.
    –> Prioridade para instância de variáveis usadas em 'controles.py', 'Funcs.py' e 'Banco03.py'
    """
import pandas
import pandas as pd
import datetime

historic = [ ]
tabelaDeProcessos = {}

import numpy as np

global itens, contas, contratos, propriedades, classes_c2, backups, Rank, data_reg, dic_reg, \
	avisos, reinantes, leis, lideres


global data_atual


def atual_data() -> object:
    historic.append("activate function atual_data()...")
    data = str(datetime.date.today())
    ano, mes, dia = data[0:4], data[5:7], data[8:]
    hr = str(datetime.datetime.now())[11:19]
    ms = str(datetime.datetime.now().isoformat(timespec='milliseconds'))[-1:-7:-1]
    data_atual = f"{dia}/{mes}/{ano}-{hr}:{ms}"
    del hr, ano, mes, data
    return data_atual


itens = {
	'None': '0',
	'kunai': '10',
	'kunai_curva': '10',
	'shuriken': '10',
	'senbons': '10',
	'makibishi': '10',
	'raihashis': '10', 'flecha_comum-curta(1_lote_2uni)': '10',
	'pena_para_escrita': '10',
	'vidraça_com_tinta_para_pena': '10',
	'hip_pouchbolsa': '50',
	'soprador_com_sabão': '50',
	'selo_explosivo': '50',
	'bomba_de_luz': '50',
	'bomba_de_fumaça': '50',
	'bomba_de_fumaça_mineral': '100',
	'fios_de_aço(1m)': '50',
	'guisos': '50',
	'pássaro_mecânico': '50',
	'pergaminho': '100',
	'fuuma_shuriken': '100',
	'shuriken_gigante': '100',
	'bomba_de_gelo': '100',
	'dardo_de_injeção(5_uni)': '100',
	'antídoto': '100',
	'flecha_grande(1_lote_2uni)': '100',
	'bomba_de_pimenta': '100',
	'tampões_de_ouvido': '250',
	'pano_de_selamento': '300',
	'kusari-fundo': '300',
	'shuriken_quadrada': '300',
	'mangual': '300',
	'ataduras(1m)': '300', 'pergaminho_com_tinta_e_caneta': '400',
	'pinças_de_tesoura': '400',
	'nunchaku': '500',
	'katana_simples': '500',
	'bõ': '500',
	'arco': '500',
	'pesos_de_treinamento': '500',
	'rádio_comunicador_(3uni)': '500',
	'kusarigama': '500',
	'tanto': '500',
	'danko': '500',
	'esfera_explosiva': '500',
	'bola_de_selos_explosivos': '500',
	'corrente_do_bastão_de_vento': '500',
	'atana_mediana': '1000',
	'lâminas_deunai': '1000',
	'guarda_chuva': '1000',
	'braceletes_de_ferro': '1000',
	'boneco_de_metal': '1000', 'armadura_de_chakra(protetora)': '1000', 'cartões_de_informações_ninja': '1200',
	'etiqueta_de_selamento': '1300', 'catapulta_de_shuriken_gigante': '1500',
	'balista': '1500',
	'braceletes_de_selamento': '2000',
	'espada_retrátil': '2000', 'alto_falante_ressonante_de_eco': '2000',
	'foice': '2000',
	'lançador_de_agulhas': '2000',
	'johyo': '2000',
	'tekkõkagi': '2000',
	'braço_de_cabo_retrátil': '2000', 'garra_de_lâmina_tripla_aprimorada': '2000',
	'armadura_de_batalha_shinobi': '2000',
	'manoplas_de_metal': '2000', 'lâminas_de_chakra_de_konoha': '2000',
	'canhão_elétrico': '2000',
	'hidro-bomba_(2_uni)': '2000',
	'serra_circula_de_marionete': '2000',
	'bastão_resistente': '2500',
	'katana_resistente': '3000',
	'yodai_sensu': '3000',
	'lançador_de_pulso': '3000',
	'jidanda': '3000', 'atirador_de_dardos_de_injeção': '3000',
	'escudo_retrátil': '3000',
	'corte_da_lua': '3000',
	'hyotan': '4000',
	'katana_super_resistente': '5000',
	'ocarina': '5000', 'braço_de_perfuração_mecânica': '5000',
	'canhão_da_cabeça_de_leão': '5000',
	'canhão_de_bomba_de_chakra': '5000',
	'chaves_de_braços_verdantes': '5000',
	'traje_de_lodo': '10000',
	'lançador_de_shurikens': '10000',
	'lançador_de_kunai_portátil': '10000', 'dispositivo_de_rompimento_de_chakra': '15000',
	'tsuru000ame': '80000', 'armadura_de_chakra_(absorve)': '100000',
	'tobishachimaru': '200000',
	'2045': '400000', 'marionete_de_madeira_vermelha': '90000',
	'marionete_formiga_negra': '100000',
	'marionete_salamandra': '120000',
	'marionete_veloz': '145000',
	'marionete_golem': '150000',
	'marionete_guardiã': '140000',
	'marionete_guardiã_gigante': '160000',
	'marionete_abelha_rainha': '195000',
	'marionete_base': '240000',
	'marionete_escorpião': '280000',
	'marionete_automatizada': '300000',
	'marionete_mestresuprema': '400000',
	'kiba_(espadas_do_trovão)': '500000',
	'kusanagi_(espada_serpente)': '600000',
	'shibuki(respingo)': '500000',
	'nuibari_(grande_agulha)': '350000', 'kabutowari_(rachadora_de_elmos)': '600000',
	'kuribiribocho_(lâmina_do_executor)': '600000', 'hiramekarei_(espadas_gêmeas)': '800000',
	'gunbai_(arranjo_do_exército)': '600000',
	'gamatasu': '600000',
	'gamaken': '600000',
	'gamahiro': '600000',
	'gamariki': '600000',
	'gama': '600000',
	'gamagoro': '600000',
	'gamaken2': '600000',
	'gamamaru': '600000',
	'gamariki2': '600000',
	'gamatatsu': '600000',
	'gekomatsu': '600000',
	'gerotora': '600000',
	'osuke': '600000',
	'shima': '600000',
	'gamakichi': '600000',
	'ikari_wa_hebi_cobras_raivosas': '500000',
	'jay_ermida': '600000',
	'kyodaijya': '600000',
	'aoda': '600000',
	'serpentes_de_três_cabeças': '700000', 'yamata_cobra_de_várias_cabeças': '800000',
	'aliança_fajulta': '10',
	'buquê_de_flores_simples': '10',
	'papel_de_presente_simples': '10',
	'vestido_fajulto': '50',
	'terno_fajulto': '50',
	'papel_de_presente': '50',
	'aliança_de_namoro': '50',
	'aliança_de_noivado': '100',
	'buquê_de_flores': '100',
	'vestido': '500',
	'terno': '500',
	'buquê_de_flores_de_luxo': '500',
	'aliança_de_casamento': '1000',
	'vestido_de_casamento': '1000',
	'terno_para_cerimônias': '1000',
	'tratamento_médico': '1000',
	'aliança_de_diamante': '2500', 'certidão_de_responsabilidade_para_ter_pets': '5000',
	'transplante_oficial': '20000',
	'casa_comum': '40000', 'casa_com_cerquinhas_brancas': '65000',
	'casa_gótica': '65000',
	'mansão': '80000',
	'terreno_para_casa': '80000',
	'terreno_geral': '90000',
	'seguro_eterno': '90000',
	'espingarda': '9000',
	'carabina': '9000',
	'metralhadora': '40000',
	'submetralhadora': '12000',
	'fuzil_de_assalto': '20000',
	'rifle_sniper': '25000',
	'revólver': '8000',
	'pistola': '6000',
	'taser': '5000',
	'stun_gun': '4000',
	'eletrodos_para_taser': '500',
	'bateria_para_taser_e_stun_gun': '900',
	'tripé': '1000',
	'silenciador': '30000',
	'munição(12_uni)': '5000',
	'extensor_de_mira': '1000',
	'binóculo_20x50': '1000',
	'kit_manutenção_de_armas': '1000',
	'colete_a_prova_de_balas': '1000',
	'coldre': '30',
	'algema_ultra_forte': '850',
	'kit_primeiros_socorros': '700',
	'combustível_para_fogo_1l': '600',
	'bússola': '500',
	'sinalizador': '500',
	'corda_de_alpinismo': '400',
	'luz_química': '50', 'capacete_com_proteção_facial': '350',
	'amolador_de_facas': '300',
	'pá': '200',
	'picareta': '200',
	'canivete': '170',
	'soco_inglês': '170',
	'capacete_tático': '170',
	'esqueiro_zippo': '50',
	'ponteiro_a_laser_quente': '60',
	# eventos
	# Especiais
	'Grimório Fascínios Elementais (Lvl1)': '1',
	'Grimório Da Classe (Lvl1)': '1',
	'Grimório Fascínios Chave': '1',
	'Grimório Fascínios Elementais (Lvl2)': '2',
	'Grimório Fascínios Da Classe (Lvl2)': '2',
	'Grimório Fascínios Elementais (lvl3)': '3',
	'Grimório Fascínios da Classe (lvl3)': '3',
	'Bijuu': '100'
	}

contas = \
	{
		'contas em conjunto/NPC':
			{
				'times':
					{
						'iluminati': [ 0.0, 0.0 ],
						'~Devs': [ 180980.0, 1.0 ],
						'ຊYamata': [ 90000.0, 0.0 ]
						},
				'npcs':
					{
						'NPC Okyem Kurai (Meyko Ivory)': [ 2500.0, 0.0 ],
						'Corpo-Morto Ashiki Zuky (Meyko Ivory)': [ 0.0, 30.0 ],
						'Corpo-Vivo ਹTakumo Ivory (Meyko Ivory)': [ 0.0, 30.0 ],
						"Corpo-Vivo Akaza Shiro (Meyko Ivory)": [ 0.0, 30 ],
						"Corpo-Vivo Raijin Ivory (Meyko Ivory)": [ 0.0, 30 ],
						'NPC Chaos Kurai (Chaos Akaguma)': [ 2500.0, 0.0 ],
						'NPC Yu Hokori ( Yu Zuky)': [ 2500.0, 0.0 ],
						'Corpo-Vivo Nito Zuky (Yu Zuky)': [ 0.0, 30.0 ],
						'Corpo-Vivo Kibba Hokori (Yu Hokori)': [ 0.0, 30.0 ]
						}
				},
		'reino da folha':
			{
				'tsuki':
					{'Norushige Tsuki': [ 30.0, 5.0 ],
					 '≠±¬°°≈‹Susumo Tsuki': [ 451473.0, 443.5 ]},
				'inu':
					{'Meeh Inu': [ 847.0, 847.0 ],
					 'Lize Inu': [ 30.0, 5.0 ]},
				'ivory':
					{'Meyko Ivory 2045 - (1.710.466, 956,5)': [ 0.0, 0.0 ],
					 'Leandro Ivory': [ -14500.0, -22.0 ],
					 'Broca Ivory': [ -970.0, -1.0 ],
					 'Alackbaki Ivory': [ 970.0, 1.0 ],
					 'Zaraky Ivory': [ 3524.0, 11.5 ],
					 '~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory': [ 1323320.0, 1236.0 ]
					 },
				'zuky':
					{'Dexter Zuky': [ 0.0, 5.0 ],
					 'Sora Zuky': [ 230.0, 8.0 ],
					 'Mika Zuky': [ 30.0, 5.0 ],
					 'Ryle Zuky': [ 23.0, 5.0 ],
					 'Lily Zuky': [ 5030.0, 7.0 ],
					 '~‹‹≈¤°°ຊ€Yu Zuky': [ 349992.0, 155.5 ]
					 },
				'uzuki':
					{'ਹ¤¤Naomi Uzuki': [ 30, 50 ]},
				'shiro':
					{'Tioo Shiro': [ 48024.0, 65.0 ]}
				},
		'reino da chuva':
			{
				'runbon':
					{
						'Klaithous Telbos Yui Runbon': [ 30.0, 5.0 ],
						'≈Shi Runbon': [ 42900.0, 56.0 ]
						},
				'senko':
					{
						'Korin Senko': [ 24.0, 5.0 ]
						},
				'kurai':
					{
						'Maja Kurai': [ 13000.0, 10.0 ],
						'≈Ninguem Kurai': [ 11530.0, 6.0 ]
						},
				'kieta':
					{
						'Lize Inu Kieta': [ 30.0, 5.0 ]
						}
				},
		'reino do som':
			{
				'akaguma':
					{
						'Ishikawa Akaguma': [ 39790.0, 65.5 ],
						'~-ຊ±¬°Chaos Akaguma': [ 638868.0, 512.0 ]
						},
				'yoso':
					{
						'Ki Yoso': [ 0.0, 5.0 ],
						'Sophia Yoso': [ 0.0, 5.0 ]
						},
				'terepasu':
					{'Dante Sparda Terepasu': [ 0.0, 5.0 ]}
				},
		'reino da nevoa':
			{
				'kori':
					{'Godzebul Kori': [ 30.0, 5.0 ]}
				},
		'reino da areia':
			{
				'hokori':
					{'Kyoto Hokori': [ 30.0, 5.0 ]},
				'sanzu':
					{'Akutagawa Sanzu': [ 30.0, 5.0 ]}
				}
		}


def pan():
	aSE = [ ]
	aDT = [ ]
	for sec, dic_clas in contas.items():
		a = pandas.Series(contas[ sec ], copy=True, name=sec)
		aSE.append(a)
		print(a)
		dt = pandas.DataFrame(a, columns=[ sec ], copy=True)
		aDT.append(dt)
		print(dt)
	print(f"\n\n{aDT}")


# contratos = { ['nomes envolvidos']: {'Tipo': '', 'Acordo': '', "Inicio": '', "Final": "", 'Penalidade': ''} }
# {'Tipo': "Herança/", 'Acordo': 'O primeiro a morrer ou evadir, têm seus itens, propriedades, saldo e corpo dado ao outro.', 'Início': 'dia/mes/ano', 'Final': "Eterno", 'Penalidade': 'Multa nível máximo'}
contratos = {
	('~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory', 'ਹ¤¤Naomi Uzuki'):
		{'Tipo': "Herança/Eterno",
		 'Acordo': 'O primeiro a morrer ou evadir, têm seus itens, propriedades, saldo e corpo dado ao outro.',
		 'Início': '2023',
		 'Final': "Eterno",
		 'Penalidade': 'Multa nível máximo'},
	('~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory', 'ਹ¤¤Naomi Uzuki'):
		{'Tipo': 'Invocação',
		 'Acordo': 'Sempre que necessário, os envolvidos na partida podem invocar um ao outro com técnica da invocação',
		 "Inicio": '2023', "Final": "Eterno", 'Penalidade': 'Múlta Nível Máximo'},
	('~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory', 'Corpo-Vivo ਹTakumo Ivory (Meyko Ivory)'):
		{'Tipo': "Herança/Eterno",
		 'Acordo': 'O primeiro a morrer ou evadir, têm seus itens, propriedades, saldo e corpo dado ao outro.',
		 'Início': '2023',
		 'Final': "Eterno",
		 'Penalidade': 'Multa nível máximo'},
	('~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory', "Corpo-Vivo Raijin Ivory (Meyko Ivory)"):
		{'Tipo': "Herança/Eterno",
		 'Acordo': 'O primeiro a morrer ou evadir, têm seus itens, propriedades, saldo e corpo dado ao outro.',
		 'Início': '2023',
		 'Final': "Eterno",
		 'Penalidade': 'Multa nível máximo'},
	('~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory', "Corpo-Vivo Akaza Shiro (Meyko Ivory)"):
		{'Tipo': "Herança/Eterno",
		 'Acordo': 'O primeiro a morrer ou evadir, têm seus itens, propriedades, saldo e corpo dado ao outro.',
		 'Início': '2023',
		 'Final': "Eterno",
		 'Penalidade': 'Multa nível máximo'},
	('~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory', '≠±¬°°≈‹Susumo Tsuki'):
		{'Tipo': "Outros",
		 'Acordo': 'Meyko dará um coração Ivori para Susumo Tsuki, em troca do mesmo dar um de seou Ornous Tsuki.',
		 'Início': '2023',
		 'Final': "Eterno",
		 'Penalidade': 'Multa nível máximo'},
	('~‹‹≈¤°°ຊ€Yu Zuky', 'Corpo-Vivo Kibba Hokori (Yu Hokori)'):
		{'Tipo': "Herança/Eterno",
		 'Acordo': 'O primeiro a morrer ou evadir, têm seus itens, propriedades, saldo e corpo dado ao outro.',
		 'Início': '2023',
		 'Final': "Eterno",
		 'Penalidade': 'Multa nível máximo'},
	('~‹‹≈¤°°ຊ€Yu Zuky', 'Corpo-Vivo Nito Zuky (Yu Zuky)'):
		{'Tipo': "Herança/Eterno",
		 'Acordo': 'O primeiro a morrer ou evadir, têm seus itens, propriedades, saldo e corpo dado ao outro.',
		 'Início': '2023',
		 'Final': "Eterno",
		 'Penalidade': 'Multa nível máximo'}
	}

propriedades = {
	'iluminati':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'~Devs':
		{'Grimório Fascínios Elementais (lvl1)': 2, 'Grimório da Classe (lvl1)': 1,
		 'Grimório Fascínios Chave': 1, 'a': 0},
	'ຊYamata':
		{'Grimório Fascínios Elementais (lvl1)': 2, 'Grimório da Classe (lvl1)': 1,
		 'Grimório Fascínios Chave': 1, 'Bijuu': 5},
	'NPC Okyem Kurai (Meyko Ivory)':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Corpo-Morto Ashiki Zuky (Meyko Ivory)':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Corpo-Vivo ਹTakumo Ivory (Meyko Ivory)':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	"Corpo-Vivo Akaza Shiro (Meyko Ivory)":
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	"Corpo-Vivo Raijin Ivory (Meyko Ivory)":
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'NPC Chaos Kurai (Chaos Akaguma)':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'NPC Yu Hokori ( Yu Zuky)':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Corpo-Vivo Nito Zuky (Yu Zuky)':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Corpo-Vivo Kibba Hokori (Yu Hokori)':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Norushige Tsuki':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'≠±¬°°≈‹Susumo Tsuki':
		{'Grimório Fascínios Elementais (lvl2)': 2, 'Grimório Fascínios da Classe (lvl2)': 1,
		 'Grimório Fascínios Elementais (lvl1)': 2, 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Meeh Inu':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Lize Inu':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Meyko Ivory 2045 - (1.710.466, 956,5)':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Leandro Ivory':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Broca Ivory':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Alackbaki Ivory':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Zaraky Ivory':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory':
		{'Grimório Fascínios Elementais (lvl2)': 2, 'Grimório Fascínios da Classe (lvl2)': 1,
		 'Grimório Fascínios Elementais (lvl1)': 2, 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Dexter Zuky':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Sora Zuky':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Mika Zuky':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Ryle Zuky':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Lily Zuky':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'~‹‹≈¤°°ຊ€Yu Zuky':
		{'Grimório Fascínios Elementais (lvl2)': 2, 'Grimório Fascínios da Classe (lvl2)': 1,
		 'Grimório Fascínios Elementais (lvl1)': 2, 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'ਹ¤¤Naomi Uzuki':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Tioo Shiro':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Klaithous Telbos Yui Runbon':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'≈Shi Runbon':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Korin Senko':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Maja Kurai':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'≈Ninguem Kurai':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Lize Inu Kieta':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Ishikawa Akaguma':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'~-ຊ±¬°Chaos Akaguma':
		{'Grimório Fascínios Elementais (lvl2)': 2, 'Grimório Fascínios da Classe (lvl2)': 1,
		 'Grimório Fascínios Elementais (lvl1)': 2, 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Ki Yoso':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Sophia Yoso':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Dante Sparda Terepasu':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Cha Belez Kori':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Godzebul Kori':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Kyoto Hokori':
		{'Grimório Fascínios Elementais (lvl1)': 2,
		 'Grimório da Classe (lvl1)': 1, 'Grimório Fascínios Chave': 1},
	'Akutagawa Sanzu':
		{'Grimório Fascínios Elementais (lvl1)': 2, 'Grimório da Classe (lvl1)': 1,
		 'Grimório Fascínios Chave': 1, 'S': 1000}
	}

classes_c2 = {
	"contas em conjunto/NPC":
		[ "times", "npcs" ],
	"reino da folha":
		[ "tsuki", "inu", "ivory", "zuky", "uzuki", "shiro" ],
	"reino do som":
		[ "akaguma", "yoso", 'terepasu', 'kokyo' ],
	"reino da chuva":
		[ "kieta", 'runbon', 'senko', 'kurai' ],
	"reino da nevoa":
		[ 'kori', "same", "shio" ],
	"reino da areia":
		[ "sanzu", "hokori", "mushi" ]
	}

data_reg = "11/07/2023-02:09:01"

dic_reg = {data_reg: contas}  # registro atual

avisos: list[ dict[ str ] ] = [ {"avisos de atualizacoes": {data_reg: "None"}}, {
	"avisos gerais": {data_reg: "None"}} ]  # Avisos[0 = Avisos de mudança[data]] [1 = Avisos gerais[data]

reinantes = {'reino da folha': '~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory'}

leis = {"reino da folha": "Ativas"}


"""class DictLeaders():
	classes: list

	def __int__(self, classes=None):
		classes = list(self)
		self.classes = classes

D = DictLeaders
# Primeiro: Instâncie a classe:
lis = list([1, 2])
E = DictLeaders(classes=lis)
# Segundo: Preencha os argumentos:
print(f"{DictLeaders = }, {D = }, {E = } ", file=None)"""


def declare_leaders(leaders=None):
	global historic
	data_atual = atual_data()
	historic.append(f'Acionada função "declare_leaders" as {data_atual}')
	if leaders is None:
		lideres = {'tsuki': '≠±¬°°≈‹Susumo Tsuki',
				   'inu': 'Meeh Inu',
				   'ivory': '~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory',
				   'zuky': '~‹‹≈¤°°ຊ€Yu Zuky',
				   'uzuki': 'None',
				   'shiro': 'None',
				   'akaguma': '~-ຊ±¬°Chaos Akaguma',
				   'terepasu': 'None',
				   'yoso': 'None',
				   'kokyu': 'None',
				   'kieta': 'None',
				   'runbon': '≈Shi Runbon',
				   'kurai': '≈Ninguem Kurai',
				   'senko': 'None',
				   'kori': 'None',
				   'same': 'None',
				   'shio': 'None'}
	else:
		lideres = leaders
	return lideres


def fix_leaders(leaders=None):
	"""

	-> Verifica se as chaves da variável 'lideres' cobrem as classes da var 'contas'.
	Returns: None

	"""
	# Computing function:
	global historic, tabelaDeProcessos
	data_atual = atual_data()
	historic.append(f'acionada função "fix_leaders()" as {data_atual}')
	# ----		Code	---- #
	desc = [] # Var para preencher a 'tabelaDeProcessos'
	# Take the 'lideres' var
	if leaders is None:
		lideres = declare_leaders()
	else:
		lideres = leaders
	# Computing lideres var:
	ClassesInLideres = [ ]
	for cla, lider in lideres.items():
		""" Resgata os valores da variável 'lideres', guardando as classes do RPG em var 'cla' """
		cla = cla.strip().lower()
		ClassesInLideres.append(cla)
	# PONTO DE CHECAGEM (lideres in contas.classes):
	tratos_li = 0
	ClassesInConts = [ ]
	ClassesAdicionadas = [ ]
	for sec, dic_cla in contas.items():
		for cla, conts in dic_cla.items():
			""" Verifica a var 'contas', capturando as classes presentes no registro """
			ClassesInConts.append(cla)
			if cla not in ClassesInLideres.copy():
				""" Caso a classe presente no registro, não esteja dentre as classes citadas na var. 'lideres', adicioná-a """
				cla = cla.strip().lower()
				desc.append(F"A classe: {cla}, não estava incluída na variável 'lideres' atual. Adicionamos agora, e o líder de tal classe está referido como 'None'.")
				lideres[ cla ] = 'None'  # Aloca a classe nova ao var 'lideres'.
				ClassesInLideres.append(cla)  # Atualiza as classes contidas na var 'lideres'.
				ClassesAdicionadas.append(cla)
				tratos_li += 1
	classes_co = ClassesInConts.__len__()
	classes_li = ClassesInLideres.__len__()
	desc.append(f"{ClassesInLideres = }\n\n{ClassesInConts = }")
	desc.append(f"Houve {tratos_li} tratementos para a variavel 'lideres', adicionando: {cla}. ")
	desc.append(F"Agora lideres contém {classes_li} classes (chaves), assim como 'contas' armazena {classes_co} classes. (classes_li pode ser valor maior que classes_co, mas não o inverso)")
	desc.append(F"Fim da função 'ajeita_lideres()'.")
	# Gabarita os atos:
	tabelaDeProcessos[f'log de fix_leaders() ás {data_atual}'] = desc
	return lideres

lideres = fix_leaders()



Rank = {'~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory': {'Lutas': 47, 'Caças': 0, 'Partidas': 2, 'Missões': 6},
		'≠±¬°°≈‹Susumo Tsuki': {'Lutas': 31, 'Caças': 0, 'Partidas': 1, 'Missões': 0},
		'~-ຊ±¬°Chaos Akaguma': {'Lutas': 22, 'Caças': 2, 'Partidas': 3, 'Missões': 5},
		'~‹‹≈¤°°ຊ€Yu Zuky': {'Lutas': 21, 'Caças': 1, 'Partidas': 1, 'Missões': 6},
		'Alackbaki Ivory': {'Lutas': 0, 'Caças': 0, 'Partidas': 0, 'Missões': 3},
		'≈Shi Runbon': {'Lutas': 0, 'Caças': 0, 'Partidas': 0, 'Missões': 1},
		'≈Ninguem Kurai': {'Lutas': 0, 'Caças': 0, 'Partidas': 0, 'Missões': 1},
		'Maja Kurai': {'Lutas': 0, 'Caças': 0, 'Partidas': 0, 'Missões': 1},
		'Klaithous Telbos Yui Runbon': {'Lutas': 0, 'Caças': 0, 'Partidas': 0, 'Missões': 0},
		"ਹ¤¤Naomi Uzuki": {'Lutas': 26, 'Caças': 2, 'Partidas': 0, 'Missões': 6},
		'Zaraky Ivory': {'Lutas': 3, 'Caças': 0, 'Partidas': 2, 'Missões': 0}
		}


def declare_backups():

	# Computing function:
	global historic, tabelaDeProcessos
	historic.append(f'Activate function "declare_backups()"')
	# ----		Code	---- #
	lideres = fix_leaders()
	backups = {
		"contas":
			{"04/03/2024-16:04:01": (contas.copy())},
		"lideres": {"04/03/2024-16:04:01": (lideres.copy())},
		"reinantes": {"04/03/2024-16:04:01": (reinantes.copy())},
		"avisos": {"04/03/2024-16:04:01": (avisos.copy())},
		"leis": {"04/03/2024-16:04:01": (leis.copy)},
		"Rank": {"04/03/2024-16:04:01": (Rank.copy())},
		"contratos": {'04/03/2024-16:04:01': (contratos.copy())},
		"propriedades": {'04/03/2024-16:04:01': (propriedades.copy())},
		"itens": {"04/03/2024-16:04:01": (itens.copy())}
		}
	return backups
backups = declare_backups()

# Caso adicione mais categorias no backup, lembre-se de mudar a func backups_fc de Banco.py.

# print(contas, backups, itens, propriedades, contratos, leis, avisos, reinantes, lideres, leis, Rank, sep='\n\n>>>')


"""
contas = [
	{'contas em conjunto/NPC': [
		{'times': [
			{'iluminati': [ 0.0, 0.0 ]},
			{'~Devs': [ 180980.0, 1.0 ]},
			{'ຊYamata': [ 90000.0, 0.0 ]}
			]},
		{'npcs': [
			{'NPC Okyem Kurai (Meyko Ivory)': [ 2500.0, 0.0 ]},
			{'Corpo-Morto Ashiki Zuky (Meyko Ivory)': [ 0.0, 30.0 ]},
			{'Corpo-Vivo ਹTakumo Ivory (Meyko Ivory)': [ 0.0, 30.0 ]},
			{"Corpo-Vivo Akaza Shiro (Meyko Ivory)": [ 0.0, 30 ]},
			{"Corpo-Vivo Raijin Ivory (Meyko Ivory)": [ 0.0, 30 ]},
			{'NPC Chaos Kurai (Chaos Akaguma)': [ 2500.0, 0.0 ]},
			{'NPC Yu Hokori ( Yu Zuky)': [ 2500.0, 0.0 ]},
			{'Corpo-Vivo Nito Zuky (Yu Zuky)': [ 0.0, 30.0 ]},
			{'Corpo-Vivo Kibba Hokori (Yu Hokori)': [ 0.0, 30.0 ]}
			]}
		]},
	{'reino da folha': [
		{'tsuki': [
			{'Norushige Tsuki': [ 30.0, 5.0 ]},
			{'≠±¬°°≈‹Susumo Tsuki': [ 451473.0, 443.5 ]}
			]},
		{'inu': [
			{'Meeh Inu': [ 847.0, 847.0 ]},
			{'Lize Inu': [ 30.0, 5.0 ]}
			]},
		{'ivory': [
			{'Meyko Ivory 2045 - (1.710.466, 956,5)': [ 0.0, 0.0 ]},
			{'Leandro Ivory': [ -14500.0, -22.0 ]},
			{'Broca Ivory': [ -970.0, -1.0 ]},
			{'Alackbaki Ivory': [ 970.0, 1.0 ]},
			{'Zaraky Ivory': [ 3524.0, 11.5 ]},
			{'~€±±☆≈≈≠•¬¬¬¬¬‹‹‹‹‹°°°¤@Meyko Ivory': [ 1323320.0, 1236.0 ]}
			]},
		{'zuky': [
			{'Dexter Zuky': [ 0.0, 5.0 ]},
			{'Sora Zuky': [ 230.0, 8.0 ]},
			{'Mika Zuky': [ 30.0, 5.0 ]},
			{'Ryle Zuky': [ 23.0, 5.0 ]},
			{'Lily Zuky': [ 5030.0, 7.0 ]},
			{'~‹‹≈¤°°ຊ€Yu Zuky': [ 349992.0, 155.5 ]}
			]},
		{'uzuki': [
			{'ਹ¤¤Naomi Uzuki': [ 30, 50 ]}
			]},
		{'shiro': [
			{'Tioo Shiro': [ 48024.0, 65.0 ]}
			]}
		]},
	{'reino da chuva': [
		{'runbon': [
			{'Klaithous Telbos Yui Runbon': [ 30.0, 5.0 ]},
			{'≈Shi Runbon': [ 42900.0, 56.0 ]}
			]},
		{'senko': [
			{'Korin Senko': [ 24.0, 5.0 ]}
			]},
		{'kurai': [
			{'Maja Kurai': [ 13000.0, 10.0 ]},
			{'≈Ninguem Kurai': [ 11530.0, 6.0 ]}
			]},
		{'kieta': [
			{'Lize Inu Kieta': [ 30.0, 5.0 ]}
			]}
		]},
	{'reino do som': [
		{'akaguma': [
			{'Ishikawa Akaguma': [ 39790.0, 65.5 ]},
			{'~-ຊ±¬°Chaos Akaguma': [ 638868.0, 512.0 ]}
			]},
		{'yoso': [
			{'Ki Yoso': [ 0.0, 5.0 ]},
			{'Sophia Yoso': [ 0.0, 5.0 ]}
			]},
		{'terepasu': [
			{'Dante Sparda Terepasu': [ 0.0, 5.0 ]}
			]}
		]},
	{'reino da nevoa': [
		{'kori': [
			{'Godzebul Kori': [ 30.0, 5.0 ]}
			]}
		]},
	{'reino da areia': [
		{'hokori': [
			{'Kyoto Hokori': [ 30.0, 5.0 ]}
			]},
		{'sanzu': [
			{'Akutagawa Sanzu': [ 30.0, 5.0 ]}
			]}
		]}
	]"""


