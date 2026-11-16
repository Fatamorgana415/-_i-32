class Student:
    college = "FKTBP VNU"   
    count = 0               

    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1

    def full_name(self):
        return f"{self.name} {self.surname}"

    def age(self, year):
        return year - self.birth_year

    def card(self, year=2026):
        lines = [
            self.full_name(),
            f"group: {self.group}",
            f"age in {year}: {self.age(year)}",
        ]
        width = max(len(line) for line in lines)
        border = "+" + "-" * (width + 2) + "+"
        body = [f"| {line.ljust(width)} |" for line in lines]
        return "\n".join([border, *body, border])


if __name__ == "__main__":
    me = Student("Sasha", "Romanitch", "IT-32", 2009)
    other = Student("Oksana", "Makarchuk", "IT-23", 2008)
    print(me.card())
    print(other.card())
    