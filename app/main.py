def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """
    Convert cat and dog ages to human years.
    """

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    def cat_to_human(age: int) -> int:
        if age < 15:
            return 0

        human = 1
        age -= 15

        if age < 9:
            return human

        human += 1
        age -= 9

        return human + age // 4

    def dog_to_human(age: int) -> int:
        if age < 15:
            return 0

        human = 1
        age -= 15

        if age < 9:
            return human

        human += 1
        age -= 9

        return human + age // 5

    return [cat_to_human(cat_age), dog_to_human(dog_age)]
