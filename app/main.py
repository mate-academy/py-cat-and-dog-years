def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0:
        return []
    if cat_age >= 24:
        cat_age_human = 2 + ((cat_age - 24) // 4)
    elif cat_age >= 15:
        cat_age_human = 1
    else:
        cat_age_human = 0
    if dog_age >= 24:
        dog_age_human = 2 + ((dog_age - 24) // 5)
    elif dog_age >= 15:
        dog_age_human = 1
    else:
        dog_age_human = 0
    return [cat_age_human, dog_age_human]
