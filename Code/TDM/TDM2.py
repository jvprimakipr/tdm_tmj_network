from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 2'

pages2 = [[c.mag, 'Dud Van Winkle', c.fig()], # capa (Dud parece o Dudu)
          [],
          [c.mag, c.dud],
          [c.mag, c.dud],
          [c.mag, c.dud],
          [c.mag, c.dud, c.fig()],
          ['Mulher - História', 'Homem - História', 'Boi 1', 'Boi 2', 'Cachorro', 'Galo', 'Galinha', c.dud, 'Dud Van Winkle'],
          [c.mag, c.dud, 'Dud Van Winkle', 'Vovó - História'],
          ['Dud Van Winkle', 'Vaca', 'Galinha', 'Tartaruga', 'Caracol'],
          [c.mag, c.dud, 'Dud Van Winkle'],
          ['Dud Van Winkle'],
          [c.dud, c.mag, 'Construtor 1', 'Construtor 2', 'Construtor 3'],
          ['Construtor 4', 'Construtor 5', c.child(), c.mot()],
          [c.mau, 'Dud Van Winkle', c.fig()],
          [c.mau, 'Dud Van Winkle'],
          ['Dud Van Winkle', c.dud, c.mag],
          [c.dud, c.mag, c.pen], # penadinho era num brinquedo
          [c.dud, c.mag, c.mau, 'Dud Van Winkle'], # fim da história
          [],
          [c.cas],
          [c.cas], # fim da história
          [c.ceb, c.mon, c.mag, c.san],
          [c.cas, c.mon, c.mag, c.san],
          [c.mon, c.mag, c.san, c.xav], # fim da história
          [c.moca, c.min],
          [c.mon, c.mag, c.san, c.moca, c.min, c.chov, c.floq, 'Cachorro Verde Aleatório'],
          [c.franj, c.bid, c.moca, c.min, c.chov, c.floq, 'Cachorro Verde Aleatório'], # fim da história
          [c.lob, c.zvam],
          [c.zvam, c.pen, c.fra, c.mum], # fim da história
          [c.mon, c.mag, c.mar, 'Vendedor de Picolé'], # fim da história
          [],
          [c.mon, c.ceb, 'Titi', 'Super Homem', c.cas], # fim da história
          [],
          [],
          [],
          [c.pit, 'Homem das Cavernas 1', 'Homem das Cavernas 2'],
          [c.pit, 'Homem das Cavernas 1', 'Homem das Cavernas 2'],
          [c.pit, 'Homem das Cavernas 1', 'Homem das Cavernas 2'],
          [c.pit, 'Dente de Sabre', 'Dinossauro Amarelo'],
          [c.pit, 'Homem das Cavernas 3', 'Homem das Cavernas 4'], # fim da história
          [],
          [c.dud],
          [c.dud],
          [c.dud, c.mdud], # fim da história
          [c.mag, c.franj],
          [c.mag, c.franj],
          [c.mag, c.franj],
          [c.franj],
          [c.mag, c.franj],
          [c.mag, c.franj],
          [c.mag, c.franj], # fim da história
          [c.mag, c.mmag], # acho que ela quem chama a magali para casa (não aparece, só o balão de voz)
          [c.mag, 'Anjo da Guarda da Magali'], # fim da história
          [],
          [c.bid, 'Pedra'], # a pedra fala!!!
          [c.bid, 'Pedra', c.manf],
          [c.bid, c.manf, 'Desenhista 1', 'Desenhista 2', 'Desenhista 3'],
          [c.bid, c.manf, 'Pedra'],
          [c.bid, 'Pedra', c.manf],
          [c.bid, c.manf, 'Pedra'],
          [c.bid, c.manf, 'Pedra'],
          [c.bid, c.manf, 'Pedra'],
          [c.bid, c.manf, 'Pedra'],
          [c.bid, c.manf, 'Desenhista 1', 'Desenhista 2', 'Desenhista 3'],
          [c.bid, c.manf, 'Desenhista 1', 'Desenhista 2', 'Desenhista 3', 'Pedra']] # fim da história
