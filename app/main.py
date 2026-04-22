def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_to_human = 0
    dog_to_human = 0
    if cat_age < 0:
        cat_age = 0
    if dog_age < 0:
        dog_age = 0
    if cat_age >= 15:
        cat_to_human += 1
        if cat_age >= 24:
            cat_to_human += 1
            if cat_age >= 28:
                cat_to_human += 1
                cat_age -= 28
                cat_to_human += cat_age // 4
    if dog_age >= 15:
        dog_to_human += 1
        if dog_age >= 24:
            dog_to_human += 1
            if dog_age >= 29:
                dog_to_human += 1
                dog_age -= 29
                dog_to_human += dog_age // 5
    return [cat_to_human, dog_to_human]
