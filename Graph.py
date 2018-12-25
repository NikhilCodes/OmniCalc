from sympy import Symbol
from Scalc import *
from matplotlib.pyplot import *
from numpy import linspace, zeros

def show_graph(exp, limit = list()):
    limit[0] = float(eval(limit[0]))
    limit[1] = float(eval(limit[1]))
    
    x = Symbol('x')
    title(str(exp)+' Graph')
    exp_ = eval(exp)
    coord1 = linspace(limit[0], limit[1], 1000)
    x_axis = [linspace((limit[0] if limit[0]<0 else 0),limit[1],1000), zeros([1000,1])]
    plot(*x_axis,'--', color='black')
    try:
        coord2 = [float(exp_.subs({x: _})) for _ in coord1]
    except AttributeError:
        coord2 = [float(exp) for _ in coord1]
    except TypeError as e:
        print(e)
        return

    y_axis = [zeros([1000,1]), linspace(float(min(coord2)), float(max(coord2)) ,1000)]
    plot(*y_axis,'--', color='black')
    xlabel('Domain --->')
    ylabel('Range --->')
    plot(coord1, coord2)
    show()

if __name__ == '__main__':
    show_graph('e**x', ['0.0001','10'])
