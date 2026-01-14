# from typing import Tuple
#
#
# def get_human_age(cat_age: int, dog_age: int) -> Tuple[int, int]:
#     if cat_age < 15:
#         human_age1 = 0
#     elif cat_age < 24:
#         human_age1 = 1
#     else:
#         human_age1 = 2
#         additional_years = (cat_age - 24) // 4
#         human_age1 += additional_years
#
#     if dog_age < 15:
#         human_age2 = 0
#     elif dog_age < 24:
#         human_age2 = 1
#     else:
#         human_age2 = 2
#         additional_years = (dog_age - 24) // 5
#         human_age2 += additional_years
#
#     return human_age1, human_age2


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert(animal_age: int, each_year: int) -> int:
        if animal_age < 15:
            return 0
        if animal_age < 24:  # 15 + 9
            return 1
        return 2 + (animal_age - 24) // each_year

    cat_human = convert(cat_age, 4)
    dog_human = convert(dog_age, 5)

    return [cat_human, dog_human]
