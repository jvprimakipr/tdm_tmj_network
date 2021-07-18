from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 7'

pages7 = [[c.beg, c.mon, c.mar, c.ceb, c.cas, c.xav, c.nim, c.doc, c.hum, c.jer, c.end],
          [],
          [c.den, c.mon, c.carfru, c.den, c.mag],
          [c.beg, c.mar, c.mon, c.mag],
          [c.mar, c.mon, c.mag],
          [c.mon, c.mag, c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mar, c.mon, c.mag, c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mar, c.mon],
          [c.mon, c.mar, c.ceb, c.cas, c.child(), c.child(), c.child(), c.shade(), c.shade(), c.shade()],
          [c.cas, c.ceb, c.mon, c.mar],
          [c.cas, c.ceb, c.mar, c.mag, c.mon, c.nim, c.xav, c.hum],
          [c.cas, c.ceb, c.mar, c.mag, c.mon, c.nim, c.xav, c.hum, c.den, c.carfru],
          [c.cas, c.ceb, c.mar, c.mag, c.mon, c.nim, c.xav, c.hum, c.den, c.carfru],
          [c.cas, c.ceb, c.mag, c.mon, c.nim, c.xav, c.hum, c.carfru],
          [c.cas, c.ceb, c.mar, c.mag, c.mon, c.nim, c.xav, c.hum, c.den, c.carfru],
          [c.ceb, c.mar, c.mag, c.mon, c.nim, c.den, c.carfru, c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.shade(), c.shade()],
          [c.mon, c.mag, c.den, c.carfru, c.child(), c.child(), c.child(), c.child(), c.child(), c.child()],
          [c.mon, c.mag, c.den, c.carfru, c.mar, c.mau, c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade(), c.shade()],
          [c.mon, c.mag, c.den, c.carfru, c.mar, c.mau, c.ali, c.child(add = -1), c.child(add = -2), c.child(add = -3), c.child(add = -4), c.child(add = -5), c.child(add = -6), c.child(add = -7), c.child(add = -8), c.child(add = -9), c.child(add = -10), c.child(add = -11), c.child(add = -12), c.shade(add = -1), c.shade(add = -2), c.shade(add = -3), c.shade(add = -4), c.shade(add = -5), c.shade(add = -6)], # coloquei repetidos por que daria muita criança num só gibi / fim da história
          [c.cas, c.ceb, c.end], # fim da história
          [],
          [c.beg, c.mag, c.ceb, c.mon, c.san, c.mmag],
          [c.mon, c.san, c.ceb, c.cas, c.mcas, c.zlui, c.end], # fim da história
          [c.beg, c.cas, c.mon, c.ceb],
          [c.cas, c.mag, c.mau, c.ali, c.end], # fim da história
          [c.beg, c.paj],
          [c.paj, c.cac, 'Índia', 'Índio'],
          [c.paj, c.cac, 'Índia', 'Índio', c.pap, c.end], # fim da história
          [c.beg, c.cas],
          [c.mon, c.mag, c.ceb],
          [c.dud, c.xav, c.spa, c.anj, 'Anjo 1', 'Anjo 2', 'Anjo 3', c.end], # fim da história
          [],
          [], # [c.jot, c.mon, c.ceb, c.cas, c.mag], # passatempo
          [], # [c.mon, c.mag, c.ceb, c.cas, c.bid, c.gen], # correio
          [], # [c.mon, c.quin, c.nim, c.cas], # correio
          [c.beg, 'Equilibrista', c.mon, c.mag, c.fig(), c.shade(), c.shade(), c.shade(), 'Palhaço 1', 'Palhaço 2'],
          ['Homem Bala', c.mon, c.mag, c.shade(add = -1), c.shade(add = -2), c.shade(add = -3), c.shade(), c.shade(), c.shade(), c.shade(), 'Palhaço 3'], # fim da história
          ['Mulher 1', 'Mulher 2', 'Mulher 3'],
          ['Mulher 3', 'Mulher 4', c.pen, 'Fantasma do Sultão', c.end], # fim da história
          [],
          [],
          [c.beg, c.mar],
          [c.mar, 'Gato'],
          [c.mar, 'Pitbull'],
          [c.mar, c.luc, c.mon, c.den, c.mag, c.end], # fim da história
          [c.beg, c.ceb, c.mag, c.mon],
          [c.ceb, c.mon, c.mag, 'Alienígena 1 - gibi 7', 'Alienígena 2 - gibi 7', 'Alienígena 3 - gibi 7', 'Alienígena 4 - gibi 7', 'Alienígena 5 - gibi 7', 'Alienígena 6 - gibi 7'], # fim da história
          [c.ast],
          [c.ast, 'Policial Alien'],
          [c.ast, 'Policial Alien'],
          [c.ast, 'Policial Alien', 'Computador do Astronauta', 'Senhorita Argh', 'Alien 1', 'Alien 2'],
          [c.ast, 'Senhorita Argh', 'Alien 1', 'Alien 2'],
          [c.ast, 'Alien 1', 'Alien 2', 'Alien 3', 'Senhorita Argh', c.fig(), c.fig()],
          [c.ast, 'Alien 1', 'Alien 2', 'Senhorita Argh'],
          [c.ast, 'Alien 1', 'Alien 2', 'Senhorita Argh'],
          [c.ast, 'Alien 1', 'Alien 2', 'Senhorita Argh'],
          [c.ast, 'Alien 1', 'Alien 2', 'Senhorita Argh', c.mast, c.end], # fim da história
          [c.beg, c.mon, c.mmon, c.ceb, c.mceb, c.mag, c.mmag, c.cas, c.mcas, c.end], # fim da história
          [c.beg, c.ceb],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb],
          [c.ceb, c.pceb],
          [c.mau, c.mar, c.end], # fim da história
          [c.beg, c.ceb, c.lou, c.end]] # tirinha do final
