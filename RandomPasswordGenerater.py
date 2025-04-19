import random 
import string
print ("Welcome to the Random Password Generator")

def main():
    
 lenght = int(input("Enter the password length you want : "))
 lowerd = string.ascii_lowercase
 upperd = string.ascii_uppercase
 digitsd = string.digits 
 speciald = string.punctuation 
 combine = lowerd + upperd + digitsd + speciald 
 x=random.sample(combine, lenght)
 password = "".join(x)
 print("Password")
 main()
 main()
