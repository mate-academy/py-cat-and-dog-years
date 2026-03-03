def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert_to_human(animal_years: int, step: int) -> int:
        if not isinstance(animal_years, int):
            raise TypeError("animal_years must be int")

        if animal_years < 0 or animal_years > 101:
            raise AttributeError

        if animal_years < 15:
            return 0

        if animal_years < 24:
            return 1

        human_years = 2

        human_years += (animal_years - 24) // step

        return human_years

    cat_years = convert_to_human(cat_age, 4)
    dog_years = convert_to_human(dog_age, 5)

    return [cat_years, dog_years]
