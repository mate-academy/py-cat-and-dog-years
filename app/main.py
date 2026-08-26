def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, (int, float)) or not isinstance(dog_age, (int, float)):
        raise TypeError("Ages must be integers")
    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError("Ages must be integers")

    def calculate_cat_years(age: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // 4

    def calculate_dog_years(age: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // 5

    return [calculate_cat_years(cat_age), calculate_dog_years(dog_age)]
