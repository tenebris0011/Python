import string
import random
import os
import errno

use = input('What is the password for?' ) #This is so that it labels what the generated numbers are for.
flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
def id_generator(size=10, chars=string.ascii_letters + string.digits):
        return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

id = id_generator()

f = open('password.txt', 'a')

f.write(use + "\n")
f.write(id + "\n")
f.write("\n")

f.close()

try:
    file_handle = os.open('password.txt', flags)
except OSError as e:
    if e.errno == errno.EEXIST:
        pass
    else:
        raise
else:
    with os.fdopen(file_handle, 'w') as file_obj:
        file_obj.write(use + "\n")
        file_obj.write(id + "\n")

