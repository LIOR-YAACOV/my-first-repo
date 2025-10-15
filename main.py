from Student import Student
from Employee import Employee

student = Student("Alex", 25, "English", 2, 90)
# student.foo()
print("This is from programmer 1")

employee = Employee("John", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()









