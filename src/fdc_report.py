from constants.fdc_constants import Meals, Foods, Amounts, is_probiotic
from fdc_repo import get_meals, get_food


def print_meals(meals):
    diet = get_meals(meals)
    print(diet)
    print()
    diet.print_nutrients()
    probiotics = [food for meal in diet.meals for food in meal.foods if is_probiotic(food)]
    if len(probiotics) != 0:
        print('Probiotics:\n' + '\n'.join([food.name for food in probiotics]))


def print_food(food_id):
    food = get_food(food_id)
    print(food)
    print(f'{len(food.nutrients)} nutrients')
    food.print_nutrients()
    if is_probiotic(food):
        print(f'{food.name} is a probiotic')


# print(search_foods('pickle', sources=[Source.FOUNDATION_FOOD, Source.SR_LEGACY_FOOD], page=1))
# print_food(171284)

meals = [
    Meals.OATMEAL
]
additional_meal = {
    'Meal': {
        Foods.COTTAGE_CHEESE_DRY: 125,
        Foods.FLOUR_WHEAT: Amounts.TABLESPOON,
        Foods.FLOUR_POTATO: .5 * Amounts.TABLESPOON,
        Foods.TOMATO_CANNED: 3 * Amounts.TABLESPOON,
        Foods.BUTTER: .5 * Amounts.TEASPOON,
        Foods.BREAD_RYE: 67,
        Foods.CHIVES: 20,
        Foods.KIMCHI: 20
    }
}
meals.append(additional_meal)
print_meals(meals)
# diet = get_meals([meal])
# print(diet)
# print()
# diet.print_nutrients()
# print_food(170051)  # 173417
