class Checkout:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price

    def remove_item(self, item, price):
        self.items.remove(item)
        self.total -= price

    def get_total(self):
        return self.total

    def reset_cart(self):
        self.items = []
        self.total = 0