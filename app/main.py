def get_human_age(cat_years: float, dog_years: float) -> list[int]:
    """
    Converts cat and dog years to human years.
    """
    cat_human = convert_to_human(cat_years, 15, 9, 4)
    dog_human = convert_to_human(dog_years, 15, 9, 5)
    return [cat_human, dog_human]


def convert_to_human(years: float, first: float, second: float, each: float) -> int:
    """
    Converts given years to human years using provided rules.
    """
    if years < first:
        return 0
    elif years < first + second:
        return 1
    else:
        return int((years - first - second) // each + 2)
