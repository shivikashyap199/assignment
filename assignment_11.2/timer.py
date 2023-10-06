import time
def find_primes(min, max):
    primes = []
    for num in range(min, max + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time

with Timer() as t:
    p = find_primes(2, 20000)
    print('total primes', len(p))

print('total time taken', t.time_taken)