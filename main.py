#Conditionals <elif>
x = int(input("What is x > "))
y = int(input("What is y > "))

            if(x<y):
                print("X Is less than Y")
            elif(x>y):
                print("X Is Greater than Y")
            else:
                print("X Is equal to Y")

    #Conditional <AND> <OR>
#conditional <not equal !>
if (x!=y):
    print("X is not equal to y")
else:
    print("x is equal to y")
    
 # Operator <%>
def main():
   x = int(input("What is X > "))
    if is_even(x):
            print("Even")
    else:
            print("Odd")
 
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
            
            
main()

# Match 
name = input("Enter Your Name > ")
    match name:
        case "Harry" | "Hagrid" | "Goofy" :
            print("Gryffindor")
        case "Hermione" :
            print("Eagles")
        case "Draco" :
            print("Pythinist")
        case _:
            print("Re-Enter")

print("You can do 75 hard !")
print("Dont lose hope")
