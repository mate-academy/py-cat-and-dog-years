def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    def convert(age: int, first: int, second: int, each: int) -> int:
        if age < first:
            return 0
        elif age < first + second:
            return 1
        else:
            return 2 + (age - first - second) // each

    cat = convert(cat_age, 15, 9, 4)
    dog = convert(dog_age, 15, 9, 5)
    return [cat, dog]
