def convert_to_human(
    animal_age: float,
    first_year: float,
    second_year: float,
    each_year: float
) -> int:
    if animal_age <= first_year:
        return 0

    remaining = animal_age - first_year

    if remaining <= second_year:  # ← ВАЖНО: <=
        return 1

    age = 2
    remaining -= second_year
    age += int(remaining // each_year)

    return age


def get_human_age(cat_age: float, dog_age: float) -> tuple[int, int]:
    return (
        convert_to_human(cat_age, 14, 9, 4),
        convert_to_human(dog_age, 14, 9, 4)
    )


def get_human_age(cat_age: float, dog_age: float) -> tuple[int, int]:
    """
    Возвращает возраст кошки и собаки в человеческих годах.
    """
    return (
        convert_to_human(cat_age, 14, 9, 4),
        convert_to_human(dog_age, 14, 9, 4)
    )
