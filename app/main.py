def get_human_age(cat_age: int, dog_age: int) -> list:
    validate(cat_age, dog_age)
    cat_to_human = convert_to_human(cat_age, 15, 9, 4)
    dog_to_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(
        animal_age: int, first_year: int, second_year: int, each_year: int
) -> int:
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year


def validate(cat_age: int, dog_age: int) -> None:
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Value must be >= 0")
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Invalid type")
    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError("Invalid type")


print(get_human_age(40, 50))
