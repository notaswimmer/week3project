from lib import optimizer as op

import matplotlib.pyplot as plt


values = op.bruteSearch(op.f1,50,op.f1bounds)
x = [values[z][0] for z in range(len(values)-1)]
y = [values[z][1] for z in range(len(values)-1)]




print(x)
plt.plot(x,y, 'ro')
plt.ylabel('value')
plt.xlabel('n')
plt.show()