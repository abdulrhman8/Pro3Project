class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ahmad', 'bader', 1000)
emp_2 = Employee('Abdulrhman', 'Khaled', 600)

print(emp_2.fullname())
