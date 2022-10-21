class Food:
    def __init__(self, id, name, source, nutrients):
        self.id = id
        self.name = name
        self.source = source
        self.nutrients = nutrients

    def __init__(self, abridged_food, nutrients):
        self.id = abridged_food.id
        self.name = abridged_food.name
        self.source = abridged_food.source
        self.nutrients = nutrients

    def __str__(self):
        return f'{self.name} (id: {self.id}, source: {self.source})'

    def print_nutrients(self):
        print('Nutrients:')
        for nutrient, amount in sorted(self.nutrients.items()):
            print(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit}')


class AbridgedFood:
    def __init__(self, id, name, source):
        self.id = id
        self.name = name
        self.source = source

    def __str__(self):
        return f'{self.name} (id: {self.id}, source: {self.source})'
