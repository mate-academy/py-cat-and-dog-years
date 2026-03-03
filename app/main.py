from typing import List


def _animal_to_human(age: int, step: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step


def get_human_age(cat_age: int, dog_age: int) -> List[int]:
    return [
        _animal_to_human(cat_age, 4),
        _animal_to_human(dog_age, 5),
    ]
