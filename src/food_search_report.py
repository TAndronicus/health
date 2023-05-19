from constants.fdc_constants import is_probiotic, Foods
from fdc_repo import get_food, search_foods, Source


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


print(search_foods('paprika', sources=[Source.FOUNDATION_FOOD, Source.SR_LEGACY_FOOD], page=1))
print_food(Foods.PEPPER)
