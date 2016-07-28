import string
import random

def id_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
    
print (id_generator())
