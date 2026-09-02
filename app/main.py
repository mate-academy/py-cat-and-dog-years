def get_human_age(cat_age: int, dog_age: int) -> list:
    if (not isinstance(cat_age, int) or not isinstance(dog_age, int)
            or isinstance(cat_age, bool) or isinstance(dog_age, bool)):
        raise TypeError("Invalid data type entered")

    result = [0, 0]
    cat_old = 4
    dog_old = 5

    result[0] = calculation_age(cat_age, cat_old)
    result[1] = calculation_age(dog_age, dog_old)

    return result


def calculation_age(age: int, old: int) -> int:
    if 15 <= age <= 23:
        return 1
    elif age >= 24:
        return (age - 24) // old + 2
    return 0
