def sieve(limit):
    primes=[True]*(limit+1)
    primes[0],primes[1]=False,False
    p=2
    while p*p<=limit:
        if primes[p]:
            for i in range(p*p, limit+1, p):
                primes[i]=False
        p+=1
    
    prime_numbers=[i for i, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

try:
    n=int(input("enter a number to check: "))
    if n<2:
        print("There are no prime numbers less than 2")
    else:
        print(f"Prime numbers up to {n}:")
        print(sieve(n))
except ValueError:
    print("enter a valid integer!")