class Foods:
    # Bread
    SUNFLOWER_BREAD = 1100825
    # Diary
    DRY_COTTAGE_CHEESE = 1098050
    # Herbs
    CHIVES = 1103349
    # Fats
    FLAX_OIL = 2058238
    # Sweets
    LOTUS = 1984148
    LADY_FINGERS = 2008520


class Meals:
    BREAD_WITH_CHEESE_AND_FLAX_OIL = {
        'Bread with cheese and flax oil': {
            Foods.SUNFLOWER_BREAD: 100,
            Foods.DRY_COTTAGE_CHEESE: 50,
            Foods.CHIVES: 20,
            Foods.FLAX_OIL: 10
        }
    }
    LOTUS = {
        'Lotus': {
            Foods.LOTUS: 8
        }
    }
    LADY_FINGERS = {
        'Lady finger': {
            Foods.LADY_FINGERS: 6
        }
    }
