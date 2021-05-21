"""Top-level package for BBone Sensors."""

__author__ = """Alexis Jeandet"""
__email__ = 'alexis.jeandet@member.fsf.org'
__version__ = '0.1.0'


class Metric:
    __slots__ = ['path', 'name', 'value', 'time']

    def __init__(self, path, name, value, time):
        self.path = path
        self.name = name
        self.value = value
        self.time = time
