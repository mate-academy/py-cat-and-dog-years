def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if (
        not isinstance(cat_age, int)
        or not isinstance(dog_age, int)
        or isinstance(cat_age, bool)
        or isinstance(dog_age, bool)
    ):
        raise TypeError("Ages must be integers")

    cat_human = 0
    dog_human = 0

    if cat_age >= 15:
        cat_human = 1 if cat_age < 24 else 2 + (cat_age - 24) // 4

    if dog_age >= 15:
        dog_human = 1 if dog_age < 24 else 2 + (dog_age - 24) // 5

    return [cat_human, dog_human]
