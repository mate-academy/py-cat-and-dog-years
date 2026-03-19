def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.

    Rules:
    - Cat: first 15 years = 1 human yr, next 9 = +1, then every 4 = +1
    - Dog: first 15 years = 1 human yr, next 9 = +1, then every 5 = +1
    """
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Age must be an integer")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

    def calculate_years(age: int, extra_divisor: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // extra_divisor

    return [calculate_years(cat_age, 4), calculate_years(dog_age, 5)]
