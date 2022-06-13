from constants.fdc_constants import Meals
from fdc_client import FdcClient

API_KEY = 'KV2tU1GXpctVLUhg9btY30W2XGnqu5QGPFSeq8AL'

meals = [
    Meals.BREAD_WITH_CHEESE_AND_FLAX_OIL
]
client = FdcClient(API_KEY)
diet = client.get_meals(meals)
print(diet)
print()
diet.print_nutrients()