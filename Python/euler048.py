import time
start=time.perf_counter()
total=0
for i in range (1,1001):
    total+=(i**i)
print(str(total)[-10:])
print(f'Time Taken : {time.perf_counter()-start}')

#9110846700
#Time Taken : 0.013161400000000004