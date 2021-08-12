class Restaurant():
    def __init__(self, name, cousine):
        self.restaurant_name = name
        self.cousine_type = cousine

    def describe_restaurant(self):
        print('Name: ' + self.restaurant_name.title())
        print("Cousine: " + self.cousine_type.title())

    def open_restaurant(self):
        print("The restaurant \"" + self.restaurant_name.strip().title() + "\" is open." )


restaurant =  Restaurant("CoolName", "StrangeCousine")
restaurant.describe_restaurant()
restaurant.open_restaurant()
