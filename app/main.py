def get_human_age(cat_age: int, dog_age: int) -> list:
    cat = 0
    dog = 0
    if cat_age < 15:
        cat = 0
    elif cat_age < 24:
        cat = 1
    else:
        cat = (cat_age - 24) // 4 + 2
    if dog_age < 15:
        dog = 0
    elif dog_age < 24:
        dog = 1
    else:
        dog = (dog_age - 24) // 5 + 2
    return [cat, dog]
