import random
correct_words = ["raiden", "and", "jean", "are", "hot"]
picked_word = random.choice(correct_words)
lives = 5
guessed_word = ["_"] * len(picked_word) # i need to do this because this will show the player how many characters there are and the len(picked_word) would get the amount of characters and multiply it with the dash
while lives > 0: # this while loop keeps repeating this code until the amount of lives has reached 0
    if "".join(guessed_word) == picked_word:
        break
    index = 0
    guessed = False
    user_input = input("Guess here:").strip()
    for x in picked_word: # scans the hangman word(picked_word)
        if user_input == x:
            guessed = True # this would later in the code (line 17) allow the player to see their progress
            guessed_word[index] = x # makes the sure the letter the player picked if correct is in the right place
        index += 1 # keeps track of the amount of characters
    if guessed:
        print("Good job")
        print(guessed_word)
    else:
        print("Invalid guess")
        lives -= 1
        print("You now have" , lives, "lives")
if "".join(guessed_word) == picked_word:
    print("ggs only")
else:
    print("Game over")