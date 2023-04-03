#float calculator
x = float(input("What is x ? : "))
y = float(input("What is y ? : "))
z = round(x + y) # it will round the figure
z = round(x / y ,3) # it will cutdown whole number with last 3 decimal
print (f"{z:.2f}")
print (f"{z:,}")

# Creating our Own function
def main():
name_your = input("What is Your name ? : ")
hello(name_your)

def hello(to="Coders") :
    print("Hello," , to)
    
main()

# square program with function
def main():
  x = int(input("Enter x : "))
  print("Square of x is : " , square(x))
      
def square(n):
  return n * n
    
main()
