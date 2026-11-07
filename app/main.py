def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    for age in (cat_age, dog_age):
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError("Age must be an integer")
        if age < 0:
            raise ValueError("Age must not be negative")

    def convert(age: int, step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // step

    return [convert(cat_age, 4), convert(dog_age, 5)]
