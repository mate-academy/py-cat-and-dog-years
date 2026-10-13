def get_human_age(cat_age: int , dog_age: int) -> list:
    ages = (cat_age, dog_age)

    if any(type(age) is not int for age in ages):
        raise TypeError("Ages must be integers")

    if any(age < 0 for age in ages):
        raise ValueError("Ages cannot be negative")

    if cat_age < 15:
        cat_human_age = 0
    elif cat_age < 24:
        cat_human_age = 1
    else:
        cat_human_age = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        dog_human_age = 0
    elif dog_age < 24:
        dog_human_age = 1
    else:
        dog_human_age = 2 + (dog_age - 24) // 5

    return [cat_human_age, dog_human_age]
