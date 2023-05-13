from enum import Enum

from src.resource.resource import Resource


class Resources(Resource, Enum):
    water = Resource("water", 2, 100, 100, True, 0.5)
    food = Resource("food", 2, 100, 100, True, 0.5)
    sunlight = Resource("sunlight", 2, 100, 100, True, 0.5)
