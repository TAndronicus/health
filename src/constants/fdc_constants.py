class FoodConstants:
    # Bread
    SUNFLOWER_BREAD = 1100825
    # Diary
    DRY_COTTAGE_CHEESE = 1098050
    # Herbs
    CHIVES = 1103349
    # Fats
    FLAX_OIL = 2058238


class Meals:
    BREAD_WITH_CHEESE_AND_FLAX_OIL = {
        'Bread with cheese and flax oil': {
            FoodConstants.SUNFLOWER_BREAD: 100,
            FoodConstants.DRY_COTTAGE_CHEESE: 50,
            FoodConstants.CHIVES: 20,
            FoodConstants.FLAX_OIL: 10
        }
    }
