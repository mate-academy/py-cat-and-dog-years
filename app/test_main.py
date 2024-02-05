import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_live,dog_live,expected_result",
    [
        (-5, -4, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (28, 28, [3, 2]),
    ],
    ids=[
        "should be zeros, if value is negative",
        "should be zeros, if arguments are zeros",
        "should be zeros, if arguments less than 15",
        "should be differences between ints of years in list",
    ]
)
def test(
        cat_live: int,
        dog_live: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_live, dog_live) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("0", 0, TypeError),
        (0, "0", TypeError),
    ],
    ids=[
        "should raise exception when cat age is not number",
        "should raise exception when dog age is not number"
    ]
)
def test_raise_exception_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
