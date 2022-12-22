# Integer prime factorization
# N ∊ N
# Create a list of N's prime 
# Methods used Trial division
# 
from utils import Utils


class TrialDivison():
    
    def __init__(self) -> None:
        
        N: int = 0
        nums: list[int] = []
        numm: list[int] = []
        
        self.N = N
        self.nums_snail = nums
        self.nums_rabbit = numm
    
    def get_N(self, N: int) -> None:
        self.N = N
    
    def snail_algorithm(self) -> list[int]:
        N = self.N
        factor: int = 2    
        while N > 1:
            if N % factor == 0:
                self.nums_snail.append(factor)
                N //= factor
            else:
                factor += 1
        return self.nums_snail
    
    def rabbit_algorithm(self) -> list[int]:
        N = self.N
        factor: int = 2
        
        while N % factor == 0:
            self.nums_rabbit.append(2)
            N //= 2
        factor = 3
        while factor * factor <= N:
            if N % factor == 0:
                self.nums_rabbit.append(factor)
                N //= factor
            else:
                factor += 2
        if N != 1:
            self.nums_rabbit.append(N)
        return self.nums_rabbit
    
        
def main() -> int:
    num: int = 0
    factor = TrialDivison()
    print(Utils.message(0))
    while True:
        num = int(input(Utils.message(3)))
        factor.get_N(num)
        print(f"Slow method:\n{factor.snail_algorithm()}\n" + 
              f"Fast method:\n{factor.rabbit_algorithm()}")
        
        if Utils.terminate():
            break
    
    return 0


if __name__ == "__main__":
    main()
