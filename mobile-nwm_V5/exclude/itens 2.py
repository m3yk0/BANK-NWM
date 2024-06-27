import pandas
import Numinous as N


# from Itens_fold import Itens_Bruto


def declare_eventos(fonte=None):
	"""

	-> instância com propriedades, um dicionário chamado "dict_eventos", baseado em uma string de texto-fonte.

	:param fonte: Opcional None (é pego a fonte incluída internamente na função). Caso parâmetro != None, a fonte deve ser:
		- string de múltiplas linhas. Cada linha = nome de item novo.
		- Não deve haver linhas em branco. (\n\n).
		- Pode haver, opcionalmente, o indicativo de preço ":" após o nome do item, (onde 'nome' fica atrás de ':' e preço fica a direita(frente) do indicativo ).
		- Caso haja preço, também é possível citar o indicativo de descrição, símbolo "#", onde a esquerda do símbolo de hashtag fica o preço, e a direita -> fica a Descrição.
		- Caso haja preço + descrição, importante citar que nela, não deve haver outros símbolos indicativos como "\n" (pull de linha), ":" e "#".
		- Caso fornecido somente o nome e sem outros indicativos, então o preço padrão será "0", e ficará sem descrição.

	:returns: caso sem erros, retorna dicionário. Key= Nome_item: Value= list([preço, descrição])

	"""
	if fonte is None or fonte == 'Eventos_Bruto.csv':
		pass
		# from entrance.Store_fold.Eventos_fold import Eventos_Bruto
		# Eventos = pandas.read_csv('Eventos_fold.Eventos_Bruto.csv')
	elif fonte is not None:
		Eventos = fonte
	# Define dict_eventos:
	dict_eventos = {}
	Eventos = Eventos.strip().split("\n")
	# define dicionário:
	for i, e in enumerate(Eventos):
		name = N.Numinous(e).strip().title()
		if ":" in e:
			namexprice = e.split(":")
			name = namexprice[ 0 ].strip()
			price = namexprice[ -1 ].strip()
			if price == "":
				price = 0
			if "#" in e:
				priceXdesc = price.split("#")
				desc = priceXdesc[ -1 ].strip()
				price = price(priceXdesc[ 0 ].strip())
			else:
				desc = "Sem_Descrição"
		else:
			price = 0
			desc = "Sem_Descrição"
		dict_eventos[ name ] = list([ price, desc ])
	return dict_eventos


declare_eventos()


def price(text="", remove_simbols=True):
	"""
	pega texto e deixa somente os números, para transformar em INT
	
	:returns: -2 caso resultado final não seja um digito, e retorna Texto transformado em Int caso resultado final == True to isdigit.
	"""
	lis = "a b C d e f g h I J K L m n o p q r s t U V w X y z".lower().split(" ")
	for e in lis:
		text = text.replace(e, "")
		text = text.replace(e.upper(), "").strip()
	if remove_simbols is True:
		lis2 = "@ # & _ - ( ) = % * ' : / ! ? + , . £ € ¥ ¢ © ® ™ ~ ¿ ¡ ^ > < } ] [ ` ; ÷ \ | ¦ ¬ × § ¶ °".split(" ")
		for e in lis2:
			text = text.replace(e, "")
	text = text.replace(" ", "").replace("\n", "").replace("\t", "")
	if "" == text:
		return -1
	elif text.isdigit():
		return int(text)


