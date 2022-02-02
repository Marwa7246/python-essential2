from sys import path
path.append('../packages')

import extra.iota
print(extra.iota.funI())

from extra.good.alpha import funA
print(funA())

from extra.good.best.sigma import funS
print (funS())