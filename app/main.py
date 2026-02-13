def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("ages must be non-negative")
    cat_to_human = to_human(cat_age, 4)
    dog_to_human = to_human(dog_age, 5)
    return [cat_to_human, dog_to_human]


def to_human(age: int, block: int) -> int:
    if age < 15:
        return 0
    if age <= 23:
        return 1
    human = 2
    leftover = age - 24
    human += leftover // block
    return human


get_human_age(14, 13)