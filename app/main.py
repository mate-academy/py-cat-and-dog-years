def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]

    if cat_age in range(15, 24):
        result[0] = 1
    elif cat_age == 24:
        result[0] = 2
    elif cat_age > 24:
        result[0] = (cat_age - 24) // 4 + 2

    if dog_age in range(15, 24):
        result[1] = 1
    elif dog_age == 24:
        result[1] = 2
    elif dog_age > 24:
        result[1] = (dog_age - 24) // 5 + 2

    return result
