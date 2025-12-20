def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]
    if cat_age >= 15:
        result[0] += 1
        cat_age -= 15
        if cat_age >= 9:
            result[0] += 1
            cat_age -= 9
            if cat_age >= 4:
                result[0] += cat_age // 4
    if dog_age >= 15:
        result[1] += 1
        dog_age -= 15
        if dog_age >= 9:
            result[1] += 1
            dog_age -= 9
            if dog_age >= 5:
                result[1] += dog_age // 5
    return result
