import time 
from sympy import factorint

start= time.perf_counter()

for i in range(10000,10_000_000):
	list_sum=sum([num for num in range(i+1)])
	counter=1
	fact_dict=factorint(list_sum)
	#print(fact_dict)

	for j in fact_dict.values():
		counter*=(j+1)

	if counter>500:
		print(list_sum)
		break


print(f'time taken : {time.perf_counter()-start}' )

#76576500
#time taken : 2.315941146