"""
the Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def sieve_of_eratosthenes(bound):

    primes = list(range(2, bound))
    for divisor in range(2, bound):
        for stride in range(2 * divisor, bound, divisor):
            if stride in primes:
                primes.remove(stride)
                
    # Return a list of the prime numbers in range(2, bound)
    return primes

#function call to find primes upto 200
print((sieve_of_eratosthenes(200)))
#function call to find primes upto 2000
print((sieve_of_eratosthenes(2000)))
