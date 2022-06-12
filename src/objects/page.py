class Page:
    def __init__(self, data, page_number, max_pages):
        self.data = data
        self.page_number = page_number
        self.max_pages = max_pages

    def __str__(self):
        if len(self.data) == 0:
            postfix = 'No data.'
        else:
            postfix = 'Data:\n'
            for el in self.data:
                postfix += str(el) + '\n'
        return f'Page {self.page_number}/{self.max_pages}. {postfix}'
