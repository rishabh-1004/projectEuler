###---Euler5--###
import time 
start=time.perf_counter()
c=0
for i in range (10000000,50000000000,40):
      if (i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0 and i%20==0):
        print (i)
        break
        
        
print(f"Soltion took: {time.perf_counter()-start}")

#232792560
#Soltion took: 0.5619840350000231

