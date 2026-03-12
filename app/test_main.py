from app.main import get_human_age


def test_years() -> None:
    cases = [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
    for cat_years, dog_years, expected in cases:
        assert get_human_age(cat_years, dog_years) == expected
