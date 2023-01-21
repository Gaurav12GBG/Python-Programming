
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses limited to only 9 times: ")

while number_of_guesses <= 9:
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("You entered less number please input greater number.\n")
    elif guess_number > 18:
        print("You entered greater number please input smaller number.\n")
    else:
        print("You Won !!!!!\n")
        print("Number of guesses he took to finish.", number_of_guesses)
        break
    print(9-number_of_guesses, "no.of guesses he took to finish")
    number_of_guesses = number_of_guesses + 1

if number_of_guesses > 9:
    print("Ohh No,Sorry Game Over !!!")


# for i in range(1, 16):
#     print(i)
#     i = i + 1


