import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,h_cat_age,h_dog_age",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17)
    ],
    ids=[
        "Age zero",
        "Age 14 for both",
        "Age 15 for both",
        "Age 23 for both",
        "Age 24 for both",
        "Age 27 for both",
        "Age 28 for both",
        "Age 100 for both"
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       h_cat_age: int,
                       h_dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [h_cat_age, h_dog_age]
