from random import choice
from words import sozlar
def get_word():
    return choice(sozlar)

def display(user_letters , word):
    display_letter = ''
    for letter in word :
        if letter in user_letters:
            display_letter += letter
        else :
            display_letter += "_"
    return display_letter

def play():
    word = get_word()
    word_letters = set(word);
    
    user_letters = ''
    print(f"men {len(word)} xonali soz o'yladim >>> ")
    while word_letters :
        print(display(user_letters , word))
        if user_letters :
            print(f"shu vaqtgacha kiritgan harflaringiz {user_letters}")
        letter = input("harf kiritng >>>")
        if letter in user_letters :
            print("bu harfni kiritgansiz boshqa harf kiriting")
            continue
        elif letter in word :
            word_letters.remove(letter)
            print(f"{letter} togri")
        else :
            print("bunday harf yoq")
        user_letters += letter
    print(f"tabriklaymiz siz {word} sozini {len(user_letters)} ta uruinoshda topdingiz");
    
play()