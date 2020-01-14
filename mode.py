from enum import Enum

class Mode(Enum):
    PUNISHMENT = 1
    REPAIR = 2

class StartingPoint(Enum):
    ALL = 1
    NONE = 2
    RANDOM = 3
    BEST = 4