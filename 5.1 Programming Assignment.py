# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Darin Young
# 4/9/2024

menu = """\nSimple Math and Average Calculator
        
        0: Exit Program
        1: Basic Calculator (+ - * /)
        2: Average Calculator"""


def calculateAverage():
    total = 0
    try:
        quantityOfNumbers = int(input("How many numbers do you want to calculate the average for? "))
        for i in range(quantityOfNumbers):
            num = float(input("Enter number {}: ".format(i + 1)))
            total += num
        average = total / quantityOfNumbers
        print("The average of the {} numbers is: {:.2f}".format(quantityOfNumbers, average))
    except ValueError:
        print("\nPlease enter a valid number.")


def performCalculation(operation):
    try:
        num1 = int(input("Please provide the first number: "))
    except ValueError:
        print("Please enter a number.")
    try:
        num2 = int(input("Please provide the second number: "))
    except ValueError:
        print("Please enter a number.")

    if operation == "+":
        total = num1 + num2
        print(f"{num1} + {num2} = {total}")
    elif operation == "-":
        total = num1 - num2
        print(f"{num1} - {num2} = {total}")
    elif operation == "*":
        total = num1 * num2
        print(f"{num1} * {num2} = {total}")
    elif operation == "/":
        total = num1 / num2
        print(f"{num1} / {num2} = {total}")
    else:
        print("Unable to compute. Please enter + - / or * as your operation.")


def main():
    done = False

    while not done:
        print(menu)

        menuSelection = input("\nPlease make a selection: ")

        if menuSelection == "0":
            print("\nThanks for using the program!")
            done = True
        elif menuSelection == "1":
            operation = input("What operation would you like to perform?: ")
            performCalculation(operation)
        elif menuSelection == "2":
            calculateAverage()
        else:
            print("Please make a valid selection.")

if __name__ == "__main__":
    main()
