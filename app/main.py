def get_human_age(cat_age: int, dog_age: int) -> list:
    result = []
    if cat_age <= 14:
        result.append(0)
    elif cat_age <= 23:
        result.append(1)
    else:
        result.append((cat_age - 24) // 4 + 2)

    if dog_age <= 14:
        result.append(0)
    elif dog_age <= 23:
        result.append(1)
    else:
        result.append((dog_age - 24) // 5 + 2)

    return result