def define_habilidades():
	habilidades = """

0~ Conjurações Rayus - Yonhom Nukite (Facada Infernal - Lança de Quatro Dedos): 430K
Desc: Usuário faz basicamente dedos ou unhas do Rayus mais poderoso possível, tal como que sua mão, ao final de seu dedos, tivessem laminas brilhantes como um ‘sabre de luz’ é a técnica Rayus mais forte, por isso, ela consegue cortar absolutamente tudo que tem uma densidade fisica, sendo entendido como fascinio que corta itens de resistência nível 6 (e o máximo de resis da forja é 4, 2x mais poderoso que tudo) Nota: 1EXP = dedo crescer 1cm para frente (grossura do dedo não aumenta, apenas largura, seu dedo ficar mais longo, porém de Rayus e não carne real) Nota2: 200EXP ou menos = 1 dedo ser acrescido (400EXP= 2 dedos, 600= 3…)

Kirin (Girafa): 420.000
Desc: Somente caso o clima esteja nuvoso, com nuvens ao arredor da arena, é possível tal fascínio. Usuário ergue um de seus braços aos céus, logo, em 1s com o braço erguido, um dragão feroz, gigante de Rayus surge das nuvens. Ao comando do usuário abaixar seu braço na direção do oponente, o dragão de raios vai até o oponente na velocidade de um raio, assim eletrocutando 100% o oponente e tudo que foi atingido pelo tamanho do dragão, cujo certamente, colapsará instantaneamente. Nota: 1EXP= dragão ter 1M de comprimento (rabo até cabeça). Nota2: 1EXP= dragão ter 1M de circunferência/grossura. Nota3: 1EXP= dragão ir até 1M longe do usuário

Juurokuchuu Shibari (Estilo Relâmpago - Armadilha de Dezesseis Pilares): 400K
Desc: Após uma sequencia de selos, Usuário envia Rayus para o subterrâneo, este Nespiritus Rayus faz com que rochas se pilastrem e saiam da terra. Tais rochas vão para a superfície, e uma seguida da outra, se ergue até que o oponente que está no centro da armadilha. Agora completamente preso, até mesmo por cima. Por ser do estilo raio, nem quem está dentro, nem quem está do lado de fora, pode encostar nas pilastras, caso encoste, fica paralisado por 1 turno ou 10 min. Nota: 1EXP= armadilha conter 1M (min 3M para prender oponentes). Nota2: Usuário pode especificar com teto aberto ou fechado. Nota3: dura 2 turnos, após isso, a armadilha volta ao solo. Nota4: em questão de 5 milésimos após finalizar os selos, a armadilha já está pronta.

Liberação de relâmpago roxo: 400.000
Desc: Este fascinio, faz com que, todos os fascinios Rayus que usuário usar durante 2 turnos, receba poderes muito maiores, desencadeia um fluxo de eletricidade roxa para atacar alvos, detendo de um poder capaz de destruir inclusive as técnicas de Liberação de Gelo, caso tal Rayus encoste em algo, a parte que tocou neste Rayus roxo, é desintegrada na hora.

Raimu Raito (Ribalta): 200.000
Desc: Uma das mais poderosas técnicas de Rayus existentes. É uma técnica de colaboração em que quatro usuários de Rayus se movem para o Norte, Sul, Leste e Oeste da região em que estão, e liberam seus Nespirituss simultaneamente. Quando isso acontece, quatro trovões emanam de seu corpo e se juntam para destruir toda a região em que a técnica foi usada, incinerando completamente os metros cúbicos demarcado pela posição de cada usuário do Fascínio. Nota: Após usuários ficarem em posição, demora apenas 1 segundo para que eles façam feitios e logo em 0,5s a área ser completamente devastada, matando todo ser vivo que possa estar dentro do cerco. Nota2: 1EXP= 1M de altura do fascinio (o máximo é o EXP do usuário com menor EXP) (caso a altura do fascinio seja muito baixa, basta oponente pular alto quando ocorrer a eletricidade, que o mesmo saia do foco do fascinio)

Raiso Gekishin (Estilo Relâmpago - Tremor do Rato de Relâmpago): 350.000
Desc: O usuário lança de suas mãos vários pequenos discos de Rayus cortantes, cujo explodem ao acertar o alvo. Nota: 1EXP = disco conter 1cm. Nota2: 1EXP= disco correr até 1M longe do usuário. Nota3: O raio da explosão, é sempre o dobro do tamanho do disco especificado na nota 1 (disco de 2M(200cm) = explosão de 4M(400cm))

Raijingubonbā (Bomba Crescente): 250.000
Desc: Usuário energiza seus membros com Rayus, caso os membros energizados, encoste em oponente, o mesmo fica paralisado por 2 turnos, e todos que encostarem neste oponente paralisado, também serão paralisados
Nota: 100EXP ou menos = energizar 1 membro (1 braço, 1 mão, 1 dedo, tórax, etc, caso 200EXP= 2 membros…)

0~ Conjurações Jordus - Shishi Dojou (fascinio de Reissureição Supremo do Estilo Terra - Corpos do solo): 600.000
Desc: Utilizando o solo local, o usuário pode reviver os mortos. A segunda versão permite ao usuário reviver alguém perfeitamente, com até mesmo aparência de vivo, seu cheiro, enfim, é uma ressurreição 100% real, podendo usar suas habilidades de quando era vivo, com a adição de que o revivido é obrigado a obedecer o seu invocador, estando ciente de tudo o que está fazendo, assim como tendo as lembranças de seu passado. Nota: Revive 1 pessoa por uso
Nota2: Pessoa dura por 3 turnos, após isso, vira poeira. Nota3: Apenas fascinios Elementais, Kerinous e fascinios Chave podem ser usados pelo ser revivido, fascinios comprados, adquiridos como médico, anbu , etc e harinous, não. Nota4: demora 10 min, 1 rodada para revitalizar totalmente alguém (usuário inicia em um turno, apenas no outro o ser é revivido). Nota5: A pessoa revivida, renasce saindo de baixo da terra. Nota6: Após pessoa ser revivida, a ordem da batalha muda, logo, a pessoa revivida fica na ordem da luta, como na vez seguinte do usuário do fascinio (Ex: Cleber invocou Fulano e Samuel é oponente, ordem estava 1-Cleber, 2-Samuel, logo, a ordem ficará 1-Cleber, 2-Fulano, 3-Samuel) O juiz deve mandar a mensagem da ordem nova no chat caso o fascinio tenha sido bem sucedido. Usuário do fascinio cena como usuário e como pessoa revivida.

Shishi Dojou Sekandomōdo (fascinio de Reissureição Supremo do Estilo Terra - Corpos do solo. Segundo Modo): 500.000
Desc:  Utilizando o solo local, o usuário pode reviver os mortos que morreram no local. A primeira versão permite ao usuário reviver continuamente um grande número de pessoas como zumbis, sem racionalidade, não são muito fortes, nem usam fascinios, porém em massa, podem ser bastante incomodativos e até letais. Os zumbis são bem fáceis de destruir, possuindo algo como uma resistência nível 1. Se a técnica for desativada pelo usuário, ou se ele for morto, os zumbis se transformam em poeira. Nota: 1EXP = fazer um zumbi a 1M longe do usuário. Nota2: Cada zumbi, pode andar apenas até 30M longe de onde nasceram, caso passem tal distância, se restam a poeira. Nota3: Oponentes que forem mortos pelos zumbis, podem virar zumbis também, usuário pode até mesmo equipar alguns zumbis com armamentos e armadura para deixar mais interessante. Nota4: dura 2 turnos, após isso, os mortos-vivos viram poeira. Nota5: 100EXP = fazer 1 zumbi (pode inventar que zumbi sai de baixo da terra, ou transformar um lutador morto nisto caso tenha 200EXP para isso)

0~ Conjurações Vindus - Rasenshuriken (Estilo Vento - Rasen Shuriken) (necessita de rasengan) : 400.000
Desc: A técnica Fuuton mais poderosa que existe. O Shinobi cria um grande Rasengan azul claro no formato de uma Fuuma Shuriken, após realizar a Transformação de Forma para transformar o Nespiritus em uma Shuriken, e a Transformação de Natureza para dar à técnica as características do vento. Por ter sido criada de um Rasengan ordinário, o usuário não pode lançar o Rasen Shuriken, portanto, precisa fazer contato direto com o inimigo. Ao ser atingido pelo fascinio, o oponente é lançado 30M para longe enquanto seu corpo é atingido por milhares de agulhas de vento microscópicas que causam danos na linha Numinous. Após isso, a vítima se torna incapaz de realizar fascinios pelo resto de sua vida caso sobreviva. Nota: 1EXP = Rasenshuriken conter 1cm (fascinio precisa ter pelo menos, o tamanho exato do oponente (ou maior) para que ao atingi-lo, o mesmo fique em corta-Nespiritus permanentemente). Nota2: Caso alguém seja afetado por tal, deve botar na ficha ‘Corta-Nespiritus permanente’ e retirar os elementos, dofascinios, Kerinous, harinous e ninfascinios comprados da ficha, já que usuário não os tem mais.

0~ Conjurações Brandus - Benijigumo (Estilo Fogo - Aranha Vermelha): 310.000
Desc: Usuário solta uma esfera flamejante de sua boca, 1s após ela ser disparada, começa a ter aspectos de aranha, tendo patas, presas e formato. A aranha então pode perseguir oponentes e até mesmo, usar ela mesma o fascinio Benijigumo, porém claro, gasta do usuário. Nota: 1EXP= aranha conter 1cm (muito pequena, pode ser facilmente morta). Nota2: 1EXP= aranha andar até 1M longe de onde foi criada (serve para aranhas filho tb)

0~ Conjurações Vandus - Ukojizai fascinio (Técnica da Chuva de Tigre Total): 430K
Desc: Um Ninfascinio de percepção, onde o usuário cria uma grande chuva que cobre toda a região usando seu próprio Nespiritus. Quando algum Shinobi estranho adentra a chuva, o usuário fica sabendo imediatamente, informações como sexo, quem o acompanha, peso, tamanho, força, alguns itens, sua localização e etc. Nota: 100EXP ou menos = Chuva durar 1 turno. Nota2: 1EXP= chuva ser iniciada a 1M longe do usuário. Nota3: 1EXP= chuva cobrir 1m2

Suiryuudan no fascinio (Estilo Água - fascinio Dragão de Água): 400.000
Desc: 1s após terminar uma sequencia de feitio, particulas de água se juntam desde o subterrâneo até rios próximos, se reúnem rapidamente, logo, em 3s após terminar a sequencia, muita água é juntada e começa a se formar em um dragão de sjuiton que pode engolir, perseguir, quebrar, etc. nota1: 1exp = 1M de comprimento (altura/tamanho do corpo entre calda até cabeça). nota2: 1exp = 1M de largura (grossura/raio). nota3: mínimo 3M de largura e 5M comprimento p engolir humanos. nota4: dura 1 Turno. nota5: p cada metro de altura deve ter pelo menos 2M a mais de comprimento. nota6: selo quebrado = sem fascinio. nota7: 1EXP = criar o dragão a 1M do usuário. Nota8: 1EXP = dragão perseguir até 1M de distancia de onde foi criado.

Takitsubo no fascinio (Estilo Água - fascinio da Base da Cachoeira): 250.000
Desc: Usuário corta um pedaço de seu corpo e posiciona em algum lugar, sempre que usuário fazer um selo de mão com uma mão, o pedaço energizado de Nespiritus Vandus do usuário começará a despejar água, esta é uma técnica para se criar uma nascente de água em qualquer lugar que usuário deixou pelo menos 5cm de seu DNA. Nota: 1EXP= fazer 1L de água sair do membro. Nota2: 1EXP = água ser criada a uma velocidade de 500m/h(meio, 0,5 km/h por EXP) (um soco forte tem cerca de 30km/h)

0~ Conjurações Abrangentes - Rasengan - (Esfera Espiral): 500.000
Desc: Um Resengan, é a forma de manipulação de Nespiritus puro, em volta de uma esfera espiral de Nespiritus, é uma técnica que somente avançados conseguem, tanto, que nem é necessário uso de feitio para criar tal esfera. Após usuário criar a esfera em usa mão, o mesmo encosta a sua mão em quanto segura a esfera até o oponente, logo, a esfera age como ácido, corroendo tudo que toca. Nota: 1EXP= rasengan ter 1cm de circunferência. Nota2: Apenas Nespiritus serve de defesa contra rasengan, outros meios, qualquer armadura, até mesmo a mais resistente de todas, não protege caso não seja especifica com Nespiritus.

Kibaku Fuuda no fascinio (fascinio dos Papéis Bomba): 300.000
Desc: Após deixar preparados no chão diversos papéis bombas, o usuário faz um selo com sua mão para que todos os papéis bombas se movam pelo chão e se prendam ao corpo do alvo. Então, os selos explodem ao comando do usuário. Nota: 1EXP= selos andarem até 1M longe do usuário. Nota2: 1EXP = selos perseguirem a 1km/h

Técnica de Clonagem - Mil clones: 250.000
(necessita do fascinio ‘técnica de clonagem’)
Desc: Um ninfascinio que cria uma cópia intangível de seu próprio corpo, por padrão, são criados a 1 metro ao lado do usuário, São exatamente iguais ao usuário em relação aparência física, caso usuário não tenha um braço, o clone também não terá.  Um clone da técnica de clonagem, não tem a capacidade de atacar mas é melhor somente para confundir o inimigo, por serem sem substancia alguma, não levantam poeira, não fazem pegadas, porém, apesar disso, ainda podem carregar alguns itens, mas tudo que exige um pouco demais do clone, o faz ser dissipado. A diferença deste, é que não segue o tanto de clones por patentes, podendo fazer mais de centenas de clones, mesmo sendo um Noumin. Nota: 1EXP = 1 clone intangível.

Técnica de Clonagem: 200.000
Desc: Um ninfascinio que cria uma cópia intangível de seu próprio corpo, por padrão, são criados a 1 metro ao lado do usuário, São exatamente iguais ao usuário em relação aparência física, caso usuário não tenha um braço, o clone também não terá.  Um clone da técnica de clonagem, não tem a capacidade de atacar mas é melhor somente para confundir o inimigo, por serem sem substancia alguma, não levantam poeira, não fazem pegadas, porém, apesar disso, ainda podem carregar alguns itens, mas tudo que exige um pouco demais do clone, o faz ser dissipado. Nota: Segue a patente, onde Numin=2 clones, Workin 3 e Maxin 5. Nota2: Em lutas com pessoas que sabem corretamente evitar meta-game, pode enganar perfeitamente até mesmo Maxins caso tal fascinio seja usado engenhosamente.

0~ Conjuração Médica - Espada Forte: 300.000
Desc: Este fascínio consiste em aprimorar o tamanho e potência da lâmina de alguma espada ao infundi-la com Numinous. nota: 1EXP = lâmina crescer 1cm para cima (sua ponta aumenta). nota2: 1EXP = lâmina crascer 0,5cm para as laterais (1cm a mais no total para as laterais). nota3: Com isso, a lâmina também vem a ser aprimorada com +1 nível de resistência

Punho Adamantino: 200.000
Desc: Usuário reúne energia algo semelhante a energia médica junto a sua própria energia numinous, criando assim um nespiritus que concede forca sobre-humana. nota: 2EXP = A resistência é aderida a 1 membro (como mão, perna, cabeça, etc). nota2: 10EXP = A resistência do membro melhorado fica numa resistência nível 2 (menos de 10 = resis 1. 20EXP = resis 3 (max)) Podendo assim quebrar itens de tais resistências e arremessar oponentes para o dobro (30EXP = triplo) de distância de sua patente

Chiyu Naiteki no fascinio: 200.00
Desc: fascinio no qual o Ladino médico fecha os olhos e concentra Nespiritus medico na ponta dos dedos e os coloca na cabeça do alvo. Utilizado para curar doenças psicológicas que foram implantadas e tirar memórias falsas, podendo até mesmo retirar paciente de genfascinio ou de algum coma.
Nota: dura 1 turno inteiro cujo os dedos do Ladino com fascinio médico deva ficar na cabeça do paciente para que o fascinio seja efetivo.

Yuu no Nespiritus (Nespiritus de Ajuda): 250.000
Desc: O Ladino consegue enviar o seu Nespiritus para outro Ladino com o contato corporal, facilitando assim os seus fascinios, ou ajuda-lo a recuperar algum Nespiritus perdido, retirando o estado ‘corta-Nespiritus’ de algum aliado.

Numinous no Saikousei: 300.000
Descrição: fascinio onde momentos antes de ter seus Numinous afetados, o dono do fascinio fortifica seus Numinous com feitios enviando Nespiritus protetor e curativo nos Numinous, impedindo que quando um ataque ocorra no turno posterior contra os Numinous, danifique seus regulatórios de Nespiritus, Isso impede que usuário fique em corta-Nespiritus (sem poder realizar fascinios). Nota: Dura 2 turnos contando o primeiro em que o fascinio já é iniciado, após isso a proteção se desfaz. Nota2: Pode ser usado em outras pessoas também, ao dono do fascinio ficar 1 turno inteiro enviando Nespiritus protetor e regenerativo aos Numinous de seu aliado, o próximo turno inteiro o aliado já fica protegido, porém nem no primeiro turno nem no posterior ao segundo o aliado já é beneficiado, mas sim somente 1 turno após o dono do fascinio ficar constantemente com as mãos no aliado enviando Nespiritus ao mesmo.

Takaiheki no fascinio: 500.000
Desc: fascinio médico utilizado para forjar a morte de alguém. Ao tocar em certos 5 pontos no pescoço do alvo, este entra em estado momentâneo de morte. O alvo precisa estar imóvel, pois os pontos são de difícil acesso. Esse estado de morte não dura mais de cinco minutos, ou 1 turno, pois depois de cinco minutos a pessoa volta ao normal. Muito útil para cirurgias complicadas, pois nesse estado nenhum órgão do alvo se move. Nota: O turno inicial é também o turno final

Fushi Tensei (Reencarnação do Corpo Vivo): 2.500.000
Desc: O dono do hidden-fascinio junto com seu futuro hospedeiro, se senta a 1M um a frente do outro, dentro de um circulo de 2M de circunferência de sangue de um dos 2 , o usuário então une suas mãos a cabeça da vítima e começa a expelir o Nespiritus do corpo da vitima até que não reste nada, enfraquecendo a mente do hospedeiro, o usuário então
induz a vítima a dormir e igualmente o usuário dorme junto a ela, suas mentes estão conectadas e ambos compartilham um sonho na mesma realidade, o usuário que ainda tem Nespiritus e força, dentro da mente da vítima fraca e sem força, mata o hospedeiro dentro do sonho, o hospedeiro então acorda e suga todo o Nespiritus do ex-corpo do usuário, este é o ato final, ao hospedeiro que na verdade já é o próprio usuário sugar todo Nespiritus do ex-corpo do usuário, o mesmo então pode se levantar e viver sua vida durante 9 meses no RPG até que tenha que novamente fazer tais etapas para trocar novamente de corpo com algum hospedeiro, pois exatamente daqui a 271 dias o usuário morrerá junto com o corpo de seu já velho hospedeiro permanentemente. Nota: Isto mata permanentemente o hospedeiro. Nota2: o usuário então poderá fazer todo fascinio que o seu hospedeiro fazia, caso o hospedeiro tenha Kers. (coração ou olhos de algum clã de Kerinous) o usuário poderá controlar tais Ker. novas, porém não mais as antigas do seu corpo evadido. Nota3: fascinios aprendidos e comprados continuarão com o usuário, fascinios aprendidos e comprados pela vitima serão esquecidos e quem invadiu o corpo do hospedeiro não faz fascinios estilo harinous ou hiddens que a vítima tenha aprendido antes do dia em que foi realizado o fascinio Fushi Tensei, somente os que o usuário aprender depois ou tinha aprendido no próprio corpo de usuário. Nota4: Todos os bens materiais como itens e ryos são transferidos ao usuário, o EXP da vítima também é adicionado ao EXP do usuário.

0~ Categoria ninpou: Sumi Ninpou (Arte Ladino da Tinta): 0
Desc: descrição do ninpou de tinta: Esta é uma técnica que permite ao usuário animar os desenhos como se a tinta ganhasse vida e faz com que os desenhos ajam conforme as vontades do usuário. Nota: mesmo comprando o ninpow de tinta, somente é possível realiza-lo comprando pergaminho e algo para escrita (sangue, lápis, caneta, pena, etc ) o pergaminho será o papel e o desenho será feito pelo material de escrita, a tinta então é energizada com Nespiritus refinado do usuário, o que dá a capacidade da pintura, sair do pergaminho e agir como se fosse um ser vivo. Nota2: Água é um grande ponto fraco deste ninpou, fora qualquer golpe relativamente ofensivo a tais pinturas a fazem dissiparem-se. Nota3: 1EXP = o desenho possuir 1cm (Caso não seja especificado o tamanho do desenho, será o máximo do EXP do usuário). Nota4: Alguns desenhos se forem pequenos ou grandes demais, podem perder sua efetividade ou não representarem tão bem o que deveriam ser. Nota5: O desenho em questão pode ser desenhado em qualquer tamanho no pergaminho, o seu tamanho que ficará após sair do pergaminho é decidido pelo EXP do usuário (alguns desenhos devem ter pelo menos o tamanho de um homem para conseguir de fato erguer ou empurrar algum Ladino (tamanho eficiente: 2M, ou 200EXP, com 200EXP Boa parte dos fascinios podem ser eficazes como deveriam ser)). Nota6: 1EXP = desenhos se distanciarem 1M do usuário. Nota7: todos ninpou deste tipo duram 2 turnos ou até serem destruídos ou comandados a se destruir pelo usuário. Nota8: O fascinio não pode ser tão moldado, ou seja, caso usuário desenhe um tigre (e tenha comprado o fascinio lançamento do predador perseguidor, o qual me refiro), o tigre já terá sua função de enrolar-se em algum oponente e leva-lo até o pergaminho, não é possível fazer desenhos no pergaminho e ditar suas funções livremente (como criar uma largatixa que se esconde na calça de alguém) somente é possível fazer um desenho e uma função desde que vc tenha comprado o fascinio e o mesmo exista no rpg. Nota9: Todo desenho (fascinio) demora pelo menos 1s para ser desenhado e então sair do papel. Nota10: Bote esta descrição no primeiro turno ou assim que realizar algum fascinio deste ninpou

Fuuinfascinio - Koshi Tandan (Técnica de Selamento - Lançamento do Predador Perseguidor): 0
Desc: Sai cria um tigre de tinta. O tigre sai do papel e morde o inimigo, enrolando-se nele. Assim, com o inimigo preso, o tigre volta ao pergaminho junto com seu alvo, prendendo-o dentro do pergaminho e selando-o. Nota: O tigre aumenta sua largura até que possa dar pelo menos 2 voltas completas no alvo, o tamanho que o tigre cresce não é ligado ao EXP

Ninpou • Sumi Senshi (Arte Ladino - Guerreiros de Tinta): 0
Desc: Sai desenha em seu pergaminho dois guerreiros grandes que saem do papel e atacam quem estiver por perto. Esses dois guerreiros são o Deus do Vento e o Deus do Trovão, que possuem uma força descomunal. Não se sabe se possuem algum outro poder. nota: 50EXP por guerreiro (ex: 50exp= conseguir desenhar e dar vida somente ao guerreiro Deus do Vento OU do Trovão, 100EXP = dar vida tanto ao Deus do Vento como ao Deus do Trovão ao mesmo tempo). Nota2: Caso usuário tenha menos de 100EXP, ainda pode fazer o segundo guerreiro, gastando o fascinio uma vez para cada guerreiro

Ninpou - Inkuwāmu (Arte Ladino - Verme de tinta): 0
Desc: Sai cria diversos vermes de tamanhos diferentes feitos de tintas, o que pode causar desconforto aos oponentes, ainda que em grande quantidades, usuário pode arremessa-las para cima do oponente para tentar atrasa-lo, também podem servir como obstáculo que oponente pisa em cima e pode escorregar. Nota: 1EXP= 1 verme de tinta (especificar o tamanho de cada). Nota2: os vermes rastejam e deixam tinta no chão como rastro meloso.

Choujuu Giga - Ryuu (Pegaminho da Super Besta - Dragão): 0
Desc: Sai desenha um dragão em seu pergaminho. Esse dragão emerge e ataca o inimigo, mordendo e levando ele para o céu. Por fim, o solta o alvo até que ele tenha uma queda, meio segundo após o alvo atingir o chão, o dragão cai em direção ao alvo com grande velocidade, se desmanchando-se no oponente enchendo-o de tinta e causando ferimentos ao mesmo

Ninpou • Sumi Taka (Arte Ladino - Falcão de Tinta): 0
Desc: Usuário do ninpou de tinta, desenha um falcão que caso seja de um tamanho grande o bastante, o usuário pode subir no falcão e voar, porém caso impacte em algo, desmancha rapidamente, pode também permitir que outras pessoas subam em cima e voe com tal falcão, podendo até 2 pessoas subir ao mesmo tempo no mesmo, ou levar bagagem semelhante ao peso e tamanho de 2 homens. Nota: 1EXP=voar 1M de distância de onde foi criado. nota: este ninpou de tinta em especifico é melhor moldável, assim que é criado, ele não faz alguma ação como voar, mas sim fica parado, então usuário pode decidir o que o desenho fará, desde que contenha na desc. Nota: 2M= apenas 1 homem voar, para mais Ladinos ou bagagens voar, deve ser maior.

Ninpou - Dai Sumi Dragon (Arte Ladina - Grande Dragão de Tinta): 0
Desc: Um dragão chinês de tinta grande e comprido é desenhando, o mesmo então pode voar e morder tão forte algum oponente, que retira seus membros, também é capaz de cuspir tinta como cuspisse fogo, a tinta então pode cegar alguém por 1 turno caso atinga os olhos.
nota: este ninpou de tinta em especifico é melhor moldável, assim que é criado, ele não faz alguma ação como morder ou cuspir, mas sim fica parado, então usuário pode decidir o que o dragão fará, desde que contenha na desc.

Ninpou • Sumi Hebi (Arte Ladino - Cobra de Tinta): 0
Desc: Sai cria cobras (todas devem ter o mesmo tamanho) as cobras então dependendo do tamanho, podem entrar em lugares pequenos como fendas, fechaduras, também são capazes de morder alguém, ou enrolar-se em alguém, também carregar em suas costas algo. Nota: este ninpou de tinta em especifico é melhor moldável, assim que é criado, ele não faz alguma ação como voar, mas sim fica parado, então usuário pode decidir o que o desenho fará, desde que contenha na desc. Nota2: Este desenho em especifico pode fazer coisas que não contenha na desc desde que o juiz aceite, tal como poder comer coisas, arrancar pedaços, etc. Nota: 10EXP= 1 cobra

Ninpou - Sumi Nezumi (Arte Ladino - Ratos de Tinta): 0
Desc: Sai desenha ratos que servem para farejar inimigos ou outras coisas assim encontrando-as. Os ratos se espalham por uma área considerável. Eles também podem importunar o inimigo subindo no corpo deles e mordendo-os, embora não cause muito dano eles podem distrair o oponente. Nota: este ninpou de tinta em especifico é melhor moldável, assim que é criado, ele não faz alguma ação como perseguir, mas sim fica parado, então usuário pode decidir o que o desenho fará, desde que contenha na desc. nota2: 1EXP = 1 rato. Nota3: 1EXP = ratos poderem andar  até 3M longe do usuário

Sumi Bunshin no fascínio (Técnica do Clone de Tinta): 0
Desc: Usando sua técnica de tinta, Sai cria um clone. Se o clone for machucado gravemente ele se desmancha parecendo que está derretendo e a tinta fica no chão onde clone foi dissipado.nota: este clone se comporta como técnica de clonagem, não da golpes nem usa nenhum fascinio, é melhor usado para distrações ou algo do tipo, do que em lutas. Nota2: tais clones, 1s depois de serem vitalizados, assumem a aparência leal de seu usuário, não parecem de tinta. Nota3: Este desenho em especifico pode fazer coisas que não contenha na desc desde que o juiz aceite, tal como poder comer coisas, arremessar, etc

Ninpou - Companheiro de tinta: 0
Desc: Usuáro pode fazer qualquer ser, desenhar e dar vida a qualquer coisa que possa imaginar, o algo em questão que foi criado, não ataca e nem serve para usar sua força ou coisas relacionadas, porém seguem o criador por 4 turnos inteiro, após isso, se dissipam, o que usuário pode fazer alguma criatura bizarra medonha que viva atrás de si como um guardião, o que pode espantar alguns oponentes. Nota: 1EXP = as criaturas andarem até 1M longe (seja a frente ou atrás, dos lados, etc) de seu criador
Nota2: Usuário pode optar pelo ser companheiro ter capacidade de voar e deixar ou não rastro de tinta por onde passa (caso usuário não cite tais coisas, por padrão, o ser não irá voar e não deixará rastro)

Ninpou - Armazém de tinta: 0
Desc: Usuário cria qualquer desenho e o da vida (assim como o fascinio companheiro de tinta) porém a função deste tal desenho é carregar coisas, seja bagagens ou pessoas, até mesmo pode agarrar oponentes, porém ainda é frágil, até mesmo uma mordida do oponente na ‘mão’ da criatura, pode faze-la se desmanchar.
Nota: O algo que foi criado não acompanha o usuário, pode ser algo que se locomova até o local que tenha algo que o ser deseje agarrar, porém após agarrar, fica parado e não solta mais.
Nota2: É usado melhor em situações onde se pode criar armadilhas.

Ninpou - Sumi Nagashi (Arte Ladino - Fluxo de Tinta): 0
Descrição: Usuário do ninpou de tinta, cria alguma poça de tinta em algum lugar, seja pintando o local, pingando tinta ou apartir de algum desenho que tenha se dissipado e deixado tinta no local (seja o local chão, teto, etc) quando oponente está próximo a poça, a mesma cria tentáculos que prendem o oponente aonde a poça foi formada
Nota: 1EXP = 1 tentáculo
Nota2: 2EXP = os tentáculos ‘saírem’ até 1M de distância de onde a poça foi criada (máximo 30M)
Nota: É mais uma técnica de desenho/ que os desenhos podem fazer, do que de fato alguma pintura.

Ninpou  Sumigasumi (Arte Ladino • finalização de tinta): 0
Descrição: Os desenhos do usuário então, após saírem do pergaminho, podem se disfarçar de poça de tinta, e quando o oponente esta próximo da aparentemente inofensiva poça de tinta, a poça retoma a sua forma e função para qual foi criada. Nota: O desenho então pode ficar por 2 turnos como poça, após isso, a tinta se resseca e fica inútil.
Nota2: Um desenho dura 2 turnos, mas caso fique em poça por 2 turnos, ainda poderá se transformar em desenho novamente e receberá +2 turnos de vida, como se tivessem acabado de ter sido criados de um pergaminho, isso pode aumentar a longevidade de um desenho, mas igualmente a maioria de todo fascinio do rpg, pode ser feito somente 3x.
Nota: É mais uma técnica de desenho/ que os desenhos podem fazer, do que de fato alguma pintura.

Ninpou Sumi Shawaa (Arte Ladino - Chuveiro de Tinta): 0
Descrição: Usuário ao fazer cada um de seus desenhos, pode os empurrar para cima com a caneta/lápis/etc, os desenhos ao saírem do papel, viajam a muitos metros para o alto e quando no pico de altura, que a tinta toma vida, e então podem cair no chão em cima de algum alvo (pode-se fazer diversos desenhos que voem muito alto, tempo o bastante para fazer o oponente esquecer que usuário desenhou algo, o oponente pode ficar despreparado então, e quando menos esperar, o desenho que o usuário fez a um tempo atrás, cai em cima do oponente)
Nota: 1EXP = jogar os desenhos até 1M para cima
Nota2: este É mais uma técnica de desenho/ que os desenhos podem fazer, do que de fato alguma pintura.

Ninpou - Seabon de tinta: 0
Desc: Usuário faz qualquer desenho, qualquer fascinio, seja o companheiro de tinta, seja clone de tinta ou etc, o desenho então ganhará a função de disparar de sí como um porco-espinho, varias agulhas feitas de tinta, as agulhas são finas então afiadas o bastante para realmente perfurar e até atravessar algum oponente.
Nota: É mais uma técnica de desenho/ que os desenhos podem fazer, do que de fato alguma pintura.
nota2: 1EXP = 1 seabon de tinta disparado de algum desenho.
Nota3: as agulhas são do tamanho de seabons, o tamanho deste não é moldável. 
Nota4: As agulhas podem viajam no máximo até 30M do desenho em que saíram.

0~ _*Categoria - Feitiço Tensoativo*_ : 0
Descrição: O conhecimento das propriedades tensoativas, de química e física Satisfaz o usuário conseguir replicar seu conhecimento aos seus Fascínios, desenvolvendo habilidades específicas sobretudo a Bolhas.
	 - Usando um Soprador de Bolhas (deve comprar na loja, junto com o Refill desejado), Utakata assim pode criar diversos Fascínios com base em transformar o conteúdo do refil para propriedades Tensoativas e realizar feitiços em base disto. 
Nota: Somente caso usuário compre o Soprador + Refill (de qualquer tipo), poderá realizar os fascinios do Feitiço estilo Tensoativo. 
Nota2: Usuário pode manipular a direção de cada bolha, mas somente enquanto enxerga ela. Posteriormente pode deixá-la a deriva dos ventos e da gravidade. 
nota3: caso não tenha Fascínios contrariando tal citação; 1EXP = 1 bolha de sabão
Nota4:  caso não tenha Fascínios contrariando tal citação; 1EXP = as bolhas contiverem raio de 1cm (2cm de circunferência)
nota5: Caso o EXP seja pouco e o tamanho fique pequeno, isso pode tirar a efetividade de alguns fascinios, o melhor tamanho para tais bolhas de sabão são de 30cm a 2M (30 a 200 exp)
Nota6: caso não contenha fascinio contrariando tal citação;1EXP = bolhas viajarem até 1M longe do usuário
Nota7: as bolhas demoram meio a um segundo (1 a 0,5s) para serem criadas.
Nota 8: Caso dono tenha simpatia ao estilo Vindus, é possível basear a velocidade das bolhas na velocidade de seu Vindus. Caso contrário, a velocidade é a da corrida de sua patente. 
Nota 9: Sobre os Fascínios envolvendo explosões ou ácidos, é necessário comprar o Refill de Butano ou o Refill de Ácido. 

Feitiço Tensoativo - Bolhas Explosivas: 0
Descrição: O usuário sopra uma grande quantidade de bolhas de sabão, e depois as manipula para que elas cerquem o alvo. Quando uma destas bolhas se dissipam (seja ao toque ou com ativação do usuário), liberam uma explosão de um raio de 1 terço do tamanho da bolha (divida o tamanho total da bolha por 3 para saber o tamanho da explosão) ex: bolha de 30cm terá uma explosão de 10cm, bolha de 3M=explosão de 1M
Nota: 3EXP = 1 bolha explosiva

Feitiço Tensoativo - O estouro da película de ácido: 0
Descrição: O usuário pode soprar uma grande quantidade de bolhas de sabão, o mesmo manipula elas para próximo ao rosto do oponente e dissipa a bolha, o liquido da mesma em contato com os olhos trás cegueira de 1 rodada (a rodada em que a bolha estoura é a rodada inicial e final da cegueira)

Feitiço Tensoativo - Bolha de Ácido: 0
Descrição: Utakata lança bolhas que quando aprisionam o oponente, As bolhas então sobem e são preenchidas por um líquido branco ou cinza, que na verdade é um ácido que corrói o corpo de quem está dentro. A bolha em seguida explode sem deixar rastros da vítima.
Nota: o EXP deve ser um tanto suficiente para fazer um tamanho de cerca de 2M de circunferência para as bolhas prenderem Ladino adulto, e igualmente um tanto suficiente para a bolha viajar para longe e para o alto evitando que o ácido corroa o próprio usuário
Nota2: O ácido se vapora facilmente após a explosão. 
Nota3: É da escolha do usuário, usar ácido como componente. Também é possível usar quaisquer outros líquidos. 
Nota4: demora cerca de 30 minutos para queimar toda a vítima. Os primeiros 15 são letais, e caso respire/engula, também já é letal. 

Feitiço Tensoativo - Escudo de Bolhas: 0
Descrição: Um escudo Tensoativo com resistência semelhante à melhoria de nível 2 da forja, é feito ao arredor de seus aliados, isolando tais completamente. (conseguiria defender Kunais arremessadas por Noumin)
Nota: Quanto mais resistente a bolha, mais branca ela será. Neste caso, o escudo não é transparente. 

Feitiço Tensoativo - Fascínio do Clone de Bolhas: 0
Descrição: Utakata cria clones que quando atacados estouram como se fossem bolhas.
nota: este clone se comporta como técnica de clonagem, não dá golpes nem usa nenhum fascinio, é melhor usado para distrações ou algo do tipo, do que em lutas.
Notas: leia /r9, seção Notas Gerais, para ver notas de duração e quantia dos clones. 

Feitiço Tensoativo - Bolha Implosiva: 0
Descrição: Utakata cria uma grande bolha que envolve o oponente, Então ele estala os dedos, fazendo com que a bolha imploda com a vítima dentro (o raio da explosão funciona igualmente o fascinio 'bomba de bolhas', a diferença, é que estas estouram somente ao comandar do usuário, e esta "explode de dentro para fora")

Feitiço Tensoativo - Incorporação de Bolhas: 0
Descrição: Utakata cria uma única e grande bolha que envolve-o. Ao seu comando, a bolha começa a flutuar e pode levá-lo para qualquer lugar que deseja. Foi visto que a bolha pode viajar a longas distâncias, e flutua sem nenhum risco de estourar. O usuário pode camuflar a bolha para que todos em seu exterior não enxerguem o que há dentro da bolha. A bolha também pode estourar por ordem do usuário. 
Nota: Apesar de conseguir viajar sem estourar, não é boa o suficiente para funcionar como um escudo, projeteis fortes e pontiagudos arremessados na bolha podem fazer-la estourar facilmente.
Nota2: 1EXP = "Bolha Carona" ter raio de 1M 
Nota3: Somente 4 turnos ou 4 horas de duração, após isso, estoura. 

Feitiço Tensoativo - Bolha Pegajosa: 0
Descrição: Utakata lança diversas bolhas que quando estouram liberam um líquido pegajoso, que pode colar o alvo ao chão ou em algum lugar. O único jeito de descolar-se deste líquido, é esperando 2 turnos, cuja cola fica cada vez mais dura a ponto de que no ultimo tempo se esfarela, liberando o alvo contido.
Nota: O tanto de líquido que saí da bolha é = a ½ (um meio ou metade) do tamanho total da esfera em ‘cl’ (centilitro) (ex: bolha de 100cm libera 50cl do liquido, bolha de 2M libera 1L do líquido)

Feitiço Tensoativo - Ocultação das Bolhas: 0
Descrição: Técnica em que o usuário dispara várias bolhas que flutuam ao redor da face do inimigo, e ao comando do utilizador, explodem liberando uma grande quantidade de fumaça branca para obstruir temporariamente a visão do alvo.
Nota: O tanto de fumaça que sai da bolha é o mesmo raio do tamanho da bolha (ex: bolha de 500exp = bolha de 5M = ao dissipar, fazer uma fumaça em um raio de 5M)
Nota2: A fumaça dura 2 turnos, ou 2 horas
_Nota escondida: somente o primeiro turno / primeiras horas acata em baixa visão, pois com o tempo a fumaça vai se dissipando cada vez mais)_

Feitiço Tensoativo - Explosão das Bolhas: 0 # Descrição: Usuário sopra bolhas em direção a projéteis como kunais ou shurikens, ao a bolha entrar em contato com o projétil, rebate o projétil e o faz cair no chão aonde a bolha parou, porém isto também estoura a bolha. 
Nota: 10EXP = 1 bolha anti-projétil
Nota2: 2EXP = bolha anti-projétil ter 1cm de circunferência 

0~ Feitiçaria Magnética - O Toque Possessor: 0
Desc: Em suma, o usuário aprende a interagir e recriar cargas elétricas (Tornar positivo (desequilíbrio, +Protons - Elétrons), negativo ( - Protons + Elétrons) ou Nulo= (Equilíbrio, mesma qtia. De protons e elétrons)). O Numinous carrega a capacidade desta administração dos Elétrons (Partícula subatômica composta, com valor (spin) Negativo), adicionando ou retirando elétrons, mudando a carga dos corpos que entrarem em atrito direto com o Usuário ou com outro corpo já Magnetizado pelo usuário. 
Nota: O que não sofrer atrito (encostar) no usuário, nem em objeto já Eletrizado por tal, usuário não conseguirá controlar. Entretanto, uma vez em atrito, usuário pode manipular livremente as cargas e elétrons deste algo. 
Nota2: Para afastar algo, as cargas devem serem iguais, e para aproximar, serem opostas. Entretanto, é possível afastar e aproximar sem se preocupar em citar a carga dos corpos, seu Numinous fará "automaticamente" ao seu querer de atração/repulsão, o balanceamento da carga dos corpos de interesse. 
Nota3: 1EXP = Poder afastar/trazer um corpo até 1M longe de você (após o toque nele, claro). Caso afaste algo, ou tente resgatar um corpo 'Possuído eletricamente' por você, estando além do limite de seu EXP, seria como perder o controle deste algo. Então pense 1EXP = controlar um campo elétrico de raio de 1M de você (2EXP = Seu campo aumenta p. Raio de 2M)

0~ Feitiço Geral - Agulhas Guardiãs: 0
Descrição: (Referência: poder de Jiraya) - Conjurador toca em sua testa, em quanto toque é mantido, seus fios de cabelos se unem a cada 20 fios completando em 2 segundos. O Nespiritus então age endurecendo como aço e mantendo a união como forma de engrossar, o comprimento fica maior, e ao final usuário tem cabelo feito finas e afiadas como agulhas. (considerando 150.000 fios de cabelos totais, cerca de 7.500 agulhas são feitas). O cabelo é encurtado e rejeitado quando há outro toque seu em sua testa. Pode ser feito com pelos e até mesmo com outros indivíduos, já que a base para realização é o Numinous do usuário.
Nota: 1EXP= cabelo crescer a 1 centímetro por 0 5 segundos 
Nota2: cabelo possui uma resistência comparada a resistência nível 2 da forja.
Nota3: entretanto, em 4 turnos tudo é desfeito.
	""".replace("\n(", " (").replace("nota", "Nota").replace("\nNota", "Nota").replace("\n desc",
																					   "->Descrição").replace("# ",
																											  "-").replace(
		"\nDescrição", "->Descrição").replace("#desc", "->Descrição").strip().replace("#Desc", "->Descrição").replace(
		"-Descrição", "->Descrição").replace("Desc", "->Descrição").replace("->->", "->").replace(":", ": ").replace(
		"  ", " ")
	return habilidades


