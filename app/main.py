def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")
    if isinstance(cat_age, bool) or isinstance(dog_age, bool):
        raise TypeError("Ages must not be booleans")

    def convert_years(age: int, extra_step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // extra_step

    cat_to_human = convert_years(cat_age, 4)
    dog_to_human = convert_years(dog_age, 5)

    return [cat_to_human, dog_to_human]
