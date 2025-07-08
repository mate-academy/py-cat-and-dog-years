def convert_to_human(age: int, thresholds: list[int],
                     step: int) -> int:
    if age < thresholds[0]:
        return 0
    elif age < thresholds[1]:
        return 1
    elif age < thresholds[2]:
        return 2
    else:
        return 3 + (age - thresholds[2]) // step


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        return [0, 0]

    cat_human = convert_to_human(cat_age, thresholds=[15, 24, 28], step=4)
    dog_human = convert_to_human(dog_age, thresholds=[15, 24, 29], step=5)

    return [cat_human, dog_human]
