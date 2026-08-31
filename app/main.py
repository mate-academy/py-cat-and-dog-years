def get_human_age(cat_age: int, dog_age: int) -> list:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError

    result = [0, 0]

    if 15 <= cat_age <= 23:
        result[0] = 1
    elif cat_age >= 24:
        result[0] = (cat_age - 24) // 4 + 2

    if 15 <= dog_age <= 23:
        result[1] = 1
    elif dog_age >= 24:
        result[1] = (dog_age - 24) // 5 + 2

    return result
