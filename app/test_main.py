import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, output", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 20, [3, 1]),
    (100, 100, [21, 17]),
    (-10, -10, [0, 0]),
    (5, 25, [0, 2]),
    (20, 1, [1, 0])
])
def test_animal_age_with_input_data(
        cat_age: int,
        dog_age: int,
        output: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == output


@pytest.mark.parametrize("cat_age, dog_age, error", [
    ("10", "10", TypeError),
    ([10], [10], TypeError),
    ({10: ""}, {10: ""}, TypeError),
])
def test_animal_age_with_incorrect_data_type(
        cat_age: any,
        dog_age: any,
        error: Exception
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
