class Foods:
    # Carbs
    SUNFLOWER_BREAD = 1100825
    FLOUR_WHEAT = 168896
    # Diary
    EGG = 748967
    DRY_COTTAGE_CHEESE = 1098046
    CREAM_FAT = 1097888
    # Herbs
    CHIVES = 1103349
    # Spices
    CINNAMON = 171320
    # Fats
    BUTTER = 1103823
    FLAX_OIL = 2058238
    # Sweets
    SUGAR = 1103933
    LOTUS = 1984148
    LADY_FINGERS = 2008520


class Amounts:
    TEASPOON = 5
    TABLESPOON = 15
    EGG_S = 58
    EGG_L = 68


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
    DUMPLINGS_NO_FILLING = {
        'Dumplings, no filling': {
            Foods.DRY_COTTAGE_CHEESE: 125,
            Foods.FLOUR_WHEAT: Amounts.TABLESPOON,
            Foods.EGG: .5 * Amounts.EGG_S,
            Foods.BUTTER: .5 * Amounts.TABLESPOON,
            Foods.SUGAR: .5 * Amounts.TABLESPOON,
            Foods.CREAM_FAT: .5 * Amounts.TABLESPOON,
            Foods.CINNAMON: .25 * Amounts.TEASPOON
        }
    }
