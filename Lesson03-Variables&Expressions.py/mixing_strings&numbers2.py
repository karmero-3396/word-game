# This creates a new integer variable with the value of 10
length_num = 50
width_num = 10
# If you add the numbers together, you'd get the result you expect:
print(length_num + width_num)

# You can convert thevalues to the string "50" and "10" like this:
length_string = str(length_num)
width_string = str(width_num)
# Now if you add the strings together, you'd get this: "5010"
print(length_string + width_string)
# You can also conver the strings back to integers like this:
length_num = int(length_string)
width_num = int(width_string)
# Now if you add the numbers together, you'd get the result you expect:
print(length_num + width_num)

