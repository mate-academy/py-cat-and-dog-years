def get_human_age(cat_age: int, dog_age: int) -> list:
    human_age_cat = 0
    if cat_age >= 15:
        human_age_cat += 1
    if cat_age >= 24:
        human_age_cat += 1
    if cat_age > 24:
        human_age_cat += (cat_age - 20) // 4

    human_age_dog = 0
    if dog_age >= 15:
        human_age_dog += 1
    if dog_age >= 24:
        human_age_dog += 1
    if dog_age > 24:
        human_age_dog += (dog_age - 20) // 5
    return [human_age_cat, human_age_dog]
