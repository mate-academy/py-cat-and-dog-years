def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_human_age = 0
    dog_human_age = 0

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Arguments must be integers")
    if cat_age > 120000 or dog_age > 120000:
        raise ValueError("Age is too high")

    if cat_age >= 15:
        cat_human_age += 1
        cat_age -= 15
        if cat_age >= 9:
            cat_human_age += 1
            cat_age -= 9
            cat_human_age += cat_age // 4

    if dog_age >= 15:
        dog_human_age += 1
        dog_age -= 15
        if dog_age >= 9:
            dog_human_age += 1
            dog_age -= 9
            dog_human_age += dog_age // 5

    return [cat_human_age, dog_human_age]
