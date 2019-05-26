import time
import operator

start=time.perf_counter()

def collatz_number(number):
	counter=1
	while number>1:
		if (number%2==0):
			number=number/2
		else:
			number=(3*number)+1
		#print (f"{number} -> ", end =" ")
		counter+=1
	return(counter)


values=dict()
for i in range(10_00_000,1_00_000,-1):
	length=collatz_number(i)
	#print(length,i)
	values.update({i:length})
#print(values) 
print(max(values.items(), key=operator.itemgetter(1))[0])
print(f"time taken : {time.perf_counter()-start}")
	
#837799
#time taken : 48.105039615s	