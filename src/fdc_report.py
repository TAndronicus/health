from constants.fdc_constants import Meals
from fdc_repo import get_meals

meals = [
    Meals.OATMEAL,
    Meals.DOSA
]
diet = get_meals(meals)
print(diet)
print()
diet.print_nutrients()
