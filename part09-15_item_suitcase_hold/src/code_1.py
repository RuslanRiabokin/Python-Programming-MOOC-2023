# Write your solution here:
class Item:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def name(self):
        return self._name

    def weight(self):
        return self._weight

    def __str__(self):
        return f"{self._name} ({self._weight} kg)"


class Suitcase:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._items = []

    def add_item(self, item):
        total_weight = sum(item.weight() for item in self._items)
        if total_weight + item.weight() <= self._max_weight:
            self._items.append(item)

    def print_items(self):
        for item in self._items:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self._items)

    def heaviest_item(self):
        if not self._items:
            return None
        return max(self._items, key=lambda x: x.weight())

    def __str__(self):
        num_items = len(self._items)
        total_weight = sum(item.weight() for item in self._items)
        item_plural = "items" if num_items != 1 else "item"
        return f"{num_items} {item_plural} ({total_weight} kg)"

class CargoHold:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self._suitcases = []

    def add_suitcase(self, suitcase):
        total_weight = sum(suitcase.weight() for suitcase in self._suitcases)
        if total_weight + suitcase.weight() <= self._max_weight:
            self._suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self._suitcases:
            suitcase.print_items()

    def __str__(self):
        num_suitcases = len(self._suitcases)
        available_space = self._max_weight - sum(suitcase.weight() for suitcase in self._suitcases)
        return f"{num_suitcases} suitcase{'s' if num_suitcases != 1 else ''}, space for {available_space} kg"
