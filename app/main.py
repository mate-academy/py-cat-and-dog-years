def get_human_age(cat_age: int, dog_age: int) -> list:
    def cat(cat_age: int) -> int:
        if cat_age < 15:
            return 0
        cat_age -= 15
        human = 1
        if cat_age >= 9:
            human += 1
            cat_age -= 9
            while cat_age >= 4:
                cat_age -= 4
                human += 1
        return human

    def dog(dog_age: int) -> int:
        if dog_age < 15:
            return 0
        dog_age -= 15
        human = 1
        if dog_age >= 9:
            human += 1
            dog_age -= 9
            while dog_age >= 5:
                dog_age -= 5
                human += 1
        return human
    return [cat(cat_age), dog(dog_age)]
