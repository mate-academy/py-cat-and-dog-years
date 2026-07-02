def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    if cat_age < 15:
        cat_years = 0
    elif cat_age < 24:
        cat_years = 1
    else:
        cat_years = 2 + (cat_age - 24) // 4

    if dog_age < 15:
        dog_years = 0
    elif dog_age < 24:
        dog_years = 1
    else:
        dog_years = 2 + (dog_age - 24) // 5

    return [cat_years, dog_years]
