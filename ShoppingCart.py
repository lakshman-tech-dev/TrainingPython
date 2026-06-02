class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices

    def total_bill(self):
        return sum(self.prices)

    def costliest_item(self):
        return max(self.prices)

    def discounted_bill(self):
        total = self.total_bill()

        if total > 5000:
            total = total - (total * 15 / 100)

        return total


cart = ShoppingCart([1200, 3500, 800, 1500])

print("Total Bill:", cart.total_bill())
print("Costliest Item:", cart.costliest_item())
print("Discounted Bill:", cart.discounted_bill())
