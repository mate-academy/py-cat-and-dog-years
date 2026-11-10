def get_human_age(cat_age: int, dog_age: int) -> list:
    result = []
    if cat_age < 15:
        result.append(0)
    elif cat_age < 24:
        result.append(1)
    elif cat_age == 24:
        result.append(2)
    else:
        cat_human_age = 2 + (cat_age - 24) // 4
        result.append(cat_human_age)

    if dog_age < 15:
        result.append(0)
    elif dog_age < 24:
        result.append(1)
    elif dog_age == 24:
        result.append(2)
    else:
        dog_human_age = 2 + (dog_age - 24) // 5
        result.append(dog_human_age)

    return result
