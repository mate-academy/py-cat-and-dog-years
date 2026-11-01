def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def calculate_pet_human_age(age: int, extra_step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // extra_step

    return [
        calculate_pet_human_age(cat_age, 4),
        calculate_pet_human_age(dog_age, 5),
    ]
