names  = ["Javohir" , "Suvonov" , "Ulug'bek"];

print(f"Salom {names[0]} , bugun choyxona bormi . \n{names[1]} Salom bugun choyxona bormi")

sonlar = [1, 2, -3 , 2.1];
[sonlar[0], sonlar[1]] = [sonlar[1], sonlar[0]]

print(sonlar);

t_shaxslar =['Alisher' , 'Temur']
z_shaxslar = ["Bill", "Ilon"]

a = t_shaxslar.pop(-1);
b = z_shaxslar.pop(0);

print(a + "salom"  +" " + b + "salom");

friends = [];

friends.append("Javohir")
friends.append("Jalol")
friends.append("BEk")
print(friends)
del friends[1]
friends.remove("Javohir")
friends.insert(1, "Javohir")
friends.insert(1 , "jalol")
mehmonlar = []
bek = friends.pop(0)
mehmonlar.append(bek)
print(friends)
print(mehmonlar)
