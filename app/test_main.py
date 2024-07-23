import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result_list, expected_error",
    [

        (-10, -5, [0, 0], None),
        (0, 0, [0, 0], None),
        (14, 14, [0, 0], None),
        (15, 15, [1, 1], None),
        (23, 23, [1, 1], None),
        (24, 24, [2, 2], None),
        (28, 28, [3, 2], None),
        (50, 60, [8, 9], None),
        (100, 100, [21, 17], None),
        (1000000, 1000000, [249996, 199997], None),
        ("10", 10, None, pytest.raises(TypeError))
    ]
)
def test_can_convert_to_human_age(
        cat_age: int,
        dog_age: int,
        result_list: list,
        expected_error: None | Exception
) -> None:
    if expected_error:
        with expected_error:
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == result_list
