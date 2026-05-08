def get_human_age(cat_age: int, dog_age: int) -> list:

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    def calc_age(age: int, yearly_step: int) -> int:
        if age < 15:
            return 0

        if age < 24:
            return 1

        return 2 + (age - 24) // yearly_step

    return [
        calc_age(cat_age, 4),
        calc_age(dog_age, 5),
    ]
