def calculate_animal_age(age: int, step: int) -> int:
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // step


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    return [
        calculate_animal_age(cat_age, 4),
        calculate_animal_age(dog_age, 5)
    ]
