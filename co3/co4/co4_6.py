class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
class sem1(student):
    def __init__(self, name,age,mark):
        super().__init__(name,age)
        self.mark = mark
        

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("mark:", self.mark)

class result(sem1):
    def __init__(self, name,age,mark,grade):
        super().__init__(name,mark,age)
        self.grade = grade

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("mark:",self.mark)
        print("grade:",self.grade)
        
b=result("sree",21,95,"A+")
b.display()