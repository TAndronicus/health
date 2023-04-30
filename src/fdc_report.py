from termcolor import colored

from constants.fdc_constants import Meals, is_probiotic, Foods
from fdc_repo import get_meals, get_food, search_foods, load_nutrient_checker, Source
from comparison_table import ComparisonTable

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


def print_food(food_id):
    food = get_food(food_id)
    print(food)
    print(f'{len(food.nutrients)} nutrients')
    food.print_nutrients()
    if is_probiotic(food):
        print(f'{food.name} is a probiotic')
    omega_3, omega_6 = food.calculate_omega_3_omega_6()
    if omega_3 != 0 or omega_6 != 0:
        print(f'Omega-3 to omega-6 ratio: {round(omega_3 / omega_6, 2) if omega_6 != 0 else 1000}')


def print_comparison(food_ids, food_names=None):
    table = ComparisonTable(food_ids, NUTRIENT_CHECKER, food_names)
    table.print_comparison()


print(search_foods('trout', sources=[Source.FOUNDATION_FOOD, Source.SR_LEGACY_FOOD], page=1))
print_food(175154)

meals = [
    Meals.OATMEAL,
    Meals.BREAD_WITH_CHEESE_AND_FLAX_OIL
]
print_meals(meals)

print_comparison(
    [Foods.BRAZIL_NUT, Foods.CASHEW_NUT, Foods.CHIA, Foods.COCONUT, Foods.HEMP_SEEDS, Foods.FLAXSEED, Foods.PEANUT, Foods.WALNUT],
    ['BRAZIL_NUT', 'CASHEW_NUT', 'CHIA', 'COCONUT', 'HEMP_SEEDS', 'FLAXSEED', 'PEANUT', 'WALNUT']
)
