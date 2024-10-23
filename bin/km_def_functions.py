'''
This file contains common user defined functions
'''
# Celcius to Fahrenheit
# Fahrenheit = Celcius * 9/5 + 32
def ctof(c):
    f = c * 9/5 + 32
    print(str(c)+' degree Celcius = '+str("%.2f" % f)+' degree Fahrenheit')


# Fahrenheit to Celcius
# Celcius = (Fahrenheit - 32) * 5/9
def ftoc(f):
    c = (f - 32) * 5/9
    print(str(f)+' degree Fahrenheit = '+str("%.2f" % c)+' degree Celcius')


# Celcius to Fahrenheit with input
# Fahrenheit = Celcius * 9/5 + 32
c = float(input('Enter degree in Celcius: '))
f = c * 9/5 + 32
print(str(c)+' degree Celcius = '+str("%.2f" % f)+' degree Fahrenheit')


# Then, Fahrenheit to Celcius with input
# Celcius = (Fahrenheit - 32) * 5/9
f = float(input('Enter degree in Fahrenheit: '))
c = (f - 32) * 5/9
print(str(f)+' degree Fahrenheit = '+str("%.2f" % c)+' degree Celcius')
