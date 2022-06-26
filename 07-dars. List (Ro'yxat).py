# 07-dars. List (Ro'yxat)

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Bobur', 'Doston', 'Azamat']
print("Salom", ismlar[1], "bugun darsga borasizmi?")
print(ismlar[0], "choyxonaga boramizmi?")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [4,17,5,8,-2,7.5]
print(sonlar[0] + sonlar[3])
print(sonlar[1] / sonlar[5])
sonlar.insert(2, "6")
print(sonlar)
del sonlar[3]
print(sonlar)

t_shaxslar = ['Amir Temur', 'Imom Buxoriy', 'Alisher Navoiy', 'Bobur']
z_shaxslar = ['Bill Gates', 'Elon Mask', 'Henry Ford', 'Steve Jobs']

a = t_shaxslar.pop(0)
b = z_shaxslar.pop(1)

print("Men tarixiy shaxslardan", a, "bilan, \nzamonaviy shaxslardan esa", b, "bilan \nsuhbat qilishni istar edim")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

friends = []
friends.append('Doston')
friends.append('Bobur')
friends.append('Temur')
friends.append('Azamat')
print(friends)

friends.remove('Azamat')
print(friends)

friends.append('Javlon')
friends.insert(0, 'Tillo')
print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mexmonlar = []
mexmonlar.append(friends.pop(0))
mexmonlar.append(friends.pop(1))
mexmonlar.append(friends.pop(-1))
print(mexmonlar)
