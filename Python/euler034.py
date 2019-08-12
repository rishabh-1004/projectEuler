import time
def factorial(n):
    total=1
    for i in range(1,n+1):
        total*=i
        
    return total

def createDictionary():
    dict1={}
    for i in range(0,10):
        dict1.update({i:factorial(i)})
    return dict1

def checkCuriousNumber(n):
    global dict1
    number=n
    total=0
    while n>0:
        d=n%10
        n=n//10
        total+=dict1[d]
    if(total==number):
        return True
    return False
    
start=time.perf_counter()
dict1=createDictionary()

total=0
for i in range(3,1499999):
    if(checkCuriousNumber(i)):
        total+=i
print(total)    
print(f'Time Taken: {time.perf_counter()-start}')    


#40730
#Time Taken: 2.7870684