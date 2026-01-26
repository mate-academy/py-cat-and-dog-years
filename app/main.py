from typing import List


def _validate_age(value: object, name: str) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be int")
    if value < 0:
        raise ValueError(f"{name} must be non-negative")
    return value


def _cat_to_human_years(cat_age: int) -> int:
    if cat_age < 15:
        return 0
    if cat_age < 24:
        return 1

    remaining = cat_age - 24
    return 2 + (remaining // 4)


def _dog_to_human_years(dog_age: int) -> int:
    if dog_age < 15:
        return 0
    if dog_age < 24:
        return 1

    remaining = dog_age - 24
    return 2 + (remaining // 5)


def get_human_age(cat_age: object, dog_age: object) -> List[int]:
    cat = _validate_age(cat_age, "cat_age")
    dog = _validate_age(dog_age, "dog_age")
    return [_cat_to_human_years(cat), _dog_to_human_years(dog)]
