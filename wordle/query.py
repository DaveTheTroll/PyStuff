from words import *
import sys

if len(sys.argv) == 1:
    print("query.py FIXED LETTERS")
    print("FIXED e.g. ...E. if E is known to be in fourth place")
    print("LETTERS all other known letters, can have repeats")
    exit()

fixed = sys.argv[1].lower()

W = words_all
for i in range(5):
   if fixed[i] != '.':
      W = list(filter(lambda w: w[i] == fixed[i], W))

if len(sys.argv) > 2:
    letters = (sys.argv[2] + fixed.replace(".","")).lower()
    for l in set(letters):
       W = list(filter(lambda w: w.count(l) >= letters.count(l), W))

print(W)