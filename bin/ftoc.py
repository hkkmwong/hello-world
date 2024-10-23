# Python Program to convert temperature in fahrenheit to celsius

# 20210416 added below comment block

"""
# change this value for a different result
fahrenheit = 99.5
"""

# input fahrenheit value
fahrenheit = float(input("Input fahrenheit value: "))

# calculate celsius
celsius = (fahrenheit - 32) / 1.8
print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius' %(fahrenheit,celsius))
