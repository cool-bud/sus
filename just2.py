from random import randrange as rn
from time import sleep as sl

b = 1
for i in range(1,10):
    
    sl(0.5)
    a = rn(1, 9)
    print("\033[91m "+str(a)+" \033[0m")
    b = b + a
    #print("\033[92m "+str(b)+" \033[0m")
    #print("\033[93m This text will be yellow \033[0m")
    #print("\033[94m This text will be blue \033[0m")
print("\033[92m "+str(b)+" \033[0m")