class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def highest_mark(self):
        return max(self.marks)

    def status(self):
        if min(self.marks) >= 35:
            return "Pass"
        else:
            return "Fail"


student = Student("Ravi", [78, 45, 92, 30, 67])

print("Total:", student.total())
print("Average:", student.average())
print("Highest Mark:", student.highest_mark())
print("Status:", student.status())
