# Encapsulation is mechanism of hiding variable

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # _X is called a "protected" attributed (one Underscore)
        # __X is called a "private" attribute (double underscore)
        self._salary = None
        self._num_bug_solved = 0

    def code(self):
        self._num_bug_solved += 1

    # getters
    def get_salary(self):
        return self._salary

    # setters
    def set_salary(self, base_value):
        # check value, enforce constraints
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bug_solved < 10:
            return base_value
        if self._num_bug_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer("Max", 25)

print(se.name, se.age)

for i in range(70):
    se.code()

se.set_salary(6000)
print(se.get_salary())

# Principle of abstraction is natural extension of encapsulation
# HR employee should be able to set salary, doesn't care how it is implemented
