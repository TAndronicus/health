class NutrientChecker:

    def __init__(self, nutrient_limits_list):
        self.nutrient_limits_list = nutrient_limits_list

    def get_limits(self, nutrient):
        for nutrient_limits in self.nutrient_limits_list:
            if nutrient_limits.id == nutrient.id:
                return nutrient_limits
        return None
