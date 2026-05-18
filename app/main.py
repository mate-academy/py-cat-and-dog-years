def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 15 :
        cat_in_human_age = 0
    elif cat_age < 24 :
        cat_in_human_age = 1
    else:
        cat_in_human_age = 2 + (cat_age - 24) // 4
    if dog_age < 15 :
        dog_in_human_age = 0
    elif dog_age < 24 :
        dog_in_human_age = 1
    else:
        dog_in_human_age = 2 + (dog_age - 24) // 5
    return [cat_in_human_age, dog_in_human_age]
