def get_human_age(cat_age: int, dog_age: int) -> list:
    return [get_cat_age(cat_age), get_dog_age(dog_age)]


def get_cat_age(cat_age: int) -> int:
    if cat_age < 15:
        return 0
    if 15 <= cat_age < 24:
        return 1
    elif cat_age == 24:
        return 2
    else:
        return 2 + (cat_age - 24) // 4


def get_dog_age(dog_age: int) -> int:
    if dog_age < 15:
        return 0
    if 15 <= dog_age < 24:
        return 1
    elif dog_age == 24:
        return 2
    else:
        return 2 + (dog_age - 24) // 5
