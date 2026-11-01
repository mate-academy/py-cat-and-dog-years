import pytest
import app.main as main

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
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
)
def test_basic_examples(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, ValueError),
        (15.5, 21.2, TypeError),   # float
        ("15", "21", TypeError),   # str
        (None, None, TypeError),   # None
        (True, False, TypeError),  # bool
    ],
)
def test_errors(
        cat_age: float | int,
        dog_age: float | int,
        expected: type[Exception]
) -> None:
    with pytest.raises(expected):
        main.get_human_age(cat_age, dog_age)
