class SoftwareEngineer:
    # class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # def information(self):
    #     information = f"name = {self.name}, age = {self.age}, level = {self.level}"
    #     return information

    # dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se3 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)
se1.code()
se1.code_in_language("Python")

print(se1)
print(se1 == se3)
# print(se1.information())
se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(se2.name, se2.age)
print(SoftwareEngineer.alias)
se2.code()


print(se1.entry_salary(31))
print(SoftwareEngineer.entry_salary(25))
