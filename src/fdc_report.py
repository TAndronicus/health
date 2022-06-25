from constants.fdc_constants import Meals
from fdc_client import FdcClient

API_KEY = open("key.txt", "r").read()

meals = [
    Meals.OATMEAL,
    Meals.DOSA
]
client = FdcClient(API_KEY)
diet = client.get_meals(meals)
print(diet)
print()
diet.print_nutrients()
