def sieve_of_eratosthenes(n):
    primes = set(range(2,n))
    for num in range(2, int(n**0.5) + 1):
        if num in primes:
            for mult in range(num * num, n, num):
                primes.discard(mult)
    
    return list(primes)