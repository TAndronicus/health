class Nutrient:
    def __init__(self, nutrient_data):
        self.nutrient_data = nutrient_data
        self.id = nutrient_data['id']
        self.name = nutrient_data['name']
        self.unit = nutrient_data['unitName']
