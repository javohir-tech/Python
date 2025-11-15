import re
from words import sozlar 

# word1 = "Temur"
# word2 = "Temir"
# word3 = "Tulpor"
# word4 = "Tomir"
# word5 = "taxir"

# andoza = "^t...r$"
# print(re.match(andoza , word1.lower()))
# print(re.match(andoza , word2.lower()))
# print(re.match(andoza , word3.lower()))
# print(re.match(andoza , word4.lower()))


# for word in sozlar :
#     if re.match(andoza, word) :
#         print(word)

# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# emailAndoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"

# email = re.findall(emailAndoza , matn)
# print(email[0])

passwordAndoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-_]).{8,}$"
msg = "Parol kiriting ."
msg += "(kamida 8 ta belgidan iborat , kamida bitta lotin bosh harf , 1 ta kichik harf)"
msg += '1ta son va 1 ta mahsus belgidan iborat bolishi kerak '

while True :
    passWord = input(msg)   
    if re.match(passwordAndoza , passWord):
        print('Qabul qilindi !!!')
        break
    else:
        print('!!!maxfiy soz qabul qilinmadi!!!')
