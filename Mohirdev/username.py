from random import choice

def user_name(name):
    randomNum  = choice(list(range(0, 10)))
    reverName = name[::-1]
    reverName += str(randomNum)
    return reverName


while True :
    res = input("Ismingizni kiriting >>> ")
    if not res.isdigit() :
        print(f"Hush kelibsiz {res}")
        print(user_name(res))
        break
    else:
        print("Faqat harflardan iborat bolishi kerak")
        

nums = ['1', '3', '5', '9']

def convert_add(arr) :
    return sum([int(num) for num in arr])

print(convert_add(nums))