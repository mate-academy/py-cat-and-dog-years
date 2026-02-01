import math


def convert_age(age: int, animal_to_human_ratio: int) -> int:
    if age < 15:
        return 0
    elif age < 24:
        return 1
    else:
        return math.floor((age - 24) / animal_to_human_ratio) + 2


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError
    if cat_age < 0 or cat_age > 100:
        raise ValueError
    if dog_age < 0 or dog_age > 100:
        raise ValueError

    cat_to_human_age = convert_age(cat_age, 4)
    dog_to_human_age = convert_age(dog_age, 5)

    return [cat_to_human_age, dog_to_human_age]
