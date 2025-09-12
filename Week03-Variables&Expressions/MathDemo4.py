age = input("How old are you? ")
next_birthday = ("On your next birthday, you will be " + str(int(age) + 1))
print(next_birthday)
print()
# The above code can be simplified to a single line as shown below:
# print("On your next birthday, you will be " + str(int(input("How old are you? ")) + 1))
print("You have " + str(int(input("How many egg cartons do you have? ")) * 12) + " eggs")




print("On your next birthday, you will be " + str(int(age) +1))


cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
cookies_per_person = int(cookies) / int(people)
print(f"Each person may have {cookies_per_person} cookies")