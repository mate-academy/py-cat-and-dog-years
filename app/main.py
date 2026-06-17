from math import floor


def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError
    age_numbers = [round(cat_age), round(dog_age)]
    final_age = []
    for index, age in enumerate(age_numbers):
        if age < 15:
            final_age.append(0)
        elif 15 <= age < 24:
            final_age.append(1)
        elif age >= 24:
            if index == 0:
                cat_in_human_age = floor((age - 24) / 4) + 2
                final_age.append(cat_in_human_age)
            elif index == 1:
                dog_in_human_age = floor((age - 24) / 5) + 2
                final_age.append(dog_in_human_age)

    return final_age
