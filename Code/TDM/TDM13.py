from Functions.class_TM import TM
from Functions.class_characters import characters

c = characters()
c.reset()
c.comic_book = '#tdm13'

pages13 = [[c.beg, c.dud, c.mag, c.end],
           [],
           [c.beg, c.dud, c.mag, c.cb + 'Princesa'],
           [c.mdud, c.dud],
           [c.mdud, c.dud],
           [c.mdud, c.dud],
           [c.mdud, c.dud],
           [c.mdud, c.mag],
           [c.mdud, c.mag, c.dud],
           [c.dud, c.mag],
           [c.dud, c.mag],
           [c.dud, c.mag],
           [c.dud, c.mag, c.mdud],
           [c.dud, c.mag, c.mdud, c.att()] + c.kids(5) + c.shades(19),
           [c.dud, c.mag, c.child()],
           [c.dud, c.mag],
           [c.dud, c.mag],
           [c.dud, c.mag],
           [c.dud, c.mag, c.mdud],
           [c.dud, c.mag, c.mdud],
           [c.dud, c.mag, c.fig(), c.fig(), c.end],
           [c.beg, c.chi, c.ros],
           [c.chi, c.ros, c.end],
           [],
           [c.beg, c.alm, c.pen],
           [c.alm, c.pen],
           [c.alm, c.pen],
           [c.alm, c.pen],
           [c.alm, c.pen, c.fig(), c.fig(), c.fig()],
           [c.alm, c.pen, c.fig(add = -3), c.fig(add = -2), c.fig(add = -1)],
           [c.alm, c.pen, 'Alma amante do Penadinho', c.end],
           [],
           [], # [c.bid, c.mag, c.chi, c.pen, c.san, c.ceb], # passatempo
           [], # ['Índia', c.mag, c.mon, c.san, c.chi] # correio
           [], # [c.mon, c.ceb, c.pip] # correio
           [c.beg, c.pit, c.dino()],
           [c.pit, c.dino(add = 0), c.dino(), c.end],
           [c.beg, c.mon, c.cas, c.cb + 'Alien', c.end],
           [],
           [c.beg, c.marceb, c.fig()],
           [c.marceb, c.floq],
           [c.marceb, c.floq],
           [c.marceb, c.floq],
           [c.marceb, c.floq],
           [c.marceb, c.floq, c.mceb],
           [c.marceb, c.floq, c.mceb],
           [c.marceb, c.floq],
           [c.marceb, c.floq, c.mceb, c.pceb, c.beg],
           [],
           [c.beg, c.floq, c.moca],
           [c.moca, c.bid, c.end],
           [c.beg, c.chi, c.zlel, c.prof, c.tor, c.anim(), c.mchi] + c.kids(4) + [c.end], # conferir se são figurantes mesmo
           [c.beg, c.pap, c.caf, c.jur],
           [c.pap, c.caf, c.jur],
           [c.pap, c.caf, c.jur, c.fig(), c.end],
           [c.beg, c.ceb, c.san, c.chov],
           [c.ceb, c.san, c.chov],
           [c.mon, c.san, c.chov],
           [c.mon, c.san, c.chov],
           [c.mon, c.san, c.chov],
           [c.mon, c.san, c.chov, c.fig(), c.fig()],
           [c.mon, c.san, c.chov],
           [c.mon, c.san, c.chov, c.anim()],
           [c.mon, c.san, c.chov],
           [c.mon, c.san, c.chov, c.cas, c.end],
           [c.beg, c.bid, c.fig(), c.end]]
