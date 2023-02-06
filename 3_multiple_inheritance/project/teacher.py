from project.person import Person
from project.employee import Employee
class Teacher(Person,Employee):
    def teach(self):
        return "teaching..."

ivan = Teacher()
print(ivan.teach())
print(ivan.sleep())
print(ivan.get_fired())



