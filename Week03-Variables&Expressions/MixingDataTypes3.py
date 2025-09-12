# This creates a new integer variable with the value 10 
# There is nothing magical about the "_num" in the variable name, it will just
# help us keep track of it
length_num = 10
width_num = 50
area_num = length_num * width_num # This creates a new integer variable with the value 500
print("The area of the rectangule is " + str(area_num) + " square units.") # we need to convert the integer to a string to concatenate it
# The above line could also be written using an f-string like this: 
print(f"The area of the rectangule is {area_num} square units")