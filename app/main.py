def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if (
        not isinstance(cat_age, int)
        or isinstance(cat_age, bool)
        or not isinstance(dog_age, int)
        or isinstance(dog_age, bool)
    ):
        raise TypeError

    if not (0 <= cat_age <= 100) or not (0 <= dog_age <= 100):
        raise ValueError

    if cat_age < 15:
        cat_human_age = 0
    elif cat_age < 24:
        cat_human_age = 1
    else:
        cat_human_age = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        dog_human_age = 0
    elif dog_age < 24:
        dog_human_age = 1
    else:
        dog_human_age = 2 + (dog_age - 24) // 5

    return [cat_human_age, dog_human_age]
