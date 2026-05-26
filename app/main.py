def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0 or cat_age >= 200 or dog_age >= 200:
        raise ValueError

    cat = 0
    dog = 0

    if cat_age < 15:
        pass

    elif cat_age < 24:
        cat = 1

    else:
        cat = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        pass

    elif dog_age < 24:
        dog = 1
    else:
        dog = 2 + (dog_age - 24) // 5

    return [cat, dog]
