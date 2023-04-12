from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (-5, 1, [0, 0]),
    (5, -1, [0, 0]),
    (12, 14, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (28, 28, [3, 2]),
    (16, 29, [1, 3])
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_raise_error_if_input_data_type_wrong() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat_age", 25)

    with pytest.raises(TypeError):
        get_human_age(98, "dog_age")
