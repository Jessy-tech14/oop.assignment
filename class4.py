# Class for Phones
class Phone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."
    
phone = Phone("Samsung", "Galaxy S21", 24)
print(phone.make_call("123-456-7890"))