from task1 import Student

me = Student("Sasha", "Romanitch", "IT-32", 2009)      
other = Student("Oksana", "Makarchuk", "IT-23", 2008) 

print("college через клас:     ", Student.college)
print("college через обʼєкт me: ", me.college)
print("college через обʼєкт other:", other.college)

me.college = "Another college"   
print("\nПісля me.college = ...")
print("me.college:     ", me.college)
print("other.college:  ", other.college)
print("Student.college:", Student.college)

print("\nme.__dict__:   ", me.__dict__)
print("other.__dict__:", other.__dict__)
print("Student.__dict__ (без службових):",
      {k: v for k, v in Student.__dict__.items() if not k.startswith("__")})

print("\nСтворено студентів:", Student.count)
