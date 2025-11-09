print("Sevimli kinoblarizni kiriting");

savol = "(Dasturni to'xtatish uchun 'stop' deb yozing) ";
flag = True
n=1
while flag :
    qiymat = input(f"{n} chi sevimli kitob . {savol}")
    if qiymat == 'stop':
        flag = False
        print('dastur tugadi>>>')
    else: 
        print(qiymat)