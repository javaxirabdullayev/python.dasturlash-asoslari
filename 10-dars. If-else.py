# 10-dars. If-else

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

kirish = input("Loginingizni yozing: ")
if kirish.lower() == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print("Xush kelibsiz,", kirish, "!")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
a = input("1-sonni kiriting: ")
b = input("2-sonni kiriting: ")
if a==b:
    print("Sonlar teng")
else: 
    print("Sonlar teng emas")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
a = int(input("Istalgan son kiriting: "))
if a >= 0:
    print("Musbat son")
else:
    print("Manfiy son")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
a = int(input("Istalgan son kiriting: "))
if a >- 0:
    print(a**(1/2))
else:
    print("Musbat son kiriting!")