def pegar_conjurações():
	habilidades = define_habilidades()
	# Define variável 'conjurações' = dict()
	split_hab = habilidades.split("\n\n")
	conjurações = {}
	nomes_hab = [ ]
	descs_hab = [ ]
	for i, e in enumerate(split_hab):
		# print(i, ">")
		split = e.split("->")
		# print(split)
		nome = split[ 0 ]
		desc = split[ -1 ]
		conjurações[ nome ] = desc
	preços = {}
	for k, v in conjurações.copy().items():
		k_new = k.upper().strip()
		price = k_new.split(
			":")  # Cria lista com Nome e Preço (o nome deve estar antes dos dois pontos ':' e o preço deve estar após)
		p0 = price[ 0 ]
		P1 = price[ 1 ]
		preços[ p0 ] = price(P1)  # Bota em dict, onde nome=Key, preço=Value
		k_new = tuple(price)
		conjurações[ k_new ] = conjurações.pop(k)  # conjurações = dict Key=tuple(['name', price]): Val=str(desc)
		v_new = v.strip().replace("Nota", "\nNota")
	return conjurações


def ver_conjurações():
	conjurações = pegar_conjurações()
	num = 0
	cont = 0
	cont2 = 0
	for K, V in conjurações.items():
		if cont == 0:
			print("""
.\t\t~—__________-<|>-__________—~
.\t\t\t   *HABILIDADES*
.\t\t~—_______________________—~""")
			print("\n\n")
		cont += 1
		cont2 += 1
		Nome = K[ 0 ].strip()
		if "0~" in Nome[ 0:3 ]:
			num += 1
			Nome = Nome.replace("0~", f" *>* ")
			cont2 = 1
			if "JORDUS" in Nome.upper():
				print("""
*~—————~*		
*Conjurações Especiais - Elemento Jordus*
.\t\t\t\t\t\t\t\t\t  *~—————~*\n""")
			elif "VINDUS" in Nome.upper():
				print("""
*~—————~*		
*Conjurações Especiais - Elemento Vindus*
.\t\t\t\t\t\t\t\t\t  *~—————~*\n""")
			elif "VANDUS" in Nome.upper():
				print("""
*~—————~*		
*Conjurações Especiais - Elemento Vandus*
.\t\t\t\t\t\t\t\t\t  *~—————~*\n""")
			elif "BRANDUS" in Nome.upper():
				print("""
*~—————~*		
*Conjurações Especiais - Elemento Brandus*
.\t\t\t\t\t\t\t\t\t  *~—————~*\n""")
			elif "RAYUS" in Nome.upper():
				print("""
*~—————~*		
*Conjurações Especiais - Elemento Rayus*
.\t\t\t\t\t\t\t\t\t  *~—————~*\n""")
			elif "TENSOATIVO" in Nome.upper():
				print("""
*~—————~*		
*Feitiços - Fascínios Tensoativos*
.\t\t\t\t\t\t\t\t\t  *~—————~*\n""")
				print(
					"Feitiços/Feitiçarias não são comparáveis com Ryos, mas sim com R$ dinheiro real, ou VIPs (VIP pode ganhar categoria inteira)")
		Price = K[ -1 ].strip()
		if Price == '0':
			Price = "1 $"
			if "CATEGORIA" in Nome.upper():
				Price = "_$10 ou $20 (para obter TODOS os feitiços desta categoria)_"
		Desc = N.Numinous(V)
		print(f"\n- _{cont} > {num}.{cont2}_ {Nome}: {Price}", f" {Desc}", end="\n")
	return None


