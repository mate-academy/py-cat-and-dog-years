def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    # --- type validation ---
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    # --- value validation ---
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    def convert_cat(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // 4

    def convert_dog(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // 5

    return [convert_cat(cat_age), convert_dog(dog_age)]