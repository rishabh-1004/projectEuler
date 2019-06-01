from itertools import permutations
import time

start=time.perf_counter()
perms=[''.join(p) for p in permutations ('0123456789')]
sort=sorted(perms)
print (sort[999999])
print(f'Time taken: {time.perf_counter()-start}')

#2783915460
#Time taken: 1.424219800001083 