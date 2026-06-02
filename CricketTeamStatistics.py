class Player:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def highest_score(self):
        return max(self.scores)

    def lowest_score(self):
        return min(self.scores)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

    def half_centuries(self):
        count = 0

        for score in self.scores:
            if score >= 50:
                count += 1

        return count


player = Player("Virat", [45, 102, 78, 35, 61])

print("Highest Score:", player.highest_score())
print("Lowest Score:", player.lowest_score())
print("Average Score:", round(player.average_score(), 1))
print("Half Centuries:", player.half_centuries())
