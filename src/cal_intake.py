WEIGHT = 70
BODY_FAT_PERCENTAGE = 10
ACTIVITY = 4
PHASE = 'bulking'

CARBS_KCAL = 4
FATS_KCAL = 9
MIN_FAT_RATIO = .15
MAX_FAT_RATIO = .3


def print_measurement(meas, value):
    print(f'{meas}: {round(value)}')


def translate_activity(activity):
    if activity == 1:
        print('Sedentary (Little to no exercise in a week)')
        return 1.1
    elif activity == 2:
        print('Lightly active (Light exercise 1-3 days/week)')
        return 1.2
    elif activity == 3:
        print('Moderately active (Moderate exercise 3-5 days/week)')
        return 1.35
    elif activity == 4:
        print('Very active (Hard exercise 6-7 days/week)')
        return 1.45
    elif activity == 5:
        print('Extremely active (Very hard exercise + physical job)')
        return 1.7
    else:
        raise Exception('Improper activity')


def translate_phase(phase):
    if phase == 'cutting':
        return 0.8
    elif phase == 'bulking':
        return 1.1
    else:
        raise Exception('Improper phase')


activity, phase = translate_activity(ACTIVITY), translate_phase(PHASE)
lbm = (1 - BODY_FAT_PERCENTAGE / 100) * WEIGHT
print_measurement('Lean body weight', lbm)
bmr = 370 + 21.6 * lbm
print_measurement('Basal metabolic rate', bmr)
tdee = bmr * activity
print_measurement('Total daily energy expenditure', tdee)
goal_intake = tdee * phase
print_measurement('Goal caloric intake during ' + PHASE, goal_intake)
min_fat, max_fat = MIN_FAT_RATIO * goal_intake / FATS_KCAL, MAX_FAT_RATIO * goal_intake / FATS_KCAL
min_carb, max_carb = (1 - MAX_FAT_RATIO) * goal_intake / CARBS_KCAL, (1 - MIN_FAT_RATIO) * goal_intake / CARBS_KCAL
print(f'Carbs: [{round(min_carb)} - {round(max_carb)}]g, fats: [{round(min_fat)} - {round(max_fat)}]g')
