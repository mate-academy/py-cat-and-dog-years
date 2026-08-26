def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Animal age must be an integer")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Animal age cannot be negative")

    human_age = []

    if cat_age < 15:
        human_age.append(0)
    elif cat_age < 24:
        human_age.append(1)
    else:
        human_age.append(2 + (cat_age - 24) // 4)

    if dog_age < 15:
        human_age.append(0)
    elif dog_age < 24:
        human_age.append(1)
    else:
        human_age.append(2 + (dog_age - 24) // 5)

    return human_age
