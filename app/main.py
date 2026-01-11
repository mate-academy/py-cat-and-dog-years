def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_age = 0
    dog_human_age = 0

    if cat_age > 15 and cat_age % 15 > 0:
        cat_human_age += 1
        cat_age -= 15
        if cat_age > 9 and cat_age % 9 > 0:
            cat_human_age += 1
            cat_age -= 9
            cat_human_age += cat_age // 4

    if dog_age > 15 and dog_age % 15 > 0:
        dog_human_age += 1
        dog_age -= 15
        if dog_age > 9 and dog_age % 9 > 0:
            dog_human_age += 1
            dog_age -= 9
            dog_human_age += dog_age // 5

    return [cat_human_age, dog_human_age]
