# 25-dars. Son topish o'yini.


import random as r

def sontop(x=10):
    random_number = r.randint(1,x)

    print("Keling, o'ylagan sonni topish o'yinini o'ynaymiz")
    print("1 dan 10 gacha son o'yladim topa olasizmi?")
    
    trying = 0
    while True:
        trying += 1
        user_number = int(input(">>> "))  
        if user_number < random_number:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
        elif user_number > random_number:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
        else:
            break
    print(f"Topdingiz {random_number} sonini o'ylagan edim. Siz {trying} ta taxmin bilan topdingiz. Tabriklayman!!!")
    
    return trying
        

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    
    trying = 0
    
    while True:
        trying += 1
        if quyi != yuqori:
            taxmin = r.randint(quyi,yuqori)
        else:
            taxmin = quyi
        answer = input(f"Siz {taxmin} sonini o'yladingiz: to'gri (T)," 
                        f" men o'ylagan son bundan kattaroq (+), men o'ylagan son "
                        f"bundan kichikroq (-)? ").lower()
        if answer == '-':
            yuqori = taxmin - 1
        elif answer == '+':
            quyi = taxmin + 1
        else:
            break
    print(f"Men {trying} ta taxmin bilan topdim!")
    return trying
                

def play(x=10):
    yana = True
    while yana:
        trying_user = sontop(x)
        trying_pc = sontop_pc(x)
        if trying_user > trying_pc:
            print("Men yutdim!")
        elif trying_user < trying_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0)"))
        
        
print(play())