def declare_itens(text=None):
	"""
	
	-> declare_itens envolve a captura de itens em um longo texto Fonte, transformando em listas e dicionários, retornando um dicionário.
	
	:param text: opcional str(). Caso sem texto fornecido (None), é pêgo o texto de itens já imbuído na função. Caso fornecido, o texto incluso deve conter as especificações citadas abaixo, sendo então assimilado como Fonte para instanciar o objeto retornado. 
		
	:return: retorna dicionário com múltiplos itens; "itens_with_desc_and_price", onde Key= str("Nome"): Value= list([int(preço), str("descrição")]) 
	
	- O texto Fonte deve ser formado por:
		'Nome_item' + ':' + valor + '#' + 'descrição_item' + '\\n' + 'Nome_item2' ...:
			'Nome_item' = Será a Key em string, formatada pelo Numinous.Numinous(), para o dicionário temporário  'Descrição' e ao dicionários retornado '
			':' ou '-' = indicação de separação entre o nome e o preço (nome a esquerda) : (preço a direita do sinal), para formação de lista [nome, price/desc]
			'valor' = o valor deve ser sem formatação e bem caracteres que atrapalhem sua assimilação, será convertido em INT ao final, e adicionando como valor do item nomeado. 
			'#' imediatamente após o valor, indicativo de separação de Preço (á esquerda deste símbolo) # Descrição (á direita do tal símbolo '#')
			'descrição_item' = Será a descrição do item. Ela pode ser um texto longo, mas de forma alguma deve conter os caracteres [ ':', '-', '#', '\\n']. Ou seja também deve ser em uma única linha, e não ter símbolos indicativos para evitar erros ou indicações indevidas. 
			'\n' = pulo de linha. Ele é o primeiro indicador de separação de itens, separando por cada linha sendo um novo Item (ITEM = " \nNome:val#desc\n ")
		- Indique itens raros com prefixo "Rare", invocações prefixo "Inv.", Diversos com prefixo "¬"
	"""
	if text is None:
		ITENS = """
		Kunai- 10 ryos#
		Kunai Curva-10 ryos
		Shuriken-10 ryos
		Senbons-10 ryos
		Makibishi-10 ryos
		RaiHashis-10 ryos
		Flecha comum/curta(um lote = dois uni)-10 ryos
		Pena para escrita - 10r 
		Vidraça com tinta para pena - 10r
		Hip pouch/bolsa - 50r
		Soprador com sabão - 50r
		Selo explosivo-50 ryos
		Bomba de luz-50 ryos
		Bomba de fumaça-50 ryos
		Bomba de fumaça mineral - 100 ryos
		Fios de aço(1m)-50 ryos
		Guisos-50 ryos
		Pássaro Mecânico-50 ryos
		Pergaminho- 100 ryos
		Fuuma Shuriken-100 ryos
		Shuriken gigante-100 ryos
		Bomba de gelo-100 ryos
		Dardo de injeção(5 uni)-100 ryos
		Antídoto -100 ryos
		Flecha grande(um lote = dois uni)- 100 ryos 
		Bomba de Pimenta -100 ryos
		Tampões de ouvido-250 ryos
		Pano de selamento-300 ryos
		Kusari Fundo-300 ryos
		Shuriken Quadrada-300 ryos
		Mangual-300 ryos
		Ataduras(um Metro)-300 ryos 
		Pergaminho com tinta e caneta - 400r - 
		Pinças de Tesoura-400 ryos
		Nunchaku-500 ryos
		Katana simples-500 ryos
		Bõ - 500 Ryos 
		Arco -500 ryos
		Pesos de treinamento-500 ryos
		Rádio Comunicador (três uni)-500 ryos
		Kusarigama -500 ryos
		Tantõ -500 ryos
		Danko-500 ryos
		Esfera Explosiva-500 ryos
		Bola de Selos Explosivos-500 ryos
		Corrente do Bastão de Vento-500 ryos
		Refill vazio - 500 ryos # Tal qual um cilindro de aço que cabe 500 ML de algum conteúdo, com uma tampa de rosquear. Refill é o cilindro, seu diferencial é a capacidade de retenção e proteção térmica (conteúdo mantém temperatura internamente, e não conduz para a parte externa), também tendo proteção ao odor e totalmente blindado a impactos e vazamentos. Muito útil para guardar venenos, ácidos, gases e estado líquido por temperaturas extremas, etc. Usuário pode especificar os tamanhos da garrafa térmica, sendo de 10 litros o limite de armazenamento. > materiais aço reforçado (externo), Plástico (em espuma), borracha, vidro espelhado reforçado, camada de Vácuo e interior mais vidro.
		Refill com Água - 550 Ryos # O Refill anteriormente citado no /qitens, agora preenchido com água mineral apropriada ao consumo.  > materiais aço reforçado (externo), Plástico (em espuma), borracha, vidro espelhado reforçado, camada de Vácuo e interior mais vidro. Conteúdo = H2O
		Refill de Ácido - 1.000 Ryos # O Refill anteriormente citado no /qitens, agora preenchido com ácido.  > materiais aço reforçado (externo), Plástico (em espuma), borracha, vidro espelhado reforçado, camada de Vácuo e interior mais vidro. Conteúdo = Ácido 
		Refill de Butano - 1.000 Ryos # O Refill anteriormente citado no /qitens, agora preenchido com GLP Gás liquefeito Pressurizado > materiais aço reforçado, Plástico (em espuma), borracha, vidro espelhado reforçado, camada de Vácuo e interior mais vidro. Conteúdo = Butano 
		Katana mediana-1.000 ryos
		Lâminas de kunai-1.000
		Guarda–Chuva-1.000 ryos
		Braceletes de ferro-1000 ryos 
		Boneco de Metal-1.000 ryos
		Armadura de Numinous(protetora) - 1.000 ryos
		Cartões de Informações Ninja (/CDIN) - 1.200 ryos
		Etiqueta de Selamento -1.300 ryos
		Catapulta de Shuriken Gigante-1.500 ryos
		Balista-1.500 ryos 
		Braceletes de selamento-2.000 ryos 
		Espada retrátil-2.000 ryos 
		Alto falante ressonante de eco-2.000 ryos
		Foice-2.000 ryos
		Lançador de agulhas-2.000 ryos 
		Jōhyō-2.000 ryos 
		Tekkõ kagi-2.000 ryos
		Braço de Cabo Retrátil-2.000 ryos
		Garra de Lâmina Tripla Aprimorada-2.000 ryos
		Armadura de Batalha Shinobi-2.000 ryos
		Manoplas de Metal-2.000 ryos
		Lâminas de Chakra - 2.000 ryos
		Cano Elétrico-2.000 ryos
		Hidro–Bomba (dois uni)-2.000 ryos
		Serra Circular de Marionete-2.000 ryos
		Bastão resistente - 2.500 ryos 
		Katana resistente-3.000 ryos
		Kyodai Sensu -3.000 ryos
		Lançador de Pulso-3.000 ryos
		Jidanda-3.000 ryos
		Atirador de Dardos de Injeção-3.000 ryos
		Escudo Retrátil-3.000 ryos
		Corte da Lua- 3.000 ryos
		Hyōtan - 4.000 ryos
		Katana super resistente-5.000 ryos
		Ocarina-5.000 ryos
		Braço de perfuração mecânica-5.000 ryos
		Canhão da Cabeça de Leão-5.000 ryos
		Canhão de Bomba de Chakra-5.000 ryos
		Chaves de Braços verdantes-5.000 ryos
		Traje de Lodo- 10.000 ryos
		Lançador de shurikens-10k
		Lançador de Kunai Portátil-10.000 ryos
		Dispositivo de Rompimento de Chakra-15.000 ryos
		Tsurukame-80k
		Armadura de chakra (absorve)- 100.000 ryos
		Tobishachimaru-200.000 ryos
		Projeto Dois Mil e Quarenta e Cinco 2045- 400.000
		Marionete De Madeira Vermelha - 90K 
		Marionete Formiga Negra- 100k
		Marionete Salamandra- 120k
		Marionete Veloz- 145k
		Marionete Golem- 150k
		Marionete Guardiã- 140k
		Marionete Guardiã Gigante- 160k
		Marionete Abelha Rainha - 195k
		Marionete Base - 240k
		Marionete Escorpião - 280k
		Marionete Automatizada - 300k
		Marionete Mestre/Suprema- 400k
		Rare Kiba (Espadas do trovão) - 400k
		Rare Kusanagi (Espada Serpente) - 400k
		Rare Shibuki (Respingo) - 400k
		Rare Nuibari (Grande agulha) - 400k
		Rare Kabutowari (Rachadora de Elmos) - 400k
		Rare Kuribiribocho (Lâmina do executor) - 400k
		Rare Hiramekarei (Espadas gêmeas) - 400k
		Rare Gunbai (Arranjo do Exército) - 400k
		Inv. Gamatasu-600.000 ryos
		Inv. Gamaken-600.000 ryos
		Inv. Gamahiro-600.000 ryos
		Inv. Gamariki-600.000 ryos
		Inv. Gama-600.000 ryos
		Inv. Gamagoro-600.000 ryos
		Inv. Gamaken-600.000 ryos
		Inv. Gamamaru-600.000 ryos
		Inv. Gamariki-600.000 ryos
		Inv. Gamatatsu-600.000 ryos
		Inv. Gekomatsu-600.000 ryos
		Inv. Gerotora-600.000 ryos
		Inv. Kosuke-600.000 ryos
		Inv. Shima-600.000 ryos
		Inv. Gamakichi-600.000 
		Inv. Ikari wa Hebi(Cobras Raivosas) - 500.000
		Inv. Jya - 600.000 ryos
		Inv. Jay Ermida - 600.000 ryos
		Inv. Kyodaijya - 600.000 ryos
		Inv. Aoda-600.000 ryos
		Inv. Serpentes de três cabeças-700.000 ryos
		Inv. Yamata cobra de várias cabeças - 800.000
		¬ Aliança fajulta: 10ryos
		¬ Buquê de flores simples:10 ryos 
		¬ Papel de presente simples: 10 ryos 
		¬ Vestido fajulto: 50 ryos
		¬ Terno fajulto: 50 ryos
		¬ Papel de presente: 50 ryos 
		¬ Aliança de namoro: 50 ryos 
		¬ Aliança de noivado: 100 ryos 
		¬ Buquê de flores: 100 ryos
		¬ Vestido: 500 ryos 
		¬ Terno: 500 ryos 
		¬ Buquê de flores de luxo: 500 ryos
		¬ Aliança de casamento: 1.000 ryos
		¬ Vestido de casamento: 1K
		¬ Terno para cerimônias: 1K
		¬ Tratamento médico: 1.000 ryos
		¬ Aliança de diamante: 2.500 ryos 
		¬ Certidão de responsabilidade para ter PETs: 5.000 ryos 
		¬ Transplante oficial: 20.000 ryos
		¬ Casa comum: 40K
		¬ Casa com cerquinhas brancas: 65K
		¬ Casa gótica: 65K
		¬ Mansão: 80K 
		¬ Terreno para casa: 80K 
		¬ Terreno geral: 90K
		¬ Seguro Eterno(metade do valor do item pago todos os meses): 0
		¬ Seguro mensal(Valor inteiro do item pago uma vez): 0
		¬ Seguro diário(Valor do item ÷ Sete, pago todos os dias): 0 #(Valor do item ÷ 7. Prazo de 24 horas. Compra acumulada, gasta uma unidade por vez. Ou seja, caso compre 2 seguro diário para um mesmo item, significa que este item será assegurado por 2 dias) 
		€ Espingarda: 9000 # 9K/5EXP 
		€ Carabina: 9000# 9K/5EXP  
		€ Metralhadora: 40000 #40K/5EXP 
		€ Submetralhadora: 12000 # 12K/5EXP  
		€ Fuzil de assalto: 20000 # 20K/5EXP 
		€ Rifle Sniper: 25000 # 25K/5EXP 
		€ Revólver: 8000 # 8K/5EXP  
		€ Pistola: 6000 # 6K/5EXP 
		€ Taser: 5000 #5K/5EXP 
		€ Stun Gun: 4000 # 4K/5EXP
		€ Eletrodos para Taser: 500r 
		€ Bateria para Taser e Stun Gun: 900r
		€ Tripé: 1000
		€ Silenciador: 5000
		€ Munição(12 uni): 2500
		€ Extensor de mira: 1000
		€ Binóculo 20*50: 1000
		€ KIT manutenção de armas: 1000
		€ Colete a prova de balas: 1000
		€ Coldre: 30r 
		€ Algema ultra forte: 850r  
		€ KIT Primeiros–Socorros: 700r 
		€ Combustível para fogo 1L: 600 Ryos 
		€ Bússola: 500r 
		€ Sinalizador: 500r 
		€ Corda de alpinismo: 400r
		€ Luz química: 50r 
		€ Capacete com proteção facial: 350r
		€ Amolador de facas: 300r 
		€ Pá: 200r  
		€ Picareta: 200r 
		€ Canivete: 170r 
		€ Soco–Inglês: 170r 
		€ Capacete tático: 170r
		€ Esqueiro Zippo: 50r
		€ Ponteiro a laser quente: 80r # Objeto preto cilíndrico se assemelha com punhal de espada. Com 3cm de circunferência e 20cm de comprimento. Em sua ponta, contém saída de luz, em quanto em sua outra ponta, há tampa de rosquear para se colocar bateria. No meio do objeto, há um pequeno botão de 5mm. Ao pressionar, libera uma luz extremamente forte e fina — O laser disparado alcança 10KM; o comprimento de sua onda é de 450nw; e sua potência de 50.000MW.  — O tamanho do feixe de luz é de 10mm — A cada 4 segundos o feixe parado em um ponto fixo, aumenta a temperatura deste ponto em 40°C — Caso o laser fique aceso por mais de 40 segundos (1.600°C), a caneta se queimará. — O resfriamento da caneta demora o dobro do tempo em que você utilizou. Caso não espere o tal tempo, a caneta queimará. — Apenas 3 segundos, já é suficiente para cegar alguém, queimar fósforo, ascender gás volátil. Veja /r10, e a temperatura de combustão de cada matéria para verificar os segundos necessários para causar danos em cada material do oponente > Materiais Bateria, ferro, cobre eletrólito, aço silício, vidro
		""".strip()

	# - - - Computação do texto-fonte passado como parâmetro - - - #
	elif text is not None:
		if "\n" not in text:
			print(
				F"ERRO. Não foi detectado nenhuma quebra de nova linha no texto-fonte. Impossível realizar separação dos itens. ")
			return None
		elif ":" not in text or "-" not in text:
			print(F" ERRO. Não foi detectado separador de nome ':'  preço")
			return None
		ITENS = text

	# --- Code ---#
	Descrição = {}
	Itens = ITENS.strip().split("\n")  # separa os itens em listas [item valor], [item2 valor2]
	for n, e in enumerate(Itens):
		""" Sempre que houver um dos símbolos ":" ou "-", separa em 2 onde string antes de ":" seria nome, e string após ":" seria valor.' """
		# - - - Separação [Nome, Preço/Desc] - - - 
		if ":" in e:
			a = e.split(":")
		elif "-" in e:
			a = e.split("-")
		else:
			# Caso não seja possível realizar separação:
			print(f"{Itens[ n - 1 ]}\ndel >{Itens[ n ]}<")
			del Itens[ n ]
		# - - - Cria chave = Nome do item (formatado) - - - #
		chave = a[ 0 ].title().replace("  ", " ").replace("*", "").replace("SASUKE", "").replace("NINJA",
																								 "LADINO").replace(
			"CHAKRA", "NESPIRITUS").replace("KONOHA", "REINO DA FOLHA").strip()
		chave = N.Numinous(chave)
		# - - - Separa o Preço da Descrição - - - #
		valor_desc = a[ 1 ].split("#")
		# Aloca a descrição (Deve ser o texto logo em seguida ao sinal de hashtag '#'):
		Desc = valor_desc[ -1 ]
		if "#" not in e:
			Desc = "Sem_Descrição"
		# - - - Cria o valor = preço como Value da var dicionário 'Descrição' e 'itens_with_...price' - - - #
		val = price(valor_desc[ 0 ].lower().replace("k", "000"))
		# val = valor do item (separado entre 'nome:' e '# descrição'), sempre deve ser Number
		Descrição[ chave ] = list([ float(val), Desc ])

	# - - instância variável 'itens_with_desc_and_price' 
	itens_with_desc_and_price = Descrição
	return itens_with_desc_and_price


def declare_cardapio(font=None):
	if font is None:
		cardápio = """
			# Especial 
			Rodízio de doces - 150
			Rodízio de sal (carnes, churrasco, pratos) - 250r
			Rodízio de aguardente (cerveja, vinho, drinks) - 150r
			Rodízio de Anã - 300r
			# Sal
			Lámen simples- 15ryous
			Lámen completo- 30ryous
			Lámen com verduras- 20ryous
			Lámen com bacon- 20ryous
			Lámen com ovos- 20ryous
			Lámen grande- 30ryous
			Lámen extra grande- 40ryous 
			Lámen médio- 25ryous
			Lámen pequeno- 10ryous
			Guioza- 12ryous
			Rolinho primavera- 9ryous
			Rolinho primavera vegano- 9ryous
			Arroz chop suey- 6ryous
			Yakisoba de carne/porção- 17ryous
			Yakisoba de carne e frango/porção- 17ryous
			Carne com brócolis- 30ryous
			Frango xadrez- 30ryous
			Frango agridoce com legumes- 30ryous
			Porco agridoce- 30ryous 
			Pastel carne/frango/queijo - 5ryous
			Pizza/inteira- 40ryous
			Pizza Fatia - 6 ryous
			Lasanha- 28ryous
			Salgados de festa (coxinha, risole, queijo etc) - 1 ryous 
			strogonoff - 25r
			porção de Picanha - 40r
			porção de alcatra - 30r
			Porção de Batata frita - 19r
			Porção de mandioca frita - 20r
			salada - 10r
			Dogão - 12r
			Hambúrguer - 13r
			# Doces 
			Dango/uni- 3ryous
			Mitarashi/uni- 3ryous
			Manju/bandeja- 13ryous
			Ichigo Daifuku/uni- 5ryos
			Crepe japonês- 4ryous
			Taiyaki/uni- 4ryous
			Dorayaki/bandeja- 16ryous
			Anpan/uni- 3ryous
			Yukimi Daifuku- 3ryous
			Kompeito- 9ryous
			Kakigori pequeno- 8ryous
			Kakigori médio- 10ryous
			Kakigori grande- 12ryous
			Warabi Mochi/pedaço- 4ryous
			Monaka/bandeja- 6ryous
			Konnyaku Jelly/pacote- 8ryous
			Ohagi/uni- 3ryous
			Bolo comum- 10r
			Bolo de aniversário- 20r
			Bolo com nome- 25r
			Bolo personalizado- 50r
			Bolo de casamento- 100r
			Bem-casado(5 uni) - 10r
			Brigadeiro de festa- 1r
			Beijinho de festa- 1r
			Bala de coco/açúcar- 1r
			Tartaruguita - 1r
			Danoninho - 2r
			# Bebidas (450ml)
			Sorvete (tigela pequena) - 5r
			Sorvete (casquinha) - 3r
			Sorvete (tigela grande) - 15r
			Suco de abacate- 3ryous
			Suco de caju- 3ryous
			Suco de uva- 3ryous
			Suco de manga- 3ryos
			Suco de melão- 3ryous
			Suco de laranja- 3ryous
			Suco de laranja e acerola- 3ryous
			Suco de mamão- 3ryous
			Suco de maracujá- 3ryous
			Suco de pêssego- 3ryous
			Suco de abacaxi- 3ryous
			Suco de abacaxi com hortelã- 3ryous
			Suco de morango- 3ryous
			Suco de melancia- 3ryous
			Suco de limão- 3ryous
			Café- 4ryous
			Leite- 3ryous
			Café com leite- 5 ryous
			Toddynho- 4ryous 
			Refrigerante- 2ryous
			Água mineral- 3ryous
			Água gaseificada-6ryous
			Água c/ gás-6ryous
			Água da torneira-1ryous
			# Doses (50ML)
			Maria mole- 5ryous
			Gin- 4ryous
			Whisky - 4ryos
			Vodka - 3ryos
			Canelinha/hifive - 3ryos
			51 - 2 ryos
			# Taças (350ml)
			Espumante - 7 ryos
			Champanhe - 5 ryos 
			Hoppy- 3ryous
			Shochu - 4
			Shukurimu- 4ryous
			Taça Vinho tinto - 7 ryos 
			Taça Vinho branco - 8 ryos 
			Taça Vinho gaseficado - 6ryos 
			Taça vinho seco - 5
			# Garrafas
			Garrafa vinho seco- 35 
			Garrafa vinho gaseficado - 36 
			Garrafa Vinho tinto - 37 
			Garrafa vinho branco - 38
			Garrafa 51 - 20
			Garrafa cantinho do vale- 20
			Garrafa wisky - 34
			Garrafa Gin - 34
			Garrafa vodka - 34
			Garrafa askov - 16
			Garrafa energético - 13
			Garrafa de saque chinês - 30
			Garrafa refrigerante - 6
			# Cervejas
			Cerveja 1L - 10r
			Cerveja 710ML - 7
			Cerveja 500ML - 6r
			Cerveja 350 ML - 5r
			Torre de Chopp - 20ryos
			Cerveja preta - 7ryos
			Cerveja artesanal - 9 ryos/500ml
			Cerveja amanteigada - 7ryos/500ml
			Cerveja sem álcool - 5 ryos/1L
			Shopp artesanal do N.W.M - 10r/1L
			# Fumos
			Cigarro-7ryos o maço (qualquer marca)
			Caximbo de tabaco-5ryos
			Narguille - 4ryos (uso no local) 
			Charuto - 5ryos
			# Drink
			Cigarrin do mal - 5 pila
			Caipirinha de (limão/morango/maracujá)-5 ryos
			Sharingan mery-8ryos
			Whisky suer-8ryos
			Kurama suer- 10ryos
			Batida branca - 7 ryos
			Drink N.W.M (forte) - 10r
			# Outros
			Chimarrão - 9ryos
			Energético - 3 ryos
			Porção de asinha - 10 ryos
			Porção de batata frita - 9ryos
			Porção mandioca frita - 8 ryos
			Pastel - 5 ryos 
			Pizza - 30 ryos 
			Brotinho - 16 ryos
			Esfiha - 10 ryos 
			Tortuguita - 1 ryo
			#  Cafeteria
			Leite - 2r
			Chocolate quente - 3r
			Chocolate gelado - 3r
			Caramelo quente -3r
			Chocolate com caramelo- 4r
			Frapppucino - 10r
			Cappucino- 5r
			Ice coffe- 4r
			Coffe Macchiato- 5r
			Coffe Caramel-5r
			Flat White-5r
			Mocha_ 5r
			Dippio- 2r
			Cafe puro - 2r
			Café com leite - 4r
			Chá gelado - 5 ryos 
			Chá - 4 ryo
					""".strip()

	cardápio = cardápio.split("\n")
	car3 = {}
	for i, e in enumerate(cardápio):
		e = e.strip().title()
		e = N.Numinous(e)
		if "#" in e:
			cat = e.replace("#", "¬")
		else:
			namexprice = e.split("–")
			name = namexprice[ 0 ]
			preço = namexprice[ -1 ]
			preço = price(preço)
			car3[ name ] = [ preço, cat ]
	cardápio = car3
	return cardápio


