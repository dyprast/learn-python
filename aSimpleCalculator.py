num    = float(input("Enter first number: "))
num_   = float(input("Enter second number: "))
op     = input("Enter operator: ")

if op == "+":
    print(num + num_)

elif op == "-":
    print(num - num_)

elif op == "/":
    print(num / num_)

elif op == "*":
    print(num * num_)

else:
    print("Invalid operator")