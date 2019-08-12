import time

def champerowne(n):
    answer=''
    for c in range(n):
        answer+=str(c)
    return answer


start=time.perf_counter()
numbers=champerowne(200000)
answer=1
for i in range(6):
    answer*=int(numbers[10**i])
print (answer)
print(f'Time Taken : {time.perf_counter()-start}')

#210
#Time Taken : 0.11365779999999999