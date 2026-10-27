def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 15:
        cat_human_age = 0
    elif cat_age < 24:
        cat_human_age = 1
    else:
        years = (cat_age - 24) // 4
        cat_human_age = years + 2
    if dog_age < 15:
        dog_human_age = 0
    elif dog_age < 24:
        dog_human_age = 1
    else:
        years = (dog_age - 24) // 5
        dog_human_age = years + 2
    return [cat_human_age, dog_human_age]
