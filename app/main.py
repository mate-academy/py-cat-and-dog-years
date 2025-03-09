def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """Преобразует возраст кота и собаки в человеческие годы.

    Аргументы:
    cat_age -- возраст кота в кошачьих годах
    dog_age -- возраст собаки в собачьих годах

    Возвращает:
    Список, где первый элемент - возраст кота в человеческих годах,
    а второй элемент - возраст собаки в человеческих годах.
    """
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    """Преобразует возраст животного в человеческие годы.

    Аргументы:
    animal_age -- возраст животного в годах животного
    first_year -- количество лет за первый год
    second_year -- количество лет за второй год
    each_year -- количество лет за каждый следующий год

    Возвращает:
    Возраст животного в человеческих годах.
    """
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year
