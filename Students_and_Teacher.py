class student:
    def __init__(self):
        self.name = "Rahul"
        self.age = 20
        self.marks = 90
        
    def study(self):
        print("Student is studying...")
        
class teacher:
    def __init__(self):
        self.name = "none"
        self.age = "none"
        self.salary = "none"
        
    def teach(self):
        print("Teacher is teaching...")

s1 = student()
s2 = student()
t1 = teacher()

s2.name = "Aayush"
s2.age = 22
s2.marks = 85

t1.name = "Mr. Sharma"
t1.age = 40
t1.salary = 50000

print(s1.name)
print(s1.age)
print(s1.marks)
print(t1.name)
print(t1.age)
print(t1.salary)
print(s2.name)
print(s2.age)
print(s2.marks)

print(s1)
print(s2)
print(t1)