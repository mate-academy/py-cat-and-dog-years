from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_list",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-100, -100, [0, 0]),
    ]
)
def test_should_return_correct_list(
        cat_age: int,
        dog_age: int,
        human_age_list: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_list


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "32",
            "27",
            TypeError,
            id="should raise TypeError if ages not integer"
        ),
    ]
)
def test_raising_type_error_correctly(
        cat_age: str,
        dog_age: str,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
