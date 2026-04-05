def get_human_age(cat_age: int, dog_age: int) -> list:

    result = []
    if cat_age < 15:
        result.append(0)
    elif 15 <= cat_age <= 23:
        result.append(1)
    elif cat_age >= 24:
        cat = ((cat_age - 24) // 4) + 2
        result.append(cat)

    if dog_age < 15:
        result.append(0)
    elif 15 <= dog_age <= 23:
        result.append(1)
    elif dog_age >= 24:
        dog = ((dog_age - 24) // 5) + 2
        result.append(dog)

    return result
