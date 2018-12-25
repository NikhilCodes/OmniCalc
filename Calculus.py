import sympy
from sympy import integrate as integ
from sympy import diff
from collections import defaultdict
from sympy import Symbol
from Scalc import *

class GenerateSymbols(defaultdict):
    def __missing__(self, key):
        return Symbol(key)

def integrate(expr):
    if expr=='Nikhil Nayak(9663)':
        return ('Hey There Creator!, Integrating Up Your DNA!')
    x = Symbol('x')
    res = str(eval('integ('+expr+', x)')).replace('**','^').replace('*','').replace('pi', 'π')+'  +  Constant'
    return res

def differ(expr):
    if expr=='Nikhil Nayak(9663)':
        return ('Hey There Creator!, Differenciating Up Your Foe!')
    x = Symbol('x')
    res = str(eval('diff('+expr+',x)')).replace('**','^').replace('*x','x').replace('pi', 'π')
    return res

if __name__ == '__main__':
    print(str(differ('6**(x)')))
