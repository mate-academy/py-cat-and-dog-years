def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """
    Convert cat and dog ages to human years.

    Cat years:
        - first 15 cat years → 1 human year
        - next 9 cat years → +1 human year
        - every next 4 cat years → +1 human year

    Dog years:
        - first 15 dog years → 1 human year
        - next 9 dog years → +1 human year
        - every next 5 dog years → +1 human year
    """
    # Validate inputs
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(
    animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    """
    Helper function to convert animal age to human years.
    """
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year
