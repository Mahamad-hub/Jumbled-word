import random


def choose_rand():
    words = ['calculator', 'algebra', 'nation', 'math', 'mouse', 'gym', 'table', 'anime', 'game', 'library']
    return random.choice(words)


def shuffle_letters(word):
    return ''.join(random.sample(word, len(word)))


def final_score(firstscore, secondscore):
    print(f"First Player score: {firstscore}")
    print(f"Second Player score: {secondscore}")


def declare_winner(firstscore, secondscore, firstname, secondname):
    if firstscore > secondscore:
        print(f"{firstname}, You are the winner!! Your score is {firstscore}. Thank you for playing!")
    elif secondscore > firstscore:
        print(f"{secondname}, You are the winner!! Your score is {secondscore}. Thank you for playing!")
    else:
        print("It's a tie! Thank you for playing!")


def play_game():
    print("Welcome to Two-Player-Jumbled-Words Game\n")

    firstname = input("Enter the first player's name: ")
    secondname = input("Enter the second player's name: ")

    print("Type 'Stop' or 'Exit' to leave the program and see your scores.")

    firstscore = 0
    secondscore = 0
    attempt = 0

    while True:
        # if attempt is an even number, first player will have their turn. if odd then it is second players turn
        if attempt % 2 == 0:
            print(f"\n{firstname}, it's your turn!")
        else:
            print(f"\n{secondname}, it's your turn!")

        word = choose_rand()
        jumbled_word = shuffle_letters(word)
        print(f"Jumbled word: {jumbled_word}")
        right = input("Your answer: ")

        # user has the option to exit the program form here
        if right.lower() in ['stop', 'exit']:
            print("Game Ends!")
            break

        # if attempt is an even number then first players score will be displayed.
        # if attempt is an odd number then second players score will be displayed.

        if right.lower() == word:
            print("You are correct!")

            if attempt % 2 == 0:
                firstscore += 1
                print(f"Your score is: {firstscore}")
            else:
                secondscore += 1
                print(f"Your score is: {secondscore}")
        else:
            print("You are incorrect!")
            if attempt % 2 == 0:
                print(f"Your score is: {firstscore} ")
            else:
                print(f"Your score is: {secondscore} ")

        attempt += 1
    final_score(firstscore, secondscore)
    declare_winner(firstscore, secondscore, firstname, secondname)

    play_again = input("\nDo you want to play again? (Y for Yes/N for No) ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thank you for playing!")


if __name__ == '__main__':
    play_game()