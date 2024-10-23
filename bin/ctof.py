# Python Program to convert temperature in celsius to fahrenheit

# 20210416 added below comment block

"""
# change this value for a different result
celsius = 37.5
"""

# input celsius value
celsius = float(input("Input celsius value: "))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
