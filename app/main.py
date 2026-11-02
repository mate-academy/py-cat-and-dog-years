def convert_to_human(
    age: int,
    first_year: int,
    second_year: int,
    each_year: int
) -> int:
    if (not isinstance(age, int) or isinstance(age, bool)
            or not isinstance(first_year, int)
            or isinstance(first_year, bool)
            or not isinstance(second_year, int)
            or isinstance(second_year, bool)
            or not isinstance(each_year, int)
            or isinstance(each_year, bool)):
        raise TypeError("All arguments must be integers")

    age = max(0, age)

    if age < first_year:
        return 0
    elif age < first_year + second_year:
        return 1

    return 2 + (age - first_year - second_year) // each_year


def get_human_age(cat_age: int, dog_age: int) -> list:
    if (not isinstance(cat_age, int) or isinstance(cat_age, bool)
            or not isinstance(dog_age, int)
            or isinstance(dog_age, bool)):
        raise TypeError("Age must be an integer")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age must be greater than or equal to 0")

    cat_age = max(0, cat_age)
    dog_age = max(0, dog_age)

    cat_human_age = convert_to_human(
        cat_age, first_year=15, second_year=9, each_year=4
    )
    dog_human_age = convert_to_human(
        dog_age, first_year=15, second_year=9, each_year=5
    )

    return [cat_human_age, dog_human_age]
