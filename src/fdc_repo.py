import csv
import os

from domain.diet import Diet
from domain.food import AbridgedFood, Food
from domain.meal import Meal
from domain.nutrient_checker import NutrientChecker
from domain.nutritient import Nutrient
from domain.page import Page
from domain.simple_nutrient_limits import SimpleNutrientLimits

# Source: https://www.kaggle.com/datasets/stoicstatic/fooddata-central-nutrition-and-component-data

PAGE_SIZE = 50

# db files
FOOD_CSV = 'data/food.csv'
FOOD_NUTRIENT_CSV = 'data/food_nutrient.csv'
NUTRIENT_CSV = 'data/nutrient.csv'
# limits files
NUTRIENT_LIMITS_CSV = 'data/nutrient_limits.csv'
NUTRIENT_LIMITS_DEPENDENT_GENERATOR_CSV = 'data/nutrient_limits_dependent_generator.csv'
NUTRIENT_LIMITS_GENERATED_CSV = 'data/nutrient_limits_generated.csv'

FOOD_ID = 0
FOOD_SOURCE = 1
FOOD_DESCRIPTION = 2

FOOD_NUTRIENT_FOOD_ID = 1
FOOD_NUTRIENT_NUTRIENT_ID = 2
FOOD_NUTRIENT_AMOUNT = 3

NUTRIENT_ID = 0
NUTRIENT_NAME = 1
NUTRIENT_UNIT = 2

NUTRIENT_LIMIT_ID = 0
NUTRIENT_LIMIT_LO = 3
NUTRIENT_LIMIT_HI = 4

DEPENDENT_NUTRIENT_LIMIT_ID = 0
DEPENDENT_NUTRIENT_LIMIT_NAME = 1
DEPENDENT_NUTRIENT_LIMIT_UNIT = 2
DEPENDENT_NUTRIENT_LIMIT_MULTIPLIER = 3
DEPENDENT_NUTRIENT_LIMIT_PARENT_ID = 4
DEPENDENT_NUTRIENT_LIMIT_DISTRIBUTION = 6

DISTRIBUTION_LOWER_TAIL = 'lower-tail'
DISTRIBUTION_BOUNDED = 'bounded'
DISTRIBUTION_UPPER_TAIL = 'upper-tail'


class Source:
    EXPERIMENTAL_FOOD = 'experimental_food'
    SR_LEGACY_FOOD = 'sr_legacy_food'
    SAMPLE_FOOD = 'sample_food'
    MARKET_ACQUISTION = 'market_acquistion'
    SUB_SAMPLE_FOOD = 'sub_sample_food'
    FOUNDATION_FOOD = 'foundation_food'
    AGRICULTURAL_ACQUISITION = 'agricultural_acquisition'
    BRANDED_FOOD = 'branded_food'
    SURVEY_FNDDS_FOOD = 'survey_fndds_food'


def matches_phrases(line, phrases):
    for phrase in phrases:
        if phrase not in line:
            return False
    return True


def matches_source(expected_sources, excluded_sources, actual_source):
    return (expected_sources is None or actual_source in expected_sources) and (excluded_sources is None or actual_source not in excluded_sources)


def search_foods(phrase, page=1, sources=None, excluded_sources=None):
    phrases, res = phrase.lower().split(' '), []
    page_number, elements_in_page = 1, 0
    with open(FOOD_CSV) as file:
        next(file)
        for food_data in csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            if matches_phrases(food_data[FOOD_DESCRIPTION].lower(), phrases) and matches_source(sources, excluded_sources, food_data[FOOD_SOURCE]):
                if page_number == page:
                    res.append(AbridgedFood(food_data[FOOD_ID], food_data[FOOD_DESCRIPTION], food_data[FOOD_SOURCE]))
                elements_in_page += 1
                if elements_in_page == PAGE_SIZE - 1:
                    page_number, elements_in_page = page_number + 1, 0
    return Page(res, page, page_number)


def get_food_abridged(food_id):
    with open(FOOD_CSV) as file:
        next(file)
        for food_data in csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            if int(food_data[FOOD_ID]) == food_id:
                return AbridgedFood(food_id, food_data[FOOD_DESCRIPTION], food_data[FOOD_SOURCE])
    raise Exception(f"No such food: {food_id}")


def get_food(food_id):
    food_nutrients_table = get_nutrients([food_id])
    nutrient_data = get_nutrient_data()
    abridged_food = get_food_abridged(food_id)
    nutrients = {nutrient_data[nutrient_id]: nutrient_amount for (nutrient_id, nutrient_amount) in food_nutrients_table[food_id]}
    return Food(abridged_food, nutrients)


'''
Returns a dictionary {nutrient_id: Nutrient}
'''


def get_nutrient_data():
    nutrients, counter = {}, 0
    with open(NUTRIENT_CSV) as file:
        next(file)
        for nutrient_data in csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            nutrients[int(nutrient_data[NUTRIENT_ID])] = Nutrient(int(nutrient_data[NUTRIENT_ID]), nutrient_data[NUTRIENT_NAME],
                                                                  nutrient_data[NUTRIENT_UNIT], counter)
            counter += 1
    return nutrients


