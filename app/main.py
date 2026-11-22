def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    if cat_age < 0 or dog_age < 0:
        raise ValueError

    if cat_age < 15:
        human_age = 0
    elif 15 <= cat_age <= 23:
        human_age = 1
    elif 24 <= cat_age <= 27:
        human_age = 2
    else:
        human_age = ((cat_age - 24) // 4) + 2

    if dog_age < 15:
        dog_human_age = 0
    elif 15 <= dog_age <= 23:
        dog_human_age = 1
    elif 24 <= dog_age <= 28:
        dog_human_age = 2
    else:
        dog_human_age = ((dog_age - 24) // 5) + 2
    return [human_age, dog_human_age]
