import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,excepted_result",
    [
        pytest.param(0, 0, [0, 0], id="test should return zero age human if age animal zero"),
        pytest.param(14, 14, [0, 0], id="test should return zero age human if animal is young"),
        pytest.param(15, 15, [1, 1], id="test should return one years"),
        pytest.param(23, 23, [1, 1], id="test should return one years"),
        pytest.param(24, 24, [2, 2], id="test should return two years"),
        pytest.param(27, 27, [2, 2], id="test should return two years"),
        pytest.param(28, 28, [3, 2], id="test should return different years"),
        pytest.param(100, 100, [21, 17], id="test should return different years")
    ]
)
def test_should_check_the_correctness_of_the_conversion_to_human_years(
        cat_age: int,
        dog_age: int,
        excepted_result: list) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == excepted_result