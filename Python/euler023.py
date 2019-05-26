
import time
import math

def divisors(n):
    yield 1
    largest = int(math.sqrt(n))
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n // i


def is_abundant(n):
    if n<12:
        return False
    return (sum(divisors(n))>n)

def is_abundant_sum(n):
    abundants_set = set(abundants)
    for i in abundants:
        if i>n:
            return False
        if (n-i) in abundants_set:
            return True
    return False

start=time.perf_counter()
abundants = [x for x in range(1, 28123 + 1) if is_abundant(x)]
sum_of_non_abundants = sum(x for x in range(1, 28123 + 1) if not is_abundant_sum(x))

print(sum_of_non_abundants)
print(f'Time taken : {time.perf_counter()-start} ')

#4179871
#Time taken : 11.4341219