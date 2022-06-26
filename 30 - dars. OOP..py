# 30-dars. OOP

# Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])

# Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.

# Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.

# Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.

# Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)

# Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.

# Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.

# Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating. 

# Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.


class Shaxs:
    def __init__(self, name, lastname, passport, age):
        self.name = name
        self.lastname = lastname
        self.passport = passport
        self.age = age
    def get_info(self):
        info = f"{self.name} {self.lastname}. "
        info += f"Passport = {self.passport}, {self.age} yoshda."
        return info
    def get_age(self):
        age = self.age
        return age
    
person = Shaxs('Javoxir', 'Abdullayev', 'AA 5166918', 29)


class Talaba(Shaxs):
    def __init__(self, name, lastname, passport, age):
        self.fanlar = []
        super().__init__(name, lastname, passport, age)
    def fanga_yozil(self):
                
           


class Fan:
    def __init__(self, nomi, talabalar_soni,):
        self.nomi = nomi
        self.talabalar_soni = talabalar_soni
        
    
fan1 = Fan('Matematika', 5)
fan2 = Fan('English', 11)
fan3 = Fan('Tarix', 9)    
    
        
            
