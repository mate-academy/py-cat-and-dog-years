def get_human_age(cat_age: int, dog_age: int) -> list | Exception:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    if cat_age < 0 or dog_age < 0:
        raise ValueError

    cat_to_human_age = 0
    if cat_age in range(0, 15):
        cat_to_human_age = 0
    if cat_age in range(15, 24):
        cat_to_human_age = 1
    if cat_age > 23:
        cat_to_human_age = 2 + (cat_age - 24) // 4

    dog_to_human_age = 0
    if dog_age in range(0, 15):
        dog_to_human_age = 0
    if dog_age in range(15, 24):
        dog_to_human_age = 1
    if dog_age > 23:
        dog_to_human_age = 2 + (dog_age - 24) // 5

    return [cat_to_human_age, dog_to_human_age]
