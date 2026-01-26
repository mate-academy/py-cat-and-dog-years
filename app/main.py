from typing import List


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


def get_human_age(cat_age: int, dog_age: int) -> List[int]:
    return [_cat_to_human_years(cat_age), _dog_to_human_years(dog_age)]
