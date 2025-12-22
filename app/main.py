def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError
    cat_count = 0
    dog_count = 0
    if cat_age >= 15:
        cat_count += 1
        if cat_age >= 24:
            cat_count += 1 + (cat_age - 24) // 4
    if dog_age >= 15:
        dog_count += 1
        if dog_age >= 24:
            dog_count += 1 + (dog_age - 24) // 5
    return [cat_count, dog_count]
