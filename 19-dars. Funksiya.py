# 19-dars. Funksiya

# 1-masala.
#   Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

def birthyear(name, age):
    """ Yoshini hisoblaydigan dastur"""
    print(f"{name.title()} {2022-age} - yilda tug'ilgan")
    
birthyear("bobur", 20)

# 2- masala.
#   Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def square(number):
    """Kvadrat va kubni hisoblovchi dastur"""
    print(f"{number} sonining kvadrati = {number**2} ga teng. \n"
          f"{number} sonining kubi = {number**3} ga teng.")

square(5)

# 3-masala.
#   Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

def odd_even(numb):
    """Toq va juftligini topish"""
    if numb % 2 == 0:
        print(f"{numb} soni - juft son.")
    else:
        print(f"{numb} soni - toq son.")

odd_even(5)

# 4-masala.
#   Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def big_small(numb1, numb2):
    """ Katta kichik aniqlash funksiyasi"""
    if numb1 > numb2:
        print(numb1)
    elif numb1 < numb2:
        print(numb2)
    else:
        print("Sonlar teng")

big_small(10, 10)

# 5-masala.
#   Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.

def number(x,y):
    """Kvadratini aniqlash funskiyasi"""
    print(x**y)

number(5,2)

# 6-masala.
#   Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

def number(x):
    """Kvadratini aniqlash funskiyasi"""
    print(x**2)

number(5)

# 6-masala.
#   Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

def numb(x):
    """Qoldiqsiz bo'linishi funksiyasi"""
    for n in range(2,11):
        if not x%n:
            print(f"{x} {n} ga qoldiqsiz bo'linadi.")
numb(60)            
        