from Measurements import *
from Block import CloseFittingBodice
import matplotlib.pyplot as plt

b = CloseFittingBodice(StandardSize("10"))

(n,x,y) = b.PointsAsArrays()
plt.figure()
for i in range(len(x)):
    plt.text(x[i], y[i], n[i])
plt.plot(x, y, 'x')

for p in b.Pieces():
    (x,y) = p.PointArrays(True)
    plt.plot(x, y, '-')

plt.gca().invert_yaxis()
plt.axis('equal')
plt.grid()

plt.show()