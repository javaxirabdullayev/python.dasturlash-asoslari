# 21-dars. Funksiya va ro'yxat

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 


def big_letter(names):
    for n in range(len(names)):
        names[n] = names[n].title()
        
names = ['ali', 'vali', 'hasan', 'husan']
big_letter(names)
print(names)

# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring


def big_letter(names):
    names = names[:]
    for n in range(len(names)):
        names[n] = names[n].title()
    return names
        
names = ['ali', 'vali', 'hasan', 'husan']
new_names = big_letter(names)
print(names)
print(new_names)

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {(str(ism)).title()}ning bahosini kiriting:  ")
        baholar[ism] = baho
    return baholar
talabalar = ['ali', 'vali', 'xasan', 'xusan']
baholar = bahola(talabalar)
print(baholar)