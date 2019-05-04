###---Euler4--###
import time 
start=time.perf_counter()

def checkPalindrome(number):
  n=number
  c=0
  while n>0:
    d=n%10
    n=n//10
    c=(c*10)+d
  if(number==c):
    return True
  else:
    return False
palindromes=[]
maximum=0
for i in range(999,100,-1):
  for j in range(999,100,-1):
    s=i*j
    if checkPalindrome(s) and s>maximum:
      maximum=s
      palindromes.append([s,i,j])
      break
print(palindromes[-1])
print(f"Soltion took: {time.perf_counter()-start}")

#[906609, 993, 913]
#Soltion took: 0.840646518000085