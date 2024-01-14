secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Type word all lowercase")
print("The word is an animal, you will receive clues when incorrect!")

while guess != secret_word and not (out_of_guesses):
    if guess_count< guess_limit:
        guess = input("Enter guess = ")
        guess_count += 1b
        if guess_count == 1 and guess != secret_word:
            print("It likes plants and is about 1.8 meters tall")
        if guess_count == 2 and guess != secret_word:
            print("It can run at a speed of about 34.7 miles per hour")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win! GOOD JOB!")















#i = 1
#while i <= 10:
 #   print(i)
  #  i += 1
#print("Done with loop")


#monthConversions= {
 #   "Jan": "January",
  #  "Feb": "February",
   # "Mar": "March",
    #"Sep": "September",
#}

#print(monthConversions["Jan"])
#print(monthConversions.get("Sepe", "Not a valid key"))