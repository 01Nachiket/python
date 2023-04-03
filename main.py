# Ask user for their name , it will take input and also do strip and title functionality in one line
name = input("Enter Your Name : ").strip().title()

# Remove Whitespaces from string and make all words capital 
#name = name.strip().title()

# This function will split andd choose which to take from user first name and last name
first , last = name.split(" ")
print (f"hello , {first}")
# Capitalize user name 
#name = name.capitalize()

# This function will capital all str in output
#name = name.title()

# say hello to user
print (f"Hello , {name}")

#Calculator with nested function
x = int(input("What is X ?"))
y = int(input("What is y ?"))
print (x + y)

#above code in one line
print(int(input("Enter x : ")) + (int(input("Enter y :")))
      
