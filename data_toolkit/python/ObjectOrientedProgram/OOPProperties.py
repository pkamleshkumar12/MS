class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    # getter
    @property
    def salary(self):
        return self._salary

    # setter
    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary


se = SoftwareEngineer()
# se.set_salary(6000)
se.salary = 6000
# print(se.get_salary())
print(se.salary)
del se.salary
# print(se.salary)  => this will throw AttributeError: 'SoftwareEngineer' object has no attribute '_salary'

