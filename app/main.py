def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("ages must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("ages must be non-negative")

    human_age = [0, 0]
    if cat_age == 0 and dog_age == 0:
        return human_age

    while cat_age > 24:
        cat_age -= 4
        human_age[0] += 1

    if cat_age >= 24:
        cat_age -= 24
        human_age[0] += 2
    elif cat_age >= 15:
        cat_age -= 15
        human_age[0] += 1

    while dog_age > 24:
        dog_age -= 5
        human_age[1] += 1

    if dog_age >= 24:
        dog_age -= 24
        human_age[1] += 2
    elif dog_age >= 15:
        dog_age -= 15
        human_age[1] += 1

    return human_age
