def get_human_age(cat_age: int, dog_age: int) -> list:
    return [_convert(cat_age, 4), _convert(dog_age, 5)]


def _convert(age: int, step: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step
