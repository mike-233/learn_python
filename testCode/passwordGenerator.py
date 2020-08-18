
import random
import string
def get_random_password_string(length_password) :
    password_charaters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_charaters) for x in range(length_password))
    
    print("Your password generator is : "+password)
    
    
number = int(input("Entrer la longueuur du mot de passe : "))
get_random_password_string(number)