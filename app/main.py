def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def calculate_cat_age(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // 4

    def calculate_dog_age(age: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // 5

    return [calculate_cat_age(cat_age), calculate_dog_age(dog_age)]
