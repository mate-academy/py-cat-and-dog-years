from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age,dog_age,human_age",
                         [
                             (0, 0, [0, 0]),
                             (14, 14, [0, 0]),
                             (15, 15, [1, 1]),
                             (23, 23, [1, 1]),
                             (24, 24, [2, 2]),
                             (27, 27, [2, 2]),
                             (28, 28, [3, 2]),
                             (100, 100, [21, 17])
                         ]
                         )
def test_get_human_age(cat_age: int, dog_age: int, human_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize("cat_age,dog_age,expected_error",
                         [
                             pytest.param(-1, 0, ValueError, id="is negative"),
                             pytest.param(
                                 101,
                                 200,
                                 ValueError,
                                 id="is too big"),
                             pytest.param(1, "14", TypeError, id="wrong type"),
                         ])
def test_get_human_age_error(cat_age: int,
                             dog_age: int,
                             expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
