def get_human_age(cat_age: int, dog_age: int) -> list:
    def calculate(age: int, step: int) -> int:
        human_age = 0
        if age >= 15:
            human_age += 1
            age -= 15
        else:
            return human_age

        if age >= 9:
            human_age += 1
            age -= 9
        else:
            return human_age

        human_age += age // step
        return human_age

    result_cat = calculate(cat_age, 4)
    result_dog = calculate(dog_age, 5)

    return [result_cat, result_dog]
