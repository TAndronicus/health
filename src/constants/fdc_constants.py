class Foods:
    # Carbs
    BARLEY = 170284
    BREAD_MULTIGRAIN = 168013
    BREAD_RYE = 172684
    BREAD_SUNFLOWER = 1100825
    BREAD_WHEAT = 172686  # No aminoacids
    BUCKWHEAT = 170685
    FLOUR_CORN = 169696
    FLOUR_SOY = 174273
    FLOUR_WHEAT = 168896
    MILLET = 169702
    OATS = 173904
    PASTA = 168927
    QUINOA = 168874
    RICE_BROWN_MEDIUM_GRAIN = 168875
    RICE_WHITE_LONG_GRAIN = 168877
    RICE_WHITE_SHORT_GRAIN = 168881
    SEMOLINA = 168933
    # Diary and equivalents
    BUTTERMILK = 172225
    CHEESE_EDAM = 173419
    CHEESE_MOZZARELLA = 170845
    COTTAGE_CHEESE_DRY = 172182
    CREAM_FATTY = 1097888
    EGG = 748967
    MILK = 172217
    TOFU = 172461
    YOGURT = 171284
    # Vegetables
    ASPARAGUS = 168389
    BEAN_CANNED = 173741
    BEAN_RAW = 175193
    BEET = 169145
    BROCCOLI = 170379
    CARROT = 170393
    CAULIFLOWER = 169986
    CELERY = 169988
    CHICKPEA_CANNED = 173801
    CHICKPEA_RAW = 173756
    CUCUMBER = 169225
    EGGPLANT = 169228
    GARLIC = 1103354
    LEEK = 169246
    LENTIL_GREEN = 172420
    LENTIL_RED = 174284
    MUSHROOM_BUTTON = 366857
    ONION = 1103364
    PEPPER_SWEET_RED = 170108
    POTATO = 170026
    POTATO_SWEET = 168482
    RADISH = 169276
    SPINACH_FROZEN = 169287
    TOMATO = 170457
    ZUCCHINI = 169291
    # Fruits
    APPLE = 171688
    BANANA = 173944
    BLUEBERRY = 171711
    GRAPEFRUIT = 173033
    KIWIFRUIT = 168153
    LEMON = 167746
    MELON_CANTALOUPE = 169092
    MELON_HONEYDEW = 169911
    ORANGE = 169097
    PEAR = 169118
    STRAWBERRIES_FROZEN = 1102712
    STRAWBERRIES_RAW = 167762
    TANGERINE = 169105
    WATERMELON = 167765
    # Nuts & dried fruits
    CASHEW_NUT = 170162
    DACTYL_DEGLET_NOOR = 171726
    FIG_DRIED = 174665
    FLAXSEED = 169414
    PEANUT = 172430
    PLUM_DRIED = 168162
    RAISIN = 168165
    WALNUT = 170186
    # Herbs
    CHIVES = 1103349
    LOVAGE = 1034291
    PARSLEY = 170416
    # Spices
    CINNAMON = 171320
    CURRY = 170924
    PEPPER = 170931
    # Fats
    BUTTER = 1103823
    CANOLA_OIL = 172336
    FLAX_OIL = 1103860
    OLIVE_OIL = 171413
    SUNFLOWER_OIL = 171025
    # Sweets
    CHOCOLATE_DARK = 170272
    LADY_FINGERS = 172821
    LOTUS = 367950
    SUGAR = 1103933
    XYLITOL = 392084


class Amounts:
    TEASPOON = 5
    TABLESPOON = 15
    CHOCOLATE_PIECE = 6
    EGG_S = 58
    EGG_L = 68


class Meals:
    BREAD_WITH_CHEESE_AND_FLAX_OIL = {
        'Bread with cheese and flax oil': {
            Foods.BREAD_SUNFLOWER: 100,
            Foods.COTTAGE_CHEESE_DRY: 50,
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
            Foods.COTTAGE_CHEESE_DRY: 125,
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
    OMELET = {
        'Omelet': {
            Foods.ASPARAGUS: 25,
            Foods.EGG: Amounts.EGG_L,
            Foods.TOFU: 40,
            Foods.BUTTER: .5 * Amounts.TEASPOON,
            Foods.SUNFLOWER_OIL: Amounts.TEASPOON
        }
    }