def declare_all_itens():
	"""
	
	-> Declara variável com os itens padrões (declare_itens()) e itens especiais (declare_eventos())
	
	:returns: dict 'all_itens' 
	"""
	# instância variáveis:
	itens = declare_itens()
	eventos = declare_eventos()
	cardápio = declare_cardapio()
	all_itens = {}
	# - - - Captura var 'itens' 
	for K, V in itens.items():
		all_itens[ K ] = V
	# - - - Captura var 'eventos'
	for K, V in eventos.items():
		all_itens[ K ] = V
	# - - - Captura var 'cardápio'
	for K, V in cardápio.items():
		all_itens[ K ] = V
	return all_itens


def organiza_allitens():
	"""
	
	referência das variáveis "Eventos", "Itens" e "Cardápio" 
	"""
	dict_all_itens = declare_all_itens()
	itensAZ = [ ]  # itens em ordem alfabética A a Z
	its = [ ]
	for k, v in dict_all_itens.items():
		preço = str(v[ 0 ])
		nome = k.title().strip()
		preço = price(preço)
		its.append([ preço, nome ])
		itensAZ.append(f"{nome}: {preço} $")
	itensAZ.sort()
	for i, e in enumerate(itensAZ.copy()):
		itensAZ[ i ] = F"{i} > " + e

	# print(*itensAZ, sep="\n")
	# Organiza todos itens pelo preço (menor - maior)
	its.sort()
	# print(its)
	sor = sorted(its, key=lambda *its: its[ 0 ])
	itens01 = dict()
	# transforma em dicionário:
	for i, e in enumerate(sor):
		k = sor[ i ][ 0 ]
		v = sor[ i ][ 1 ]
		itens01[ v ] = k
	return [ itensAZ, itens01 ]


# organiza_allitens()

def materiais():
	lis = "madeira, papel Kraft, argila, carvão vegetal, ouro, ferro, diamante, Mischmetal, zinco, cobre eletrólito, couro, pena, seda, plástico Polietileno, vidro comum Float, Silicone, Tinta Acrílica, TNT, aço, fibra de carbono, Pólvora negra, hidrogênio, Vidro, Silício, Luminol, Aço Reforçado, Ácido, Butano".title().strip().split(
		", ")
	itens = declare_itens()
	dic = {}
	for k, v in itens.items():
		Desc = v[ -1 ].title().strip().replace("(Blindado)", "").replace("Reforçado", "").replace("Espelhado",
																								  "").replace("Vácuo",
																											  "").replace(
			"Interior", "").replace("Interno", "").replace("Exterior", "").replace("Camada", "").replace("De",
																										 "").replace(
			"Mais", "").replace("Externo", "").replace("Em", "").replace("Espuma", "").replace("  ", "").replace("(",
																												 "").replace(
			")", "").replace("E", "").replace("=", "").replace("Conteúdo", "")
		mate = Desc.replace("Materiais", "").replace("Materiais:", "").strip().split(">")[ -1 ]
		conteúdo = mate.strip().split(", ")
		k = k.strip().replace("\n", "").title()
		if "Sem_Descrição" not in conteúdo:
			dic[ k ] = conteúdo
	for k, v in dic.copy().items():
		for element in v:
			if element not in lis:
				print(f" - rerirado '{element}' de '{k}' ")
				search = dic[ k ].index(element)
				del dic[ k ][ search ]
		if dic[ k ] == [ ]:
			del dic[ k ]

	print(dic)


# materiais()


def ver_itens(descrição=False, apenas_dados=False):
	itens = declare_itens()
	allitens = declare_all_itens()
	eventos = declare_eventos()
	c = 0
	dic = {
		"elite": [ "€", 0 ],
		"invocações": [ "Inv.", 0 ],
		"raros": [ "Rare", 0 ],
		"marionetes": [ "Marionete", 0 ],
		"diversos": [ "¬", 0 ],
		"PIB": [ "?", 0 ],
		"min": [ "?", 0 ],
		"max": [ "?", 0 ],
		"média": [ "?", 0 ],
		"resto": [ "?", 0 ]}
	# simple = {}
	for k, v in itens.items():
		if 0 == c and apenas_dados is False:
			print("""
.\t\t\t┏•━•━•━ ◎ ━•━•━•┓
.\t\t\t\t*Arsenaria*
.\t\t\t┗•━•━•━ ◎ ━•━•━•┛ 
	\n	""")
			min = max = PIB = v[ 0 ]
			min_k = max_k = k
		c += 1
		valor = v[ 0 ]
		Desc = v[ -1 ].replace("–", "\n–").replace("> Materi", "\n> Materi")
		nome = k.title().strip().replace("\n", "")
		# Separa as categorias e guarda os dados:
		for key, element in dic.items():
			categoria = "arsenal".upper()
			if element[ 0 ] in nome.split(" ")[ 0 ]:
				dic[ key ][ -1 ] += 1
				categoria = key.upper().strip()
			if dic[ key ][ -1 ] == 1 and not apenas_dados and categoria != "ARSENAL":
				print("\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n")
				print(f".\t*{categoria}:*\n")
				if categoria in "ELITE" and apenas_dados is False:
					print("""
> SOMENTE INDIVÍDUOS COM MÉRITO DE ELITE, OU ENTÃO, INDIVÍDUOS SEM FASCÍNIOS KERINOUS/HARINOUS/ELEMENTAIS, PODEM COMPRAR DESTA CATEGORIA.\n
Armas: \n (NOTA¹: Em sua compra, você deve citar o nome, fabricante e cartucho (de acordo com a vida real) \n NOTA²: Independente da marca, sua arma será baseada em tiro de repetição. Para "upar" ela para Semi-automatica ou automática, vá na forja do Iõ \n NOTA3: Independente da marca, poder, tudo, o preço será de acordo com a categoria de arma (Pistola, Rifle Espingarda, etc.); e não seu fabricante\n NOTA⁴: Igualmente para munição: na compra, cite seu calibre, para qual arma servirá, e seu formato/nome).\n\n""")

		# simple[nome] = valor
		if max < valor:
			max = valor
			max_k = nome
		if min > valor and valor > 0:
			min = valor
			min_k = nome
		if valor > 0:    PIB += valor
		if c == itens.__len__():
			média = round(PIB / itens.__len__(), 2)
			dic[ "PIB" ] = [ "?", PIB ]
			dic[ "max" ] = [ max_k, max ]
			dic[ "min" ] = [ min_k, min ]
			dic[ "média" ] = [ f"PIB/{c}", média ]
		# Mostra:
		if not apenas_dados:
			if descrição:
				print(f" _¬{c}-_ > {nome.replace('Inv.', '').replace('€', '').replace('¬', '')}:  *{valor}*\n{Desc}",
					  end="\n\n")
			elif not descrição:
				print(f"{nome.replace('Inv.', '').replace('€', '').replace('¬', '')}: {valor} r", end="\n")

	# max = simple[max(simple, key=simple.get)]
	# min = min(simple)
	if not apenas_dados:
		print(f"\n.\t~-______________________-~\n")
		print(
			f" Existem {c} itens no total, sendo:\n Invocações: {dic[ 'invocações' ][ -1 ]} \n Raros: {dic[ 'raros' ][ -1 ]} \n Marionetes: {dic[ 'marionetes' ][ -1 ]} \n Diversos: {dic[ 'diversos' ][ -1 ]} \n Elite: {dic[ 'elite' ][ -1 ]}\n Arsenaria\n Com  restantes.\n")
		print(
			f"Mais caro: {dic[ 'max' ]}\n Soma de todos os preços: {dic[ 'PIB' ][ -1 ]}\n Menor valor: {dic[ 'min' ]},\n Média: {dic[ 'média' ][ -1 ]}")

	return dic


# print(ver_itens( ))


