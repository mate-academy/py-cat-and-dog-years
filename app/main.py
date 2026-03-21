def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    def calculate_age(animal_age: int, divider: int) -> int:
        if animal_age < 15:
            return 0
        if animal_age < 24:
            return 1
        return 2 + (animal_age - 24) // divider

    return [calculate_age(cat_age, 4), calculate_age(dog_age, 5)]
