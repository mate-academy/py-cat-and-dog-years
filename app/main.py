def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]

    cat_age = cat_age - 15

    if cat_age >= 0:
        result[0] = 1
    else:
        result[0] = 0

    if cat_age > 0:
        cat_age = cat_age - 9
        if cat_age >= 0:
            result[0] += 1
        else:
            result[0] = 1

    while cat_age > 0:
        cat_age = cat_age - 4
        if cat_age < 0:
            break
        result[0] += 1

    dog_age = dog_age - 15
    if dog_age >= 0:
        result[1] = 1
    else:
        result[1] = 0

    if dog_age > 0:
        dog_age = dog_age - 9
        if dog_age >= 0:
            result[1] += 1
        else:
            result[1] = 1

    while dog_age > 0:
        dog_age = dog_age - 5
        if dog_age < 0:
            break
        result[1] += 1

    return result
