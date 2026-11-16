from task1 import Person, Student, GroupLeader
classes = [Person, Student, GroupLeader]
person = Person("Ivan", "Petrenko")
me = Student("Sasha", "Romanitch", "IT-32")
leader = GroupLeader("Olena", "Koval", "IT-32", "+380 67 000 00 00")
objects = [("person", person), ("me", me), ("leader", leader)]

print("issubclass(рядок, стовпець)")
print(" " * 14 + "".join(c.__name__.ljust(14) for c in classes))
for a in classes:
    print(a.__name__.ljust(14) + "".join(str(issubclass(a, b)).ljust(14) for b in classes))

print("\nisinstance(обʼєкт, клас)")
print(" " * 14 + "".join(c.__name__.ljust(14) for c in classes))
for name, obj in objects:
    print(name.ljust(14) + "".join(str(isinstance(obj, c)).ljust(14) for c in classes))

print("\nGroupLeader.__mro__:")
for cls in GroupLeader.__mro__:
    print(" ", cls)
