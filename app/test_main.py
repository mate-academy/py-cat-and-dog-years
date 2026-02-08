import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (
            0,
            0,
            [0, 0]
        ),
        (
            14,
            14,
            [0, 0]
        ),
        (
            15,
            15,
            [1, 1]
        ),
        (
            23,
            23,
            [1, 1]
        ),
        (
            24,
            24,
            [2, 2]
        ),
        (
            28,
            28,
            [3, 2]
        ),
        (
            100,
            100,
            [21, 17]
        ),
        (
            0,
            15,
            [0, 1]
        ),
        (
            27,
            27,
            [2, 2]
        )
    ]
)
def test_my_all_tests(cat_age: int,
                      dog_age: int,
                      expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error", [
        (
            -2,
            15,
            ValueError
        ),
        (
            "str",
            15,
            TypeError
        )
    ]
)
def test_should_raise_errors(cat_age: int,
                             dog_age: int,
                             expected_error: BaseException) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
