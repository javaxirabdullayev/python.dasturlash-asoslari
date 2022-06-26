# 11-dars. Bir nechta shartlarni tekshirish

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son = float(input("Juft son kiriting: "))
if son%2:
    print("Bu son juft emas!")
else:
    print("Rahmat!")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = int(input("Yoshingizni kiriting: "))
if yosh<4 or yosh>60:
    print("Chipta siz uchun bepul!")
elif 4<yosh<18:
    print("Chipta narxi - 10000 so'm!")
else:
    print("Chipta narxi - 20000 so'm!")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
if a>b:
    print(f"{a}>{b}")
elif a==b:
    print(f"{a}={b}")
else: 
    print(f"{a}<{b}")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar = ['sut', 'non', 'suv', 'qatiq', 'olma', 'nok', 'qaymoq', 'hurmo']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Kechirasiz, do'konimizda {mahsulot} yo'q")

mahsulotlar = ['sut', 'non', 'suv', 'qatiq', 'olma', 'nok', 'qaymoq', 'hurmo']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
    
    
bor_mahsulotlar = []
mavjud_emas = []
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
        
if mavjud_emas:
    print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
        print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
foydalanuvchilar = ['jawa', 'ninza', 'bobur', 'azamat', 'sanjar']
kirish = input(f"Yangi login kiriting: ")
if kirish in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
son = int(input("Butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f" {son} soni {n} ga qoldiqsiz bo'linadi")
    

 
