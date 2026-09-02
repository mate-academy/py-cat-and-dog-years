def get_human_age(cat_age: int, dog_age: int) -> list:
    for age, name in [(cat_age, "cat_age"), (dog_age, "dog_age")]:
        if isinstance(age, bool) or not isinstance(age, int):
            raise TypeError(f"{name} must be an int, got {type(age).__name__}")
        if age < 0:
            raise ValueError(f"{name} must be non-negative, got {age}")

    def convert(age: int, step_after_24: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // step_after_24

    return [convert(cat_age, 4), convert(dog_age, 5)]
