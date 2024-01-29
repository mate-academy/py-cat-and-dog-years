import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result, test_id",
    [
        (
            14,
            14,
            [0, 0],
            "age between 0 and 14 should equal 0"
        ),
        (
            23,
            23,
            [1, 1],
            "age between 15 and 23 should equal 1"
        ),
        (
            27,
            27,
            [2, 2],
            "age between 24 and 27 should equal 2"
        ),
        (
            28,
            28,
            [3, 2],
            "age older than 28 should depend on the type of animal"
        ),
        (
            100,
            100,
            [21, 17],
            "age older than 28 should depend on the type of animal"
        ),
        (
            -5,
            -10,
            [0, 0],
            "negative age is impossible, should return 0"
        )
    ]
)
def test_convert_age(cat_age: int,
                     dog_age: int,
                     result: list,
                     test_id: str) -> None:
    assert get_human_age(cat_age, dog_age) == result, test_id


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
