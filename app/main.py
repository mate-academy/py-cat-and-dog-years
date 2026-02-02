def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(age: int, first: int, second: int, each: int) -> int:
        if age < first:
            return 0
        if age < first + second:
            return 1
        return 2 + (age - first - second) // each

    cat_human = convert(cat_age, 15, 9, 4)
    dog_human = convert(dog_age, 15, 9, 5)

    return [cat_human, dog_human]
