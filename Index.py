# def kattaHarf(ismlar) :
#     qaytaradi = [];
#     while ismlar : 
#         katta = ismlar.pop().title();
#         qaytaradi.append(katta)
#     return qaytaradi;


# print(kattaHarf(ismlar[:]))
# print(ismlar)

def bahola(ismlar) :
    baholar = {}
    i =0 ;
    while i < len(ismlar) :
        ism = ismlar[i];
        baho = int(input(f"{ism.title()} ga baho qoying >>> "))
        baholar[ism.title()] = baho
        i+=1
    return baholar  
        
ismlar = ['ali', 'vali', 'hasan', 'husan']

print(bahola(ismlar[:]))
print(ismlar)