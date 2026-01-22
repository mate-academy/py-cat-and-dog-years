def convert_to_human_age(animal_age: int, each_year: int) -> int:
    if animal_age < 15:
        return 0
    if animal_age < 24:
        return 1
    return 2 + (animal_age - 24) // each_year


def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_each_year = 4
    dog_each_year = 5

    return [
        convert_to_human_age(cat_age, cat_each_year),
        convert_to_human_age(dog_age, dog_each_year),
    ]
