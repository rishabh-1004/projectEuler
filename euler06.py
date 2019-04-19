###---Euler6--###
import time
start = time.time()
sum_of_square=0
square_of_sum=0
total=0
for i in range(1,101):
  sum_of_square=sum_of_square+ pow(i,2)
  total=i+total
square_of_sum=pow(total,2)
final_answer= square_of_sum-sum_of_square
print(final_answer)
print(f"Solution took: {time.time()-start}")

#25164150
#Solution took: 0.00007534100006978406
