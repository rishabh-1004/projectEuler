import math

def reverse_string(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

def SieveOfEratosthenes(n): 
      
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
           
        if (prime[p] == True): 
              
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    return prime


#while i:
 
#######Check for truncatable primes##########
def checkTruncatablePrime(c):
    s=0
    counter1=0
    while c>0:
        d=c%10
        c=c//10
        if(counter1<1):
            s=(1*d)+s    
        else:
            s=(int(math.pow(10,counter1))*d)+s
        counter1+=1
        #print("s",s)
        if not (list1[s]):
            return False
    return True

def checkTruncatablePrimeLeft(c):
    s=0
    counter1=0
    while c>0:
        d=c%10
        c=c//10
        s=s*10+d
        counter1+=1
        #print("s",s)
        if not (list1[s]):
            return False
    return True


import time
start= time.perf_counter()
list1=SieveOfEratosthenes(999999)
list1[1]=False
counter=0
sum_=0
i=11
while counter<11:
    if(list1[i]):
        #print(i)
        #print(int(reverse_string(str(i) )))
        if(checkTruncatablePrime(i) and checkTruncatablePrimeLeft( int(reverse_string(str(i) )) )):
            #print("Truncatable: ",i)
            counter+=1
            sum_=sum_+i
    i+=1
print(sum_)
print(f'Time Taken :  {time.perf_counter()-start}')

#748317
#Time Taken :  0.4576106