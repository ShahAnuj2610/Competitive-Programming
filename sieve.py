def SieveOfEratosthenes(n):
    prime = [True for i in xrange(n+1)]
    p=2
    while(p * p <= n):
        if (prime[p] == True):
            for i in xrange(p * 2, n+1, p):
                prime[i] = False
        p+=1
    ans = []
    for p in xrange(2, n):
        if prime[p]:
            ans.append(p)
            
    return ans

primes = SieveOfEratosthenes(3000)

print primes
