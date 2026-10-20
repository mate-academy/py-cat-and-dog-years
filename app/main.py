def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.

    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1
    """
    valid_types = (int, float)
    if (
            not isinstance(cat_age, valid_types)
            or not isinstance(dog_age, valid_types)
            or isinstance(cat_age, bool)
            or isinstance(dog_age, bool)
    ):
        raise TypeError("Ages must be numbers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    def calculate_cat_human_years(age: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // 4

    def calculate_dog_human_years(age: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // 5

    return [
        calculate_cat_human_years(cat_age),
        calculate_dog_human_years(dog_age)
    ]
