from sys import path
path.append('../packages/Extrapack.zip')

import extra.ugly.psi
print(extra.ugly.psi.FunP())

import extra.good.beta as bt
print(bt.FunB())