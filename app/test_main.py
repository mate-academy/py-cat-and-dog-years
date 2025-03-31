import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_in_human_years,dog_in_human_years,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "Age = 0",
        "Cat & Dog age < 15",
        "Cat & Dog age = 15",
        "Cat & Dog age between 15 and 23",
        "Cat & Dog age = 24",
        "Cat & Dog age = 27",
        "Cat & Dog age = 28",
        "Cat & Dog age = 100"

    ]
)
def test_correct_functionality(cat_in_human_years: int,
                               dog_in_human_years: int,
                               result: tuple[int, int]
                               ) -> None:
    assert (
        get_human_age(cat_in_human_years, dog_in_human_years) == result
    ), (f"Cat's: {cat_in_human_years}, "
        f" and Dog's: {dog_in_human_years}"
        f" should be equal to {result}")
