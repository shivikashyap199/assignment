from math import sqrt
class PrimeRange:
    def __init__(self, start, end=None):
        if end is None:
            self.start = 2
            self.end = start
        else:
            self.start = start
            self.end = end

    def is_prime(self, n):
        prime_flag = 0
        if(n > 1):
            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return True
            else:
                return False
        else:
             return False

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        while not self.is_prime(self.start):
            self.start += 1
        prime = self.start
        self.start += 1
        return prime

if __name__ == '__main__' :
    for p in PrimeRange(10):
        print(p, end=' ')  
    print("\n")

    primes = PrimeRange(10, 20)
    it = iter(primes)

    print(next(it))  
    print(next(it))  
    print(next(it))  
    print(next(it))  
    print(next(it))  