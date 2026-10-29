def get_human_age(cat_age: int, dog_age: int) -> list:
    if (
            not isinstance(cat_age, int)
            or not isinstance(dog_age, int)
            or isinstance(cat_age, bool)
            or isinstance(dog_age, bool)
    ):
        raise TypeError("Ages must be integers")

    def convert_age(age: int, divisor: int) -> int:
        if age < 15:
            return 0

        if age < 24:
            return 1

        return 2 + (age - 24) // divisor

    cat_human_age = convert_age(cat_age, 4)
    dog_human_age = convert_age(dog_age, 5)

    return [cat_human_age, dog_human_age]