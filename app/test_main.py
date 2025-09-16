from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age,dog_age,human_age",
                         [
                             (-1, -1, [0, 0]),
                             (0, 0, [0, 0]),
                             (14, 14, [0, 0]),
                             (15, 15, [1, 1]),
                             (15, 29, [1, 3]),
                             (23, 23, [1, 1]),
                             (24, 24, [2, 2]),
                             (24, 29, [2, 3]),
                             (27, 27, [2, 2]),
                             (28, 28, [3, 2]),
                             (100, 100, [21, 17]),
                         ],
                         )
def test_animal_to_human_age(cat_age: int, dog_age: int,
                             human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