def temporária():
	text = """
	Kunai- 10 ryos
- espécie de faca de arremesso que mede cerca de 20 a 40cm, pode ser usada em luta corporal ou a distância. 
- após comprar ninja adquire técnica shurikenjutsu (técnicas de espadas de mão) 
> Materiais: Aço, Madeira
 

Shuriken-10 ryos
- objeto pontiagudo, normalmente com 5 pontas afiadas, feita para combate a distância, pode medir de 10 a 20cm. 
- após comprar ninja adquire técnica shurikenjutsu (técnicas de espadas de mão) 
> Materiais: Ferro
 
Senbons-10 ryos
- como agulhas maiores de metal, podem medir de 3 a 10cm
- serve tanto para combate corporal como a distância. 
- após comprar ninja adquire técnica shurikenjutsu (técnicas de espadas de mão) 
> Materiais: Ferro
 
Makibishi-10 ryos
- objeto pontiagudo pequeno de 3 a 5cm
- quando jogadas ao chão, quase que não se percebem, e os inimigos podem acabar pisando nelas e tendo feridas dificultando o caminhar 
> Materiais: Ferro
 

Flecha curta(lote de 2 uni)- 10 ryos
- Flechas pretas ou marrons de 45cm a 90cm 
- Pode ser usado para ataques corporais, a distância como lanças ou com maior força e precisão com um arco
> Materiais: Madeira, Aço
 
Pena para escrita - 10r 
- isto nada mais é, do que uma pena branca, onde seus fios possuem uma tamanho de 20cm, contem uma ponta dura em uma das extremidades, é usado esta ponta para molha-la com tinta e poder rabiscar em algum lugar.
- Precisa comprar a tinta, esta pena é solo, sem tinta.
> Materiais: Pena
 
Vidraça com tinta para pena - 10r
- Isto é um pote de vidro transparente ou levemente azulado, que parece preto graças a seu conteúdo interno, onde o pote tem um formato que lembra um diamante dos desenhos (formato hexaquisoctaédrica ou faceta) onde a extremidade menor (fim ou começo do diamante, onde se assemelha a um cone ou triângulo) possui uma rosca, ao gira-la, usuário tem acesso ao conteúdo da vidraça (a tinta) a abertura é pequena o bastante para não vazar muito porém grande o bastante para poder molhar uma pena com a tinta - porém pode-se imaginar uma simples vidraça quadrada com tampa também de vidro.
- Contém 8cm de largura e comprimento, com 500ml de tinta dentro
> Materiais: Vidro blindado, Tinta
 
Hip pouch/bolsa - 50r
- É parecido com uma esfera ou mochila redonda com raio de 80cm, em uma pintura de cinza, com um cinto de 2M ajustável, cujo torna eficaz a possibilidade de amarrar a bolsa em qualquer lugar, seja na cintura, na perna ou até nas costas.
- cabe qualquer item de menos de 80cm dentro (kunais, shurikens, bombas e selos explosivos, tinta, pergaminhos pequenos, etc)
> Materiais: Couro
 
Soprador com sabão - 50r
- Um item com formato peculiar, cujo aparenta ser um trompete ou saxofone que também lembra um galho, sua cor dá a entender que é feito de madeira,
- Contém um cabo relativamente fino de 35cm, uma das extremidades é mais aberta gradualmente, com circunferência de 10cm, o que da a aparência de trompete. Junto.
- Este é um item que pode fazer com que qualquer líquido vire bolha, o usuário pode cuspir dentro do cabo, o que trará suprimentos para que quando assoprar em tal, consiga sair bolhas.
- As bolhas feitas por este podem ter qualquer tamanho, porém somente compradores de ninpou de bolhas de sabão conseguirão realizar jutsus com tal objeto.
> Materiais: Madeira
 
Selo explosivo-50 ryos
- um selo, como um papel retangular que mede de 5 a 15cm, que ao ser acionado através de chakra, pode explodir. 
- feito para combate a distância (explosão de 1 a 5M de destruição) 
> Materiais: Papel, TNT, Substância Energizada
 
Bomba de luz-50 ryos
- Tal como uma pequena bolinha cerca de 5cm de diâmetro, possui o desenho de um manuscrito, o mesmo ajuda na ação em que o usuário escolha quando ela possa ser ativada (explodida) emitindo de longe chakra para o selo da bomba, levando-a a explodir
- Quando ativadas liberam uma luz tão radiante que podem cegar o inimigo, usadas para escapar do inimigo ou armadilhas, 
- A menos de 3metros da bomba a vitima fica cega por 3 rodadas (contanto a inicial) de 4 a 7M fica por 1 turno, de 8 a 11M fica 1 turno porém com visão, tal visão é enxergar nada além de 5M de distância. 
> Materiais: ???(temporariamente não listado) 

Bomba de fumaça-50 ryos
- tal como uma pequena bolinha cerca de 10cm de diâmetro, possui o desenho de um manuscrito, o mesmo ajuda na ação em que o usuário escolha quando ela possa ser ativada (explodida) emitindo de longe chakra para o selo da bomba, levando-a a explodir
- Quando detonadas liberam uma cortina de fumaça que ajuda o ninja a escapar
- Tal cortina de fumaça dura por 1 turno, uma bolinha dessas cobre uma área de 5M, mais bombas de fumaça podem aumentar a área a ser afetada pela fumaça 
> Materiais: ???(temporariamente não listado) 
 

 
Fios de aço(1m)-50 ryos
-fios de aço extremamente resistente em comprimento medem 1 metro e tem largura quase que um fio de cabelo. 
-bons em combate a curta distância 
> Materiais: Aço
 
Guizos-50 ryos
- espécie de sino circular que mede cerca de 2 a 5cm.
- muito utilizado em treinos, distrações ou ninjas que manipulam o som.
> Materiais: ferro
 
Pássaro Mecânico-50 ryos
- Semelhante a um brinquedo de corda um pássaro amarelo de 10cm
- mais útil em missões o passado pode voar até 1Km de distância do chão na velocidade de um humano correndo, pode colocar pergaminhos na boca do mesmo que ele leva para o local desejado
- bom em combate a distância, uma manada destes pode atrapalhar a visão do oponente, caso o pássaro encoste em algo cai no chão e quebra.
> Materiais: Ferro, Plástico, Tecnologia
 
Pergaminho- 100 ryos
- Tal como um pedaço de pano branco ultra resistente e flexível (não tem tamanho padrão, ao comprar você escolhe o tamanho, caso não cite um tamanho, será o original) tamanho original: de 1M de cumprimento e 60cm de largura com finura de papel, com bordas avermelhadas 
- pode colar um pergaminho no outro para ficar maior em cumprimento ou largura
- 1 É feito para selar itens dentro dele, caso consiga fazer um pergaminho grande o suficiente com um selo/kanji de selamento escrito nele, tudo que encostar no pergaminho irá para dentro dele em um limbo como se fosse um céu que parece que está caindo infinitamente, mas nunca varia sua velocidade.
- 2 fora selar É usado também para invocar coisas, por exemplo, caso você tenha um item da ficha, você poderá invoca-lo a partir de um kanji (manuscrito) com o nome que se remeta a tal item
- 3 selamento avançado - você pode até mesmo selar pessoas ou seres como bijuus dentro disto caso tenha um pergaminho grande-o quanto, para invoca-lo a qualquer hora da batalha (precisa do acordo “roubo de corpo”)
- 4 selamento avançado permanente - faz com que ao selar tal ser, no final da luta, você ainda tenha o ser ou oponente selado no pergaminho, podendo invocar em outras lutas, o oponente não cenará na luta, mas você cenará como se fosse ele, em seu turno (precisa do acordo “roubo de corpo” para você cenar como ele, caso não tenha tal acordo, a pessoa deve entrar na batalha e ela mesma cenar em até 1H após ter sido invocada, caso contrário, você pode cenar no lugar)
> Materiais: Papel, Madeira, Borracha, Substância Energizada
 
Fuuma Shurikens Gigante -100 ryos
- espécie de shuriken porém maior podendo chegar a 2M de cumprimento de uma ponta a outra, tem 4 pontas e um furo no meio onde geralmente é onde botam as mãos. 
- suas 4 lâminas podem ser dobradas para guardar de forma melhor. 
- pode ser usada em combate corpo a corpo ou a distância. 
  > Materiais: Ferro
 
 
Flecha gigante(lote de 2 uni) - 100 ryos
- Tal como uma flecha de aço preto de 3M de cumprimento e 20cm de grossura com penas de 30cm e pontas triangulares afiadas para fincar em pedras
- Não é efetivo em ataque corporal, seu peso faz ser ataques mais lentos que causam uma desvantagem, são melhores usadas com o item balista.
> Materiais: Aço
 
Bomba de gelo-100 ryos
-  tal como uma esfera cristalina azul cerca de 10cm de diâmetro, possui o desenho de um manuscrito, o mesmo ajuda na ação em que o usuário escolha quando ela possa ser ativada (explodida) emitindo de longe chakra para o selo da bomba, levando-a a explodir
- quando detonadas, lançam um torrente, centenas de espinhos de gelo a um raio cerca de 6M do local. 
> Materiais: ???(temporariamente não listado) 
 
Dardo de injeção(5 uni)-100 ryos
- das penas até a ponta são 10cm, sendo 1cm das penas atrás, 5cm do tambor que contém substância (caso não bote veneno neles, virão sem substância alguma) e 4cm de agulha
- assim que o dardo acerta um alvo, o veneno entra na corrente sanguínea da vítima
- podem ser lançadas a mão ou com o item lançador de dardos de injeção
> Materiais: Pena/Papel, Ferro
 
Antídoto (uni)-100 ryos
- um frasco parecido com um dardo de injeção, contém 8cm, sendo 5cm o tambor que fica o antídoto e 3cm de agulha
- pode tomar o antídoto de várias formas, tomando ele o ninja abre e ingere, e a mais comum encostando a agulha no paciente envenenado fazendo o antídoto ir pela corrente sanguínea do paciente.
- Para fazer efeito você deve envenenar o antídoto com algum veneno (ex: veneno paralítico) ao envenenar o antídoto na forja, você contem o antídoto do veneno paralítico, podendo por exemplo curar um aliado, caso você não bote o veneno no antídoto, ele será inutil e não irá curar nada (precisa comprar antídoto e botar o veneno que quer a cura nele, é assim que se consegue cura de algum veneno)
> Materiais: Ferro
 
Bomba de Pimenta (uni)-100 ryos
- Tal como uma pequena esfera vermelha de 5cm que após estouradas (com chakra) fazem uma fumaça em raio de 1M, quem inala tal fumaça fica por 2 turnos com visão limitada a 10M e forte ardências na garganta, nos pulmões e nos olhos, confundindo os sentidos.
- Alguns usuário usam a bomba de pimenta em sí mesmos pois sua forte composição faz o usuário acordar de qualquer genjutsu dado que instiga os sentidos de quem respira o gás apimentado, acordando de genjutsus.
> Materiais: ??? (temporariamente não listado) 
 
lâminas de chakra -100 ryos
- tal como um soco inglês, ou um punhal que vc bota os dedos, porém, com uma lâmina em baixo. Mede aproximadamente 10 a 15cm. 
- feito de um aço especial adere a energia do chakra facilmente, quando energizado seu poder de corte aumenta em centenas de vezes 
- útil em combate corpo a corpo e em longa distância por poder ser arremessado. 
> Materiais: Aço, Substância Energizada
 
Tampões de ouvido-250 ryos
- Tal como um pequeno algodão laranja que é introduzido no canal auditivo para impedir a passagem de sons que podem ser prejudiciais tal como genjutsus a base de sons
- Parte ruim que quer usuário fica menos capaz, não pode usar seus sentidos de audição para interpretar localização de oponentes entre outras coisas que são ocasionadas ao tampar os ouvidos.
> Materiais: Borracha

Pano de selamento -300 ryos
- Tal com uma cartolina, ou uma toalha pode ter o tamanho que o ninja quiser (especifique na hora do uso) o padrão é ter 1M de comprimento e 10M de largura.
- Um material resistente que só pode ser rasgado com itens que podem aumentar sua capacidade de corte. Se assemelha a um papel tal como o material das ataduras, porem maior e com uma pequena taxa de elasticidade extra.
- Usado bastante para prender oponentes tal como mumificar (embalar) os mesmos, eles enrolam rapidamente tal pano na vitima e é quase que impossível de escapar quando a vitima fica toda amarrada. Quando a vitima toda embrulhada fica parecendo um casulo.
> Materiais: Papel, Madeira, Borracha, Substância Energizada
 
Kusari-Fundoo-300 ryos
- uma espécie de corrente feita de aço resistente com pesos de 50cm ligados à cada extremidade, tal corrente tem um comprimento de 30M no total
- útil em combate a longa e média distância.
- após comprar ninja adquire técnica Kusarigamajutsu (técnicas de kusarigama)
> Materiais: Aço
 
Mangual-300 ryos
- uma arma que contem 3 partes; cabo, corrente e esfera, uma coisa ligada a outra, sendo assim, o cabo tem cerca de 30cm, corrente de 3M e uma bola com cerca de 50cm de circunferência, tal bola é repleta de relevos pontiagudos tal como espinhos. 
> Materiais: Madeira, Ferro
 
Ataduras(1m)-300 ryos 
-cumprimento de 1M e largura de15cm 
-uma espécie de faixa branca normalmente usuário enrola no corpo em lugares estratégicos para deixar o local mais rígido tal nas mãos deixar um soco mais forte. 
- muito resistente, usuários Kami ou sannins podem aderir chakra aos bandages fazendo-os levitar e cortar até mesmo rochas. 
> Materiais: Borracha, Papel
 
Pinças de Tesoura-400 ryos
- Tal como uma tesoura grande de 35cm com lâminas de de 20cm e cabos de 15cm
- É tão forte que pode cortar o braço de um ninja, ou usar a tesoura como uma espécie de faca impulhalando o alvo sem abrir e fechar as laminas
- após comprar ninja adquire técnica shurikenjutsu (técnicas de espadas de mão)
> Materiais: Aço
 
Pergaminho com tinta e caneta - 400r
- Como todos pergaminho, podes definir o tamanho do mesmo
- se assemelha a um pano com tecido que lembra um papel, contém 2 faces sendo uma branca levemente amarelada cujo serve para escrever ou desenhar, a outra face do papel é vermelha e as vezes com detalhes dourados ou pretos ou de outras cores. Em uma das laterais, contém um cano aparentemente de madeira, cujo contém uma tampa que sai, ao retirar a tampa, dentro do cano há tinta, e a tampa é uma caneta que já sai molhada com tinta ao desrosquiar do pergaminho
- o pergaminho vem enrolado em si mesmo/no cano, não estraga na água, é um pergaminho usado por Sai onde ele faz seus desenhos.
> Materiais: Papel, Tinta, Ferro, Madeira
 
Nunchaku-500 ryos
- se assemelha a 2 bastões de ferros de 30cm unidos por uma corrente de mais 30cm. Ponta a ponta medem aproximadamente 90cm
- boas em combate corporal 
> Materiais: Ferro, Borracha, Madeira
 
Katana simples-500 ryos
- espécie de espada japonesa. A diferença dessa é que o material não é reforçado e quase todo tipo de tentativa de estrago, quebra ela. 
-  sua lâmina mede 1m e cabo 30cm
- especializada em combate corpo a corpo. 
- após a compra, o ninja adquire habilidade de kenjutsu (técnicas com espadas) 
> Materiais: Ferro, Madeira
 
Arco -500 ryos
- um arco de aproximadamente 1M feito de ferro ou madeira. 
- precisa comprar munição (flechas-10ryos)
- após comprar ninja adquire técnica kyüjutsu (técnicas de arco) 
> Materiais: Ferro ou madeira (cite na ficha a escolha), Borracha
 
Pesos de treinamento-500 ryos
- se assemelham com uma fita adesiva branca, ao amarrar essa fita no braço por exemplo, tal item faz pressão no local e pode deixar o material, objeto, membro pesado. 
> Materiais: Couro, Aço
 
Bō - 500 Ryos
- bastão de madeira de aproximadamente 1M
- útil em muitas técnicas, e em combate corpo a corpo 
- após comprar ninja adquire técnica bōjutsu (técnicas do bastão) 
> Materiais: Madeira
 
Rádio comunicador (3 uni)-500 ryos
- algo como um fone de ouvido com um microfone que geralmente fica na gola da roupa. 
- tal item aceita muitas frequências e para ativá-lo basta apertar o botão que fica próximo ao pescoço do usuário. 
> Materiais: Plástico, Tecnologia, Borracha, Ferro
 
Kusarigama -500 ryos
- uma espécie de foice (cabo de 30cm e lâmina de 25cm) com uma extensa corrente com cerca de 29 metros na extremidade de baixo (que fica longe da lâmina) 
- boa tanto em combate corpo a corpo quanto a distância.
- após comprar ninja adquire técnica Kusarigamajutsu (técnicas de kusarigama) 
> Materiais: Ferro
 
Tantõ -500 ryos
- Tal como uma pequena espada parecendo mais uma faca pelo seu tamanho, tem lamina de 20cm e cabo de 10cm, seu tamanho pode facilitar em muitas coisas como ataques rápidos onde não se deve demorar muito para sacar tal arma.
- após a compra, o ninja adquire habilidade de kenjutsu (técnicas com espadas) 
> Materiais: Aço
 
Danko-500 ryos
-Tal como uma lança/espada em forma de cruz, contem um cabo de 30cm com 2 protetores de mão na parte de cima de cada lado, sua lamina tem cerca de 1M, porém, o cabo contem um botão, quando acionado libera uma corda entre a lamina e o cabo, tal corda tem cerca de 29M, podendo arremessar a lamina para longe, o cabo pode enrolar vitimas, quando o botão é pressionado novamente, a corda se retrai em questão de segundos (cerca de 2s) com a lamina ligada de volta ao cabo.
- útil em combate corporal ou a longa distancia.
- após a compra, o ninja adquire habilidade de kenjutsu (técnicas com espadas) 
> Materiais: Ferro
 
Esfera Explosiva-500 ryos
- Uma esfera preta de 1M de circunferência 
- Tal esfera pode ser arremessada com as mãos ou com catapulta de shuriken gigante
- Ao lançar tal esfera ela explode ao encostar em algo, fazendo uma explosão que atinge tudo num raio de 7M de distância de onde explodiu 
- pode lançar kunais até 10M de distância de onde explodiu (ninja precisa ter as kunais e especificar quantas) 
> Materiais: Papel, TNT, Ferro
 
Bola de Selos Explosivos-500 ryos
- Uma esfera branca do tamanho da bomba de luz (5cm) porém, toda coberta de selos explosivos
- O fato de ter muitos selos explosivos (aproximadamente 50) faz a explosão ser mais potente, atingindo tudo até 7M de distância
- pode ser ativada do ar (com selos de mão), ou quando encostar em algum alvo
> Materiais: Papel, TNT, Substância Energizada
 
Katana mediana-1.000 ryos
- espécie de espada japonesa. A diferença dessa é que o material é pouco mais reforçado (quebra também caso em choque com outra igual ou superior).
-  sua lâmina mede 1m e cabo 30cm
- especializada em combate corpo a corpo. 
- após a compra, o ninja adquire habilidade de kenjutsu (técnicas com espadas) 
> Materiais: Aço
 
Guarda-chuva Mecanico-1.000 ryos
-Tem aparência de um guarda-chuva comum, geralmente com cabo e lona preta, porém, como todo item ninja, o guarda-chuva também pode ser letal. sua lona (resistente o bastante para impedir fogo, jatos fracos de água e golpes relativamente fracos de itens como espadas ou kunais) tem cerca de 1M de circunferência, e seu cabo 1,3M.
- Seu cabo possui 2 botões, 1 deles quando acionado, dispara seabons da ponta da frente do guarda-chuva, podendo disparar 4 disparos por vez e 8 a cada meio segundo, pode ser usado como uma arma semi-automática. (precisa comprar os seabons)
- Fora o botão dos seabons, o cabo tem outro botão de trava, que faz com que a extremidade do cabo se solte do guarda-chuva, virando assim, uma espada que tem 1M.
- usuário pode acoplar outras coisas como lança-chamas ou hidro-bomba, oque fará sair fogo ou água da ponta do guarda-chuva. os seabons serão arremessados junto com a água ou fogo . caso não tenha nenhum desses itens (lança-chamas, hidro-bomba, seabons) oque realmente vem junto com o guarda-chuva é somente a espada, o resto, deve ser acoplado.
> Materiais: Aço, Fibra de carbono, Borracha
 
Braceletes de ferro-1000 ryos
- são um par de braceletes de ferro reforçado que ficam em volta do braço do usuário começando nos pulsos e terminando próximo ao cotovelo, tem espinhos não tão afiados, mas caso acerte alguém com considerável força, pode fazer estragos.
> Materiais: Ferro
 
Armadura de chakra(protetora)1.000 ryos
- Armadura que protege dos pés até ombros feita de aço cinza-branco reforçado que flui chakra
- Não tem as mesmas propriedades que armadura de chakra que absorve, porém, danifica quase tudo que encosta nela, caso oponente encoste a mão, será como se estivesse encostando no fogo queimando parcialmente a mão do oponente, isso quer dizer que qualquer objeto que encoste será desgastado seja kunai, espada, etc, perdendo sua capacidade de corte (precisa reparar a ferramenta após ela encostar na armadura, pois fica quase que inutil) 
- não chega a carburar o item, mas desgasta, sendo assim, uma golpe forte pode até atravessar a armadura, mas não irá matar o usuário da armadura pois o item será menos capaz
- em troca de tal propriedade que desgasta, a armadura não é tão resistente, quase todo golpe pode encostar no usuário, mas não será tão letal (não é útil contra jutsus)
> Materiais: Aço, Substância Energizada
 
Cartões de Informações Ninja - 1.000 ryos
- Tal como um cartão alaranjado atrás e branco com informações na frente de 25cm de cumprimento e 10 de largura e fino como papel
- não é usado com arma, mas é tão poderoso quanto pois cita informações importantes do ninja requerido
- para usar, cena na batalha algo parecido ao “pego um card de informação ninja para saber de tal lutador” o lutador em questão deverá preencher com o comando “/cdin” e botar pelo menos metade das informações que podem ser botadas ali.
- Geralmente é usado no primeiro turno e diz informações úteis para usar na batalha com o oponente.
> Materiais: Papel
 
Etiqueta de Selamento -1.300 ryos
- Tal como um selo retangular com 10cm de altura, 5 de largura, é normalmente vermelho ou branco com manuscritos desenhado em tal selo, o tamanho do selo não importa muito, pois ele pode envolver coisas gigantes.
-Quando colado em algo (oponente, objeto, areia, ferramenta, etc) o selo se expande tal como vira um papel grande o suficiente para que envolva todo o objeto, o selo então fica parecendo como uma bolsa preta em volta de algum material, do lado extremo oposto (ou seja, se colocou na testa de alguém, o extremo oposto seria a nuca.) o material preto tem uma pequena bolinha branca, quando acionada (como um botão) o selamento pode se desfazer. Para impedir isso os ninjas colocam outro selo neste lado oposto também para reforçar a selagem.
- usado tanto a curta como longa distancia, pois o utilizador pode arremessar o selo em algo como no oponente, tal selo ira colar nele, e para impedir que o inimigo descole, rapidamente emitindo chakra para tal selo, faz o selo cumprir sua função de selagem.
- o processo de selagem pode ser interrompido pelo usuário, ou, caso algo assim que a selagem estiver quase completa, tal como um dedo interrompendo o caminho da selagem (sempre de acordo com o juiz)
- o processo em objetos pequenos (cerca de 1 a 1,5M) terminam mais rapidamente a selagem tal como se fosse na velocidade de um raio. em objetos maiores podem demorar mais.
> Materiais: Papel, Borracha
 
Catapulta de Shuriken Gigante-1.500 ryos
- Tal como uma catapulta normal que usa uma especie de colher/concha especial para lançar shurikens gigantes, mede cerca 10M de comprimento e 5M de largura, possui rodas, pode armazenar até 6 shurikens gigantes e jogar 2 a cada 60 segundos (tempo para colher voltar ao lugar) pode-se arremessar de 50M até 500 metros de distancia numa força mortal sobre-humana em uma velocidade de 200KM por hora.
- Pode usar esfera explosiva como munição
> Materiais: Ferro, Borracha
 
Balista-1.500 ryos
- Tal como uma ferramenta besta (arco) gigante de 3M com rodas que dispara flechas gigantes de até 3M para uma distância de 300M
- Pode lançar até 3 flechas gigantes de uma só vez (precisa comprar flechas gigantes)
- tempo de recarga é de 5s, pode arremessar flecha gigante com tanta força para atravessar uma rocha.
> Materiais: Ferro, Borracha
 
Braceletes de selamento-2.000 ryos
- mais como uma técnica que um item. Após comprado, tem a técnica de invocação de armas. 
- basicamente, o usuário pode fazer uma arma até grandes desaparecerem simplesmente envolvendo 1 dedo em cada extremidade do item e fechando suas mãos até se encontrarem. 
- após os itens serem selados, o ninja pode escrever uma marca de invocação(kanji) em algum lugar(pergaminho), e simplesmente tocando nessa marca, ou emitindo chakra para o kanji, O item será rapidamente invocado 
> Materiais: Ferro, Substância Energizada
 
Espada retrátil-2.000 ryos
- uma grande espada cinza de material resistente e afiado que quando dobrada em 3 tem o tamanho de 10cm de largura e 1.3M de comprimento. Porém, quando aberta a lâmina tem 30cm de largura e 1.30m de cumprimento
> Materiais: Aço
 
Alto falante ressonante de eco-2.000 ryos
- aparência de um grande bracelete de ferro com buracos, aproximadamente 30cm
- tem outros nomes tais como broca de som. Ao ter algum ruído ou barulho perto de tal item, como um eco, o item faz o som parecer centenas de vezes mais alto, podendo assim, confundir o inimigo e caso ele esteja muito próximo, deixá-lo com os sentidos básicos (som, visão, percepção) em risco por alguns segundos.
- Caso usuário não esteja com tampões de ouvido também será afetado.
> Materiais: Ferro
 
Foice-2.000 ryos
- Foice japonesa, se assemelha a uma kunai curva pois não é muito grande. geralmente contem uma lamina resistente preta.
- sua lamina mede cerca de 20 a 30cm, e cabo de aço preto normalmente enfaixado com 30cm de comprimento.
- pode ser usada tanto a curta como longa distancia arremessando-a.
> Materiais: Aço
 
Lançador de agulhas-2.000 ryos
- Tal como uma arma de pulso, se assemelha a uma pulseira com 5 relevos, é de tais relevos que saem os sebons, atras de cada relevo também contem um fio de 5cm a 10cm, cada fio libera um seabon do relevo. Puxando os 5 fios juntos pode-se arremessar 5 seabons de uma só vez com uma precisão mortal, com uma velocidade maior do que com as mãos também. pode-se arremessar 5 seabons a cada 2 segundos (tempo para os fios voltarem no lugar após puxados)
- o equipamento em geral tem comprimento o bastante para enrolar no braço, perna etc, os relevos tem cerca de 2cm, largura de cada faixa de 2cm, cada faixa (faixa = faixa + relevo + fio) pode armazenar até 100 seabons. 
 > Materiais: Aço
 
Jōhyō-2.000 ryos
- Tal como um apito pois assopramos tal item. mede cerca de 10cm de comprimento e 3cm de largura, se assemelha a um graveto, porem, assoprando dentro dele, sai uma corda de 29M de comprimento junto com uma “isca” uma agulha na ponta do fio. se o sopro for forte o bastante o fio pode atravessar um humano, não necessariamente precisa assoprar, pode arremessar a agulha com as mãos em quanto segura o “apito”
- É mais usado para enrolar vitimais tal como arremessar a agulha na vitima e fazer a agulha girar em volta da vitima. 
> Materiais: Cano: Madeira. Dardo: Ferro e pena. Corda: fio de aço
 
Garra de Lâmina Tripla Aprimorada-2.000 ryos
- semelhante a garras de onça porém artificial, tem um corte muito potente. 
- tamanho das garras de 20 a 30cm
- especializadas em combate corpo a corpo, são aprimoradas com chakra do usuário. 
> Materiais: Aço

Armadura de Batalha Shinobi-2.000 ryos
- É uma armadura feita de couro reforçado geralmente vermelha ou azulada
- protege pouco a cima dos joelhos até o pescoço, toda kunai, shuriken, seabon etc que chegar a mais de 15M de distância da armadura serão rebatidos, caindo no chão.
- Protege ataques comuns de espadas onde a lamina vem horizontalmente (de lado), porém, caso a lamina venha de frente, vindo a ponta a armadura, o local rasga e facilmente acerta e fere quem usa a armadura.
> Materiais: Couro, borracha

Lâminas de Chakra de Konoha(chakura tõ)-2.000 ryos
- Tal como um punhal com lâmina cinza-escura de 20cm e cabo preto de 20cm com uma tsuba(guarda) com símbolo de konohagakure de 3cm
- feito de material resistente que conduz chakra tornando-a mais afiados a ponto de cortar uma árvore ou um ninja com somente 1 golpe aumentando sua resistência também.
> Materiais: Aço, Substância espiritualmente energizada

Cano Elétrico-2.000 ryos
- tal como um cilindro aparentemente de bamboo, mede cerca de 60cm com 10 a 20cm de circunferência. 
- usado para meios de comunicação a distância, o usuário bate com a base do cano no chão, e libera um raio do cano que pode ir até 30M de distância.
- em combate a longas distancias, pode dar pequenos choques em inimigos tal como meio de distrair. 
> Materiais: Não listado (tratado como madeira) 

Hidro-Bomba (2 uni)-2.000 ryos
- tal como uma mochila com 2 cilindros de água e mangueiras, no total tem 100L de água que pode ser usada. mangueiras de 2M que vão desde suas costas (onde ficam os cilindros) até suas mãos. 
- normalmente é acoplado em marionetes, porém, diferente da serra circular, usuários também podem utilizar. 
- poderoso o bastante para cortar uma rocha desde que esteja até 10M do usuário, coisas entre 10 a 15M de distância da água são quebradas e causa arranhões, mais de 15M empurra e causa pequeno hematoma, mais de 25M causa quase nada. 30M somente molha. 
> Materiais: Ferro, Tecnologia 

Serra Circular de Marionete-2.000 ryos
- semelhante à uma shuriken de 8 pontas, é ligada à uma forma de energia como um motor que geralmente fica nas costas da marionete, sua lâmina tem cerca de 60cm de circunferência 
- tal objeto só pode ser usado por marionetes, tal como fica acoplado no lugar das mãos, ou onde usuário da marionete quiser acoplar. 
- util em combate corpo a corpo 
> Materiais: Aço, tecnologia 

Bastão resistente - 2.500 ryos
- bastão de ferro reforçado de aproximadamente 1M
- útil em muitas técnicas, e em combate corpo a corpo 
- após comprar ninja adquire técnica bōjutsu (técnicas do bastão)  
> Materiais: Aço 

Katana resistente-3.000 ryos
- espécie de espada japonesa. A diferença dessa é que o material é reforçado e resistente a quase todo tipo de tentativa de estrago. 
- mede de 1m a 1,30m
- especializada em combate corpo a corpo. 
- após a compra, o ninja adquire habilidade de kenjutsu (técnicas com espadas) 
> Materiais: Madeira, Aço 

Kyodai Sensu -3.000 ryos
- um tipo de leque gigante que pode ter  de 2 a 3M de largura e 1 a 2m de altura ponta a ponta. Feito com material super resistente que corta, pode proteger ataque de de kunai. 
- ótimo em ataques corpo a corpo ou a média distância. 
- após comprar ninja adquire técnica Tessenjutsu (técnicas com leques)
> Materiais: Fibra de carbono, Seda, Couro, Madeira 

Lançador de Pulso-3.000 ryos
- Tal como uma arma pode ser acoplada tanto por humanos como em marionetes, pode disparar qualquer tipo de bomba e selo (bomba de luz, de pimenta, de fumaça, explosiva etc) são 8 canos que geralmente usuários botam em volta de seus braços 
> Materiais: Aço, Tecnologia, Couro 



Atirador de Dardos de Injeção-3.000 ryos
- material de aço resistente
- do cabo a ponta do cano 80cm
- Se assemelha a uma sniper ou fuzil, contém uma mira que pode enxergar tudo que esteja 30M de distância perfeitamente bem
- tem mais precisão em tiros podendo acertar até mesmo uma mosca parada, usado para atirar dardos de injeção
> Materiais: Aço 

Escudo Retrátil-3.000 ryos
- Material de ferro resistente 
- fechado 30m de comprimento, aberto, 30cm de circunferência 
- bom em combate corpo a corpo 
- Semelhante a: escudo de braço circular. É um escudo que fecha e expande, geralmente fica amarrado no braço dos ninjas, abre rápido o bastante p parar uma kunai que estava um pouco longe de si (uns 5M longe já protege). 
> materiais: Aço, Couro



Hyōtan- 4.000 ryos
- estilo de baga, uma cabaça, de aproximadamente 1m a 2m (famoso amendoim do gaara) 
- vem vazia, somente se vc tiver jutsu de areia, na compra, vem com areia. 
- pode armazenar em medida líquida cerca de 300L. 
> Materiais: Argila 

Katana super resistente-5.000 ryos
- espécie de espada japonesa. A diferença dessa é que o material é  extremamente reforçado e resistente a  Todo tipo de tentativa de estrago. 
- mede de 1m a 1,30m
- especializada em combate corpo a corpo.
- após a compra, o ninja adquire habilidade de kenjutsu (técnicas com espadas) 
> Materiais: Fibra de carbono, Couro 

Ocarina-5.000 ryos
- uma espécie de gaita e flauta, com aparência de uma esfera achatada com buracos, aproximadamente 20 a 30cm 
- serve em maior objetivo tocar uma melodia, Shiin conseguia melhorar em várias vezes seus sintidos, poderes e habilidades de sua família simplesmente tocando uma Certa melodia. 
> Materiais: Ouro 

Braço de perfuração mecânica-5.000 ryos
- Acoplação apenas a fantoches (marionetes)
- Tal como um braço cinza porém as mãos contém dedos afiados que giram individualmente para fazer furos pequenos, ou todos os dedos se juntam para fazer um buraco do tamanho de um braço.
> materiais: Aço, Tecnologia, fibra de carbono 


Canhão de Bomba de Chakra-5.000 ryos
- Tal como uma bazuca preta de 1M que arremessa bolas azuis de chakra de 30cm de circunferência, que ao encostarem no alvo, faz um buraco do tamanho da esfera no alvo, qualquer item que seja feito de chakra ou energizado com chakra pode ser usado como defesa para tais esferas. 
> Materiais: Aço, substância Energizada



Traje de Lodo-5.000 ryos - por 10K
- Tal como uma armadura verde-água que protege dos pés aos ombros, ela é extremamente eficiente pois qualquer ataque que não quebra ela, fica para o usuário.
- Explicando: É feita de um material borrachudo e aderente, até viscoso, caso uma kunai acerte ela a mais de 10M de distância, a kunai não vai ultrapassar a roupa, mas ficará grudada nela, sendo assim, o usuário pode usar e roubar as armas usada contra ele
- Golpes de espadas láterais na horizontal a espada fica aderida a rouba, caso seja golpe com a ponta da espada de frente, acerta o usuário, ataques mais de perto como menos ou igual a 10 metros de distância podem causar dano a armadura e acertar usuário.
> materiais: Couro, material não listado 



Lançador de Kunai e shurikensPortátil-10.000 ryos
- espécie de arma, se assemelha a uma bazuca com saída retangular, e disparos de metralhadora, ou seja, rápidos, precisos e seguidos (precisa comprar munição) 
- mede cerca de 1M 
- especializado em combate à longa distância. 
> Materiais: Aço, Borracha 

Dispositivo de Rompimento de Chakra-15.000 ryos
- Tal como uma pequena esfera preta de 10cm de circunferência, usuário posiciona ela no chão pré-configurada para sua vontade
- Os meios de configurar demora 3 segundos, usuário pode fazer a esfera criar um campo de força ativado por um simples selo de mão, o campo de força é um domo azul de um raio de até 30M de onde foi posta criando um domo que fecha todas as direções frente, lados, baixo, cima. Tudo que fica dentro de tal domo fica impossibilitado de usar chakra, no caso, oponente, até mesmo usuário que ficar dentro fica sem jutsus por 2 turnos.
- Ao configurar o usuário pode decidir o raio de circunferência que o domo será criado, sem configurar é inúltil.
- a pessoa precisa estar totalmente dentro do domo, o domo dura 2 turnos, após isso o dispositivo se sobrecarrega e apaga, libertando o que tem dentro. 
- O domo não é um campo com força, qualquer coisa pode passar por ele, exceto chakra, Chakras muito fortes tal como de uma bijuu não são contidos e o domo apaga na hora após encostar em chakra da mesma (afeta jinchuriki sem transformação)
- Dispositivo quebrado faz o domo se apagar também.
> Materiais: Tecnologia, Ferro, Substância quebra energia 

Tsurukame-80k - por 50k
- Tal como uma armadura como um casco de tartaruga, pode ser deixada nas costas ou na frente do usuário, repele kunais entre outras coisas pois é feito de metal resistente 
- é repleto de buracos de 20cm de diâmetro, de tais buracos podem sair até seabons 1.000 seabons por segundo, dos mesmos buracos podem sair fios de aço que agarram quem estiver próximo a armadura (precisa comprar os seabons e fios de aço)
> Materiais: Metal, Tecnologia, couro

Armadura de chakra (absorve)- 100.000 ryos
- armadura de um material ultra forte parecido com material das lâminas de chakra. 
- o utilizador de tal armadura consegue conter alguns ataques variados que utilizam ou não, chakra. Um exemplo são as próprias lâminas de chakra, que ao chegarem perto da armadura, perderiam, ou diminuiriam totalmente sua energia de chakra que foi concentrada nas lâminas. 
- protege estando a 3M de explosão de selo explosivo, todo arremesso comum de projeteis comuns (flechas, kunais, etc) são protegidos, ataques corpo a corpo não quebra armadura mas usuário sente o golpe, não defende golpes muito fortes menos comuns
- Caso usuário de tal armadura seja atingido com algum item forjado que contém algum jutsu, o ataque é realizado, porém, o jutsu de tal item é cortado, não funcionando contra armadura.
- isso não impede o usuário de utilizar chakra em jutsus ou etc. Somente ataques externos são "desenergizados". Sendo assim, tanto naruto como Sasuke já foram vistos quebrando tal armadura com aspectos que utilizam chakra, oq dá a entender que há um limite a ser absorvido. 
> Materiais: Metal, fina camada de fibra de aço, Substância Absorve Energia 

Tobishachimaru-200.000 ryos
- Tal como um balão voador/ dirigível zeppelin com 2 grandes balões de 200M de cumprimento carregando uma cesta como um navio em baixo, navios de 150M de comprimento, 30M de largura e 30 de altura, podendo ocorrer lutas no próprio navio.
- voa em velocidade de até 70km/h e a 5KM de altura do chão, pode acomodar 60 pessoas e pode levar praticamente qualquer item da loja dentro dele tal como até catapultas para torna-lo uma Orca de combate
> Materiais: Madeira, Seda, Couro, Tecnologia, Aço, Vidro blindado, borracha, papel

2045 - 500.000 ryos
- Assim que você compra e seu card de compra é válidado no banco, sua conta bancária é duplicada e fica abaixo da sua, porém tachada e italica
- caso você morra permanente em uma luta cujo o acordo morte perm não estava em ascensão, a sua conta principal é apagada, você realmente morre, porém... É criado um clone seu a partir de algum DNA, o clone é totalmente igual a você, e você passa a controlar ele, ou seja, você morre, porém com um porto-seguro, cujo todo seu dinheiro e EXP que ficará com seu clone (que agora é você) é os mesmos ryos e EXP que tinha quando você comprou o item '2045' 
- todos seus itens que você tinha, são dados de volta ao clone, exceto os itens que você levou para a batalha cujo morreu (caso tenha levado todos para a batalha, então não terás nenhum item de volta) 
- ao se tornar um clone, na sua ficha, acima de "pp:" deve botar a área "clone:" e citar qual número de clone é (caso tenha morrido 1x e este é seu primeiro clone, então ficará "clone: 1" caso tenha morrido mais vezes e já teve vários outros clones, deverás citar o número de clones que já teve, contando o atual) não esqueça do negrito em tal área.
Materiais: Não-listado 


Marionetes


Marionete De Madeira Vermelha- 90k
- Aparenta ser um tronco vermelho de madeira de 3M de altura e circunferência de 1M, sem olhos nem nada, somente um tronco, que porém, contem 5 divisórias giratórias em tamanhos iguais, cada divisória contém 1 braço de um lado, e de outro, uma fresta cuja pode sair projéteis de até 30cm comprados pelo usuário.
- Se assemelha a um boneco de treinamento de taijutsu.
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
> Materiais: Madeira, substância energizada 

Marionete Formiga Negra- 100k
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
- rosto em forma de balde com 3 olhos e tem 2 chifres, possui 6 braços (patas) e um corpo em forma de barril de 3M que pode prender ninjas.
- cada membro é um punhal, sendo assim, usuário pode arrancar braço de tal e usar como faca
> Materiais: Tecnologia, Substância Energizada, Aço, Couro 

Marionete Salamandra- 120k
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
- salamandra se assemelha a um lagarto, têm 3 olhos sendo 2 em cada lateral outro em cima da cabeça, tem 5M de cumprimento
> Tecnologia, Substância energizada, Aço

Marionete Veloz- 145k
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
- Tal como uma formiga, suas 6 patas podem girar, possui 2 olhos, tem cerca de 2M.
> Materiais: tecnologia, substância energizada, aço 

Marionete Golem- 150k
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
- tem o formato de um homem de 3 metros, possui 2 olhos
> Materiais: Aço, Substância energizada, tecnologia 


Marionete Guardiã Gigante- 160k
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
- tem formato de um homem com 10 metros, possui 3 olhos,
 > Materiais: Aço, Substância Energizada, Tecnologia 

Marionete Inseto do Zumbido da Abelha Rainha- 195k
- Marionete com formato de uma abelha de 5M
- É capaz de voar (longitude definida por exp igualmente 99% de toda marionete) fora voar, a marionete aparentemente de aço, tem um ferrão de 30cm que pode crescer e virar algo como uma lança de 250cm ou 2 metros e meio (ou seja, a marionete fica então com 7,5M) a mesma também é capaz de arremessar por um buraco em sua barriga, itens menores ou iguais a 50cm com forte precisão, a mesma também é capaz de soltar jatos pressurizados de água e vento pela sua boca, que caso acerte o inimigo nos primeiros 5M, pode cortar (após 5M a pressão perde efeicácia e não é cortante) suas asas podem expelir fogo a até 1M de distância.
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
> Materiais: Couro, Fibra de carbono, Substância Energizada, tecnologia, aço 

Marionete Base- 240K
- É uma base de marionete, não uma marionete em si, cujo serve para tornar pessoas vivas ou mortas em marionete
- Se assemelha a uma base de ferro com 1M de circunferência, nos primeiros 30cm possui uma vara na vertical de 20cm de circunferência e altura de 1M, cujo pode ficar com até 5M de altura. 
- Sendo assim, qualquer pessoa, corpo, objeto que subir na base, a vara aparentemente de madeira, cria braços de madeira também que agarra o alvo em 13 articulações, sendo pés inteiros, joelhos, cintura, mãos inteiras, cotovelos, ombro, peitoral e pescoço . A pessoa fica presa, tudo que dono da marionete base deve fazer agora, é ter o jutsu de fios de chakra, e conecta-lo a cada articulação citada ou somente 1 fio conectado na marionete base.
- Ao conectar algo na marionete base botando alguém na base (espaço de 70cm) a base se retrai e os pés do alvo já presos, toca o chão, sendo assim, desde que o usuário contenha fios de chakra, pode controlar tanto aliados como oponentes com ajuda de tal base.
- Somente jutsus kkg (coração, olhos etc) podem ser feitos com a ordem de quem controla as marionetes, jutsus elementais, hij, aprendidos etc, não
 - após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
> Materiais: Madeira, Aço, Substância Energizada 

Marionete Escorpião/casca de humana - 280k
- Esta marionete é a marionete cuja Sasori ‘vivia’ Sendo assim, é uma marionete que pode facilmente se passar por um humano caso controlador seje bom, possuí cabelo vermelho, 2 olhos e estatura humana com altura de aproximadamente 165cm ou 1,65M
- Não há vida dentro de tal marionete (sasori não vem lá dentro) porém a mesma é capaz de realizar diversos métodos de ataques
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
> Materiais: não listado, Substância Energizada 

Marionete Automatizada- 300k
- é uma marionete com formato de um humano com braços longos e uma corcunda, contém 1 olho e aparentemente é feita de aço.
- Tal marionete possui uma ampla variedade de ataques, contra-ataques, etc, começando por suas mãos que contém garras afiadas de até 30cm, também carrega explosivos em si, que caso fogo fique por mais de 5s no corpo da marionete, ela se explode e tudo a um raio de 30M é afetado, a marionete pode ativar em seu braço braço direito algo parecido com o canhão de esferas de chakra, já no braço esquerdo, um escudo que vai crescendo e em até 2s forma uma barreira de 5M de largura e altura e espessura de 5cm feito de metal (proteje ataques de não-jutsus (itens) desde que o ataque tenha partida a 20M do escudo, oq significa que ataques corporais de perto podem facilmente destruir o escudo) a marionete também é capaz de dar saltos de até 30M sem que seja abalada pelo impacto, possui versatilidade para subir em lugares altos, usando suas garras como apoio que a faz escalar construções.
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
> Materiais: Aço, Tecnologia(impermeável), Substância Energizada 

Marionete Mestre/Suprema- 400k
- Marionete com 4 cabeças, 2 contém 3 olhos, as outras 2 contém 2, no total, são 10 olhos, possui 50 metros.
- Usuário quando pretende usar a marionete suprema, não liga fios de chakra a ela, mas sim, fica 1 turno inteiro com suas 2 mãos transmitindo chakra para a marionete, usuário não pode retirar as mãos por um turno inteiro nem usa-las para outra coisa. Com isso, o usuário da vida novamente a marionete Suprema, a mesma deve ser controlada de um método diferente de todas as outras…
- Quando a Marionete Suprema volta a vida, uma ordem nova é realizada (por ex: clebin é o dono da marionete, a ordem estava 1-joãozihn, 2-clebin, quando marionete revitalizada, fica; 1-joãozin, 2-clebin, 3-Marionete suprema) já que a marionete suprema não pode ser controlada, todo turno em que a marionete for usada, ela deve atacar pelo menos 1 vez o seu dono, mesmo que seja apenas um empurrãozinho em seu dono e um jutsu fatal no oponente, porém de qualquer jeito, deve atingir seu dono pelo menos 1x em cada rodada em que a marionete permanece ativa.
- após comprar ninja adquire técnica kugutsu (técnicas com fantoches) 
> Materiais: não listado


Ferramentas Lendárias

Kiba (Espadas do trovão) Valor: 500k
- Tal como 2 espadas com lâminas cinza-claro de 80cm com cabo marrom de 30cm, é inteiramente composta por material resistente que conduz chakra, sendo mais cortante que o normal.
- nelas, foi implementado Raiton, sendo possível criar 1 raio em qualquer lugar até 1KM de si a cada 1 turno.
- além a primeira propriedade, já contem as propriedades da forja D1 e D2 modificações de raiton
> Materiais: MDR, Substância Energizada 

Kusanagi (Espada Serpente) Valor: 600k
- Espada de material desconhecido, seu cabo azul é de 30cm, naturalmente sua lâmina branca é de 1M
- Tal espada só pode quebrar caso em choque com outra igual (caso n seja reforçada)
- primeira característica é ela se transformar a qualquer distância com simples pensamento do usuário em uma cobra de 150cm de cumprimento e 10cm de largura x altura
- segunda característica é seu cabo que pode alongar até 50M de distância (meio segundo de demora p cada metro) 
- terceira característica é ser envolvida por um material meio brilhante que pode cortar qualquer coisa do mundo
- quarta característica é usuário fazer a mesma levitar e atacar tudo até 30M de distância sozinha telepaticamente (com selo de mão)
- /Jkusanagi para mais detalhes de seus poderes. 
> Materiais: MDR, Substância Energizada 

Shibuki (Respingo) Valor: 500k
- espada com cabo branco de 60cm com uma lâmina de 130cm, ela é feita de um material ultra resistente tal que aguenta explosões.
- A cada golpe dado por ela, ela libera uma explosão que destrói tudo a um raio de 1M em onde atingiu pois é coberta de selos explosivos.
> Materiais: MDR, substância Energizada 

Nuibari (Grande agulha) Valor: 350k
- Tal como uma espada de esgrima afiada mas sem a guarda, parecendo uma agulha, com lâmina de 90cm e cabo de 20cm
- Tal espada é conhecida por furar tudo e unir, penetrando múltiplos alvos em um só golpe 
- Pode amarrar fios de aço na ponta da espada, sendo assim, perfurar oponentes múltiplas vezes e passar a agulha como se tivesse costurando o alvo pois a espada pode passar totalmente dentro de algo a se assemelhar a uma agulha. 
> Materiais: Aço, MDR

Kabutowari (Rachadora de Elmos) Valor: 600k - dx por 200K
- Espécie de machado ligado com uma corda a um martelo
- machado com cabo de 60cm e lâmina de 60cm, martelo com cabo de 60cm e parte do peso com uma circunferência de 60cm+110cm de largura, tudo feito de aço cinza-escuro reforçado 
> Materiais: Couro, Aço, Fibra de carbono 

Kuribiribocho (Lâmina do executor) Valor: 200k
- espada enorme com aparência a facas retangulares de açougueiro, mede de 4 a 6M
- feita de ferro resistente ultra reforçado e muito afiado, tal item é praticamente indestrutível. 
- usada pelos 7 espadachim da névoa, a espada tem a capacidade de se recuperar de danos simplesmente com sangue das vítimas. 
- útil em combates de curta e semi-media distância. 
> Materiais: Ferro, Substância Energizada, Fibra de carbono 

Hiramekarei (Espadas gêmeas) Valor: 800k
- tal como uma espada de Lâmina preta de 1.30M e cabo dourado de 60cm
- Ela é energizada com chakra, sendo assim, queima como ácido tudo que toca, exceto ataduras, por isso, é revestida normalmente com atadura.
- Fora sua propriedade de queimar, ela pode crescer quantos centímetros precisar para frente (cumprimento), para cima ou baixo (grossura) ou para um ou ambos os lados (largura) ( 50exp=crescer algum lado(frente/esquerdo/direito/cima/baixo), 1exp=1cm nos locais escolhidos)
> Materiais: SE (Substância Energizada), Fibra de carbono 

Gunbai (Arranjo do Exército) Valor: 200k
- Um leque cinza grande em formato e tamanho de um violão, porem com grossura de 5cm e um cabo de 30cm
- Seus vantagem é que repele praticamente qualquer ataque de itens encontrados na loja e seus jutsus sem desgastar o escudo
- sua segunda vantagem é ter suas bordas cortantes sendo parecido a uma espada, podendo cortar até espadas mais comuns, e cortar um ninja facilmente
> Materiais: Ferro, Couro, Papel, Seda 



Sapos:
Gamahiro-600.000 ryos
- Sapo grande de 100M com pele verde-água e detalhes de verde escuro e cinza
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Gama-600.000 ryos
- Sapo grande de 30M com pele laranja com detalhes azuis
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Gamagoro-600.000 ryos
-Um sapo com barriga branca e costas roxa de aproximadamente  7 metros
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Gamaken-600.000 ryos
- Sapo naturalmente 50M com pele vermelho escuro com detalhes preto
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Gamamaru-600.000 ryos
- Sapo idoso com tom alaranjado fosco e claro de aproximadamente 30M
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Gamariki-600.000 ryos
- Sapo de 30M com sua pele atrás de verde e barriga branca com um lábio vermelho como se tivesse passado batom e detalhes roxos e amarelos.
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Gamatatsu-600.000 ryos
- É um sapo com pele amarelo forte com detalhes alaranjados jutsu pequeno tem 15cm, jutsu grande tem 5M
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado


Gekomatsu /Gerotora-600.000 ryos
- um sapo com as costas verde-escudo e barriga laranja cerca de 10cm
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado


Kosuke / Shima-600.000 ryos
- Tal como um pequeno sapo de 20 a 30cm que pode até mesmo ficar nos ombros do usuário, tem uma pele verde claro e detalhes roxos
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Gamakichi-600.000 somente do naruto
- Tal como um grande sapo de 30M pele laranja com detalhes pretos
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Ikari wa Hebi(Cobras Raivosas) 500.000
- São diversas cobras brancas 50exp=1 cobra, medem 1M e “de pé” com cabeça erguida, 55cm
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Jya 600.000 ryos
-Tal como uma cobra cor verde escuro mede 220M ponta a cabeça, mas já que rasteja como “sentada” mede 210M
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Jay Ermida 600.000 ryos
-Tal como uma cobra cor branca mede 530M ponta a cabeça, mas já que rasteja como “sentada” mede 230M
- solta veneno que você comprar
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Kyodaijya 600.000 ryos
- Tal como uma cobra cor cinza esverdeada mede 610M ponta a cabeça, mas já que rasteja como “sentada” mede 300M
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Aoda de Sasuke -600.000 ryos
- Tal como uma cobra cor cinza azulada mede 600M ponta a cabeça, mas já que rasteja como “sentada” mede 250M
- detecta calor
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Serpentes de três cabeças -700.000 ryos
- um longo rabo que se divide em 3 pescoços de cabeça de cobras, sua pele atrás é marrom cinza, na frente vermelho esbranquiçado, da ponta até cabeça tem 700M, mas como rastejam como “sentadas” medem 350M
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado

Yamata-cobra de várias cabeças 800.000
- Tal como uma cobra que contém 8 cabeças, um rabo só para 8 pescoços, são brancas com escamas afiadas na parte de trás, mede 1.000M da ponta até cabeça, mas já que restejam como “sentadas” medem 600M
- Assim como toda invocação, usuário precisa escrever em um pergaminho o kanji da invocação em questão no pergaminho antes da invocação aparecer na batalha.
> Materiais: não listado 


Aliança fajulta: 10ryos
- item recriativo 
> Materiais: Metal

Buquê de flores simples:10 ryos
- item recriativo, vc pode especificar qualquer tipo de flor ao comprar. 
> Materiais: não listado 

Papel de presente simples: 10 ryos
- item recriativo 
> Materiais: Papel 
 
Vestido fajulto: 50 ryos
- item recriativo de vestimenta 
> Materiais: Seda

Terno fajulto: 50 ryos
- item recriativo de vestimenta 
> Materiais: Seda

Papel de presente: 50 ryos 
- item recriativo 
> Materiais: Papel, Plástico 

Aliança de namoro: 50 ryos
- item recriativo (cor de ferro) 
> Materiais: Ferro 

Aliança de noivado: 100 ryos
- item recriativo (cor de ouro) 
> Materiais: aço, ouro 

Buquê de flores: 100 ryos
-Item recriativo 
> Materiais: não listado 

Vestido: 500 ryos
- item recriativo
> Materiais: Seda 

Terno: 500 ryos
- item recriativo de vestimenta 
> Materiais: não-listado 

Buquê de flores de luxo: 500 ryos
- item recriativo
> Materiais: não-listado 

Aliança de casamento: 1.000 ryos
- item recriativo
> Materiais: Aço, Ouro

Vestido de casamento: 1K
- item recriativo
> Materiais: seda

Terno para cerimônias: 1K
- item recriativo
> Materiais: Seda

Tratamento médico: 1.000 ryos 
- Ninjas  que moram em vilas sem leis, devem comprar isso para que seu tratamento seja possível. 

Aliança de diamante: 2.500 ryos
- item recriativo
> Materiais: Ouro, Aço Diamante 
 
Transplante oficial: 20.000 ryos
- Ninjas que moram em vilas com leis, devem comprar isso caso faça algum transplante oficial. 

Certidão de responsabilidade para ter PETs: 5.000 ryos
— Com isto, você garante que terá responsabilidade em ter qualquer animal vivo. Garantindo um ambiente seguro e adequado, alimentação correta, e então com esta certidão, poderá levar seu PET para o hospital de graça sempre que for preciso. 
> Materiais: papel 

Casa comum: 40K
- terreno (ou seja, grupo) em que vc será administrador e poderá moldar apenas nome e bio
> Materiais: Madeira, Vidro blindado, plástico, tecnologia, ferro, ouro, metal, aço, seda, couro, argila, borracha

Casa com cerquinhas brancas: 65K
- normalmente comprado por recém casados para uma boa lua de mel
 - terreno (ou seja, grupo) em que vc será administrador e poderá moldar apenas nome e bio
> Materiais: Madeira, Vidro blindado, plástico, tecnologia, ferro, ouro, metal, aço, seda, couro, argila, borracha

Casa gótica: 80K 
- comprado normalmente por casados ou não, algo para quem quebra padrões. 
 - terreno (ou seja, grupo) em que vc será administrador e poderá moldar apenas nome e bio
> Materiais: Madeira, Vidro blindado, plástico, tecnologia, ferro, ouro, metal, aço, seda, couro, argila, borracha

Mansão: 80K
- comprado por luxuosos e também dado aos VIPs
 - terreno (ou seja, grupo) em que vc será administrador e poderá moldar apenas nome e bio
> Materiais: Madeira, Vidro blindado, plástico, tecnologia, ferro, ouro, metal, aço, seda, couro, argila, borracha

Terreno para casa: 80K
- assim como as outras casas, porém, vc personaliza (com ou sem cerquinhas, estilo gótico ou não) 
 - terreno (ou seja, grupo) em que vc será administrador e poderá moldar coisas como imagem da casa, bio e nome
> Materiais: none

Terreno geral: 90K 
- terreno em que vc pode criar oq quiser (desde casas, até clubes, lojas, etc) 
> Materiais: Madeira,
	""".strip().split("\n\n")

	for e in text:
		search = e.find("\n")
		nome = e[ 0:search ]
		Desc = "#" + e[ search: ]
		Desc = Desc.title().strip().replace("\n", " ")
		new = nome + Desc.replace("\t", "\n")
		new = new.replace("##", "#").replace("\n", "\n\n").replace("\n ", "\n\n").replace(" \n", "\n\n").replace("   ",
																												 "\n\n")
		print(new)

	text2 = """
"""


