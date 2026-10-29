def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Ages must be integers")

    def convert(age: int, divisor: int) -> int:
        if age < 15:
            return 0
        elif 15 <= age < 24:
            return 1
        else:
            return 2 + (age - 24) // divisor

    cat_human_age = convert(cat_age, 4)
    dog_human_age = convert(dog_age, 5)

    return [cat_human_age, dog_human_age]
