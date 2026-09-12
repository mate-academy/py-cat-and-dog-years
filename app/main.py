def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]
    if cat_age < 15:
        result[0] += 0
    elif 15 <= cat_age < 24:
        result[0] += 1
    else:
        result[0] += (cat_age - 24) // 4 + 2

    if dog_age < 15:
        result[1] += 0
    elif 15 <= dog_age < 24:
        result[1] += 1
    else:
        result[1] += (dog_age - 24) // 5 + 2

    return result
