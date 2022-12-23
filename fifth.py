# Two files with a text of polynominals in them
# Open them and output their sum

from utils import Utils
from random import randint as random

NUMS = ['0','1','2','3','4','5','6','7','8','9']

class PolySum():
    
    def __init__(self) -> None:
        
        poly_1: str = ""
        poly_2: str = ""
        poly_3: str = ""
        coffiecients: list[int] = []
        
        self.poly_1 = poly_1
        self.poly_2 = poly_2
        self.poly_3 = poly_3
        self.coffiecients = coffiecients
        
    def make_list(self, k) -> None:
        for i in range(k):
            self.coffiecients.append(random(-100,100))
        
    def make_file_1(self) -> None:
        poly: str = ""
        
        for i in range(len(self.coffiecients) - 1, -1, -1):
            if self.coffiecients[i] == 0:
                pass
            elif i == 0:
                poly += f"{self.coffiecients[i]}"
            else:
                poly += f"{self.coffiecients[i]}*x^{i} + "
                
        poly += " = 0"
        
        with open("poly_1.txt", 'w') as f:
            f.write(poly)
        f.close()
            
    def make_file_2(self) -> None:
        poly: str = ""
        
        for i in range(len(self.coffiecients) - 1, -1, -1):
            if self.coffiecients[i] == 0:
                pass
            elif i == 0:
                poly += f"{self.coffiecients[i]}"
            else:
                poly += f"{self.coffiecients[i]}*x^{i} + "
                
        poly += " = 0"
        
        with open("poly_2.txt", 'w') as f:
            f.write(poly)
        f.close()
        
    def readfile(self, n: int) -> None:
        
        if n == 1:
            with open("poly_1.txt", "r") as f:
                self.poly_1 = f.read()
            f.close()
        elif n == 2:
            with open("poly_2.txt", "r") as f:
                self.poly_2 = f.read()
            f.close()
    
    def sum(self) -> None:
        pwr: int = 0
        foo: str = ""
        bar: str = ""
        ch: bool = False
        baz: int = 0
        gaz: int = 0
        p_1 = list(self.poly_1)
        p_2 = list(self.poly_2)
        p_3: str = ""
        
        while len(p_1) < len(p_2):
            p_1.append(" ")
        while len(p_2) < len(p_1):
            p_2.append(" ")
            
        for i in range(len(p_1)):
            if p_1[i] == 'x':
                for j in range(len(p_2)):
                    if p_2[j] == 'x' and p_1[i + 2] == p_2[j + 2]:
                        pwr = int(p_1[i + 2])
                        for r in range(i,0,-1):
                            if p_1[r] == '-' or p_1[r] == ' ':
                                foo = str(p_1[r:i])
                        for r in range(j,0,-1):
                            if p_2[r] == '-' or p_2[r] == ' ':
                                bar = str(p_2[r:i])
                    else:
                        pwr = int(p_1[i + 2])
                        for r in range(i,0,-1):
                            if p_1[r] == '-' or p_1[r] == ' ':
                                foo = str(p_1[r:i])
                        for r in range(j,0,-1):
                            if p_2[r] == '-' or p_2[r] == ' ':
                                bar = str(p_2[r:i])
                                
            if p_1[i + 2] == '=':
                for j in range(i,len(p_1),-1):
                    if p_1[j] == ' ':
                        foo = str(p_1[j:i])
            if p_2[i + 2] == '=':
                for j in range(i,len(p_2),-1):
                    if p_2[j] == ' ':
                        bar = str(p_2[j:i])
                        
            for j in range(len(foo) - 1,0,-1):
                if foo[j] == '-':
                    ch = True
                else:
                    if ch:
                        baz += int(foo[1:]) * (10**j)    
                    baz += int(foo) * (10**j)
            if ch:
                baz *= -1
            ch = False
            for j in range(len(bar) - 1,0,-1):
                if bar[j] == '-':
                    ch = True
                else:
                    if ch:
                        gaz += int(foo[1:]) * (10**j)    
                    gaz += int(foo) * (10**j)
                if ch:
                    gaz *= -1
            baz += gaz
            if baz == 0:
                pass
            elif pwr == 0:
                poly += f"{baz}"
            else:
                poly += f"{baz} * x^{pwr} + "
                
                            
def main() -> int:
    
    p = PolySum()
    p.make_list(10)
    p.make_file_1()
    p.make_list(5)
    p.make_file_2()
    p.readfile(1)
    p.readfile(2)
    p.sum()
    
    return 0


if __name__ == "__main__":
    main()