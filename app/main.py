from typing import List


def convert_to_human(animal_age: int, first_year: int,
                     second_year: int, each_year: int) -> int:
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year


def get_human_age(cat_age: int, dog_age: int) -> List[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Вік повинен бути цілим числом")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Вік повинен бути додатнім числом")

    cat_human = convert_to_human(cat_age, first_year=15,
                                 second_year=9, each_year=4)
    dog_human = convert_to_human(dog_age, first_year=15,
                                 second_year=9, each_year=5)

    return [cat_human, dog_human]
