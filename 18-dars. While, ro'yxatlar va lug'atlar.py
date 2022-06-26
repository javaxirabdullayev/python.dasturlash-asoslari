# 18-dars. While, ro'yxatlar va lug'atlar

# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

print("Orders")

products = []
n = 1
while True:
    question = f"{n}-mahsulot nomini kiriting: "
    product = input(question)
    products.append(product)
    
    
    repeat = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
    n += 1
    if repeat != 'ha':
        break

print("Mahsulotlar ro'yxati:")
for product in products:
    print(product.title())

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.


products = {}
sign = True
while sign:
    product = input("Mahsulot nomini kiriting: ")
    price = input(f"{product.title()} narxini kiriting: ")
    products[product] = int(price)
    
    answer = input("Yana mahsulot qo'shasizmi? (ha/yo'q): ")
    if answer == "yo'q":
        sign = False  
    
for product,price in products.items():
    print(f"{product.title()} {price} so'm.")

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

orders = []
products = {'non' : 1500,
            'suv' : 2000,
            'olma' : 5000,
            'behi' : 8000,
            'shokolad' : 11000,
            'nok' : 7500}

sign = True
while sign:
    question = input("Mahsulot nomini kiriting: ")
    orders.append(question)
    
    answer = input("Yana mahsulot qo'shasizmi? (ha/yo'q): ")
    if answer != 'ha':
        sign = False

while orders:
    order = orders.pop()
    if orders in products.keys():
       price = products[order]
       print(f"{order.title()} - {price} so'm")
    else:
        print(f"Bizda {order} yo'q")
        












        
    
  