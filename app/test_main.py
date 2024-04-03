from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
])
def test_should_return_animal_age_corresponds_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list) -> None:
    assert expected_result == get_human_age(cat_age, dog_age)
