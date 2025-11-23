#   *******--------PASSWORD GENERATOR----------**********
import random
import string

def gen_pass(len =12,inlcude_num=True,include_symbol=True):
    
    #Get all letters include small and capital letters
    char = string.ascii_letters

    #check if inlcude number
    if inlcude_num == True:
        char+=string.digits

    #check if include symbol 

    if include_symbol == True:
        char+=string.punctuation

    password = ""

    for i in range(len):
        password += random.choice(char)

    return password

print("Password Generator")



len =input("Enter length of password: ")
try:
    len= int(len)   # convert string to integer
except ValueError:
    print("Wrong Input")
else:
    inlcude_num = input("Do you want numbers y/n ?: ").lower() == "y"
    inlcude_symbol = input("Do you want symbol y/n ?: ").lower() == "y"

    password= gen_pass(len,inlcude_num,inlcude_symbol)

    print(f"Your Password is \n {password}")