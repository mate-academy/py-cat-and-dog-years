def get_human_age(cat_age: int, dog_age: int) -> list:

    if cat_age < 15:
        human_cat_age = 0
    elif cat_age < 24:
        human_cat_age = 1
    elif cat_age < 28:
        human_cat_age = 2
    else:
        human_cat_age = ((cat_age - 24) // 4) + 2

    if dog_age < 15:
        human_dog_age = 0
    elif dog_age < 24:
        human_dog_age = 1
    elif dog_age < 29:
        human_dog_age = 2
    else:
        human_dog_age = ((cat_age - 24) // 5) + 2

    return [human_cat_age, human_dog_age]
