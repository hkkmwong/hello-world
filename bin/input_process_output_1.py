# Online Python - IDE, Editor, Compiler, Interpreter
# https://www.programiz.com/python-programming/online-compiler/
#
# Online Python
# https://www.online-python.com/

'''
My First Python Program - Input -> Process -> Output, with UDFs
'''
# This helps evaluate sum and average of two numbers
def sum(a,b):
    return(a + b)
def avg(a,b):
    return(sum(a,b)/2)
a = float(input('Enter 1st No.: '))
b = float(input('Enter 2nd No.: '))
print('Sum is: ' + str(sum(a,b)))
print('Average is: ' +str(avg(a,b)))