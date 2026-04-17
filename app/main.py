def get_age(years: int, divider: int) -> int:
    if years < 15:
        return 0
    if years < 24:
        return 1
    return 2 + ((years - 24) // divider)


def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError

    elif cat_age < 0 or dog_age < 0:
        raise ValueError

    else:
        cat_in_human_years = get_age(cat_age, 4)
        dog_in_human_years = get_age(dog_age, 5)

        return [cat_in_human_years, dog_in_human_years]
