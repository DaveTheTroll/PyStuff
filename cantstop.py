import sys

X = [int(x) for x in sys.argv[1:]]

N = 0
for a in range(1,7):
    for b in range(1,7):
        if a+b in X:
            N += 6*6
            #print(a,b,"*","*")
        else:
            for c in range(1,7):
                if a+c in X or b+c in X:
                    N += 6
                    #print(a,b,c,"*")
                else:
                    for d in range(1,7):
                        if a+d in X or b+d in X or c+d in X:
                            N += 1
                            #print(a,b,c,d)
                    
print("%d/%d = %.1f%%"%(N,6*6*6*6,N*100/(6*6*6*6)))
    