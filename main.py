# imports
import random
import json
import os

# constants
NUMBER_OF_QUESTIONS = 10
OPERATORS = ['+', '-', '*', '/']

# variables
score = 0

# functions
def readJSON():
    with open("data.json", "r") as file:
        return json.loads(file.read())
        
def writeJSON(JSON):
    with open("data.json", "w") as file:
        data = json.dumps(JSON)
        file.write(data)

# main
if not os.path.isfile("data.json"):
    with open("data.json", "w") as file:
        file.write('{"class": [{}, {}, {}]}')


name = input("What's your name? ")
classNumber = input("What's your class? ")

for x in range(NUMBER_OF_QUESTIONS):
    print(f"Current question: {x + 1}")
    first_number = (random.randint (1, 10))
    second_number = (random.randint (1, 10))
    operator = OPERATORS[random.randint (0, len(OPERATORS) - 1)]

    equation = f"{first_number} {operator} {second_number}"

    answer = input(f"What is {equation}? ")

    actual_answer = eval(equation)

    if float(answer) == actual_answer:
        score += 1
        print("Correct.")
    else:
        print("INCORRECT :(")

print(f"Your score is {score} out of {NUMBER_OF_QUESTIONS}.")

data = readJSON ()

if not name in data["class"][int(classNumber) - 1]:
    data["class"][int(classNumber) - 1][name] = []

data["class"][int(classNumber) - 1][name].append(score)

writeJSON (data)

for i in range(len(data["class"])):
    sortedNames = sorted(data["class"][i].keys())

    for name in sortedNames:
        scores = sorted(data["class"][i][name])

        print(f"Class {i + 1}: {name} scores: {scores}")

for i in range(len(data["class"])):
    sortedNames = sorted(data["class"][i].keys())

    for name in sortedNames:
        scores = sorted(data["class"][i][name], reverse=True)

        topThreeScores = []

        for j in range(3):
            if len(scores) > j:
                topThreeScores.append(scores[j])

        print(f"Class {i + 1}: {name} top 3 scores: {topThreeScores}")