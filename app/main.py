def get_human_age(cat_age: int, dog_age: int) -> list:
    for age in (cat_age, dog_age):
        if isinstance(age, bool) or not isinstance(age, int):
            raise TypeError(
                f"Age must be an integer, got {type(age).__name__!r}"
            )

    def calculate(age: int, over_24_divider: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // over_24_divider

    return [calculate(cat_age, 4), calculate(dog_age, 5)]
