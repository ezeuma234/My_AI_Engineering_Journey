class Student:

    def __init__(self, name, age, goal):
        self.name = name
        self.age = age
        self.goal = goal

student1 = Student("Eileen", 22, "Better grades")
student2 = Student("Tina", 23, "Faster reply time")
student3 = Student("Anita", 21, "Confident responses")

print(student1.name)
print(student1.goal)
print(student2.name)
print(student2.goal)