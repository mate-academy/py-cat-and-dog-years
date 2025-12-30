import math


def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]

    if cat_age >= 15 and cat_age < 24:
        result[0] = 1
    elif cat_age >= 24 and cat_age < 28:
        result[0] = 2
    elif cat_age >= 28:
        cat_rest_years = cat_age - 27
        result[0] = 2 + math.ceil(cat_rest_years / 4)

    if dog_age >= 15 and dog_age < 24:
        result[1] = 1
    elif dog_age >= 24 and dog_age < 29:
        result[1] = 2
    elif dog_age >= 29:
        dog_rest_years = dog_age - 28
        result[1] = 2 + math.ceil(dog_rest_years / 5)

    return result
