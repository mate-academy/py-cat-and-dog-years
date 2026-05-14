def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    if not (0 <= cat_age <= 100) or not (0 <= dog_age <= 100):
        raise ValueError

    if cat_age <= 14:
        cat_human = 0
    elif cat_age <= 23:
        cat_human = 1
    else:
        cat_human = 2 + (cat_age - 24) // 4

    if dog_age <= 14:
        dog_human = 0
    elif dog_age <= 23:
        dog_human = 1
    else:
        dog_human = 2 + (dog_age - 24) // 5

    return [cat_human, dog_human]
