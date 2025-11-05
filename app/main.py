def convert_animal_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    if animal_age <= 0:
        return 0

    if animal_age < first_year:
        return 0
    elif animal_age < first_year + second_year:
        return 1
    else:
        remaining_animal_years = animal_age - first_year - second_year
        return 2 + remaining_animal_years // each_year


def get_human_age(cat_animal_age: int, dog_animal_age: int) -> list[int]:
    if not isinstance(cat_animal_age, int) or not isinstance(dog_animal_age, int):
        raise TypeError("Both cat_animal_age and dog_animal_age must be integers")

    cat_age = convert_animal_to_human(
        cat_animal_age, first_year=15, second_year=9, each_year=4
    )
    dog_age = convert_animal_to_human(
        dog_animal_age, first_year=15, second_year=9, each_year=5
    )
    return [cat_age, dog_age]