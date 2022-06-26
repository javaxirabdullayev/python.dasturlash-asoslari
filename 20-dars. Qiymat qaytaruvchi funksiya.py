# 20-dars. Qiymat qaytaruvchi funksiya

# 1 - masala.
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

def client_info(name, surname, birth, birthplace, email = '', phone = ''):
    """ Information """
    client =      {'name' : name,
                    'surname' : surname,
                    'birth' : birth,
                    'age' : 2022 - int(birth),
                    'birthplace' : birthplace,
                    'email' : email,
                    'phone' : phone}
    return client
    
inf = client_info('Javoxir', 'Abdullayev', 1993, 'Ferghana', 'jawa_03@mail.ru', 998916627000)
print(inf)

# 2 - masala.
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

clients = []
while True:
    print("\n Quyidagi ma'lumotlarni kiriting. end = ''")
    name = input("name: ")
    surname = input("surname: ")
    birth = input("birth: ")
    birthplace = input('birthplace: ')
    email = input('email: ')
    phone = input("phone: ")
    
    clients.append(client_info(name, surname, birth, birthplace, email = '',               phone = ''))
    
    answer = input("Yana ma'lumot kiritasizmi? (yes/no): ")
    if answer == 'no':
        break
print("Clients:")
for client in clients:
    print(
        f"{client['name'].title()} {client['surname'].title()},"
        f"{client['age']} yoshda, telefon: {client['phone']} ")
    
  # 3 - masala.
  # Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def numb(a, b, c):
    """ Eng kattasini topish"""
    max = a
    if b >= max:
        max = b
    if c >= max:
        max = c
    
    return max

number = numb(1,2,3)
print(number)


# 4 - masala.
# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

def radius(n):
    """Radius, diametr, peremetr"""
    info = {
            'radius' : n,
            'diametr' : n*2,
            'peremetr' : ((n*2*3.14),".2f"),
            'yuzi' : 3.14*(n**2)}
    return info

answer = radius(5)
print(answer)


# 5 - masala.
# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar

tubb = tub_sonlar_top(2, 99)
print(tubb)


# 5 - masala.
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar
  
m = fibonacci(10)
print(m)
    
