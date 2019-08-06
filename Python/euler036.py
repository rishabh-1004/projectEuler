import time
def reverse_string(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)
    
def checkPalindrome(n):
    initial_number= n 
    if(str(n))==reverse_string(str(n)):
        return True
    return False
    
    
start=time.perf_counter()
list_of_palindromes=[] 
for i in range(0,1000000):
    #bin_a = bin(i)
    
    if(checkPalindrome(i)):
        binary = bin(i) 
        binary = binary[2:]
        binary_str=str(binary).lstrip("0")
        #print(binary_str)
        if(checkPalindrome(binary_str)):
            #print ("here")
            list_of_palindromes.append(i)
print (sum(list_of_palindromes))
print ("Time taken ",time.perf_counter()-start )

#872187
#Time taken  1.5106198000000002