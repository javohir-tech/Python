def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rangi": rangi,
        "karobka": korobka,
        "yili": yili,
        "narxi": narhi,
    }

    return avto


def avto_kirit():
    avtolar = []

    while True:
        print("\nQuyidagi ma'lumotlarni kiriting", end=" ")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narhi = input("Narhi: ")
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        javob = input("Yana moshina qo'shamizmi ? (yes/no)")
        if javob == "no":
            break
    return avtolar


def info_print(avto_info):
    print(
        f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
        f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
        f"{avto_info['yil']}-yil, {avto_info['narh']}$"
    )
