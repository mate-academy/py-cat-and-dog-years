def get_human_age(cat_age: int, dog_age: int) -> list:
    return [
        convert_to_human_age(cat_age, 4),
        convert_to_human_age(dog_age, 5),
    ]


def convert_to_human_age(age: int, years_per_human_year: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1

    return 2 + (age - 24) // years_per_human_year
