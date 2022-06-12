class Diet:
    def __init__(self, meals):
        self.meals = meals

    def __str__(self):
        return '\n'.join(map(lambda meal: str(meal), self.meals))
