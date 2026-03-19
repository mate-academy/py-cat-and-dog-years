import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
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
        "check_age_0",
        "check_age_14",
        "check_age_15",
        "check_age_23",
        "check_age_24",
        "check_age_27",
        "check_age_28",
        "check_age_100",
    ]
)
def test_check_age(cat_age: int, dog_age: int, human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_errors",
    [
        pytest.param(-5, 4, ValueError, id="data is negative"),
        pytest.param(15, -4, ValueError, id="data is negative"),
        pytest.param(2.5, 10, TypeError, id="data type is incorrect"),
        pytest.param(2, 3.2, TypeError, id="data type is incorrect"),
        pytest.param(2, "3", TypeError, id="data type is incorrect"),
        pytest.param("2", 3, TypeError, id="data type is incorrect"),
    ]
)
def test_check_expected_errors(
    cat_age: int,
    dog_age: int,
    expected_errors: type[Exception]
) -> None:
    with pytest.raises(expected_errors):
        get_human_age(cat_age, dog_age)
