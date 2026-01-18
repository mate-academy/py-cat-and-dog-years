def get_human_age(cat_age: int, dog_age: int) -> list:
    max_age = 200
    cat_age_divider = 4
    dog_age_divider = 5

    def validate_age(age: int, animal_name: str) -> int:
        if not isinstance(age, int):
            raise TypeError(f"{animal_name} age must be a number")

        if age < 0:
            raise ValueError(f"{animal_name} age cannot be negative")

        if age > max_age:
            raise OverflowError(
                f"{animal_name} age is unrealistically large"
            )
        return age

    def calculate_age(animal_age: int, special_divider: int) -> int:
        if animal_age < 15:
            return 0
        elif animal_age < 24:
            return 1
        else:
            return 2 + ((animal_age - 24) // special_divider)

    cat_age_valid = validate_age(cat_age, "Cat")
    dog_age_valid = validate_age(dog_age, "Dog")

    return [
        calculate_age(cat_age_valid, cat_age_divider),
        calculate_age(dog_age_valid, dog_age_divider)
    ]
