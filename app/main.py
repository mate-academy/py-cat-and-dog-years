def get_human_age(cat_age: int, dog_age: int) -> list:
    return [
        convert_to_human_age(cat_age, 4),
        convert_to_human_age(dog_age, 5),
    ]


def convert_to_human_age(animal_age: int, extra_year_step: int) -> int:
    if animal_age < 15:
        return 0
    if animal_age < 24:
        return 1
    return (animal_age - 24) // extra_year_step + 2
