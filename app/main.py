from typing import List


def _animal_to_human(age: int, step: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step


def get_human_age(cat_age: int, dog_age: int) -> List[int]:

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("cat_age and dog_age must be non-negative")

    cat_human = _animal_to_human(cat_age, step=4)
    dog_human = _animal_to_human(dog_age, step=5)
    return [cat_human, dog_human]
