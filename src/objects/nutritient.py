class Nutrient:
    def __init__(self, nutrient_data):
        self.nutrient_data = nutrient_data
        self.id = nutrient_data['id']
        self.name = nutrient_data['name']
        self.unit = nutrient_data['unitName']
        self.order = 0

    # noinspection PyRedeclaration
    def __init__(self, id, name, unit, order):
        self.id = id
        self.name = name
        self.unit = unit
        self.order = order

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.order < other.order
