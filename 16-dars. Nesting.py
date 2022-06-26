# 16-dars. Nesting

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
shoir0 = {
          'ism' : 'Alisher',
          'familya' : 'Navoiy',
          't_yil' : 1441,
          'umr' : 60,
          't_joy' : 'Xirot',
          'asarlar' : ["Xamsa", "Lison ut-tayr", "Munojot"]
          }
shoir1 = {
          'ism' : 'Erkin',
          'familya' : 'Vohidov',
          't_yil' : 1936,
          'umr' : 80,
          't_joy' : "Farg'ona",
          'asarlar' : ["Tong nafasi", "O'zbegim", "Qo'shiqlarim sizga"]
          }
shoir2 = {
          'ism' : 'Abdulla',
          'familya' : 'Qodiriy',
          't_yil' : 1894,
          'umr' : 44,
          't_joy' : "Toshkent",
          'asarlar' : ["O'tkan kunlar", "Mehrobdan chayon", "Obid ketmon"]
          }

shoirlar = [shoir0, shoir1, shoir2]
for shoir in shoirlar:
    print(f"{shoir['ism'].title()} "
          f"{shoir['familya']} "
          f"{shoir['t_yil']} - yilda, "
          f"{shoir['t_joy']}da tavallud topgan. "
          f"{shoir['umr']} yil umr ko'rgan. ")

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

for shoir in shoirlar:
    ism = shoir['ism']
    familya = shoir['familya']
    asarlar = shoir['asarlar']
    print(f"\n {ism} {familya}ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar) 

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
kinolar = {
            'bobur' : ['titanic', 'rambo', 'spider man'],
            'temur' : ['bomba', 'avatar', 'forsaj'],
            'azamat' : ['shaytanat', 'baron', '13-hudud']
            }
for ism, filmlar in kinolar.items():
    print(f"\n {ism.title()}ning sevimli kinolari:")
    for film in filmlar:
        print(film.title())

Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"}
       }

for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n {davlat}ning poytaxti {info['poytaxt'].title()}\n"
          f"Hududi: {info['maydon']} kv.km\n"
          f"Aholisi: {info['aholi']}\n"
          f"Pul birligi: {info['pul birligi']}")

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

davlat = input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(
        f"\n {davlat.title()}ning poytaxti {info['poytaxt'].title()}\n"
        f"Hududi: {info['maydon']} kv.km\n"
        f"Aholisi: {info['aholi']}\n"
        f"Pul birligi: {info['pul birligi']}"
        )
else:
    print("Bizda bunday davlat haqida ma'lumot yo'q")