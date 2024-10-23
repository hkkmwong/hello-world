# Python Program to convert temperature between Celsius and Fahrenheit

repeat = "y"
while repeat == "y":
    
# Choose Celsius to Fahrenheit or Fahrenheit to Celsius

    choice = input("Enter 'c' for Cel to Fah, 'f' for Fah to Cel, other values terminate program: ")

    if choice == 'c' or choice == 'f':
        
# input celsius value and calculate fahrenheit
        if choice == 'c':
            celsius = float(input("Enter Celsius value: "))
            fahrenheit = (celsius * 1.8) + 32
            print('%0.2f degree Celsius is equal to %0.2f degree Fahrenheit' %(celsius,fahrenheit))
            choice = ''
            repeat = input("Run program again? (y/n) ")

# input fahrenheit value and calculate celsius
        elif choice == 'f':
            fahrenheit = float(input("Enter Fahrenheit value: "))
            celsius = (fahrenheit - 32) / 1.8
            print('%0.2f degree Fahrenheit is equal to %0.2f degree Celsius' %(fahrenheit,celsius))
            choice = ''
            repeat = input("Run program again? (y/n) ")

    else:
        print()
        print('Wrong input, program terminated!')
        repeat = 'n'

print()
print('Completed!')
