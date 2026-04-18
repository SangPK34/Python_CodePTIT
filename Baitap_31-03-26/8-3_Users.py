class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print("Họ tên:", self.first_name, self.last_name)
        print("Tuổi:", self.age)
        print("Email:", self.email)
        print("Thành phố:", self.city)

    def greet_user(self):
        print(f"Xin chào, {self.first_name} {self.last_name}!")


u1 = User("Nguyễn", "Hà", 20, "ha@gmail.com", "Hà Nội")
u2 = User("Trương", "Phi", 21, "phi@gmail.com", "Hải Dương")
u3 = User("Lữ", "Bố", 20, "bo@gmail.com", "TP.HCM")

u1.describe_user()
u1.greet_user()
print()

u2.describe_user()
u2.greet_user()
print()

u3.describe_user()
u3.greet_user()