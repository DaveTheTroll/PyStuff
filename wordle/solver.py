from words import *
import random
try:
    import matplotlib.pyplot as plt
except:
    pass
from datetime import datetime

class game_state:
    def __init__(self, word, word_list):
        self.word = word
        self.list = word_list

    def guess(self, g=None):
        if g is None:
            g = self.list[0]
        #print(g.upper(), len(self.list))
        if g == self.word:
            return True
        else:
            self.list.remove(g)

            for l in set(g):
                ng = g.count(l)
                nw = self.word.count(l)
                if ng <= nw:    # All guessed letters are in word
                    self.list = [x for x in self.list if x.count(l) >= ng]   # remove words with less instances
                else:
                    self.list = [x for x in self.list if x.count(l) == nw]   # remove words with incorrect number of instances

            for i in range(5):
                if g[i] == self.word[i]:
                    self.list = [x for x in self.list if x[i] == g[i]]  # correct position
                elif g[i] in self.word:
                    self.list = [x for x in self.list if x[i] != g[i]]  # incorrect position
            return False

    def clone(self):
        return game_state(self.word, self.list.copy())

    def shuffle(self):
        random.shuffle(self.list)

    def play(self):
        L = []
        done = False
        while not done:
            W = self.list[random.randint(0, len(self.list)-1)]
            L.append(W)
            done = self.guess(W)
        return L

if __name__ == "__main__":
    w = "whack"
    W = words_all
    game = game_state(w, W)

    results = [0]*20
    start = datetime.now()

    START_WORD = False
    #START_WORD = "acrid"
    #START_WORD = "notes"
    START_WORD = "laser"

    print("START: ", START_WORD)
    while (datetime.now() - start).total_seconds() < 30:
        G = game.clone()
        G.word = words[random.randint(0, len(words)-1)]
        if START_WORD and G.guess(START_WORD):
            L = [START_WORD]
        else:
            L = G.play()
        results[len(L) + 1 if START_WORD else 0] += 1

    while results[-1] == 0:
        del results[-1]

    N = sum(results)
    A = ""
    B = ""
    C = ""
    for i in range(len(results)):
        A += "%7d"%i
        B += "%7d"%results[i]
        C += "    %2d%%"%int(0.5 + results[i]*100/N)

    print(N, "games")
    print(A)
    print(B)
    print(C)

    plt.bar(range(len(results)), results)
    plt.show()