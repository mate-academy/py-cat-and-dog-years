def get_human_age(cat_age: int, dog_age: int) -> list | None:
    if cat_age < 0 or dog_age < 0:
        raise ValueError

    cat_human_age = 0
    dog_human_age = 0

    if cat_age >= 15:
        cat_human_age += 1
        cat_age -= 15
        if cat_age >= 9:
            cat_human_age += 1
            cat_age -= 9
            while cat_age >= 4:
                cat_human_age += 1
                cat_age -= 4

    if dog_age >= 15:
        dog_human_age += 1
        dog_age -= 15
        if dog_age >= 9:
            dog_human_age += 1
            dog_age -= 9
            while dog_age >= 5:
                dog_human_age += 1
                dog_age -= 5

    return [cat_human_age, dog_human_age]
