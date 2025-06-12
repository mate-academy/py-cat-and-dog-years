from typing import List


def convert_to_human(pet_age: int,
                     first_year: int, second_year: int,
                     each_additional_year: int) -> int:
    if pet_age == 0:
        return 0
    elif pet_age == 1:
        return first_year
    elif pet_age == 2:
        return first_year + second_year
    return first_year + second_year + (pet_age - 2) * each_additional_year


def get_human_age(cat_age: int, dog_age: int) -> List[int]:
    return [
        convert_to_human(cat_age, 15, 9, 4),  # Cat: 15, 9, then +4/year
        convert_to_human(dog_age, 15, 9, 5),  # Dog: 15, 9, then +5/year
    ]
