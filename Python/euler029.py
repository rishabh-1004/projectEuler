import time

start=time.perf_counter()
list_=[]
for i in range(2,101):
	for j in range(2,101):
		list_.append(i**j)

print (len(set(list_)))
print (f"Time taken: {time.perf_counter()-start}")

#9183
#Time taken: 0.008497699999992392