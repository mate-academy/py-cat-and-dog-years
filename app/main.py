def _convert_age(age: int, years_per_human_year: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1

    return 2 + (age - 24) // years_per_human_year


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    return [
        _convert_age(cat_age, 4),
        _convert_age(dog_age, 5),
    ]
