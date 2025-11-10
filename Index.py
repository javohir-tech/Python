# def yoshHisobla(ism , t_yil):
#     """Yosh hisoblaydigan funksiya """
#     print(f"{ism.title()} ning yoshi {2025-t_yil}");
    
# name = input("Ismingiz>>>");
# year = int(input("Tug'ilgan yilingiz >>>"))

# yoshHisobla(name , year);

def kub(param1):
    for n in range(2, 11):
        if param1 % n==0 :
            print(f"{param1} {n} ga qoldiqsiz bo'linadi")
    
son = float(input("Sonni kiriting..."))
# son2 = float(input(" 2 chi Sonni kiriting..."))

kub(son)