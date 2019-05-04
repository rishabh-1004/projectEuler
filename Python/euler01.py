####_Euler1_####

digits=[]
for i in range(1,1000):
  if(i%3==0 or i%5==0):
    digits.append(i)

print (sum(digits))

#Output
#233168