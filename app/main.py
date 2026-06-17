def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")

    def convert(age: int, each_year: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // each_year

    return [convert(cat_age, 4), convert(dog_age, 5)]
