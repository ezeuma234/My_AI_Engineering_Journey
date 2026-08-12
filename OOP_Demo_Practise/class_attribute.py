class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")

student1 = Student("Uma", 22)
student2 = Student("Eileen", 23)

print(student1.name)
print(student2.name)

print(student1.school)
print(student2.school)