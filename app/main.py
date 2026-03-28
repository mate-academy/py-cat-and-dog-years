def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(
        dog_age, int
    ):
        raise TypeError("Age must be a number")

    cat_human = convert_age(cat_age, 15, 9, 4)
    dog_human = convert_age(dog_age, 15, 9, 5)

    return [cat_human, dog_human]


def convert_age(
    age: int,
    first_block: int,
    second_block: int,
    block_size: int,
) -> int:
    if age < first_block:
        return 0
    if age < first_block + second_block:
        return 1

    return 2 + (age - (first_block + second_block)) // block_size