# temporária()


"""
nome dos itens especiais 
	Eventos_Val = {} 
	its=[] #var com itens especiais e normais 
	for e in Eventos_key:
		its.append([-1, e.title()])  #[-1 = valor, e= item]
		e = e.strip().upper().replace(" ", "_") #formata o elemento (item de Eventos)
		Eventos_Val[e] = -1 #evenros_val = nome_item: valor(-1)
		itensAZ.append(f"{e.title()}: {-1}") #itens em ordem alfabética add str('nome_item: - 1') formatado' 

text = text.replace("\n\n", "\n").replace("EXP", "").replace("ryos", "").replace(":", "").replace("/", "").replace("Valor", "").replace("_", "").replace("k\n", "\n").replace("R\n", "\n").replace("K\n", "\n").replace("  ", " ").replace("K ", "").replace("-", "").replace(".", "").replace("Ryos", "").replace("k ", "").replace("*", "").replace("Sasuke", "").replace("Ninja", "Ladino").replace("ninja", "Ladino").replace("K\n", "").replace(" r", "")
	for e in range(0, 10):
		e = f"{e}"
		text = text.replace(f"{e}","").replace("{e}K", "").replace(f"{e}r", "") 
	text = text.replace(" L", "1L").replace("\n\n\n", "\n").replace("Binóculo", "Binóculo 20x50").replace(" r", "").replace(" K", "").replace("chakra", "Nespiritus").replace("Chakra", "Nespiritus").replace("aldeia", "reino").replace("konoha", "Reino da folha").replace("Konoha", "Reino da Folha") 
	#text = formatado """

"""if c == 1:
			maior = v
			menor = v
			k_men = c-1
			k_mai = c-1
			itens01.append(f"{v} > {k.title()}")
			a =" criou"
		else:
			a = 0
			if v > maior or v == maior:
				maior = v
				itens01.insert(k_mai, f"{maior} > {k.title()}") 
				k_mai = c-1
				print("subiu") 
				#print(F"{maior = } {k_mai = } \n{k =} {v =} ")
			if v < menor or v == menor:
				menor = v
				itens01.insert(k_men-1, f"{menor} > {k.title()}")
				k_men = c-1
				print("desceu") 
				#print(F"{menor = } {k_men = } \n{k =} {v =} ")
			if a == 0:
				print("fudeukk")
		#print(itens01[c-1])
		#print(F"\t\t//{c}\n#{menor = } {k_men = } \n{maior = } {k_mai = } \n{k =} {v =}")
		#print(itens01[c-1])
		#itens01.append(f"{v} > {k.title()}")
		#print(f"-> {k.title()}: {v} $")""" 