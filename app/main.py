def get_human_age(cat_age: int, dog_age: int) -> list:
    result = []

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be an integer.")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative.")

    if cat_age < 15:
        result.append(0)
    elif cat_age < 24:
        result.append(1)
    else:
        result.append((cat_age - 24) // 4 + 2)

    if dog_age < 15:
        result.append(0)
    elif dog_age < 24:
        result.append(1)
    else:
        result.append((dog_age - 24) // 5 + 2)
    return result
