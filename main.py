import random

class Bloco:
    pai
    v1 = []
    v2 = []
    v3 = []

    def init(self, pai = None):
        self.v1.append('a')
        self.v1.append('b')
        self.v1.append('c')
        self.pai = pai
        return random.shuffle(self.v1)

    def poss(self):
        if(len(self.v1) == 3):
            f1 = Bloco()
            f1.pai = self
            f1.v1 = self.v1
            f1.v2.append(self.v1.pop())
            f2 = Bloco()
            f2.pai = self
            f2.v3.append(self.v1.pop())
            f2.v1 = self.v1
            return v1, v2


    


total = []
fechado = []
bl = Bloco()
bl.init()
total.append(bl)
for i in total:
    if(i.v1 == ['c', 'b', 'a'] or i.v2 == ['c', 'b', 'a'] or i.v3 == ['c', 'b', 'a']):
        break
    else

    


