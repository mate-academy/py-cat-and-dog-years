def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if cat_age < 15:
        cat = 0
    elif cat_age < 24:
        cat = 1
    else:
        cat = 2 + ((cat_age - 24) // 4)

    if dog_age < 15:
        dog = 0
    elif dog_age < 24:
        dog = 1
    else:
        dog = 2 + ((dog_age - 24) // 5)

    return [cat, dog]
