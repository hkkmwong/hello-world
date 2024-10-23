'''
# install modules
python -m pip install numpy
python -m pip install pandas

'''

import numpy

arr = [1, 2, 3, 4, 5, 1] #list
arr1 = (1, 2, 3, 4, 5, 1) #tuple
arr2 = {1, 2, 3, 4, 5, 1} #set, no repeat
arr3 = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 1:'A'} #dict, no repeat

print(arr)
print(type(arr))

print(arr1)
print(type(arr1))

print(arr2)
print(type(arr2))

print(arr3)
print(type(arr3))
