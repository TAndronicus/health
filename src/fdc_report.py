from constants.fdc_constants import Meals, is_probiotic
from fdc_repo import get_meals, get_food, search_foods, Source


def print_meals(meals):
    diet = get_meals(meals)
    print(diet)
    print()
    diet.print_nutrients()
    probiotics = [food for meal in diet.meals for food in meal.foods if is_probiotic(food)]
    if len(probiotics) != 0:
        print('Probiotics:\n' + '\n'.join([food.name for food in probiotics]))
    else:
        print('No probiotics!')
    omega_3, omega_6 = diet.calculate_omega_3_omega_6()
    if omega_3 != 0 or omega_6 != 0:
        print(f'Omega-3 to omega-6 ratio: {round(omega_3 / omega_6, 2) if omega_6 != 0 else 1000}')


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


print(search_foods('pickle', sources=[Source.FOUNDATION_FOOD, Source.SR_LEGACY_FOOD], page=1))
print_food(171284)

meals = [
    Meals.OATMEAL
]
# additional_meal = {
#     'Meal': {
#         Foods.COTTAGE_CHEESE_DRY: 125,
#         Foods.FLOUR_WHEAT: Amounts.TABLESPOON,
#         Foods.FLOUR_POTATO: .5 * Amounts.TABLESPOON,
#         Foods.TOMATO_CANNED: 3 * Amounts.TABLESPOON,
#         Foods.BUTTER: .5 * Amounts.TEASPOON,
#         Foods.BREAD_RYE: 67,
#         Foods.CHIVES: 20,
#         Foods.KIMCHI: 20
#     }
# }
# meals.append(additional_meal)
print_meals(meals)
