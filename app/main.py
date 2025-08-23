def cat_years_to_human(cat_years: int) -> int:
    if not isinstance(cat_years, int) or cat_years < 0:
        raise ValueError("Cat years must be a non-negative integer")
    if cat_years == 0:
        return 0
    elif cat_years == 1:
        return 15
    elif cat_years == 2:
        return 24
    else:
        return 24 + (cat_years - 2) * 4


def dog_years_to_human(dog_years: int) -> int:
    if not isinstance(dog_years, int) or dog_years < 0:
        raise ValueError("Dog years must be a non-negative integer")
    if dog_years == 0:
        return 0
    elif dog_years == 1:
        return 15
    elif dog_years == 2:
        return 24
    else:
        return 24 + (dog_years - 2) * 5


def get_human_age(cat_years: int, dog_years: int) -> list[int]:
    return [cat_years_to_human(cat_years), dog_years_to_human(dog_years)]
