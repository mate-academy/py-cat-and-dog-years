def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0:
        cat_age = 0
    if dog_age < 0:
        dog_age = 0

    def convert(age: int, first: int, second: int, each: int) -> int:
        if age < first:
            return 0
        if age < first + second:
            return 1
        return 2 + (age - first - second) // each

    cat_human: int = convert(cat_age, 15, 9, 4)
    dog_human: int = convert(dog_age, 15, 9, 5)

    return [cat_human, dog_human]
