# main.py



def convert_to_human(years: float, first: float, second: float, each: float) -> int:
    if years < first:
        return 0
    elif years < first + second:
        return 1
    else:
        return 2 + int((years - first - second) // each)


def get_human_age(cat_years: float, dog_years: float) -> list[int]:
    cat_age = convert_to_human(cat_years, 15, 9, 4)
    dog_age = convert_to_human(dog_years, 15, 9, 5)
    return [cat_age, dog_age]
