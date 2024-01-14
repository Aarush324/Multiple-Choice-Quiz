import random
verbs = ["eat", "run", "sleep", "want", "jump", "sleep"]
nouns = ["Sekdo", "Howkey", "Dogo", "Schealaks", "Boogieman"]
print("Hello User");
print("We will be playing a game of madlibs today, hope you have fun");

what = input("Type start to start the game: ");
e = random.randint(0,5)
d = random.randint(0,4)
if what == "start":
    print("I love to " + verbs[e] + ". " + nouns[d] + " is really cool.");