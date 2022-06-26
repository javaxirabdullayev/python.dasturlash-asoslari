# 05-dars. String (matn)

# Quyidagi o'zgaruvchilarni yarating: 
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor" 
viloyat = "Samarqand"
a = f"{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."
print(a)

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
b = f"{kocha} ko\'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati."
print(b)

# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.


manzil = f"{kocha.title()} {mahalla.upper()} {tuman.lower()} {viloyat.capitalize()}"
print(manzil) 