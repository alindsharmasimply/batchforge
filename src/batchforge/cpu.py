import time


def is_prime(num: int):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def count_primes(n):
    count = 0

    start = time.perf_counter()

    for i in range(2, n):
        if is_prime(i):
            count += 1

    elapsed = (time.perf_counter() - start) * 1000
    print(f"Elapsed Time for {n} = {elapsed}")
    return count
