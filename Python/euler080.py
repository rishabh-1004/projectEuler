import time
from decimal import *

getcontext().prec = 110

start=time.perf_counter()
primeList=[True]*(100)

decimals=[]
for i in range(0,10):
    primeList[i**2]=False

for i in range(2,len(primeList)):
    if primeList[i]:
        sum=0
        number=Decimal(i).sqrt()
        number_dec = str(number).split('.')[0]+str(number).split('.')[1][0:99]
        number_dec=number_dec[0:100]
        for i in number_dec:
            sum=sum+int(i)
        decimals.append(sum)

total=0
for i in decimals:
    total=total+int(i)

print (total)
print(f'time taken: {time.perf_counter()-start}')

#40886
#time taken: 0.010985421999999995