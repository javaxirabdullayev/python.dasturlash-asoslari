# Class va obyektlar


# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo).

# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.


class user:
    def __init__(self, login, name, lastname, age, email, mobile_number):
        self.login = login
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.mobile_number = mobile_number
    def get_info(self):
        print(f"User login = {self.login} \n"
              f"User name = {self.name} \n"
              f"User lastname = {self.lastname} \n"
              f"User age = {self.age} \n"
              f"User email = {self.email} \n"
              f"User mobile number = {self.mobile_number}")

     
user1 = user('jawa', 'Javoxir', 'Abdullayev', 29, 'jawa_03@mail.ru', 998974160550)
user2 = user('bob', 'Bobur', 'Gofurov', 30, 'bob_mail.ru', 998911090811)

print(user1.get_info())


