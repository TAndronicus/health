class Meal:
    def __init__(self, foods, name='Default'):
        self.foods = foods
        self.name = name

    def __str__(self):
        if len(self.foods) == 0:
            foods_str = 'empty'
        else:
            foods_str = '\n'.join([f'{amount}g of {str(food)}' for food, amount in self.foods.items()])
        return f'Meal: {self.name}. Ingredients:\n{foods_str}'
