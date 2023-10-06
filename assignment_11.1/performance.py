import time

def performance_log(func):
    def measure_time(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        measure_time.time_taken = end_time - start_time
        return result
    return measure_time

@performance_log
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

x = find_primes(2, 11)
print(len(x))
print(x)  
print(find_primes.time_taken)  