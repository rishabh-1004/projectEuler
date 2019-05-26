###--Euler7--##
import time 

def isPrime(primes,number):
    for p in primes.keys():
      if (number%p==0):
        return False
    primes[number]=True
    return True
  

def main():
    counter=0
    primes=dict()
    for i in range(2,10_000_000_000):
      if (isPrime(primes,i)):
        counter=counter+1
        if (counter==10001):
          print(i)
          break
    
  
if __name__=="__main__":  
  start=time.perf_counter()
  main()
  print(f"Solution took: {time.perf_counter()-start}") 

#104743
#Solution took: 3.0644659470001443