def convert_to_human_years(animal_age: int, years_per_step: int) -> int:
    if animal_age < 15:
        return 0
    if animal_age < 24:
        return 1
    return (animal_age - 24) // years_per_step + 2


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    return [
        convert_to_human_years(cat_age, 4),
        convert_to_human_years(dog_age, 5),
    ]
