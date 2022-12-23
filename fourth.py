# Make a list of coffiecients of polynominal
from utils import Utils
from random import randint as random

class Polynominal():
    
    def __init__(self) -> None:
        
        k: int = 0
        coffiecients: list[int] = []
        
        self.coffiecients = coffiecients
        self.k = k
        
    def get_k(self, k: int) -> None:
        self.k = k
        
    def make_list(self) -> None:
        for i in range(self.k):
            self.coffiecients.append(random(0,100))
        
    def show_poly(self) -> str:
        
        poly: str = ""
        
        for i in range(self.k - 1, -1, -1):
            if self.coffiecients[i] == 0:
                pass
            elif i == 0:
                poly += f"{self.coffiecients[i]}"
            else:
                poly += f"{self.coffiecients[i]} * x^{i} + "
                
        poly += " = 0"
        
        return poly


def main() -> int:
    
    foo: int = 0
    p = Polynominal()
    
    while True:
        foo = int(input(Utils.message(2)))
        
        if 0 < foo <= 6:
            p.get_k(foo)
            p.make_list()
            print(p.show_poly())
        else:
            print(Utils.message(6))
        
        if Utils.terminate():
            break
            
    return 0


if __name__ == "__main__":
    main()