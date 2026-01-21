import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (1, 1, [0, 0]),
        (23, 23, [1, 1]),
        (28, 28, [3, 2]),
        (85, 85, [17, 14]),
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (1000, 1000, [246, 197]),
    ],
)
def test_should_return_correct_values(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_dog_age,expected_error",
    [
        ("10", TypeError),
        ([10], TypeError),
        ({10}, TypeError),
    ]
)
def test_should_raise_correct_error(
        cat_dog_age: int,
        expected_error: TypeError
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_dog_age, cat_dog_age)
