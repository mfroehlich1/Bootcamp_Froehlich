# > What is the operation you'd like to perform? +
# > What is the first number? 5
# > What is the second number? 12
# > 5 + 12 = 17

# def add(num1, num2):
#     solution = num1 + num2
#     return solution
#
#
# def sub(num1, num2):
#     solution = num1 - num2
#     return solution
#
# def div(num1, num2):
#     solution = num1 / num2
#     return solution


while True:
    operation = input("Choose a mathematical operation (+, -, /): ")

    num1 = input("Choose your first number: ")
    if num1.isdigit():
        num1 = int(num1)
    else:
        print("\nChoose a valid integer!!\n")
        continue

    num2 = input("Choose your second number: ")
    if num2.isdigit():
        num2 = int(num2)
    else:
        print("\nChoose a valid integer!!\n")
        continue

    if operation == "+":
        solution = num1 + num2
    if operation == "-":
        solution = num1 - num2
    if operation == "/":
        solution = num1 / num2

    print(f"\n{num1} {operation} {num2} = {solution}\n")

    cont = input("Continue? y/n: ").lower()

    if cont == "n":
        break
