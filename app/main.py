def get_human_age(cat_age: int, dog_age: int) -> list:
    human_age_cat = 0
    human_age_dog = 0

    if 15 <= cat_age < 24:
        human_age_cat = 1
    elif cat_age >= 24:
        human_age_cat = 2 + (cat_age - 24) // 4

    if 15 <= dog_age < 24:
        human_age_dog = 1
    elif dog_age >= 24:
        human_age_dog = 2 + (dog_age - 24) // 5

    return [human_age_cat, human_age_dog]
