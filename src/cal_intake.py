WEIGHT = 70
BODY_FAT_PERCENTAGE = 15
ACTIVITY = 4
PHASE = 'bulking'


def printMeasurement(meas, value):
    print(f'{meas}: {round(value)}')


def translateActivity(activity):
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


def translatePhase(phase):
    if phase == 'cutting':
        return 0.8
    elif phase == 'bulking':
        return 1.1
    else:
        raise Exception('Improper phase')


activity, phase = translateActivity(ACTIVITY), translatePhase(PHASE)
lbm = (1 - BODY_FAT_PERCENTAGE / 100) * WEIGHT
printMeasurement('Lean body weight', lbm)
bmr = 370 + 21.6 * lbm
printMeasurement('Basal metabolic rate', bmr)
tdee = bmr * activity
printMeasurement('Total daily energy expenditure', tdee)
goalIntake = tdee * phase
printMeasurement('Goal caloric intake', goalIntake)
