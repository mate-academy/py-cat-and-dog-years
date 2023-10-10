from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, output", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 20, [3, 1]),
    (100, 100, [21, 17]),
    (-10, -10, [0, 0])
])
def test_animal_age_with_input_data(
        cat_age: int,
        dog_age: int,
        output: int
) -> None:
    assert get_human_age(cat_age, dog_age) == output


@pytest.mark.parametrize("cat_age, dog_age, error", [
    ("10", "10", TypeError),
    ([10], [10], TypeError),
    ({10: ""}, {10: ""}, TypeError),
])
def test_animal_age_with_incorrect_data_type(
        cat_age: str or list or dict,
        dog_age: str or list or dict,
        error: Exception
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
