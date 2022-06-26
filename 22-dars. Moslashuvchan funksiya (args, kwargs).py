# 22-dars. Moslashuvchan funksiya (*args, **kwargs)

# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def multiply(*numbers):
    summa = 1
    for numb in numbers:
        summa *= numb
    return summa

a = multiply(1,2,3)
print(a) 

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_info(ism, familya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familya'] = familya
    return malumotlar
talabalar1 = talaba_info('Javoxir', 'Abdullayev', yosh = '29', qayerdan = 'Fargona')

print(talabalar1)