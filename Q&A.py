import random


state_capitals = {
    "Georgia": "Atlanta",
    "Illinois": "Chicago",
    "Arizona": "Phoenix",
    "Virginia": "Richmond",
}

states = list(state_capitals.keys())
random.shuffle(states)


for state in states:
    capital = state_capitals[state]
    user_answer = input(f"What is the capital of {state}? ")

    if user_answer.lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is {capital}.")

print("Done!")
