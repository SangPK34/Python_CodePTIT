class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def description_restaurant(self):
        print("Tên nhà hàng:", self.restaurant_name)
        print("Loại ẩm thực:", self.cuisine_type)


r1 = Restaurant("Pizza Home", "Ý")
r2 = Restaurant("Sushi Tokyo", "Nhật")
r3 = Restaurant("Pho Viet", "Việt Nam")

r1.description_restaurant()
print()
r2.description_restaurant()
print()
r3.description_restaurant()