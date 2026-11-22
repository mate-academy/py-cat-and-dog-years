def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age should be an integer.")
    if cat_age <= 0 or dog_age <= 0:
        raise ValueError("Age should be positive and non-zero.")

    if cat_age > 100 or dog_age > 100:
        raise ValueError("Out of range.")

    if cat_age < 15:
        human_age_for_cat = 0
    elif cat_age < 24:
        human_age_for_cat = 1
    else:
        human_age_for_cat = 2 + ((cat_age - 24) // 4)

    if dog_age < 15:
        human_age_for_dog = 0
    elif dog_age < 24:
        human_age_for_dog = 1
    else:
        human_age_for_dog = (2 + ((dog_age - 24) // 5))

    return [human_age_for_cat, human_age_for_dog]
