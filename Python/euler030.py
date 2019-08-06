import time
from itertools import combinations_with_replacement
start=time.perf_counter()
ex,s=5,0
p={str(i): i**ex for i in range(0,10)}

for cx in combinations_with_replacement('0123456789',ex+(ex>=5)):
    t=sum(p[x] for x in cx)
    sd=sum(p[x] for x in str(t))
    if(t==sd and t>9):
        s+=t

print (s)
print ("Time taken" , time.perf_counter()-start )


#443839
#Time taken 0.07704169999999999