#float calculator
x = float(input("What is x ? : "))
y = float(input("What is y ? : "))
z = round(x + y) # it will round the figure
z = round(x / y ,3) # it will cutdown whole number with last 3 decimal
print (f"{z:.2f}")
print (f"{z:,}")

# Creating our Own function
'''def main():
name1 = input("What is Your name ? : ")
hello(name1)

def hello(to="Coders") :
    print("Hello," , to)
    
main()'''

# square program with function
def main():
  x = int(input("Enter x : "))
  print("Square of x is : " , square(x))
      
def square(n):
  return n * n
    
main()
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
