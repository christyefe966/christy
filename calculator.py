# Create functions to hold each mathematical operations

def add(num1, num2):
    return num1 + num2

def substract(x, y):
    return x - y

def divide(x, y):
    return x / y 

def multiply(x, y):
    return x * y



# Display function on the screen

print("selsect the operation ")
print("1. Add")
print("2. Substract")
print("3. divide")
print("4. multiply")

# Take input from the user
choice = input("Enter choice(1,2,3,4):")

# Take numbers from user

num1 = float(input("Enter first number"))
num2 = float(input("Enter Second number"))

# Perform the operation based on the user chioce

if choice == "1":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == "2":
    print(f"{num1} - {num2} = {substract(num1, num2)}")
elif choice == "3":
    print(f"{num1} / {num2} = {divide(num1, num2)}")
elif choice == "4":
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
else:
    print("Mathematical operation does not exist")
