friends = {
    "ali" : ['Taxtlar oyini' , "nimadir"],
    "javohir" : ["breking bad " , "baxt"]
}

for key , qiymat in friends.items() : 
    print(f"{key} ning sevimli filmi quyidagilar " , end="")
    for kino in qiymat : 
        print(kino, end="")