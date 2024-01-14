

from Question import Question

questions_prompts = [
    "Who is the second president of United StateS?\n(a) George Washington\n(b) Andrew Jackson\n(c) John Adams\n\n",
    "How many presidents got assassinated in office?\n (a) 3\n (b) 4\n (c)6\n (d)8\n\n",
    "Which gas is the most abundant in the atmosphere?\n (a) nitrogen\n (b) oxygen\n (c) carbon dioxide\n\n",
    "Clouds are formed by which process?\n (a) condensation\n (b) evaporation\n (c) precipitation\n\n",
    "Who wrote the poems “Annabel Lee” and “The Raven?\n (a) Edgar Allen Poe\n (b) Shakespeare\n (c) Pablo Nerdua\n\n"
]

questions = [
    Question(questions_prompts[0],"c"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "a"),
    Question(questions_prompts[3], "a"),
    Question(questions_prompts[4], "a"),
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print( "You got " + str(score) + " out of " + str(len(questions)) + " right!")

user_input = input("Hi, you will be taking a test to see if you are as smart as an 8th grader, please type start to start the test\n")
if user_input == "start":
    run_test(questions)