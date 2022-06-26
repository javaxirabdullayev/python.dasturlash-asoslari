# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
# Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
# Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
# Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
# dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)





class Avto:
    def __init__(self, model, color, box, year, km = 0):
        self.model = model
        self.color = color
        self.box = box
        self.year = year
        self.km = 0
    def get_info(self):
        return f"Avto model = {self.model}\n" f"Avto color = {self.color} \n" f"Avto box = {self.box} \n" f"Avto year = {self.year} \n" f"Avto kilometr = {self.km} \n"

    def set_km(self, new_km):
        self.km = new_km
        
    def update_km(self):
        self.km += 1
        

avto1 = Avto('Malibu', 'black', 'auto', 2022)
avto2 = Avto('Gentra', 'black', 'auto', 2021)


avto1.set_km(100)

avto1.update_km()


class Avtosalon:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.number = 0
    def get_info(self):
            return f" Name - {self.name}\n Cars - {self.cars} \n KM number - {self.number} \n"
    
    def add_car(self,car):
         self.cars.append(car)
         self.number += 1

salon = Avtosalon("Chevrolet")
salon.add_car(avto1)
salon.add_car(avto2)

print(avto1.__dict__)

 
print(dir(Avto))

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Avto))