from typing import *


class Psokit:
    def __init__(self, p: Set[str]):
        self.pos = set([w for w in p if not w.startswith("-")])
        self.neg = set([w[1] for w in p if w.startswith("-")])

    def __add__(self, other):
        pos = self.pos.difference(other.neg).union(
            other.pos.difference(self.neg))
        neg = self.neg.difference(other.pos).union(
            other.neg.difference(self.pos))
        return Psokit(pos.union(set([f"-{w}" for w in neg])))

    def __str__(self):
        return " + ".join(self.pos.union(set(["-" + w for w in self.neg])))

    def __hash__(self) -> int:
        return hash(str(self))

    def isEmpty(self):
        return len(self.pos) == 0 and len(self.neg) == 0

    def __eq__(self, value: object) -> bool:
        return self.pos == value.pos and self.neg == value.neg


def alg(cnf: set[Psokit]):
    while True:
        n = []
        to_pass = [w for w in cnf]
        for i in range(len(to_pass)):
            for j in range(i, len(to_pass)):
                n.append(to_pass[i] + to_pass[j])
                print(
                    f'{i}:{j}   :   {to_pass[i]} | {to_pass[j]} -> {to_pass[i] + to_pass[j]}')
                if n[-1].isEmpty():
                    return True
        if set(n).issubset(cnf):
            return False
        print("-"*10 + "New" + "-"*10)
        cnf = cnf.union(set(n))


if __name__ == "__main__":
    p1 = Psokit({"-D", "Z"})
    p2 = Psokit({"-C", "-M"})
    p3 = Psokit({"-P", "-Z"})
    p4 = Psokit({"A"})
    p5 = Psokit({"C", "D"})
    p5 = Psokit({"C", "D"})
    p6 = Psokit({"M"})
    p7 = Psokit({"P"})
    print(alg({p1, p2, p3, p4, p5, p6, p7}))
    # p = Psokit({"a", "c"})
    # q = Psokit({"a", "c"})
    # print(set([p]) <= (set([q])))
