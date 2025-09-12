# This creates a new integer variable with the value of 10
# There is nothing magical about the "_num" in the variable name, it will just
# help us keep track of it
length_num = 50
width_num = 10

# If you add the numbers together, you get the result you expected:
print(length_num + width_num) # this will print 60
# But if you try to add a number and a string together, you will get an error:

# length_num + "10" # this will cause an error
# You can convert the values to the strings "50 and "10" like this:
length_str = str(length_num)
width_str = str(width_num)
print(length_str + width_str) # this will print "5010"
# or you can convert the strings "50" and "10" to numbers like this:
# length_num = int(length_str)
# width_num = int(width_str)
# # The computer now thinks of these variable as two characters, the digit 5 followed
# by the digit 0, and the digit 1 followed by the digit 0.

# If you try to add the two strings together, it will concatenate them, or display
# one after the other:
print(length_str + width_str) # This displays: 5010