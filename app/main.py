from math import floor


def get_human_age(cat_age: int, dog_age: int) -> list:
    human_dog_age = 0
    human_cat_age = 0
    if dog_age < 15:
        human_dog_age = 0
    elif 15 <= dog_age < 24:
        human_dog_age = 1
    elif dog_age >= 24:
        human_dog_age = 2 + floor((dog_age - 24) / 5)
    if cat_age < 15:
        human_cat_age = 0
    elif 15 <= cat_age < 24:
        human_cat_age = 1
    elif cat_age >= 24:
        human_cat_age = 2 + floor((cat_age - 24) / 4)

    return [human_cat_age, human_dog_age]
