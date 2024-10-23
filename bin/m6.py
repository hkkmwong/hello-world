# First Mark Six File
# 19 April 2021
import random
i=1
while i<7:
    x = round(random.random(),5) # random() shall give a no. from 0.00001 to 0.99999
    y = int(x*49)
    if y !=0:
        print(x, y)
        i +=1
