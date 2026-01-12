def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages must be non-negative")

    cat_human = 0
    dog_human = 0

    # --- CAT ---
    if cat_age >= 15:
        cat_human += 1
        cat_age -= 15
    else:
        return [0, 0] if dog_age < 15 else [0, None]

    if cat_age >= 9:
        cat_human += 1
        cat_age -= 9

    if cat_age > 0:
        cat_human += cat_age // 4

    # --- DOG ---
    if dog_age >= 15:
        dog_human += 1
        dog_age -= 15
    else:
        return [cat_human, 0]

    if dog_age >= 9:
        dog_human += 1
        dog_age -= 9

    if dog_age > 0:
        dog_human += dog_age // 5

    return [cat_human, dog_human]
