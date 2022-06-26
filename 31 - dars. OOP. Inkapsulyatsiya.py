# 31 - dars. OOP. Inkapsulyatsiya

# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.

# Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.

# Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing 


class Shaxs:
    odamlar_soni = 0
    def __init__(self, name, lastname, passport, age):
        self.name = name
        self.lastname = lastname
        self.passport = passport
        self.__age = age
        Shaxs.odamlar_soni += 1
    
    def get_age(self):
        return self.__age
    
    
    def add_age(self, age):
        if age >= 0:
            self.__age += age
        else:
            print("Yoshni kamaytirib bo'lmaydi")
    
    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni


talaba1 = Shaxs('Javoxir', 'Abdullayev', "AA 5166918", 29)

talaba1.add_age(-5)

print(talaba1.get_age())   



print(talaba1.odamlar_soni)