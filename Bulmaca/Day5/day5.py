
class Crates:
    def __init__(self, dimension):
        self.C = []
        for _ in range(dimension):
            self.C.append([])
    def copy(self):
        L = len(self.C)
        C = Crates(L)
        for i in range(L):
            C.C[i] = self.C[i].copy()
        return C
    def fill(self, Li):
        j = 0
        for i in range(1, len(Li), 4):
            if Li[i] != " ":
                self.C[j].insert(0, Li[i])
            j += 1
    def top(self):
        return "".join(map(lambda x: x[-1], self.C))
    def apply_proc(self, P, is_9001 = False):
        list_ = self.C[P.frm][-P.move:]
        self.C[P.to].extend(list_ if is_9001 else reversed(list_))
        self.C[P.frm] = self.C[P.frm][:-P.move]
class Prod:
    def __init__(self, txt):
        splitted = txt.split(" ")
        self.move = int(splitted[1])
        self.frm = int(splitted[3]) - 1
        self.to = int(splitted[5]) - 1
        
file = open('veriler.txt', 'r')
input_ = file.readlines()

C1 = Crates(9)
procedures = []

for i in range(0, len(input_)):
    L_ = input_[i].strip("\n")
    if i < 8:
        C1.fill(L_)
        continue
    if i > 9:
        procedures.append(Prod(L_))

C2 = C1.copy()

for P in procedures:
    C1.apply_proc(P)
    C2.apply_proc(P, True)

print("[Part1]: ", C1.top())
print("[Part2]: ", C2 .top())