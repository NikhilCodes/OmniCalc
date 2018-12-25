from sympy import oo as Infinity
from sympy import nan, ln, sin, cos, tan, sec, csc, cot, asin, acos, atan, asec, acsc, acot, sinh, cosh, tanh, sech, csch, coth
import sympy as s
pi = s.pi
e = s.E
log = ln
cosec, acosec, cosech = csc, acsc, csch
del s
def solve(expr):
    if expr=='Nikhil Nayak(9663)':
        return ('Hey There Creator!, Summing Up Your Wish!')
    try:
        res = eval(expr)
        return str(res).replace('pi', 'π').replace('zoo', 'Infinity').replace('csc', 'cosec').replace('**', '^')
    except ZeroDivisionError:
        if eval(expr.split('/')[0])==0:
            return nan
        elif eval(expr.split('/')[0])<0:
            return -Infinity
        else:
            return Infinity
print(solve('-1/0'))
