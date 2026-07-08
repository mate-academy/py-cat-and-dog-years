def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(pet_age: int, extra_year_rate: int) -> int:
        human_age = 0
        if pet_age >= 15:
            human_age = 1
            pet_age -= 15
            if pet_age >= 9:
                human_age = 2
                pet_age -= 9
                human_age += pet_age // extra_year_rate

        return human_age

    return [convert(cat_age, 4), convert(dog_age, 5)]
