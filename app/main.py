def cat_age_to_human_age(cat_age: int) -> int:
    if cat_age < 15:
        return 0
    if cat_age < 24:
        return 1
    return 2 + (cat_age - 24) // 4


def dog_age_to_human_age(dog_age: int) -> int:
    if dog_age < 15:
        return 0
    if dog_age < 24:
        return 1
    return 2 + (dog_age - 24) // 5


def get_human_age(cat_age: int, dog_age: int) -> list:
    return [cat_age_to_human_age(cat_age), dog_age_to_human_age(dog_age)]
