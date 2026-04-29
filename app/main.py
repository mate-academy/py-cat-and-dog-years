def get_human_age(cat_age: int, dog_age: int) -> list:
    human_age = [0, 0]
    if 15 <= cat_age and 15 <= dog_age:
        human_age[0] = 1
        human_age[1] = 1
    if 24 <= cat_age and 24 <= dog_age:
        human_age[0] = 2
        human_age[1] = 2
    if cat_age >= 28:
        human_age[0] += (cat_age - 24) // 4
    if dog_age >= 29:
        human_age[1] += (dog_age - 24) // 5
    return human_age
