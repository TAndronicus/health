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

    def calculate_omega_3_omega_6(self):
        omega_3, omega_6 = 0, 0
        for nutrient, amount in self.nutrients.items():
            if ' n-3' in nutrient.name:
                omega_3 += amount
            elif ' n-6' in nutrient.name:
                omega_6 += amount
        return [omega_3, omega_6]


class AbridgedFood:
    def __init__(self, id, name, source):
        self.id = id
        self.name = name
        self.source = source

    def __str__(self):
        return f'{self.name} (id: {self.id}, source: {self.source})'
