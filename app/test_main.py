from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (15, 24, [1, 2]),
        (28, 36, [3, 4]),
        (48, 56, [8, 8]),
        (64, 72, [12, 11])
    ])
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
