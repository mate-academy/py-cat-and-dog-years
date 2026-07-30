def get_human_age(cat_age: int, dog_age: int) -> list:
    def convert(age: int, third_step: int) -> int:
        if age < 15:
            return 0

        human_age = 1
        age -= 15

        if age >= 9:
            human_age += 1
            age -= 9
        else:
            return human_age  # ← якщо не досягли 9 — зупиняємось

        human_age += age // third_step

        return human_age

    return [convert(cat_age, 4), convert(dog_age, 5)]
