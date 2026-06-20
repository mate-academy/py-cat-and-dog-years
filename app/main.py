def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    if cat_age < 0 or dog_age < 0:
        raise ValueError

    if cat_age < 15:
        human_cat_age = 0
    elif cat_age < 24:
        human_cat_age = 1
    else:
        human_cat_age = 2 + ((cat_age - 24) // 4)

    if dog_age < 15:
        human_dog_age = 0
    elif dog_age < 24:
        human_dog_age = 1
    else:
        human_dog_age = 2 + ((dog_age - 24) // 5)

    return [human_cat_age, human_dog_age]
