def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be an integer")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

    cat_human = 0
    dog_human = 0

    if cat_age >= 15:
        cat_human += 1
    if cat_age >= 24:
        cat_human += 1
    if cat_age >= 28:
        cat_human += (cat_age - 24) // 4

    if dog_age >= 15:
        dog_human += 1
    if dog_age >= 24:
        dog_human += 1
    if dog_age >= 29:
        dog_human += (dog_age - 24) // 5

    return [cat_human, dog_human]
