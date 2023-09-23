from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    country: str


    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def __str__(self):
        return f"This is __str__: {self.name}, {self.age}"

    # def __repr__(self):
        # return f"Student(name='{self.name}', age={self.age})"

student = Student("Alice", 18, "India")
print(str(student))

