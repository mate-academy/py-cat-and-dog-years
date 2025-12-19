def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age must be non-negative")

    def cat_to_human_age(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return ((age - 24) // 4) + 2

    def dog_to_human_age(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return ((age - 24) // 5) + 2

    return [cat_to_human_age(cat_age), dog_to_human_age(dog_age)]
