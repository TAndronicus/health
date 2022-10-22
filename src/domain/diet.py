from termcolor import colored


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

    def print_nutrients(self, nutrient_checker=None):
        if nutrient_checker is not None:
            self.print_nutrients_with_checker(nutrient_checker)
        else:
            self.print_nutrients_raw()

    def print_nutrients_raw(self):
        print('Nutrients:')
        for nutrient, amount in sorted(self.get_nutrients().items()):
            print(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit}')

    def print_nutrients_with_checker(self, nutrient_checker):
        print('Nutrients:')
        for nutrient, amount in sorted(self.get_nutrients().items()):
            nutrient_limits = nutrient_checker.get_limits(nutrient)
            if nutrient_limits is None:
                print(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit}')
            else:
                if nutrient_limits.lo <= amount <= nutrient_limits.hi:
                    print(colored(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit} [{nutrient_limits.lo} - {nutrient_limits.hi}]', 'green'))
                else:
                    print(colored(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit} [{nutrient_limits.lo} - {nutrient_limits.hi}]', 'red'))

    def calculate_omega_3_omega_6(self):
        omega_3, omega_6 = 0, 0
        for nutrient, amount in self.get_nutrients().items():
            if ' n-3' in nutrient.name:
                omega_3 += amount
            elif ' n-6' in nutrient.name:
                omega_6 += amount
        return [omega_3, omega_6]
