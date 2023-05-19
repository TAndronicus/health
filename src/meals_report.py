from termcolor import colored

from constants.fdc_constants import Meals, is_probiotic, Foods
from fdc_repo import get_meals, load_nutrient_checker

NUTRIENT_CHECKER = load_nutrient_checker()
OMEGA_3_TO_OMEGA_6_LO = .25


def print_meals(meals):
    diet = get_meals(meals)
    print(diet)
    print()
    diet.print_nutrients(NUTRIENT_CHECKER)
    probiotics = [food for meal in diet.meals for food in meal.foods if is_probiotic(food)]
    if len(probiotics) != 0:
        print('Probiotics:\n' + '\n'.join([food.name for food in probiotics]))
    else:
        print('No probiotics!')
    omega_3, omega_6 = diet.calculate_omega_3_omega_6()
    if omega_3 != 0 or omega_6 != 0:
        ratio = round(omega_3 / omega_6, 2) if omega_6 != 0 else 1000
        print(colored(f'Omega-3 to omega-6 ratio: {ratio}', 'green' if ratio >= OMEGA_3_TO_OMEGA_6_LO else 'red'))


def as_meal(food_id, amount, food_name):
    return {food_name: {food_id : amount}}


print_meals([
    Meals.OATMEAL,
    Meals.SCRAMBLED_EGGS,
    Meals.CHICKPEA_CUTLETS,
    Meals.BEETROOTS,
    as_meal(Foods.RICE_WHITE_LONG_GRAIN, 75, 'Rice'),
    Meals.MACKEREL
])
