from math import floor


def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]

    if cat_age < 15:
        result[0] = 0
    elif 15 <= cat_age < 24:
        result[0] = 1
    elif cat_age == 24:
        result[0] = 2
    elif cat_age > 24:
        cat_age -= 24
        result[0] = floor(cat_age // 4) + 2

    if dog_age < 15:
        result[1] = 0
    elif 15 <= dog_age < 24:
        result[1] = 1
    elif dog_age == 24:
        result[1] = 2
    elif dog_age > 24:
        dog_age -= 24
        result[1] = floor(dog_age // 5) + 2

    return result
