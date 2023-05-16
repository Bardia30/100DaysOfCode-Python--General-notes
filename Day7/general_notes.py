import random
 
from hangman_art import stages, logo

from hangman_words import word_list



lives = 6
end_of_game = False

print(logo)

rand_num = random.randint(0,2)

chosen_word = word_list[rand_num]
# chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(0, len(chosen_word)):
    display.append("_")


while not end_of_game:


    guess = input("Guess a letter: ").lower()



    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
    if guess not in display: 
        lives = lives -1
    if lives == 0:
        print("you lose")
        end_of_game = True

    print(display)
    if "_" not in display:
        end_of_game =True
        print("you win")
    
    print(stages[lives])