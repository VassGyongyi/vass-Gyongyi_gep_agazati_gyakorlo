from Gep import Gep
gep_list = []
def feldolgoz():
    f = open('gep.txt','r',encoding='utf-8')
    f.readline().strip()
    sorok = f.readlines()

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("!")
        gep_list.append(Gep(sor))
        i += 1
    f.close()
    #print(gep_list[0].id)
def gepek_szama():
    print(len(gep_list))

def atlag():
    i = 0
    ossz = 0
    db = 0
    while i<len(gep_list):
        if gep_list[i].id % 2 == 0:
            #print(gep_list[i].id)
            db += 1
            ossz += gep_list[i].id
        i += 1
    print(int(ossz/db))

def legkisebb():
    i = 0
    max = 200
    index = 0
    while i < len(gep_list):
        if gep_list[i].id < max:
            index = i
            max = gep_list[i].id
        i += 1
    print(gep_list[index].id, gep_list[index].hely)
