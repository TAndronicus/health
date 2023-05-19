from comparison_table import ComparisonTable
from constants.fdc_constants import Foods
from fdc_repo import load_nutrient_checker

NUTRIENT_CHECKER = load_nutrient_checker()


def print_comparison(food_ids, food_names=None):
    table = ComparisonTable(food_ids, NUTRIENT_CHECKER, food_names)
    table.print_comparison()


print_comparison(
    [Foods.APPLE, Foods.BANANA, Foods.BLUEBERRY, Foods.GRAPEFRUIT, Foods.KIWIFRUIT, Foods.MELON_CANTALOUPE,
     Foods.MELON_HONEYDEW, Foods.ORANGE, Foods.PEAR, Foods.STRAWBERRIES_RAW, Foods.TANGERINE, Foods.WATERMELON],
    ['APPLE', 'BANANA', 'BLUEBERRY', 'RAPEFRUIT', 'KIWIFRUIT', 'MELON_CANTALOUPE', 'MELON_HONEYDEW', 'ORANGE', 'PEAR',
     'STRAWBERRIES_RAW', 'TANGERINE', 'WATERMELON']
)
print_comparison(
    [Foods.BRAZIL_NUT, Foods.CASHEW_NUT, Foods.CHIA, Foods.COCONUT, Foods.HEMP_SEEDS, Foods.FLAXSEED, Foods.PEANUT,
     Foods.WALNUT],
    ['BRAZIL_NUT', 'CASHEW_NUT', 'CHIA', 'COCONUT', 'HEMP_SEEDS', 'FLAXSEED', 'PEANUT', 'WALNUT']
)
print_comparison(
    [Foods.BARLEY, Foods.BUCKWHEAT, Foods.MILLET, Foods.QUINOA, Foods.RICE_WHITE_SHORT_GRAIN,
     Foods.RICE_WHITE_LONG_GRAIN, Foods.RICE_BROWN_MEDIUM_GRAIN, Foods.RICE_WILD, Foods.SEMOLINA, Foods.PASTA,
     Foods.POTATO, Foods.POTATO_SWEET],
    ["BARLEY", "BUCKWHEAT", "MILLET", "QUINOA", "RICE_WHITE_SHORT_GRAIN", "RICE_WHITE_LONG_GRAIN",
     "RICE_BROWN_MEDIUM_GRAIN", "RICE_WILD", "SEMOLINA", "PASTA", "POTATO", "POTATO_SWEET"]
)
print_comparison(
    [Foods.FLOUR_WHEAT, Foods.FLOUR_WHEAT_WHOLE_GRAIN, Foods.FLOUR_RYE, Foods.FLOUR_POTATO, Foods.FLOUR_SOY,
     Foods.FLOUR_CORN, Foods.FLOUR_RICE],
    ["FLOUR_WHEAT", "FLOUR_WHEAT_WHOLE_GRAIN", "FLOUR_RYE", "FLOUR_POTATO", "FLOUR_SOY", "FLOUR_CORN", "RICE"]
)
