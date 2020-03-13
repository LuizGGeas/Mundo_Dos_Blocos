import random

class Bloco:
    pai = None
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
        f = []
        if(len(self.v1) == 3):
            f1 = Bloco()
            f1.pai = self
            f1.v1 = self.v1
            f1.v2 = self.v2
            f1.v3 = self.v3
            f1.v2.append(f1.v1.pop())
            f2 = Bloco()
            f2.pai = self
            f2.v1 = self.v1
            f2.v2 = self.v2
            f2.v3 = self.v3
            f2.v3.append(f2.v1.pop())
            f.append(f1)
            f.append(f2)
        elif (len(self.v2) == 3):
            f1 = Bloco()
            f1.pai = self
            f1.v1 = self.v1
            f1.v2 = self.v2
            f1.v3 = self.v3
            f1.v1.append(f1.v2.pop())
            f2 = Bloco()
            f2.pai = self
            f2.v1 = self.v1
            f2.v2 = self.v2
            f2.v3 = self.v3
            f2.v3.append(f2.v2.pop())
            f.append(f1)
            f.append(f2)
        elif(len(self.v3) == 3):
            f1 = Bloco()
            f1.pai = self
            f1.v1 = self.v1
            f1.v2 = self.v2
            f1.v3 = self.v3
            f1.v1.append(f1.v3.pop())
            f2 = Bloco()
            f2.pai = self
            f2.v1 = self.v1
            f2.v2 = self.v2
            f2.v3 = self.v3
            f2.v2.append(f2.v3.pop())
            f.append(f1)
            f.append(f2)
        elif(len(self.v1) == 2):
            if(len(self.v2 == 1)):
                f1 = Bloco()
                f1.pai = self
                f1.v1 = self.v1
                f1.v2 = self.v2
                f1.v3 = self.v3
                f1.v1.append(f1.v2.pop())
                f2 = Bloco()
                f2.v1 = self.v1
                f2.v2 = self.v2
                f2.v3 = self.v3
                f2.v2.append(f2.v1.pop())
                f3 = Bloco()
                f3.pai = self
                f3.v1 = self.v1
                f3.v2 = self.v2
                f3.v3 = self.v3
                f3.v3.append(f3.v2.pop())
                f4 = Bloco()
                f4.pai = self
                f4.v1 = self.v1
                f4.v2 = self.v2
                f4.v3 = self.v3
                f4.v3.append(f4.v1.pop())
                f.append(f1)
                f.append(f2)
                f.append(f3)
                f.append(f4)
            else:
                f1 = Bloco()
                f1.pai = self
                f1.v1 = self.v1
                f1.v2 = self.v2
                f1.v3 = self.v3
                f1.v2.append(f1.v3.pop())
                f2 = Bloco()
                f2.pai = self
                f2.v1 = self.v1
                f2.v2 = self.v2
                f2.v3 = self.v3
                f2.v1.append(f2.v3.pop())
                f3 = Bloco()
                f3.pai = self
                f3.v1 = self.v1
                f3.v2 = self.v2
                f3.v3 = self.v3
                f3.v2.append(f3.v1.pop())
                f4 = Bloco()
                f4.pai = self
                f4.v1 = self.v1
                f4.v2 = self.v2
                f4.v3 = self.v3
                f4.v3.append(f4.v1.pop())
                f.append(f1)
                f.append(f2)
                f.append(f3)
                f.append(f4)
        elif(len(self.v2) == 2):
            if(len(self.v1 == 1)):
                f1 = Bloco()
                f1.pai = self
                f1.v1 = self.v1
                f1.v2 = self.v2
                f1.v3 = self.v3
                f1.v1.append(f1.v2.pop())
                f2 = Bloco()
                f2.v1 = self.v1
                f2.v2 = self.v2
                f2.v3 = self.v3
                f2.v3.append(f2.v2.pop())
                f3 = Bloco()
                f3.pai = self
                f3.v1 = self.v1
                f3.v2 = self.v2
                f3.v3 = self.v3
                f3.v3.append(f3.v1.pop())
                f4 = Bloco()
                f4.pai = self
                f4.v1 = self.v1
                f4.v2 = self.v2
                f4.v3 = self.v3
                f4.v2.append(f4.v1.pop())
                f.append(f1)
                f.append(f2)
                f.append(f3)
                f.append(f4)
            else:
                f1 = Bloco()
                f1.pai = self
                f1.v1 = self.v1
                f1.v2 = self.v2
                f1.v3 = self.v3
                f1.v2.append(f1.v3.pop())
                f2 = Bloco()
                f2.pai = self
                f2.v1 = self.v1
                f2.v2 = self.v2
                f2.v3 = self.v3
                f2.v1.append(f2.v3.pop())
                f3 = Bloco()
                f3.pai = self
                f3.v1 = self.v1
                f3.v2 = self.v2
                f3.v3 = self.v3
                f3.v3.append(f3.v2.pop())
                f4 = Bloco()
                f4.pai = self
                f4.v1 = self.v1
                f4.v2 = self.v2
                f4.v3 = self.v3
                f4.v1.append(f4.v2.pop())
                f.append(f1)
                f.append(f2)
                f.append(f3)
                f.append(f4)
        elif(len(self.v3) == 2):
            if(len(self.v2 == 1)):
                f1 = Bloco()
                f1.pai = self
                f1.v1 = self.v1
                f1.v2 = self.v2
                f1.v3 = self.v3
                f1.v1.append(f1.v2.pop())
                f2 = Bloco()
                f2.v1 = self.v1
                f2.v2 = self.v2
                f2.v3 = self.v3
                f2.v3.append(f2.v2.pop())
                f3 = Bloco()
                f3.pai = self
                f3.v1 = self.v1
                f3.v2 = self.v2
                f3.v3 = self.v3
                f3.v1.append(f3.v3.pop())
                f4 = Bloco()
                f4.pai = self
                f4.v1 = self.v1
                f4.v2 = self.v2
                f4.v3 = self.v3
                f4.v2.append(f4.v3.pop())
                f.append(f1)
                f.append(f2)
                f.append(f3)
                f.append(f4)
            else:
                f1 = Bloco()
                f1.pai = self
                f1.v1 = self.v1
                f1.v2 = self.v2
                f1.v3 = self.v3
                f1.v2.append(f1.v3.pop())
                f2 = Bloco()
                f2.pai = self
                f2.v1 = self.v1
                f2.v2 = self.v2
                f2.v3 = self.v3
                f2.v1.append(f2.v3.pop())
                f3 = Bloco()
                f3.pai = self
                f3.v1 = self.v1
                f3.v2 = self.v2
                f3.v3 = self.v3
                f3.v2.append(f3.v1.pop())
                f4 = Bloco()
                f4.pai = self
                f4.v1 = self.v1
                f4.v2 = self.v2
                f4.v3 = self.v3
                f4.v3.append(f4.v1.pop())
                f.append(f1)
                f.append(f2)
                f.append(f3)
                f.append(f4)
        elif len(self.v1) == 1 and len(self.v2) == 1 and len(self.v3) == 1:
            f1 = Bloco()
            f1.pai = self
            f1.v1 = self.v1
            f1.v2 = self.v2
            f1.v3 = self.v3
            f1.v1.append(f1.v2.pop())
            f2 = Bloco()
            f2.pai = self
            f2.v1 = self.v1
            f2.v2 = self.v2
            f2.v3 = self.v3
            f2.v1.append(f2.v3.pop())
            f3 = Bloco()
            f3.pai = self
            f3.v1 = self.v1
            f3.v2 = self.v2
            f3.v3 = self.v3
            f3.v2.append(f3.v1.pop())
            f4 = Bloco()
            f4.pai = self
            f4.v1 = self.v1
            f4.v2 = self.v2
            f4.v3 = self.v3
            f4.v2.append(f4.v3.pop())
            f5 = Bloco()
            f5.pai = self
            f5.v1 = self.v1
            f5.v2 = self.v2
            f5.v3 = self.v3
            f5.v3.append(f5.v1.pop())
            f6 = Bloco()
            f6.pai = self
            f6.v1 = self.v1
            f6.v2 = self.v2
            f6.v3 = self.v3
            f6.v3.append(f6.v2.pop())
            f.append(f1)
            f.append(f2)
            f.append(f3)
            f.append(f4)
            f.append(f5)
            f.append(f6)
        return f

final = [ 'c', 'b', 'a' ]
total = []
fechado = []
bl = Bloco()
bl.init()
total.append(bl)

while(total[0].v1 != final or total[0].v2 != final or total[0].v3 != final):
    posss = total[0].poss()
    for i in posss:
        k = 0
        for j in fechado:
            if i.v1 == j.v1 and i.v2 == j.v2 and i.v3 == j.v3:
                k = 1
        if k == 0:
            total.append(i)
    fechado.append(total.pop(0))


    
finalmente = []
finalmente.append[total[0]]
while(finalmente[len(finalmente)-1].pai != None):
    finalmente.append(finalmente[len(finalmente)].pai)
for i in reversed(finalmente):
    print(i)