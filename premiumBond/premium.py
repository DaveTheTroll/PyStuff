import matplotlib.pyplot as plt
import numpy as np

prizes =    (
        (	1.00E+06	,	2	),
        (	1.00E+05	,	5	),
        (	5.00E+04	,	11	),
        (	2.50E+04	,	21	),
        (	1.00E+04	,	54	),
        (	5.00E+03	,	106	),
        (	5.00E+02	,	5574	),
        (	1.00E+02	,	30190	),
        (	5.00E+01	,	30190	),
        (	2.50E+01	,	3163537	)
    )

odds = 34500

# Summary
N = 0
V = 0
for (v, n) in prizes:
    N += n
    V += v * n

bonds = N*odds

print("Total number of prizes %d"%(N))
print("Total prize fund £%d"%(V))
print("Total number of bonds %d"%bonds)
print("Mean win %.2f%% (1/%.1f)%%"%(100*V/bonds, 1/(100*V/bonds)))

prizes = np.array(prizes)
prizes[:,1] /= bonds

def hist(P, N):
    plt.bar(P[:,0], P[:,1], edgecolor=[1,0,0], lw=1, ls='-')
    plt.title("%d Bonds"%N)
    plt.show()

#hist(prizes, 1)

def factorial(N):
    F = 1
    for n in range(2, N+1):
        F *= n
    return F

def binom_coef(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

bonds = 5

# Number of wins
win = []
v = prizes[-1,0]
p = prizes[-1,1]
print(v, p)
S = 0
for k in range(1,bonds+1):
    n = bonds
    Cnk = binom_coef(n, k)
    print("==============",k)
    print(Cnk, p**k, (1-p)**(n-k))
    V = v*k
    P = Cnk * p**k * (1-p)**(n-k)
    win.append((V, P))
    S += P
print("S", S)

print(win)
#hist(win, bonds)