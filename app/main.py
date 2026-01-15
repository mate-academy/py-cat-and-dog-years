def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]

    if cat_age < 15:
        result[0] = 0
    elif cat_age < 24:
        result[0] = 1
    else:
        result[0] = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        result[1] = 0
    elif dog_age < 24:
        result[1] = 1
    else:
        result[1] = 2 + (dog_age - 24) // 5

    return result
