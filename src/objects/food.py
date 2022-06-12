class Food:
    def __init__(self, id, name, source, nutrients):
        self.id = id
        self.name = name
        self.source = source
        self.nutrients = nutrients

    def __str__(self):
        return f'{self.name} (id: {self.id}, source: {self.source})'


class AbridgedFood:
    def __init__(self, id, name, source):
        self.id = id
        self.name = name
        self.source = source

    def __str__(self):
        return f'{self.name} (id: {self.id}, source: {self.source})'
