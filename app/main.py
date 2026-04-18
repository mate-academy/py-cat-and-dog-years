class IsOutOfRangeError(Exception):
    pass


class NegativeAgeError(IsOutOfRangeError):
    def __str__(self) -> str:
        return "Age can't be negative"


class LargeAgeError(IsOutOfRangeError):
    def __str__(self) -> str:
        return "Age is too big"


def get_human_age(cat_age: int, dog_age: int) -> list:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError()
    if cat_age < 0 or dog_age < 0:
        raise NegativeAgeError()
    if cat_age > 35 or dog_age > 35:
        raise LargeAgeError()
    return [to_human(cat_age, 4), to_human(dog_age, 5)]


def to_human(age: int, step: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step
