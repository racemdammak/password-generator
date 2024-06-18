import string
import random

pwd = False
while pwd == False:
    pwd_len = int(input("the length of the password (must be betwwen 8 and 16): "))
    if 8 <= pwd_len <= 16 :
        pwd = True
numbers = input("do you want numbers in your password? (Y/N): ")
uppercases = input("do you want uppercase letters in your password? (Y/N): ")
symboles = input("do you want symboles in your password? (Y/N): ")
password = "" 

char_set = string.ascii_lowercase

if numbers.upper() == 'Y':
    char_set += string.digits
if uppercases.upper() == 'Y':
    char_set += string.ascii_uppercase
if symboles.upper() == 'Y':
    char_set += string.punctuation

password = password.join(random.choices(char_set, k=pwd_len))
print(password)