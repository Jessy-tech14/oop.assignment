# Class for Computers
class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def get_specs(self):
        return f"{self.brand} with {self.processor} processor and {self.ram}GB RAM."
    
computer = Computer("Dell", "Intel i7", 16)
print(computer.get_specs())