def get_human_age(cat_age: int, dog_age: int) -> list:
    final_ages = [0, 0]

    # CAT
    if 15 <= cat_age < 24:
        final_ages[0] = 1
    if 24 <= cat_age < 28:
        final_ages[0] = 2
    if cat_age >= 28:
        extra_cat_age = cat_age - 24
        if extra_cat_age // 4 >= 1:
            final_ages[0] = 2 + (extra_cat_age // 4)

    # DOG
    if 15 <= dog_age < 24:
        final_ages[1] = 1
    if 24 <= dog_age < 29:
        final_ages[1] = 2
    if dog_age >= 29:
        extra_dog_age = dog_age - 24
        if extra_dog_age // 5 >= 1:
            final_ages[1] = 2 + (extra_dog_age // 5)

    return final_ages
