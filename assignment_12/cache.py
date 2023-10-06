import time
cached_data = {}

def cached(func):
    def inner(*args, **kwargs):
        if args in cached_data:
            return cached_data[args]
        result = func(*args, **kwargs)
        cached_data[args] = result
        return result
    
    return inner

def performance_monitor(func):
    def measure_time(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    
    return measure_time

@cached
@performance_monitor
def factorial(n):
    print(f"Calculating factorial({n})")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


R1 = factorial(5)  
print(f"R1 = {R1}")
R2 = factorial(5)  
print(f"R2 = {R2}")
R3 = factorial(7)  
print(f"R3 = {R3}")