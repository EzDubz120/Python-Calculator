import time
op = input("enter operator ")
time.sleep(1)
number1 = float(input("enter the first number "))
number2 = float(input("enter the second number "))

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "*":
    print(number1 * number2)
elif op == "x":
    print(number1 * number2)
elif op == "/":
    print(number1 / number2)
elif op == "÷":
    print(numbers / number2)
else:
    print("invalid operator")
    print("please enter a valid operator")
