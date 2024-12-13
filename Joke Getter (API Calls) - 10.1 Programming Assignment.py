# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Darin Young
# 5/13/2024

import requests

chuck_norris_category_choices = {
    "0": "Exit Program",
    "1": "Animal",
    "2": "Career",
    "3": "Celebrity",
    "4": "Dev",
    "5": "Explicit",
    "6": "Fashion",
    "7": "Food",
    "8": "History",
    "9": "Money",
    "10": "Movie",
    "11": "Music",
    "12": "Political",
    "13": "Religion",
    "14": "Science",
    "15": "Sport",
    "16": "Travel"
}


def chuck_norris_joke_getter(userSelection):
    chuck_Norris_Url = f"https://api.chucknorris.io/jokes/random?category={userSelection}"

    response = requests.get(chuck_Norris_Url)

    if response.status_code == 200:
        data = response.json()
        joke = data.get("value")

        print("\nChuck Norris Joke:")
        print(joke)
    else:
        print("Failed to retrieve Chuck Norris joke. Status code:", response.status_code)


def bored_activity_getter():
    done = False

    while not done:
        bored_activity_url = "http://www.boredapi.com/api/activity/"

        response = requests.get(bored_activity_url)

        if response.status_code == 200:
            data = response.json()
            activity_type = data.get("type")
            activity = data.get("activity")

            print("""
Boring Activity Generator
-------------------------""")
            print(f'Type: {activity_type.title()}. Activity: {activity}')
        else:
            print("Failed to retrieve bored activity. Status code:", response.status_code)

        done = get_more_jokes()


def cat_fact_getter():
    done = False

    while not done:
        cat_fact_url = "https://catfact.ninja/fact"

        response = requests.get(cat_fact_url)

        if response.status_code == 200:
            data = response.json()
            fact = data.get("fact")

            print("""
Cat Fact Generator
-------------------------""")
            print(f'Fact: {fact}.')
        else:
            print("Failed to retrieve cat fact. Status code:", response.status_code)

        done = get_more_jokes()


def chuck_norris_joker():
    done = False

    while not done:
        print("""
Chuck Norris Joke Categories
----------------------------""")
        for item in chuck_norris_category_choices:
            print(f'{item}: {chuck_norris_category_choices[item]}')
        menuSelection = input("\nPlease make a selection: ")

        if menuSelection == "0":
            print("\nThanks for using the program! I hope you enjoyed wasting time!")
            done = True
        elif menuSelection in chuck_norris_category_choices:
            categorySelection = chuck_norris_category_choices[menuSelection]
            chuck_norris_joke_getter(categorySelection.lower())
            done = get_more_jokes()
        else:
            print("Please make a valid selection.")


def get_more_jokes():
    done = False

    while not done:
        userSelection = input(
            "\nDo you want to hear more? Enter y for another or n to go back to the previous menu: ").lower()
        if userSelection == "y":
            return False
        elif userSelection == "n":
            return True
        else:
            print("Please make a valid selection.")


menu = """\nDarin's Time Wasting Program

        0: Exit Program
        1: Chuck Norris Jokes
        2: Random activity for when you're bored
        3: Random fact about cats"""


def main():
    done = False

    while not done:
        print(menu)

        menuSelection = input("\nPlease make a selection: ")

        if menuSelection == "0":
            print("\nThanks for using the program! I hope you enjoyed wasting time!")
            done = True
        elif menuSelection == "1":
            chuck_norris_joker()
        elif menuSelection == "2":
            bored_activity_getter()
        elif menuSelection == "3":
            cat_fact_getter()
        else:
            print("Please make a valid selection.")


if __name__ == "__main__":
    main()
