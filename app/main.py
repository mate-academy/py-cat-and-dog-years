def get_human_age(cat_age: int, dog_age: int) -> list:
    human_cat_age, human_dog_age = 0, 0

    if cat_age >= 15:
        human_cat_age += 1
    if cat_age >= 24:
        human_cat_age += 1
        human_cat_age += (cat_age - 24) // 4

    if dog_age >= 15:
        human_dog_age += 1
    if dog_age >= 24:
        human_dog_age += 1
        human_dog_age += (dog_age - 24) // 5

    return [human_cat_age, human_dog_age]
