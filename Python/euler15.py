import time
start=time.perf_counter()
def paths(n):
	i=1
	c=1
	while i<=n:
		c=c*(n+i)/i
		i+=1
	return c	

print (f"total no of possible paths: {int(paths(20))}")
print(f"Total time taken : {time.perf_counter()-start}")

#137846528820
# 0.00019594299999999704s