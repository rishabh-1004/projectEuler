###---Euler3--###
import time 
start=time.perf_counter()


def primeFactorization(number):
  def isPrime(primes,n):
    for p in primes.keys():
      if n%p ==0:
        return False
    primes[n]=False
    return True

  n=2
  while not number==1 and n<=number:
        if(isPrime(primes,n)):
          if number%n==0:
            primes[n]=True
            number=number/n
        n=n+1 

  return [n for n in primes.keys() if primes[n]]      
primes=dict()
x=600851475143
s=primeFactorization(x)
print (s[-1])
print(f"Soltion took: {time.perf_counter()-start}")

#6857
#Soltion took: 0.0259857280000233
