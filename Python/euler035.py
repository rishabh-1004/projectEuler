import time
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime


def iscircularprime(n):
    global primes
    s=str(n)
    for i in range(len(s)):
        s=s[-1] + s[0:-1]
        if not primes[int(s)]:
            return False
    return True

start=time.perf_counter()
primes=SieveOfEratosthenes(10000000)
primes[0]=primes[1]=False
counter=0
for i in range(2,1000000):
    if(primes[i]):
        if(iscircularprime(i)):
            counter+=1
print(counter)
print(f'Time Taken : {time.perf_counter()-start}')

#55
#Time Taken : 3.4590515