import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
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
        "0 cat/dog years should convert into 0 human age.",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27 cat/dog years should convert into 2 human age.",
        "28 cat years should convert into 3 human age, and dog years to 2.",
        "100 cat/dog years should convert into 21 and 17 human ages.",
    ]
)
def test_get_human_age_returns_correct_values(
        cat_age: int,
        dog_age: int,
        expected: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected, (
        f"Expected human age for cat age {cat_age} "
        f"and dog age {dog_age} should be {expected}, "
        f"but got {get_human_age(cat_age, dog_age)}."
    )


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_exception",
    [
        # negative values
        (-1, -1, ValueError),
        (-10, 0, ValueError),
        (0, -5, ValueError),

        # out of range values
        (101, 101, ValueError),
        (150, 200, ValueError),
        (120, 50, ValueError),

        # Invalid type inputs
        ("10", "5", TypeError),
        (None, None, TypeError),
        ([], [], TypeError),
        ({}, {}, TypeError),
    ],
    ids=[
        "Negative ages should raise ValueError (-1, -1)",
        "Negative and zero age should raise ValueError (-10, 0)",
        "Zero and negative age should raise ValueError (0, -5)",

        "Ages over 100 should raise ValueError (101, 101)",
        "Very high ages should raise ValueError (150, 200)",
        "Out of range ages should raise ValueError (120, 50)",

        "String input should raise TypeError ('10', '5')",
        "None input should raise TypeError (None, None)",
        "List input should raise TypeError ([], [])",
        "Dictionary input should raise TypeError ({} , {})"
    ]
)
def test_get_human_age_raises_exceptions(
        cat_age: any,
        dog_age: any,
        expected_exception: ValueError | TypeError
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
