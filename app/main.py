def get_human_age(cat_age: int, dog_age: int) -> list:
    def calculate_human_years(age: int, multiplier: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        # Start with 2 years (for the first 24 pet years)
        # then add 1 year for every 'multiplier' years after that
        return 2 + (age - 24) // multiplier

    cat_human_age = calculate_human_years(cat_age, 4)
    dog_human_age = calculate_human_years(dog_age, 5)

    return [cat_human_age, dog_human_age]
