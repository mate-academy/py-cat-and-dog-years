def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert(age: int, step_after_two: int) -> int:
        if age < 15:
            return 0
        if age < 24:
            return 1
        return 2 + (age - 24) // step_after_two

    cat_human = convert(cat_age, step_after_two=4)
    dog_human = convert(dog_age, step_after_two=5)

    return [cat_human, dog_human]
