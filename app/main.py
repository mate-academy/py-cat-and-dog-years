def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("ages must be integers")
    if cat_age < 15:
        human_age_cat = 0
    elif cat_age < 24:
        human_age_cat = 1
    else:
        human_age_cat = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        human_age_dog = 0
    elif dog_age < 24:
        human_age_dog = 1
    else:
        human_age_dog = 2 + (dog_age - 24) // 5

    return [max(0, human_age_cat), max(0, human_age_dog)]
