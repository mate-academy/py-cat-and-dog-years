import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-5, -10, [0, 0]),
    ],
    ids=[
        "age ge 0 and le 14 should equal 0",
        "age ge 15 and le 23 should equal 1",
        "age ge 24 and le 27 should equal 2",
        "age ge 28 should depend on the type of animal",
        "age ge 28 should depend on the type of animal",
        "negative age is impossible, should return 0"
    ]
)
def test_convert_age(cat_age: int,
                     dog_age: int,
                     result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(1, "new", TypeError, id="Age must be integer value"),
    ]
)
def test_raising_errors_correctly(cat_age: int,
                                  dog_age: int,
                                  expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
