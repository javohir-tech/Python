countries = ["Uzbekistan" , "Aqsh" , "Russian" , "China" , "korea"]
print(countries)
print(len(countries))
tartiblangan  = sorted(countries , reverse=True);
# sorted masssivni tartiblaydi lekin asil massivga ozgartirmaydi
# reverse=True argumenti masssivni teskari tartiblangan holatda qiladi
print(tartiblangan)
print(countries)
juftSonlar = list(range(120 , 1201 , 2));
summa = sum(juftSonlar)
# print(juftSonlar)
different = max(juftSonlar)-min(juftSonlar)
print('farqi: ', different)
print('summa : ', summa)
print(len(juftSonlar))
print(juftSonlar[:20])
print(juftSonlar[90:110])
print(juftSonlar[521:])

taomlar = ['osh' , 'manti' , 'tuxum' , 'beshbarmoq', 'mastava'];

nonushta = taomlar[:];
nonushta.append('moshxorda');
nonushta.append('grechka')
#tuple ozgartirip bolmaydigan massiv 
nonushta =tuple(nonushta);
# list() bilan uni oddiy royhatga aylantirip o'zgartirish kiritamiz
nonushta =  list(nonushta)
nonushta[0] = "qaymoq va non"
nonushta = tuple(nonushta)
print(taomlar)
print(nonushta)