def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(
<<<<<<< HEAD
        animal_age: int, first_year: int, second_year: int, each_year: int
=======
        animal_age: int,
        first_year: int,
        second_year: int,
        each_year: int
>>>>>>> 6b8665f66228d3a50b61d14a169d4e3903486e84
) -> int:
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year
