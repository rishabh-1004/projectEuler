##--Euler 2 --#
import time
start=time.perf_counter()
values=[]
a,b=0,1
for i in range(1,100):
  c=a+b
  if(c>4000000):
    break
  a=b
  b=c
  if (c%2==0):
    values.append(c)
  
   
print (sum(values))
print(f"Soltion took: {time.perf_counter()-start}")

#4613732
#Soltion took: 0.0005689879999408731