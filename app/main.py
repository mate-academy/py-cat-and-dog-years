def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert_human_age(age: int, later_step: int) -> int:
        if age < 15:
            return 0

        human_age = 1
        age -= 15

        if age >= 9:
            human_age += 1
            age -= 9

            if age > 0:
                human_age += age // later_step

        return human_age
    return [convert_human_age(cat_age, 4), convert_human_age(dog_age, 5)]
