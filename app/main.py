def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers.")
    cat_human_age = 0
    dog_human_age = 0

    if 23 >= cat_age > 14:
        cat_human_age = 1
    if 23 >= dog_age > 14:
        dog_human_age = 1
    if cat_age >= 24:
        cat_human_age = ((cat_age - 24) // 4) + 2
    if dog_age >= 24:
        dog_human_age = ((dog_age - 24) // 5) + 2
    return [cat_human_age, dog_human_age]
