from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 11'

pages11 = [[c.beg, c.mceb, c.mon, c.mag, c.ceb, c.cas, c.mag, c.end],
		   [],
		   [c.cas, c.ceb],
		   [c.beg, c.mceb, c.mon, c.mag, c.ceb, c.cas] + c.shades(4),
		   [c.mon, c.mag, c.cas, c.ceb, c.san],
		   [c.mon, c.mag, c.cas, c.ceb, c.san],
		   [c.mon, c.mag, c.cas, c.ceb, c.san, c.child(), c.att(), c.att()],
		   [c.mon, c.mag, c.cas, c.ceb, c.san],
		   [c.mon, c.mag, c.cas, c.ceb, c.san],
		   [c.mon, c.cas, c.ceb, c.san],
		   [c.mon, c.mag, c.cas, c.ceb, c.san],
		   [c.mon, c.mag, c.cas, c.ceb, c.san],
		   [c.mon, c.mag, c.cas, c.ceb],
		   [c.mceb, c.mag, c.ceb, c.mon, c.cas, c.fig(), c.shade(), c.shade()],
		   [c.cas, c.mon, c.ceb] + c.kids(7) + c.shades(8),
		   [c.cas, c.ceb, c.mon, c.mceb],
		   [c.cas, c.mon, c.mag, c.ceb, c.mceb, c.pceb],
		   [c.cas, c.mon, c.mag, c.ceb, c.mceb, c.pceb],
		   [c.mon, c.ceb, c.mceb, c.pceb, 'Motorista do Guincho'],
		   [c.cas, c.mon, c.mag, c.ceb, c.mmon, c.pmon, c.pcas, c.end],
		   [c.beg, c.pit, c.thu, 'Dente de Sabre', c.end],
		   [c.beg, c.moca, c.mon],
		   [c.moca, c.san, c.mon, c.end],
		   [],
		   [c.beg, c.fra, 'Sherlock Holmes'], # Sherlock só em pensamento
		   [c.fra],
		   [c.fra, c.zcav, c.lob], # zé caveirinha só em pensamento
		   [c.fra, c.mum, c.pen, c.alm, 'Zé Cremadinho'], # zé cremadinho e muminho só em pensamento
		   [c.fra, c.mum, c.cra, 'Mulher do Cranicóla', c.lob], # lobi só em pensamento
		   [c.fra, c.pen, c.zvam, c.lob, 'Gorila', 'Pé Grande', 'Hulk', c.end], # os 3 últimos só em pensamento
		   [c.beg, c.cas, c.fig(), c.fig(), c.end],
		   [],
		   [], # [c.tin, c.rol, c.zec, 'cara estranho com boné com um T'] # passatempos
		   [], # [c.tar, c.franj, c.pen, 'bicho azul estranho'] # correio
		   [], # [c.lou, c.bid] # correio
		   [c.beg, c.mon, c.ceb],
		   [c.ceb, c.mon, c.cas, c.tit, c.jer, c.man],
		   [c.mon, c.tit, c.man, c.jer, c.carfru, c.mag],
		   [c.mon, c.mag, c.ceb, c.cas],
		   [c.mon, c.mag, c.ceb, c.cas, c.jer, c.tit, 'Pitbull', fig(), fig(), fig()],
		   [c.mon, c.mag, c.ceb, c.cas, c.tit, c.jer, c.fig(), c.luc, c.end],
		   [c.beg, 'Pulga 1', 'Pulga 2', 'Pulga 3', 'Pulga 4', 'Pulga 5', 'Pulga 6'],
		   ['Pulga 1', 'Pulga 2', 'Pulguinha 1', 'Pulguinha 2', c.franj, c.bid, c.end],
		   [],
		   [c.beg, c.zlel, 'Vaca'],
		   [c.zlel, 'Tartaruga'],
		   [c.zlel, 'Tartaruga'],
		   [c.zlel, 'Tartaruga'],
		   [c.zlel, 'Tartaruga', 'Touro'],
		   [c.zlel, 'Tartaruga', 'Tartaruga 2', 'Jacaré', c.end],
		   [],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas],
		   [c.beg, 'Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon, c.franj],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon, c.franj],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon, c.franj, c.bid, 'Carrapato 1', 'Carrapato 2', 'Cadelinha'],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon, 'Alberto Aíston'], # alberto em holograma
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon, c.franj, 'Alberto Aíston'],
		   ['Zing Mascarado', c.ceb, c.cas, c.mon, 'Alberto Aíston'],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon, c.franj, 'Alberto Aíston'],
		   ['Homem de Chumbo', 'Zing Mascarado', c.ceb, c.cas, c.mon, c.franj, c.bid],
		   [c.ceb, c.cas, 'Sherlock Holmes'],
		   [],
		   []]
