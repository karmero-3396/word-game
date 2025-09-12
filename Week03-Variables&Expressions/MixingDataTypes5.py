quantity_from_user = input("How many items do you have? ")
# The variable quantity_from_user is a string.
# To convert it to an integer you use the int(...) notation:
quantity_number = int(quantity_from_user)

# Because the quantity_number variable is an integer you can do math with it:
double_number = quantity_number * 2

# If you want to use these values in strings, you CANNOT just add them, you first
# have to convert them to a string:

# WRONGE:
print("Twice as many is" + double_number)

# RIGHT:
double_string = str(double_number)
print("Twice as many is " + double_string)

# Or you can use f-strings:
print(f"Twice as many is {double_number}")
# You can also do this in one step:
# Right:
print("Twice as many is " + str(double_number))
