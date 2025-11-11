from random import choice
from words import sozlar

def get_word() :
    return choice(sozlar)

def display(user_letters , word):
    display_letters = '';
    for letter in word :
        if letter  in user_letters :
            display_letters+=letter
        else:
            display_letters+="_"
    return display_letters
            
def play():
    word = get_word()
    word_letters = set(word)
    users_letters = " "
    print(f"men {len(word)} uzunlikdagi soz oyladim top nahuy ");
    while word_letters:
        print(display(users_letters , word))
        if  users_letters :
            print(f"shu vaqtgacha kiritngan harflar {users_letters}")
        letter = input("Harf kiring >>> ")
        if letter  in users_letters :
            print('bu harfni kirintgansiz !!!')
            continue
        elif letter in word_letters :
            word_letters.remove(letter)
            print("siz kiritgan harf togri")
        else:
            print('bu hato')
        users_letters+=letter
    print(f"tabriklaymiz {word} urunish : {len(users_letters)}")
    
play()