import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "should return zeros for 15 cat and dog years.",
        "should return one for 15 cat and dog years.",
        "should return two for 24 cat and dog years.",
        "should return two for 27 cat and 28 dog years.",
        "should return correct human ages for 28 cat and dog",
        "should return correct human ages for 100 cat and dog"
    ]
)
def test_valid_inputs(
    cat_age: int,
    dog_age: int,
    expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        (23, -34, ValueError),
        (124124, 22551241, ValueError),
        ("21", 32, TypeError)
    ],
    ids=[
        "should raise error when age is negative",
        "test should raise error when age is very large",
        "should raise error if age is string"
    ]
)
def test_invalid_inputs(
    cat_age: int,
    dog_age: int,
    expected_error: ValueError | TypeError
) -> None:
    with pytest.raises(expected_error):
        assert get_human_age(cat_age, dog_age)
