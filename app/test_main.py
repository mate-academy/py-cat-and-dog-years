import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_res",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-1, -5, [0, 0]),
    ]
)
def test_get_human_age_should_return_correct_results(
    cat_age: int,
    dog_age: int,
    expected_res: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_res


def test_should_raise_type_error_for_invalid_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("20", 10)
    with pytest.raises(TypeError):
        get_human_age(10, "20")