'''
Returns a dictionary {food_id: [(nutrient_id, nutrient_amount), ...], ...}
'''


def get_nutrients(food_ids):
    food_ids_nutrients_tuple = {}
    with open(FOOD_NUTRIENT_CSV) as file:
        next(file)
        for food_nutrient_data in csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            if int(food_nutrient_data[FOOD_NUTRIENT_FOOD_ID]) in food_ids:
                food_id = int(food_nutrient_data[FOOD_NUTRIENT_FOOD_ID])
                if food_id not in food_ids_nutrients_tuple:
                    food_ids_nutrients_tuple[food_id] = [
                        (int(food_nutrient_data[FOOD_NUTRIENT_NUTRIENT_ID]), float(food_nutrient_data[FOOD_NUTRIENT_AMOUNT]))]
                else:
                    food_ids_nutrients_tuple[food_id].append(
                        (int(food_nutrient_data[FOOD_NUTRIENT_NUTRIENT_ID]), float(food_nutrient_data[FOOD_NUTRIENT_AMOUNT])))
    return food_ids_nutrients_tuple


def get_foods(id_amount_dict, name='Default'):
    foods_amounts = {}
    food_nutrients_table = get_nutrients(id_amount_dict.keys())
    nutrient_data = get_nutrient_data()
    for food_id, amount in id_amount_dict.items():
        abridged_food = get_food_abridged(food_id)
        nutrients = {nutrient_data[nutrient_id]: nutrient_amount for (nutrient_id, nutrient_amount) in food_nutrients_table[food_id]}
        foods_amounts[Food(abridged_food, nutrients)] = amount
    return Meal(foods_amounts, name)


def get_meals(meals):
    return Diet([get_foods(ingredients, name) for meal in meals for name, ingredients in meal.items()])


def create_nutrient_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)
    open(file_name, 'w').close()


def propagate_limits(file_name, nutrient_limits_generated):
    with open(nutrient_limits_generated, 'a') as dest:
        with open(file_name, 'r') as src:
            next(src)
            for line in src:
                dest.write(line)
        dest.write('\n')


def load_base_nutrient_checker(nutrient_limits_generated):
    nutrient_limits_list = []
    with open(nutrient_limits_generated, 'r') as file:
        for line in csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            if ',' not in line[NUTRIENT_LIMIT_ID]:
                nutrient_limits_list.append(
                    SimpleNutrientLimits(int(line[NUTRIENT_LIMIT_ID]), float(line[NUTRIENT_LIMIT_LO]), float(line[NUTRIENT_LIMIT_HI]))
                )
    return NutrientChecker(nutrient_limits_list)


def propagate_limits_dependent_generator(file_name, nutrient_limits_generated, base_nutrient_checker):
    with open(nutrient_limits_generated, 'a') as dest:
        writer = csv.writer(dest, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
        with open(file_name, 'r') as src:
            next(src)
            for line in csv.reader(src, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
                parent_nutrient = base_nutrient_checker.get_simple_limits_by_id(int(line[DEPENDENT_NUTRIENT_LIMIT_PARENT_ID]))
                multiplier = float(line[DEPENDENT_NUTRIENT_LIMIT_MULTIPLIER])
                writer.writerow([
                    line[DEPENDENT_NUTRIENT_LIMIT_ID],
                    line[DEPENDENT_NUTRIENT_LIMIT_NAME],
                    line[DEPENDENT_NUTRIENT_LIMIT_UNIT],
                    [round(parent_nutrient.lo * multiplier, 3), 0][line[DEPENDENT_NUTRIENT_LIMIT_DISTRIBUTION] == DISTRIBUTION_LOWER_TAIL],
                    [round(parent_nutrient.hi * multiplier, 3), 0][line[DEPENDENT_NUTRIENT_LIMIT_DISTRIBUTION] == DISTRIBUTION_UPPER_TAIL]
                ])
        dest.write('\n')


def propagate_nutrient_file(
        nutrient_limits_generated=NUTRIENT_LIMITS_GENERATED_CSV,
        nutrient_limits=NUTRIENT_LIMITS_CSV,
        nutrient_limits_dependent_generator=NUTRIENT_LIMITS_DEPENDENT_GENERATOR_CSV
):
    create_nutrient_file(nutrient_limits_generated)
    propagate_limits(nutrient_limits, nutrient_limits_generated)
    base_nutrient_checker = load_base_nutrient_checker(nutrient_limits_generated)
    propagate_limits_dependent_generator(nutrient_limits_dependent_generator, nutrient_limits_generated, base_nutrient_checker)


def load_nutrient_checker(file_name=None):
    propagate_nutrient_file()
    nutrient_limits_list = []
    nutrient_limits_file = file_name if file_name is not None else NUTRIENT_LIMITS_CSV
    with open(nutrient_limits_file) as file:
        next(file)
        for nutrient_limits in csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            nutrient_limits_list.append(SimpleNutrientLimits(int(nutrient_limits[NUTRIENT_LIMIT_ID]), float(nutrient_limits[NUTRIENT_LIMIT_LO]),
                                                             float(nutrient_limits[NUTRIENT_LIMIT_HI])))
    return NutrientChecker(nutrient_limits_list)
