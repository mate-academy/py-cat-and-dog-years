def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if cat_age < 0 or dog_age < 0:
        raise ValueError

    def calculate_age(age: int, divisor: int) -> int:
        if age >= 24:
            return 2 + (age - 24) // divisor
        return 1 if age >= 15 else 0

    return [
        calculate_age(cat_age, 4),
        calculate_age(dog_age, 5)
    ]
