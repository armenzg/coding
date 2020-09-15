'''
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from functools import lru_cache

def is_prime(num):
    if num > 0:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False

@lru_cache
def prime_factors(num):
    if num <= 3:
        return [num]
    factors = set()
    for i in range(2, num):
        # It can only be divisible by a number that is maximum of half
        if i > num//2:
            factors.add(num)
            break
        # XXX: We can check if the number is a prime number
        if num % i == 0:
            factors.add(i)
            factors = factors.union(prime_factors(num//i))
            break

    return factors

if __name__ == "__main__":
    assert sorted(prime_factors(1)) == [1]
    assert sorted(prime_factors(2)) == [2]
    assert sorted(prime_factors(3)) == [3]
    assert sorted(prime_factors(4)) == [2]
    assert sorted(prime_factors(5)) == [5]
    assert sorted(prime_factors(13195)) == [5, 7, 13, 29]
    assert max(sorted(prime_factors(13195))) == 29
    print(max(sorted(prime_factors(600851475143))))
