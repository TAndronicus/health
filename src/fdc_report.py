from constants.fdc_constants import Meals
from fdc_repo import get_meals, get_food

meals = [
    Meals.OMELET
]


def print_meals(meals):
    diet = get_meals(meals)
    print(diet)
    print()
    diet.print_nutrients()


def print_food(food_id):
    food = get_food(food_id)
    print(food)
    print(f'{len(food.nutrients)} nutrients')
    food.print_nutrients()


# print(search_foods('potato', sources=[Source.FOUNDATION_FOOD, Source.SR_LEGACY_FOOD], page=2))
# get_food(172461).print_nutrients()
# print_meals(meals)
print_food(170026)  # 173417
