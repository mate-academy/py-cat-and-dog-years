def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_step = 4
    dog_step = 5

    def calculate(age: int, step: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1

        return 2 + (age - 24) // step

    cat_human = calculate(cat_age, cat_step)
    dog_human = calculate(dog_age, dog_step)

    return [cat_human, dog_human]
