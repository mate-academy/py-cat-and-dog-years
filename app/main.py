def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """Convert cat and dog ages (in pet years) to human years."""

    def cat_to_human(age: int) -> int:
        if age < 0:
            return 0
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // 4

    def dog_to_human(age: int) -> int:
        if age < 0:
            return 0
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // 5

    return [cat_to_human(cat_age), dog_to_human(dog_age)]
