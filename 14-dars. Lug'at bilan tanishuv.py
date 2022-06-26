# 14-dars. Lug'at bilan tanishuv

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

otam = {'ism': 'Abdullajon', "tugilgan_yili" : 1956, 'manzil' : "Farg'ona"}
onam = {'ism': "Ro'zixon", "tugilgan_yili" : 1958, 'manzil' : "Farg'ona"}
opam = {'ism': 'Xurshida', "tugilgan_yili" : 1982, 'manzil' : "Farg'ona"}
print(f"Otamning ismi {otam['ism']}, {otam['tugilgan_yili']}-yilda, {otam['manzil']} viloyatida tug'ilgan.")
print(f"Onamning ismi {onam['ism']}, {onam['tugilgan_yili']}-yilda, {onam['manzil']} viloyatida tug'ilgan.")
print(f"Opamning ismi {opam['ism']}, {opam['tugilgan_yili']}-yilda, {opam['manzil']} viloyatida tug'ilgan.")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
oilam = {
    'Javoxir' : 'osh', 
    'onam' : 'manti', 
    'Malika' : 'shashlik', 
    'Abdulloh' : 'somsa'
    }
print(f"Javoxirning sevimli taomi {oilam['Javoxir']}.")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
lugat = {
    'string' : 'matn', 
    'if' : 'agar', 
    'float' : 'butun va son', 
    "integer" : 'butun son',
    "else" : "u holda"
    }
print(lugat['string'])

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
lugat = {
    'string' : 'matn', 
    'if' : 'agar', 
    'float' : 'butun va son', 
    "integer" : 'butun son',
    "else" : "u holda"
    }
soz = input(f"So'zni kiriting: ").lower()
print(lugat.get(soz, "Bunday so'z mavjud emas"))

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
lugat = {
    'string' : 'matn', 
    'if' : 'agar', 
    'float' : 'butun va son', 
    "integer" : 'butun son',
    "else" : "u holda"
    }
soz = input(f"So'zni kiriting: ").lower()
tarjima = lugat.get(soz)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{soz.title()} so'zi {tarjima} deb tarjima qilinadi")


