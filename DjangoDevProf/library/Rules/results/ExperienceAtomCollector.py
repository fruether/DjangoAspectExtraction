__author__ = 'freddy'


class ExperienceAtomCollector:
    def __init__(self, value):
        if not isinstance(value, int):
            self.value = None
        self.value = value

    def __call__(self, *args, **kwargs):
        return self.value