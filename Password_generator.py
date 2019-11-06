''' Write a password generator in Python. Be creative with how you
generate passwords -
strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols.
The passwords should be random, generating a new
password every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list.'''

import random
import string




def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):

	return ''.join(random.choice(chars) for _ in range(size))



print(pw_gen(int(input('How many characters in your password?'))))

a= ''
my_password = '' 

for i in range(8):
    
    a += chr(random.choice(range(32,127)))
    
print(a)
    

b = random.sample(range(32,127), k=10)
print(b)

list = range(32,127)

my_password = ''

for i in range(8):
    my_password += chr(random.choice(list))
print(my_password)
