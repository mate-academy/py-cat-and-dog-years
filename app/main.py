def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age cannot be negative")

    def convert_to_human(animal_age: int, first_year: int, step: int) -> int:
        if animal_age == 0:
            return 0
        elif animal_age < first_year:
            return 0
        elif animal_age < first_year + 9:
            return 1
        else:
            extra = (animal_age - (first_year + 9)) // step
            return 2 + extra

    cat_human = convert_to_human(cat_age, 15, 4)
    dog_human = convert_to_human(dog_age, 15, 5)
    return [cat_human, dog_human]
