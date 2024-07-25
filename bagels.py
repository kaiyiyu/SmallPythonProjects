import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
      Pico         One digit is correct but in the wrong position.
      Fermi        One digit is correct and in the right position.
      Bagels       No digit is correct.
    
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))
    
    while True:
        secret_number = get_secret_num()
        
        print(f"I have thought up a number. You have {MAX_GUESSES} guesses to get it.")
        
        current_guesses = 1
        while current_guesses <=MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{current_guesses}")
                guess = input("Enter your guess: ")
                
            clues = get_clues(guess, secret_number)
            print(clues)
            current_guesses += 1
            
            if guess == secret_number:
                break
            
            if current_guesses >MAX_GUESSES:
                print(f'You ran out of guesses. The answer was {secret_number}.')
                
        # Ask player if they want to play again
        print("Do you want to play again (yes or no)?")
        if not input('> ').lower().startswith('y'):
            break
    
    print("Thanks for playing!")        
    
    
def get_secret_num():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secret_num = ''
    for digit in range(NUM_DIGITS):
        secret_num += str(numbers[digit])
    return secret_num

def get_clues(guess, secret_number):
    if guess == secret_number:
        return "You guessed it correctly!"
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico")
        
    if len(clues) == 0:
        clues.append("Bagels")
    else:
        clues.sort()
        return " ".join(clues)
    
    
if __name__ == '__main__':
    main()