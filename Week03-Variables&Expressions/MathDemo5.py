print("On your next birthday, you will be " + str(int(input("How old are you? ")) + 1)) 
print()
print("You have " + str(int(input("How many egg cartons do you have? ")) * 12) + " eggs")
print()
# The above code can be simplified to a single line as shown below:
cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
cookies_per_person = int(cookies) / int(people)
print(f"Each person may have {cookies_per_person} cookies")
print()
# The above code can be simplified to a single line as shown below:
# print("Each person may have " + str(int(input("How many cookies do you have? ")) // int(input("How many people are there? "))) + " cookies")
# Note: The above line is commented out to avoid redundancy and potential confusion during execution.
# The use of '//' ensures that the result is an integer (floor division).
# Uncomment the line below to use the single-line version
# print("Each person may have " + str(int(input("How many cookies do you have
# ")) // int(input("How many people are there? "))) + " cookies")
print("Each person may have " + str(int(input("How many cookies do you have? ")) / int(input("How many people are there? "))) + " cookies")