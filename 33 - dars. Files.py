# 33 - dars. Files

# Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching

# Quyidagi pi_million_digits.txt faylini yuklab oling (faylda   soni nuqtadan so'ng million xona aniqlik bilan yozilgan). 

# Sizning tug'ilgan kuningiz  soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.

# Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.

# Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni yangi qatordan faylga yozib boruvchi dastur tuzing. Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas).


with open('e:/python/bugun.txt') as file:
          bugun = file.read()
         
print(bugun)

with open('e:/python/pi_million_digits.txt') as file:
          pi = file.read()
         
pi = pi.rstrip()
pi = pi.replace(" ", "")
pi = float(pi)
         


faylnomi = 'info.txt'
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")


with open(faylnomi, 'a') as fayl:
    fayl.write(ism + '\n')
    fayl.write(familiya + '\n')
    fayl.write(yosh + '\n')