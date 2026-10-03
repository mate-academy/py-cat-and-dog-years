def get_human_age(cat_age: int, dog_age: int) -> list:
    def _convert_age(age: int, extra_years_rate: int) -> int:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return 2 + (age - 24) // extra_years_rate

    return [_convert_age(cat_age, 4), _convert_age(dog_age, 5)]
