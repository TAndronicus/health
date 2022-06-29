class Diet:
    def __init__(self, meals):
        self.meals = meals

    def __str__(self):
        return '\n'.join(map(lambda meal: str(meal), self.meals))

    def get_nutrients(self):
        nutrients = {}
        for meal in self.meals:
            for food, food_amount in meal.foods.items():
                for nutrient, nutrient_amount in food.nutrients.items():
                    if nutrient in nutrients:
                        nutrients[nutrient] += nutrient_amount * food_amount / 100
                    else:
                        nutrients[nutrient] = nutrient_amount * food_amount / 100
        return nutrients

    def print_nutrients(self):
        print('Nutrients:')
        for nutrient, amount in sorted(self.get_nutrients().items()):
            print(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit}')
