# Sequence of numbers.
# Program outputs unique elements
from utils import Utils


class FindUniqueNumber():
    
    def __init__(self) -> None:
        
        original: str = ""
        unique: str = ""
        
        self.original = original
        self.unique = unique
        
    def get_original(self, og: str) -> None:
        self.original = og
        
    def get_unique(self) -> str:
        l_original: list = list(self.original)
        foo: int = 0
        bar: int = 0
        size = len(l_original)
        
        for i in range(size):
            
            foo = l_original.pop(0)
            
            for j in range(size - 1):
                if foo == l_original[j]:
                    bar += 1
            
            if bar == 0:
                self.unique += str(foo)
            
            l_original.append(foo)
            foo, bar = 0, 0
        
        return self.unique
    
    
def main() -> int:
    ls = FindUniqueNumber()
    foo: str
    
    while True:
        foo = input(Utils.message(3))
        ls.get_original(foo)
        print(f"{ls.get_unique()}", sep= "/n")
        
        if Utils.terminate():
            break
    return 0


if __name__ == "__main__":
    main()
