# 15-dars. Lug'at elementlari bilan ishlash

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
lugat = {
    'string' : 'matn', 
    'if' : 'agar', 
    'float' : 'butun va son', 
    "integer" : 'butun son',
    "else" : "u holda"
    }
for kalit,qiymat in sorted(lugat.items()):
    print(f"Kalit : {kalit}")
    print(f"Qiymat : {qiymat}")

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
davlatlar = {
    'Rossiya' : 'Moskva',
    'Fransiya' : 'Parij',
    'Italiya' : 'Rim',
    'Angliya' : 'London'
    }
print("Davlatlar:")
for davlat in sorted(davlatlar.keys()):
    print(davlat)
print("Poytaxtlar:")
for davlat in sorted(davlatlar.values()):
    print(davlat)

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

davlatlar = {
    'rossiya' : 'moskva',
    'fransiya' : 'parij',
    'italiya' : 'rim',
    'angliya' : 'london'
    }
davlat = input(f"Qaysu davlat poytaxtini bilishni istaysiz: ").lower()
poytaxt = davlatlar.get(davlat)
if poytaxt == None:
    print("Kechirasiz, bizda bu haqida ma\'lumot yo\'q")    
else:
    print(f"{davlat.title()}ning poytaxti {poytaxt.title()} shahri")

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
menu = {
        'osh' : 10000,
        'manti' : 2000,
        'non' : 2000,
        'choy' : 1000,
        "sho'rva" : 9000,
        'salat' : 3000
        }
buyurtma = [] 
for n in range(3):
    buyurtma.append(input(f"{n+1} taomni kiriting: ").lower())
for ovqat in buyurtma:
    if ovqat in menu:
        print("f {buyurtma.title()} - {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {ovqat} yo'q")

