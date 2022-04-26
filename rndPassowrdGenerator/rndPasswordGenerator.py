import string
import random

def password_generator(size=15, chars=(string.ascii_uppercase + string.ascii_lowercase+string.digits)):
    return ''.join(random.choice(chars) for _ in range(size))

#change 'size' for password length

print(password_generator())
