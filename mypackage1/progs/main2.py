from sys import path

path.append('../packages')

import extra.iota
import extra.good.best.sigma
import extra.good.alpha as alp

from extra.good.best.tau import FunT

print(extra.iota.FunI())
print(extra.good.best.sigma.FunS())
print(FunT())
print(alp.FunA())
