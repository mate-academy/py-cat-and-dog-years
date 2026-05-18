def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_age = 0
    dog_human_age = 0
    if cat_age >= 15:
        cat_human_age += 1
    if cat_age >= 24:
        cat_human_age += 1
    if cat_age > 24:
        tail = cat_age - 24
        years = tail // 4
        cat_human_age += years

    if dog_age >= 15:
        dog_human_age += 1
    if dog_age >= 24:
        dog_human_age += 1
    if dog_age > 24:
        tail = dog_age - 24
        years = tail // 5
        dog_human_age += years

    return [cat_human_age, dog_human_age]
