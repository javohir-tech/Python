import json

# sonlar = (1, 2, 3, 4);
# print(type(sonlar))
# sonalar2 = json.dumps(sonlar)
# print(type(sonalar2))
# print(sonalar2)

# blump = True
# b = json.dumps(blump)
# print(b)

bemor = {
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("Ahmad", "Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2},
    ],
}

bemor__json = json.dumps(bemor , indent=4)

print(type(bemor))

print(bemor__json)
bemor2 =json.loads(bemor__json)
print(bemor2)



# with open('../Data/bemor.json', 'w') as file :
#     json.dump(bemor, file)


