from typing import Tuple


def get_human_age(cat_age: int, dog_age: int) -> Tuple[int, int]:
    human_age1 = 0
    if cat_age < 15:
        human_age1 = 0
    elif cat_age < 24:
        human_age1 = 1
    else:
        human_age1 = 2
        additional_years = (cat_age - 24) // 4
        human_age1 += additional_years

    human_age2 = 0
    if dog_age < 15:
        human_age2 = 0
    elif dog_age < 24:
        human_age2 = 1
    else:
        human_age2 = 2
        additional_years = (dog_age - 24) // 5
        human_age2 += additional_years

    return human_age1, human_age2
