import random
pwd = False
while pwd == False:
    pwd_len = int(input("the length of the password (must be betwwen 8 and 16): "))
    if 8<=pwd_len<=16 :
        pwd = True
numbers = input("do you want numbers in your password? (Y/N): ")
uppercases = input("do you want uppercase letters in your password? (Y/N): ")
symboles = input("do you want symboles in your password? (Y/N): ")
password = ""  

sym_list = ["&","@","-","_","#","{","}","(",")","[","]"]
pwd_list = list()

for i in range(97,123):
        pwd_list.append(str(chr(i)))

if numbers.upper() == 'Y':
    num = str(random.randint(0,9))
    pwd_list.append(num)
if uppercases.upper() == 'Y':
    for i in range (65,91):
        pwd_list.append(str(chr(i)))
if symboles.upper() == 'Y':
    pwd_list.extend(sym_list)

i = 1
while i <= pwd_len :
    indice = random.randint(0,len(pwd_list))
    password += pwd_list[indice]
    i += 1

print(password)

