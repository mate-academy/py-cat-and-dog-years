from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    pytest.param(
        0, 0, [0, 0],
        id="should return [0, 0] when all both are zero"
    ),
    pytest.param(
        15, 15, [1, 1],
        id="should return [1, 1] when both ages are 15"
    ),
    pytest.param(
        24, 24, [2, 2],
        id="should return [2, 2] when both ages are 24"
    ),
    pytest.param(
        28, 29, [3, 3],
        id="should return [3, 3] when ages are 28 and 29"
    ),
    pytest.param(
        28, 28, [3, 2],
        id="should return [3, 2] when both ages are 29"
    ),
])
def test_get_human_age_good(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
