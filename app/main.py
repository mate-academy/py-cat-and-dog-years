def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.
    """
    def calculate_age(age: int, extra_year_threshold: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // extra_year_threshold

    cat_human_age = calculate_age(cat_age, 4)
    dog_human_age = calculate_age(dog_age, 5)

    return [cat_human_age, dog_human_age]
