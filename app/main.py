def get_human_age(cat_age: int, dog_age: int) -> list[int]:

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be an integer")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

    if cat_age < 15:
        human_cat = 0
    elif cat_age < 24:
        human_cat = 1
    else:
        human_cat = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        human_dog = 0
    elif dog_age < 24:
        human_dog = 1
    else:
        human_dog = 2 + (dog_age - 24) // 5

    return [human_cat, human_dog]
