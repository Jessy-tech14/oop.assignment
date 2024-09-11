# Class for Schools
class School:
    def __init__(self, name, location, num_students):
        self.name = name
        self.location = location
        self.num_students = num_students

    def get_info(self):
        return f"{self.name} located in {self.location} with {self.num_students} students."
    
school = School("Greenwood High", "New York", 1200)
print(school.get_info())