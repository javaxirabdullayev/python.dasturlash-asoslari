# 32 - dars. Dunder methods

# Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling. 
# Obyekt haqida ma'lumot (__rerp__)
# Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)
# Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
# Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
# Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
# Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)). Bu metodlarni o'zingiz istagandek talqin qiling.



class Shaxs:
    odamlar_soni = 0
    def __init__(self, name, lastname, passport, age):
        self.name = name
        self.lastname = lastname
        self.passport = passport
        self.age = age
        Shaxs.odamlar_soni += 1
        
    def __repr__(self):
        return f"{self.name} {self.lastname}"
    def __eq__(self,y):
        return self.age == y.age
        
talaba1 = Shaxs('Javoxir', 'Abdullayev', 5166918, 29)
talaba2 = Shaxs('Bobur', 'Gofurov', 4165555, 30)
talaba3 = Shaxs('Javlon', 'Muminov', 1114455, 32)
print(talaba1 == talaba2)

print(talaba1)


class Fan:
    def __init__(self, name):
        self.name = name
        self.talabalar = []
               
    def __repr__(self):
        return f"{self.name} fani"
    
    def add_student(self,talaba):
        if isinstance(talaba,Shaxs): 
            self.talabalar.append(talaba)
        else:
            print("Talaba kiriting!")
            
    def __getitem__(self,index):
        return self.talabalar[index]
            
    def __setitem__(self,index,value):
        if isinstance(value,Shaxs):
            self.talabalar[index]=value
           
fanlar = Fan('Matematika')


for talaba in [talaba1, talaba2, talaba3]:
    fanlar.add_student(talaba)
    
print(fanlar[0])
    
talaba1 = Shaxs('Javoxir', 'Abdullayev', 5166918, 29)
talaba2 = Shaxs('Bobur', 'Gofurov', 4165555, 30)
talaba3 = Shaxs('Javlon', 'Muminov', 1114455, 32)


fanlar[0] = talaba2

print(fanlar[0])