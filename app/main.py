def convert_to_human(
    animal_age: float,
    first_year: float,
    second_year: float,
    each_year: float
) -> int:
    if animal_age <= first_year:
        return 0

    remaining = animal_age - first_year

    if remaining <= second_year:  # ← ВАЖНО: <=
        return 1

    age = 2
    remaining -= second_year
    age += int(remaining // each_year)

    return age


def get_human_age(cat_age: float, dog_age: float) -> tuple[int, int]:
    def convert(age: float) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        elif age < 28:
            return 2
        else:
            return 3

    return convert(cat_age), convert(dog_age)