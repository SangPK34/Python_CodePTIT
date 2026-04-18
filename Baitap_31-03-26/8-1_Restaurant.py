class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def description_restaurant(self):
        print("Tên nhà hàng:", self.restaurant_name)
        print("Loại ẩm thực:", self.cuisine_type)

    def open_restaurant(self):
        print("Nhà hàng đang mở cửa.")


restaurant = Restaurant("Pizza Home", "Ý")
restaurant.description_restaurant()
restaurant.open_restaurant()