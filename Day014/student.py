class Student:

    def __init__(self, name, age, goal):
        self.name = name
        self.age = age
        self.goal = goal

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("My goal is to be a", self.goal)
  
