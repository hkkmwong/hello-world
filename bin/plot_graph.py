# importing the required module
import matplotlib.pyplot as plt
 
# x axis values
x = [1,2,3,4,5,6,7,8,9,10]
# corresponding y axis values
y = [2,4,1,32,122,43,32,11,2,6]
 
# plotting the points
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()
