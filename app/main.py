def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert(animal_age: int, each_year: int) -> int:
        if animal_age < 15:
            return 0
        if animal_age < 24:  # 15 + 9
            return 1
        return 2 + (animal_age - 24) // each_year

    cat_human = convert(cat_age, 4)
    dog_human = convert(dog_age, 5)

    return [cat_human, dog_human]
