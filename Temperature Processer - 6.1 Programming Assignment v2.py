def processTemperatureInput(tempInput, temperatures):
    try:
        userTemp = int(tempInput)
        temperatures.append(userTemp)
    except ValueError:
        print("Please enter a number.")


def main():
    temperatures = []

    done = False

    while not done:
        userSelection = input("Enter a temperature or type 'quit' to stop: ")

        if userSelection.lower() == "quit":
            done = True
        else:
            processTemperatureInput(userSelection, temperatures)

    if temperatures:
        largestTemp = max(temperatures)
        smallestTemp = min(temperatures)
        lengthOfList = len(temperatures)

        print(
            f'''
    The largest temperature entered was {largestTemp} degrees.
    The smallest temperature entered was {smallestTemp} degrees.
    There were {lengthOfList} temperatures entered.''')

    else:
        print("No temperatures were entered.")


if __name__ == "__main__":
    main()
