def pythagoreanTriplets(limits) : 
    c, m = 0, 2
    arr1=[]
  
    # Limiting c would limit  
    # all a, b and c 
    while c < limits : 
          
        # Now loop on n from 1 to m-1 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
  
            # if c is greater than 
            # limit then break it 
            if c > limits : 
                break
  
            arr1.append([a, b, c]) 
  
        m = m + 1
    return arr1

import time
start=time.perf_counter()
triplets=pythagoreanTriplets(1000)
for i in triplets:
    if (i[0]+i[1]+i[2]==1000):
        print (i[0]*i[1]*i[2])
print (f'Total time taken : {time.perf_counter()-start}')

#31875000
#Total time taken : 0.000514584999999998