def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    # Validate types
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Ages must be integers")

    # Validate positive numbers
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    def calculate_human_years(animal_age: int, extra_year_rate: int) -> int:
        if animal_age < 15:
            return 0
        if animal_age < 24:
            return 1
        return 2 + (animal_age - 24) // extra_year_rate

    return [
        calculate_human_years(cat_age, 4),
        calculate_human_years(dog_age, 5)
    ]
