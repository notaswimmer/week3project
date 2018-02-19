#define dataset, known constant
import math
data = [[0,1.0000000],
     [15,.9743175],
     [25,.9575636],
     [35,.9373807],
     [40,.9241359],
     [45,.9048999],
     [50,.8762306],
     [60,.7698698],
     [70,.5592012],
     [80,.2626372],]


#define functions to optimize
def f1(n,r):
    return math.exp(r*n)
def f2(n,s,g,c):
    return (s**n)*(g**((c**n) - 1))

#define inverse value function, sum of error squares to be minimized
def v(funct, params):
    sum = 0
    for i in xrange(10):
        sum += (funct(data[i][0],params) - data[i][1])**2
    return sum

#define lower and upper bounds for parameters. Write them into a 2xn matrix
lbr = -0.01
ubr = 0

lbc = 1.07
ubc = 1.13

lbs = 0.996
ubs = 1

lbg = 0.98
ubg = 1

f1bounds = [[lbr,ubr]]

f2bounds = [[lbs,ubs],
            [lbg,ubg],
            [lbc,ubc]]
#define a brute force by subdividing the boundaries into halves k times
def simple(valueFunction, iterations, *parameterBounds):
    for k in 1 to iterations:
