def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("ages must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("ages must be non-negative")

    def dry_get_human_params(params: str, block_size: int) -> list:
        human = 0
        rem = 0
        if params >= 15:
            human += 1
            rem = params - 15
        if rem >= 9:
            human += 1
            rem2 = rem - 9
            human += rem2 // block_size
        return human

    cat_human = dry_get_human_params(cat_age, 4)
    dog_human = dry_get_human_params(dog_age, 5)
    return [cat_human, dog_human]
