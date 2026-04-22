from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, human_age",
                         [
                             (14, 14, [0, 0]),
                             (23, 23, [1, 1]),
                             (28, 28, [3, 2]),
                             (0, 0, [0, 0]),
                             (-777, -3, [0, 0])
                         ],
                         ids=[
                             "Age less then 15",
                             "Age less then 24",
                             "Age is 28",
                             "Age is zero",
                             "Age is negative number"
                         ])
def test_get_human_age(cat_age, dog_age, human_age) -> None:
    assert get_human_age(cat_age, dog_age) == human_age