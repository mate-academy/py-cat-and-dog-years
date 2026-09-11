def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]
    if cat_age >= 15:
        cat_age -= 15
        result[0] += 1
        if cat_age >= 9:
            cat_age -= 9
            result[0] += 1
            result[0] += cat_age // 4
    if dog_age >= 15:
        dog_age -= 15
        result[1] += 1
        if dog_age >= 9:
            dog_age -= 9
            result[1] += 1
            result[1] += dog_age // 5
    return result
