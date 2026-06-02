class Student:
    def __init__(self, attendance):
        self.attendance = attendance

    def highest_attendance(self):
        return max(self.attendance)

    def lowest_attendance(self):
        return min(self.attendance)

    def eligible_students(self):
        count = 0

        for att in self.attendance:
            if att >= 75:
                count += 1

        return count


student = Student([85, 70, 92, 65, 78, 88])

print("Highest Attendance:", student.highest_attendance())
print("Lowest Attendance:", student.lowest_attendance())
print("Eligible Students:", student.eligible_students())
