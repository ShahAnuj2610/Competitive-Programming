spf = {}
spf[1] = 1

def sieve(n):
    for i in xrange(2, n+1):
        spf[i] = i
    
    for i in xrange(4, n+1, 2):
        spf[i] = 2
    
    i = 3
        
    while i*i <= n:
        if spf[i] == i:
            j = i*i
            while j <= n:
                if spf[j] == j:
                    spf[j] = i
                j += i
        i += 1
        
def factorize(n):
    ans = []
    while n != 1:
        ans.append(spf[n])
        n /= spf[n]
        
    return ans
        
