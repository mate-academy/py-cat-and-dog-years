import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "age, result_cat, result_dog",
    [
        (0, 0, 0),
        (14, 0, 0),
        (15, 1, 1),
        (23, 1, 1),
        (24, 2, 2),
        (27, 2, 2),
        (28, 3, 2),
        (29, 3, 3),
        (31, 3, 3),
        (32, 4, 3),
        (33, 4, 3),
        (34, 4, 4),
        (36, 5, 4),
        (37, 5, 4),
        (38, 5, 4),
        (39, 5, 5),
        (40, 6, 5),
        (100, 21, 17)
    ]
)
def test_can_sum(age: int, result_cat: int, result_dog: int) -> None:
    assert (
        get_human_age(age, age) == [result_cat, result_dog]
    ), f"The result from age {age} should be {[result_cat, result_dog]}"
