import datetime as dt
import math
import re

dateAndoza = r"(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})"
emailAndoza = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"


class Person:
    def __init__(self, name, surname, age, year, month, day, email=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.year = year
        self.month = month
        self.day = day
        self.birth_day = [int(d) for d in str(dt.date(year ,  month, day)).split("-")[::-1]]

    def get_info(self):
        info = f"{self.name.title()} {self.surname.title()} {dt.date(self.year, self.month, self.day).strftime("%d-chi %h %Y")} da tug'ilgan ."
        info += f"Hozirda {self.age}  yoshda ."
        if self.email:
            info += f"Email manzili {self.email}"
        return info

    def get_life_path_number(self):
        arr = self.birth_day
        res = 0
        for n in arr:
            numstr = list(str(n))
            for num in numstr:
                res += int(num)

        while res > 10:
            resstr = list(str(res))
            res = sum([int(num) for num in resstr])

        return res

    def get_info_by_number(self, number) :
        num = number
        with open('./matn.txt', "r", encoding="utf-8") as file :
            res = file.read()
        pattern = rf"\*\s*{num}[\s\S]*?(?=\*\s*\d+|$)"

        if re.search(pattern, res):
            return re.search(pattern, res).group().strip()
        else :
            return "Bunday raqamli bo'lim topilmadi."


while True :
    name = input("Ismingizni kiriting >>> ")
    surname = input("Familyangizni kiriting >>> ")
    age = int(input("Yoshingizni Kiriting >>> "))
    email = input("Emailingizni kiriting >>>")
    db = input("Tugulgan kuningizni quyidagi tartibda kiriting (1.1.2019) >>> ")
    if re.match(dateAndoza, db) and name and surname and age and re.match(emailAndoza , email):
        arr = list(db.split("."))
        day = int(arr[0])
        month = int(arr[1])
        year = int(arr[2])
        person1 = Person(name, surname, age, year, month, day, email)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(person1.get_info())
        print(person1.get_info_by_number(person1.get_life_path_number()))
        break
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!Ma'lumotlarni kiritishda Xato qaytadan boshlang!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        continue



    
    