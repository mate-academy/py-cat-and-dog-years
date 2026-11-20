def get_human_age(cat_age: int, dog_age: int) -> list:
    result_cat_age = 0
    if cat_age >= 15:
        result_cat_age += 1
        cat_age -= 15
        if cat_age >= 9:
            result_cat_age += 1
            cat_age -= 9
            result_cat_age += (cat_age // 4)

    result_dog_age = 0
    if dog_age >= 15:
        result_dog_age += 1
        dog_age -= 15
        if dog_age >= 9:
            result_dog_age += 1
            dog_age -= 9
            result_dog_age += (dog_age // 5)

    return [result_cat_age, result_dog_age]
