# inherits, extend, override

class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working..")


class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding...")

    def debug(self):
        print(f"{self.name} is debugging ...")


class Designer(Employee):

    def draw(self):
        print(f"{self.name} is drawing ...")

    def work(self):
        print(f"{self.name} is designing ...")


se = SoftwareEngineer("Max", 20, 6000, "Junior")
print(se.name, se.age, se.level)
# se.work()
se.debug()

de = Designer("Lisa", 31, 7000)
print(de.name, de.age)
# de.work()
# de.draw()

# Polymorphism
# way to use exactly like parents but child class can keep

employee = [SoftwareEngineer("Max", 25, 6000, "Junior"),
            SoftwareEngineer("Lisa", 30, 9000, "Senior"),
            Designer("Philipp", 27, 7000)
            ]


def motivate_employees(employees):
    for emp in employees:
        emp.work()


motivate_employees(employee)
