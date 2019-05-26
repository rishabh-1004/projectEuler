import time

start=time.perf_counter()

filepath="euler018.txt"

with open(filepath,'r') as files:
	array=[]
	for each in files:
		array.append(each)

newArray=[]
for i in array:
	j=i.split(' ')
	k=[int(n) for n in j]
	newArray.append(k)
#print(newArray)


def max_path(tri):
    while len(tri) > 1:
        t0 = tri.pop()
        t1 = tri.pop()
        tri.append([max(t0[i], t0[i+1]) + t for i,t in enumerate(t1)])
    return tri[0][0]

print(max_path(newArray) )
print(f'time taken : {time.perf_counter()-start}')


#1074
#time taken : 0.00023085899965735734
