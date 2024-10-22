# This programme allows user to input no. of numbers
# Then provide the sum and average of the numbers input

r = 0
sum = 0
x = int(input("How many numbers for computation?"))
while r < x:
    var = float(input("Enter number: "))
    r += 1
    sum = sum + var
print("Sum of " + str(x) + " numbers = " + str(sum))
print("Avg of " + str(x) + " numbers = " + str(sum / x))