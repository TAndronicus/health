from fdc_repo import get_nutrients, get_nutrient_data
from utils import print_table


class ComparisonTable:
    def __init__(self, food_ids, nutrient_checker=None, food_names=None):
        self.food_ids = food_ids
        self.nutrients = get_nutrients(food_ids)
        self.nutrient_data = get_nutrient_data().values()
        self.nutrient_checker = nutrient_checker
        self.food_names = food_names

    def fill_header(self, table):
        if self.food_names is None:
            table.append(['', 'lo', 'hi'] + self.food_ids)
        else:
            table.append(['', 'lo', 'hi'] + self.food_names)

    def fill_nutrients(self, table, with_limits_only):
        for nutrient in self.nutrient_data:
            nutrient_col = f'{nutrient.name} ({nutrient.unit})'
            simple_limits = self.nutrient_checker.get_simple_limits(nutrient)
            if simple_limits is None:
                if with_limits_only:
                    continue
                row = [nutrient_col, '---', '---']
            else:
                row = [nutrient_col, simple_limits.lo, simple_limits.hi]
            for food_id in self.food_ids:
                row.append(self.get_nutrient(self.nutrients[food_id], nutrient))
            table.append(row)

    @staticmethod
    def get_nutrient(nutrient_list, nutrient):
        for nutrient_id, nutrient_val in nutrient_list:
            if nutrient_id == nutrient.id:
                return nutrient_val
        return '---'

    def print_comparison(self, with_limits_only=True):
        table = []
        self.fill_header(table)
        self.fill_nutrients(table, with_limits_only)
        print_table(table)
