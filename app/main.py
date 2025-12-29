def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be integer")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

    cat = 0 if cat_age < 15 else 1 if cat_age < 24 else 2 + (cat_age - 24) // 4
    dog = 0 if dog_age < 15 else 1 if dog_age < 24 else 2 + (dog_age - 24) // 5
    return [cat, dog]
