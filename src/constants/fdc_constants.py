class Foods:
    # Carbs
    SUNFLOWER_BREAD = 1100825
    OATS = 1101825
    SEMOLINA = 168933
    FLOUR_WHEAT = 168896
    # Diary
    EGG = 748967
    MILK = 1097512
    DRY_COTTAGE_CHEESE = 1098046
    CREAM_FATTY = 1097888
    # Vegetables
    LENTIL_RED = 174284
    POTATO = 1102882
    MUSHROOM_BUTTON = 1999629
    ONION = 1103364
    GARLIC = 1103354
    # Fruits
    STRAWBERRIES_FROZEN = 1102712
    # Herbs
    CHIVES = 1103349
    LOVAGE = 1034291
    # Spices
    CINNAMON = 171320
    CURRY = 170924
    # Fats
    BUTTER = 1103823
    CANOLA_OIL = 172336
    FLAX_OIL = 2058238
    # Sweets
    SUGAR = 1103933
    XYLITOL = 2294277
    CHOCOLATE_DARK = 170272
    LOTUS = 1984148
    LADY_FINGERS = 2186530


class Amounts:
    TEASPOON = 5
    TABLESPOON = 15
    CHOCOLATE_PIECE = 6
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
            Foods.CREAM_FATTY: .5 * Amounts.TABLESPOON,
            Foods.CINNAMON: .25 * Amounts.TEASPOON
        }
    }
    OATMEAL = {
        'Oatmeal': {
            Foods.OATS: 4 * Amounts.TABLESPOON,
            Foods.MILK: 170,
            Foods.STRAWBERRIES_FROZEN: 25,
            Foods.XYLITOL: Amounts.TEASPOON,
            Foods.CHOCOLATE_DARK: Amounts.CHOCOLATE_PIECE
        }
    }
    DOSA = {
        'Dosa': {
            Foods.EGG: Amounts.EGG_S,
            Foods.FLOUR_WHEAT: 20,
            Foods.SEMOLINA: 20,
            Foods.POTATO: 75,
            Foods.LENTIL_RED: 2 * Amounts.TABLESPOON,
            Foods.ONION: 60,
            Foods.GARLIC: Amounts.TEASPOON,
            Foods.MUSHROOM_BUTTON: 70,
            Foods.LOVAGE: .5 * Amounts.TEASPOON,
            Foods.CANOLA_OIL: 1.5 * Amounts.TABLESPOON,
            Foods.CURRY: .5 * Amounts.TEASPOON
        }
    }
