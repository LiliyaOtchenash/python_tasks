class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        'name property docs'
        print('fetch...')