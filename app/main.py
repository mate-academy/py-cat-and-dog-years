def get_human_age(cat_age: int, dog_age: int) -> list:

    result = [0, 0]
    if cat_age >= 15:
        result[0] = 1
    if dog_age >= 15:
        result[1] = 1
    if cat_age >= 24:
        result[0] += (cat_age - 24) // 4 + 1
    if dog_age >= 24:
        result[1] += (dog_age - 24) // 5 + 1

    return result
