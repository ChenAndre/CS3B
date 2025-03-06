#Define enum DaysofWeek by defining it as a class
#Define the __str__() method so that only the first letter of day is capitalized when printed


from enum import Enum, auto

class DaysOfWeek(Enum):
    Sunday = auto()
    Monday = auto()
    Tuesday = auto()
    Wedsnday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()

    def__str__(self):
        return self.name.capitalize()
