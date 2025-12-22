def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_count = 0
    dog_count = 0
    if cat_age >= 15:
        cat_count += 1
        cat_age = cat_age - 15
        if cat_age >= 9:
            cat_count += 1
            cat_age = cat_age - 9
            if cat_age >= 4:
                cat_count += cat_age // 4
    if dog_age >= 15:
        dog_count += 1
        dog_age = dog_age - 15
        if dog_age >= 9:
            dog_count += 1
            dog_age = dog_age - 9
            if dog_age >= 5:
                dog_count += dog_age // 5
    return [cat_count, dog_count]
