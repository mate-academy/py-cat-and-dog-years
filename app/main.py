def get_human_age(cat_age: int, dog_age: int) -> list:

    c_age = 0
    d_age = 0
    if cat_age >= 15:
        c_age += 1
        cat_age -= 15
        if cat_age >= 9:
            c_age += 1
            cat_age -= 9
            if cat_age != 0:
                rem_age = cat_age // 4
                c_age += rem_age

    if dog_age >= 15:
        d_age += 1
        dog_age -= 15
        if dog_age >= 9:
            d_age += 1
            dog_age -= 9
            if dog_age != 0:
                rem_age = dog_age // 5
                d_age += rem_age

    return [c_age, d_age]
