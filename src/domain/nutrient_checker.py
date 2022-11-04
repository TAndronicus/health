from termcolor import colored


class NutrientChecker:

    def __init__(self, simple_nutrient_limits_list, compound_nutrient_limits_list=[]):
        self.simple_nutrient_limits_list = simple_nutrient_limits_list
        self.compound_nutrient_limits_list = compound_nutrient_limits_list

    def get_simple_limits(self, nutrient):
        for simple_nutrient_limits in self.simple_nutrient_limits_list:
            if simple_nutrient_limits.id == nutrient.id:
                return simple_nutrient_limits
        return None

    def get_simple_limits_by_id(self, nutrient_id):
        for simple_nutrient_limits in self.simple_nutrient_limits_list:
            if simple_nutrient_limits.id == nutrient_id:
                return simple_nutrient_limits
        return None

    def get_compound_limits(self, nutrient):
        for compound_nutrient_limit in self.compound_nutrient_limits_list:
            if nutrient.id in compound_nutrient_limit.ids:
                yield compound_nutrient_limit

    @staticmethod
    def print_report_row(nutrient_limits, nutrient, amount):
        if nutrient_limits.lo <= amount <= nutrient_limits.hi:
            print(colored(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit} [{nutrient_limits.lo} - {nutrient_limits.hi}]', 'green'))
        else:
            print(colored(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit} [{nutrient_limits.lo} - {nutrient_limits.hi}]', 'red'))

    def print_report(self, nutrients):
        compound_nutrients = {}
        for nutrient, amount in nutrients:
            nutrient_limits = self.get_simple_limits(nutrient)
            if nutrient_limits is None:
                print(f'{nutrient.name} - {round(amount, 2)} {nutrient.unit}')
            else:
                self.print_report_row(nutrient_limits, nutrient, amount)
            for compound_limit in self.get_compound_limits(nutrient):
                if compound_limit in compound_nutrients:
                    compound_nutrients[compound_limit][1] += amount
                else:
                    compound_nutrients[compound_limit] = [nutrient, amount]
        for compound_limit, [nutrient, amount] in compound_nutrients.items():
            self.print_report_row(compound_limit, nutrient, amount)
