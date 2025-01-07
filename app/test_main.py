import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result",
                         [
                             (1, 1, [0, 0]),
                             (23, 23, [1, 1]),
                             (28, 28, [3, 2]),
                             (15, 15, [1, 1]),
                             (0, 0, [0, 0]),
                             (100, 100, [21, 17])
                         ]
                         )
def test_get_human_age_valid(cat_age, dog_age, expected_result) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
