# Calculate pi to a certain decimal point
from utils import Utils


class Calculate_pi:
    
    _n: int = 1000000
    
    def __init__(self) -> None:
        
        raw_pi: float = 0.0
        clean_pi: str = 'NULL'
        numbers: list[int] = []
        
        for i in range(self._n):
            if i % 2 == 1:
                numbers.append(i)
                
        self.raw_pi = raw_pi
        self.clean_pi = clean_pi
        self.numbers = numbers
    
    def get_pi(self) -> None:
        for i in range(len(self.numbers)):
            self.raw_pi += (4 / self.numbers[i]) * ((-1)**i)
            
    def check_if_allowed(self, d: int) -> bool:
        if int(repr(d)[-1]) <= (len(str(self.raw_pi))):
            return True
        else:
            return False
    
    def get_pi_with_precission(self, foo: str) -> None:
        dec: int = 0
        ch: int = 0
        
        if (foo)[1] == 'e':
            foo = str(foo)[3:]
        else:
            foo += str(len(str(foo)) - 2)
            foo = foo[len(foo) - 1:]
            ch += 1
        
        if ch != 1:
            if foo[0] != "0":
                dec += int(foo[0]) * 10
            dec += int(foo[1])
        else:
            dec += int(foo)
        
        self.clean_pi = str(self.raw_pi)
        self.clean_pi = self.clean_pi[0:dec+2]
    
        
def main() -> int:
    
    d: float = 0
    
    print(Utils.message(3))
    pi = Calculate_pi()
    pi.get_pi()
    
    while True:
        d = float(input("Enter the desiered precision of pi.\nExample d = 0.01 -> pi = 3.14\n"))
        if pi.check_if_allowed(d):
            pi.get_pi_with_precission(str(d))
            print(pi.clean_pi)
        
        if Utils.terminate():
            break

    return 0


if __name__ == "__main__":
    main()
