class Cell:

    def __init__(self):
        self.domain = range(1,10)
        self.position = []

    def remove(self, value):
        try:
            self.domain.remove(value)
        except ValueError:
            pass
