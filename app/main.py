import math
from typing import Tuple


def convert_to_human(
    animal_age: float,
    first_year: float,
    second_year: float,
    each_year: float,
) -> int:
    # Первый человеческий год
    if animal_age <= first_year:
        return 0

    # Второй человеческий год
    if animal_age <= first_year + second_year:
        return 1

    # Остаток после первых двух лет
    remaining = animal_age - first_year - second_year

    # Каждый полный each_year добавляет 1 год
    return 1 + math.ceil(remaining / each_year)


def get_human_age(cat_age: float, dog_age: float) -> Tuple[int, int]:
    return (
        convert_to_human(cat_age, 14, 9, 4),
        convert_to_human(dog_age, 14, 9, 5),
    )
