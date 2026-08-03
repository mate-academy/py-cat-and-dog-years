def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be int")

    def count_years(age: int, remainder: int) -> int:
        result = 0

        if age <= 0 or age < 15:
            return result

        if age == 15:
            return 1

        result = (age - 24) // remainder + 2

        return result

    return [
        count_years(cat_age, 4),
        count_years(dog_age, 5),
    ]
