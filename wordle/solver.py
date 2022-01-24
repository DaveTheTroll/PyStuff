from words import *
import random

class game_state:
    def __init__(self, word, word_list):
        self.word = word
        self.list = word_list

    def guess(self):
        g = self.list[0]
        print(g.upper(), len(self.list))
        if g == self.word:
            return True
        else:
            self.list.remove(g)
            for i in range(5):
                if g[i] == self.word[i]:
                    self.list = [x for x in self.list if x[i] == g[i]]
            for l in set(g):
                n = min(g.count(l), self.word.count(l))
                if n == 0:
                    self.list = [x for x in self.list if not (l in x)]
                else:
                    self.list = [x for x in self.list if x.count(l) >= n]
            return False

if __name__ == "__main__":
    w = words[0]
    W = words_all
    random.shuffle(W)
    game = game_state(w, W)

    while(not game.guess()):
        pass

