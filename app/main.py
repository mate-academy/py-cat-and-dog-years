def get_human_age(cat_age: int, dog_age: int) -> list:
    ages = [0, 0]
    if cat_age >= 15:
        ages[0] += 1
        if cat_age >= 24:
            ages[0] += 1
            if cat_age >= 28:
                ages[0] += 1
                plus_age = cat_age - 28
                ages[0] += plus_age // 4
    if dog_age >= 15:
        ages[1] += 1
        if dog_age >= 24:
            ages[1] += 1
            if dog_age >= 29:
                ages[1] += 1
                plus_age1 = dog_age - 29
                ages[1] += plus_age1 // 5
    return ages