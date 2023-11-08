import random
import string
from words import words

# Now you can use the 'words' variable in your code
# print(words)

def get_valid_word(words):
    word =random.choice(words) #randomly choose something from the list
    while '-' in word or ' ' in word :
        word =random.choice(words)
        
    return word
        
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed
    
    
    #getting user input 
    while len(word_letters):
        
        # letters used
        # ' '.join([]'a','b','cd']) --> 'a b cd'
        print('you have used these letters: ',' '.join(used_letters)) 
        
        #what current word is ( ie W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ',' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
            
                word_letters.remove(user_letter)
                
        elif user_letter in used_letters :
            print('you have already used that character . Please try again . ')

        else:
            print('Invalid character. Please try again')
    # gets here when len(word-letters) == 0
hangman()   
user_input = input('Type something:')
print(user_input)