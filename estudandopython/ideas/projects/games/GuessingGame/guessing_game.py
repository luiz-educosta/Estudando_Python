#! /usr/bin/python3
"""
A guessing game developed by Luiz Eduardo to improve your python, english and cooding experience.
* This simple game contain this functions:
    - Insert a name to play or play anonnymous mode;
    - Choose a mode to play(Easy, Medium or Hard);
    - Options to Play again, show hiscores, actual points and exit;
    - Free mode to play (You can set a range numbers to choose);
*
"""
secret_number = 43

print('##############################')
print('\n\tWelcome!\n')
print('##############################')


def main():

    first_time = 0
    while True:
        try:
            if (first_time == 0):
                player_number = int(input('Type a number:'))
            else:
                player_number = int(input('Try again:'))
            first_time += 1
            if (secret_number < player_number):
                print(
                    f'The number {secret_number} is less than {player_number}!')
            elif (secret_number > player_number):
                print(
                    f'The number {secret_number} is higher than {player_number}!')
            else:
                print(
                    f'The secret number is {secret_number}! Congratulations!')
                break
        except ValueError:
            print('Please enter an integer number!')
        except KeyboardInterrupt:
            print('\nThanks to play! Se you again!')
            exit()

            # finally:
            #     print('The game was started!')
if __name__ == '__main__':
    main()
