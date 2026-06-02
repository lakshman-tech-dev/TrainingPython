class Employee:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def best_score(self):
        return max(self.scores)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def months_above_80(self):
        count = 0
        for score in self.scores:
            if score > 80:
                count += 1
        return count


emp = Employee("Priya", [75, 82, 90, 65, 88, 70])

print("Best Score:", emp.best_score())
print("Average Score:", round(emp.average_score(), 1))
print("Months Above 80:", emp.months_above_80())
