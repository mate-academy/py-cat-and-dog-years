from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(0, 0, [0, 0], id="cat or dog years less then 15"),
        pytest.param(15, 15, [1, 1], id="cat and dog first 15 years"),
        pytest.param(24, 24, [2, 2], id="cat and dog next 9 years"),
        pytest.param(28, 28, [3, 2], id="next every 4 cat years"),
        pytest.param(100, 100, [21, 17], id="next every 5 dog years"),
    ]
)
def test_correct_cat_and_dog_years_convert(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
