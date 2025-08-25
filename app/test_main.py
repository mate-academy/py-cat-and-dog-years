import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        (0, 0, [0, 0]),
        (-1, 5, [0, 0]),
        (5, -1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (10**6, 10**6, [249996, 199997]),
        ("3", 4, int),
        (3.5, 4, int),
        (None, 2, int)
    ]
)
def test_should_be_output_human_age(cat: int, dog: int, expected: int) -> None:
    assert get_human_age(cat, dog) == expected


def test_should_not_be_invalid_inputs(cat: int,
                                      dog: int,
                                      expected: int) -> None:
    assert (type(cat) and type(dog)) == expected
