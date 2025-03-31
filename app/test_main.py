import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result_list",
    [
        (-10, -5, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (1000000, 1000000, [249996, 199997])
    ]
)
def test_can_convert_to_human_age(
        cat_age: int,
        dog_age: int,
        result_list: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == result_list


@pytest.mark.parametrize(
    "cat_age, dog_age, result_list, expected_error",
    [
        ("10", 10, None, pytest.raises(TypeError)),
        ("Fifteen", 15, None, pytest.raises(TypeError)),
        (16, "puppy", None, pytest.raises(TypeError)),
        ("kitty", 25, None, pytest.raises(TypeError))
    ]
)
def test_human_age_convertation_raise_error(
        cat_age: int,
        dog_age: int,
        result_list: list,
        expected_error: Exception
) -> None:
    with expected_error:
        get_human_age(cat_age, dog_age)
