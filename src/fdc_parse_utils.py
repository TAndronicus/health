from objects.food import Food, AbridgedFood
from objects.meal import Meal
from objects.nutritient import Nutrient
from objects.page import Page


def parse_nutrient(food_nutrient):
    return Nutrient(food_nutrient)


def parse_food_nutrients(food_nutrients):
    return {parse_nutrient(food_nutrient['nutrient']): food_nutrient['amount'] for food_nutrient in food_nutrients if 'id' in food_nutrient}


def parse_food(food):
    return Food(food['fdcId'], food['description'], food['dataType'], parse_food_nutrients(food['foodNutrients']))


def parse_foods(foods):
    return list(map(lambda food: parse_food(food), foods))


def parse_food_abridged(food):
    return AbridgedFood(food['fdcId'], food['description'], food['dataType'])


def parse_foods_abridged(foods):
    return list(map(lambda food: parse_food_abridged(food), foods))


def parse_search_result(result):
    return Page(parse_foods_abridged(result['foods']), result['currentPage'], result['totalPages'])


def parse_get_results(foods, amounts, name):
    return Meal({parse_food(food): amount for food, amount in zip(foods, amounts)}, name)
