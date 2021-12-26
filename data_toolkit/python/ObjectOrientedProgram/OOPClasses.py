# class  --> Blueprint
class SoftwareEngineer:

    # class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):

        # instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)

se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(se2.name, se2.age)
print(SoftwareEngineer.alias)
