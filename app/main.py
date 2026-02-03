def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_age = 0
    dog_human_age = 0
    if cat_age < 15:
        pass
    if cat_age >= 15:
        cat_human_age += 1
        calculate_cat_age = cat_age - 15
        if calculate_cat_age >= 9:
            cat_human_age += 1
            calculate_cat_age -= 9
            if calculate_cat_age >= 4:
                cat_range = calculate_cat_age // 4
                for _ in range(cat_range):
                    cat_human_age += 1
                    calculate_cat_age -= 4
    if dog_age < 15:
        pass
    if dog_age >= 15:
        dog_human_age += 1
        calculate_dog_age = dog_age - 15
        if calculate_dog_age >= 9:
            dog_human_age += 1
            calculate_dog_age -= 9
            if calculate_dog_age >= 5:
                dog_range = calculate_dog_age // 5
                for _ in range(dog_range):
                    dog_human_age += 1
                    calculate_dog_age -= 5

    return [cat_human_age, dog_human_age]
