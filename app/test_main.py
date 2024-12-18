import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (14, 14, [0, 0]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "cat and dog both 14 years",
        "cat and dog both 28 years",
        "cat and dog both 100 years"
    ]
)
def correct_func(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
