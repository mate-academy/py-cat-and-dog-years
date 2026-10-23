def get_human_age(cat_age: int, dog_age: int) -> list:

    cat_human_age = 0
    dog_human_age = 0

    if 15 <= cat_age <= 23:
        cat_human_age = 1
    elif cat_age >= 24:
        cat_age -= 24
        divided = cat_age // 4
        cat_human_age += 2 + divided

    if 15 <= dog_age <= 23:
        dog_human_age = 1
    elif dog_age >= 24:
        dog_age -= 24
        divided = dog_age // 5
        dog_human_age += 2 + divided
    return [cat_human_age, dog_human_age]
