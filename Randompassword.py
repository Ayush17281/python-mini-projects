# Random Password Generator Programme Using Python 

import random  #import random module
import string  #import string module 

Charvalue= string.ascii_letters + string.digits + string.punctuation  # string.ascii_letters , string.digits , string.punctuation
 
pass_len=int(input("Enter the Required Password Length : "))

#------------------------------------------------------------------------------------------------------
#method 1 using list
password=[]
for i in range(pass_len):
    password.append(random.choice(Charvalue))

final_password="".join(password)
print("Password: ",final_password)
print("Password Generated Successfully")

#------------------------------------------------------------------------------------------------------
# method 2 using string
password=""
for i in range (pass_len) :
    password+=random.choice(Charvalue)

print("Password: ",final_password)
print("Password Generated Successfully")
#------------------------------------------------------------------------------------------------------








