def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    result = [0, 0]

    if cat_age >= 15:
        result[0] += 1
    if cat_age >= 24:
        result[0] += 1
    if cat_age > 24:
        result[0] += (cat_age - 24) // 4
    if dog_age >= 15:
        result[1] += 1
    if dog_age >= 24:
        result[1] += 1
    if dog_age > 24:
        result[1] += (dog_age - 24) // 5
    return result
