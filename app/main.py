def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    def calculate_single_age(animal_age: int, step: int) -> int:
        if animal_age < 15:
            return 0
        if animal_age < 24:
            return 1
        return 2 + (animal_age - 24) // step

    return [
        calculate_single_age(cat_age, 4),
        calculate_single_age(dog_age, 5)
    ]
