import copy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('kamlesh', 30)
p2 = Person('Joe', 23)
# p2 = copy.copy(p1)

company = Company(p1, p2)
#company_clone = copy.copy(company)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 31
print(company_clone.boss.age)
print(company.boss.age)
