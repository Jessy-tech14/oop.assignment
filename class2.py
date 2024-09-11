# Class for Humans
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Hi, I'm {self.name}, a {self.age}-year-old {self.gender}."
    
human = Human("Alice", 30, "female")
print(human.introduce())