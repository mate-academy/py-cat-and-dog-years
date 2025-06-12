def convert_to_human(pet_age: int, first: int, second: int, each: int) -> int:
    if pet_age < first:
        return 0
    elif pet_age < first + second:
        return 1
    return 2 + (pet_age - first - second) // each


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    return [
        convert_to_human(cat_age, 15, 9, 4),
        convert_to_human(dog_age, 15, 9, 5),
    ]
