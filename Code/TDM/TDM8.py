from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = 'gibi 8'

pages8 = [[c.beg, c.mon, c.ceb, c.cas, c.mag, c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), c.child(), 'Planeta Terra', c.end],
          [],
          [c.ceb, c.mon, c.mag, c.cas, 'Planeta Terra'],
          [c.beg, c.mag, c.mon, c.san, c.ceb],
          [c.mag, c.mon, c.san, c.ceb, c.cas],
          [c.mag, c.mon, c.san, c.ceb, c.cas, c.shade(), c.att(), c.att(), c.child(), c.child()],
          [c.mon, c.san, 'Planeta Terra', c.shade(), c.child(), c.child(), c.child(), c.child(), c.fig()],
          [c.child(), c.mot(), c.mon, c.san, c.ceb, c.mag, c.mag, 'Planeta Terra'],
          [c.mon, c.san, c.ceb, c.mag, c.mag, 'Planeta Terra'],
          [c.mon, 'Planeta Terra'],
          ['Urso Polar', c.fig(), c.fig(), c.fig(), c.fig(), c.fig()],
          [c.mon, c.san, c.ceb, c.mag, c.mag, 'Planeta Terra'],
          ['Planeta Terra', c.mcas, c.cas, c.mceb, c.pceb, c.ceb, c.mon, c.mcas, c.pcas, c.mag, 'Padeiro'],
          [c.child(), c.mon, c.san, c.ceb, c.mag, c.mag, 'Planeta Terra'],
          [c.mon, c.ceb, 'Planeta Terra', c.san, c.mag, c.cas, 'Roteirista 1', 'Roteirista 2', 'Roteirista 3', 'Roteirista 4'],
          [c.mon, c.ceb, c.mag, c.cas, 'Planeta Terra', c.child(), c.child(), c.child(), c.child(), c.shade(), c.shade(), c.shade(), c.shade()],
          ['Planeta Terra', 'Lua', c.mon, c.ceb, c.cas, c.mag, c.end], # fim da história
          [c.beg, c.san, c.mon, c.ceb],
          [c.san, c.mon, c.ceb, c.end], # fim da história
          [],
          [c.beg, c.anj, c.ceb], # cebolinha só em balão de fala
          [c.ceb, c.san, c.mon, c.anj],
          [c.ceb, c.mon, c.san, c.anj, 'Anjinha', c.end], # fim da história
          [c.beg, c.mar],
          [c.mar],
          [c.mar],
          [c.mar, 'Sapo'],
          [c.mar, c.end], # fim da história
          [c.beg, c.naj, 'Comadre Cigarra'],
          [c.naj, 'Comadre Cigarra'],
          [c.naj, 'Comadre Cigarra'],
          [c.naj, 'Comadre Cigarra', c.jot, c.end], # jotalhão em balão de pensamento / fim da história
          [], # [c.bid, c.franj], # passatempo
          [], # [c.bid, c.mag, c.cas, c.mon, c.ceb, c.ros], correio
          [], # [c.cas, c.ceb, 'Muleque Estranho', c.luc, c.mon, c.san, c.tar] correio
          [c.beg, c.fig()],
          [c.fig(add = -1), c.fig()],
          [c.fig(add = -2), c.fig(add = -1), 'Cupido', c.mor, c.end], # fim da história
          [],
          [],
          [c.beg, c.pen, c.mum, c.zvam, c.cra, c.lob],
          [c.pen, c.mum, c.zvam, c.cra],
          [c.pen, c.mum, c.zvam, c.fig(), c.fig()],
          [c.mum, c.zvam, c.pen, c.lob], # pensando no lobi
          [c.mum, c.zvam, c.pen, c.lob], # pensando no lobi
          [c.mum, c.zvam, c.pen],
          [c.mum, c.zvam, c.pen, c.lob], # pensando no lobi
          [c.mum, c.zvam, c.pen, c.lob, c.fig(), c.shade(), c.end], # fim da história
          [c.beg, c.mceb, c.ceb, 'Médico', c.cas, c.end], # fim da história
          [c.beg, c.bid, 'Cachorro 1', c.child()], # criança só em balão de fala
          [c.bid, 'Cachorro 1', 'Cachorro 2', c.fig(), c.fig()], # o segundo figurante só em balão de fala
          [c.bid, 'Cachorro 2', 'Cachorro 3', c.fig()], # figurante só em balão de fala
          [c.bid, 'Cachorro 3', 'Cachorro 4', c.fig(), c.fig(), c.fig(), c.fig(), c.fig(), c.fig(), c.fig(), c.fig(), c.end], # figurantes em balão de fala / fim da história
          [c.beg, c.chi, c.mchi],
          [c.chi, c.hir],
          [c.chi, c.gen, c.ros],
          [c.chi, c.ros, c.mchi, c.end], # fim da história
          [],
          [c.beg, c.cas, c.end], # fim da história
          [c.beg, c.cas, c.san, c.mon, 'Menino de Pedra'],
          [c.cas, c.san, 'Menino de Pedra'],
          ['Menino de Pedra', c.child(), c.child(), c.ceb, c.san, c.mon],
          [c.cas, c.san, c.mon, 'Menino de Pedra'],
          [c.cas, c.san, c.mon, 'Menino de Pedra', c.franj],
          [c.cas, c.san, c.mon, 'Menino de Pedra', c.franj, c.end], # fim da história
          [c.beg, c.franj, c.ceb, c.mcas, c.bid, c.floq, c.cas, c.end]] # (os últimos 3 só em balão de pensamento) tirinha final
