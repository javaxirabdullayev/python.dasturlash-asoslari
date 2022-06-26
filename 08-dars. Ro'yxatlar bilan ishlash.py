# 08-dars. Ro'yxatlar bilan ishlash


# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ['Rossiya', 'Belgiya', 'Angliya', 'Italiya', 'Fransiya', 'Ispaniya']
print(davlatlar)

# Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
davlatlar.sort(reverse=True)
print(davlatlar)

# Asl ro'yxatni qaytadan konsolga chiqaring

print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'manti', 'somsa', 'kabob', 'siltama']
nonushta = []

# nonushta degan yangi ro'yxatga taomlardan nusxa oling

nonushta = taomlar[:]
print(nonushta)

del nonushta[0]
del nonushta[3]
del nonushta[2]
print(nonushta)

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.append('tvorog')
nonushta.append('smetana')
print(nonushta)

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

print(nonushta)
print(taomlar)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

nonushta = tuple(nonushta)
print(nonushta)

nonushta.append('qaymoq va non')
print(nonushta)







