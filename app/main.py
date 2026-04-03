def get_human_age(cat_age: int, dog_age: int) -> list:
    def calculate_age(age: int, extra_year_divisor: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // extra_year_divisor

    cat_human = calculate_age(cat_age, 4)
    dog_human = calculate_age(dog_age, 5)

    return [cat_human, dog_human]
