def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]

    if cat_age >= 15 and cat_age < 24:
        result[0] = 1
    elif cat_age >= 24 and cat_age < 28:
        result[0] = 2
    elif cat_age >= 28:
        result[0] = 2 + (cat_age - 24) // 4

    if dog_age >= 15 and dog_age < 24:
        result[1] = 1
    elif dog_age >= 24 and dog_age < 29:
        result[1] = 2
    elif dog_age >= 29:
        result[1] = 2 + (dog_age - 24) // 5

    return result
