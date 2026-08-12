class Student:

    def __init__(self, name, age, goal):
        self.name = name
        self.age = age
        self.goal = goal

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("My goal is", self.goal)


student1 = Student("Eileen", 22, "Better grades")
student2 = Student("Tina", 23, "Faster reply time")
student3 = Student("Anita", 21, "Confident responses")

student1.introduce()
student2.introduce()
student3.introduce()