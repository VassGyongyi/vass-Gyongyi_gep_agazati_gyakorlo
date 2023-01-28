import random
def sor(list):
    kimenet = ""
    i = 0
    while i < 15:
         vel = random.randint(-90,500)
         list.append(vel)
         if i == 14:
            kimenet += str(vel)
         else:
             kimenet += str(vel) + "*"
         i += 1
    print(kimenet)

def tizzel_oszthato(list):
    i = 0
    db = 0
    while i < len(list):
        if list[i] % 10 == 0:
            db += 1
        i += 1
    return db

def konzolra_ir(list):
    print(tizzel_oszthato(list))

def fajl_ir(list):
    f = open('kimutatas.txt','w', encoding='UTF-8')
    f.write(str(tizzel_oszthato(list)))
    f.close()
