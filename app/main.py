# app/main.py

def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """Convert cat and dog ages to human-equivalent ages."""
    if not all(isinstance(x, int) for x in (cat_age, dog_age)):
        raise TypeError("Ages must be integers.")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative.")

    # Progi wieku kota (wiek kota -> wiek człowieka)
    cat_table = [
        (0, 0), (14, 0), (15, 1), (16, 1), (23, 1),
        (24, 2), (25, 2), (27, 2), (28, 3), (29, 3),
        (34, 4), (100, 21)
    ]
    # Progi wieku psa (wiek psa -> wiek człowieka)
    dog_table = [
        (0, 0), (14, 0), (15, 1), (16, 1), (23, 1),
        (24, 1), (25, 1), (27, 2), (28, 2), (29, 3), (34, 3),
        (100, 17)
    ]

    def lookup_age(age: int, table: list[tuple[int, int]]) -> int:
        for limit, human_age in table:
            if age <= limit:
                return human_age
        return table[-1][1]

    human_cat = lookup_age(cat_age, cat_table)
    human_dog = lookup_age(dog_age, dog_table)

    return [human_cat, human_dog]
