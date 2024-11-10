import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        pytest.param(0, 0, [0, 0], id="test_both_ages_zero"),
        pytest.param(14, 14, [0, 0], id="test_less_then_15_years_is_0"),
        pytest.param(15, 15, [1, 1], id="test_15_years_is_one_human"),
        pytest.param(23, 23, [1, 1],
                     id="test_after_15_but_less_than_24_still_1"),
        pytest.param(24, 24, [2, 2], id="test_24_is_2_of_human_year"),
        pytest.param(28, 28, [3, 2],
                     id="test_after_24_cat_is_4_and_dog_is_5_to_1_human_year"),
        pytest.param(100, 100, [21, 17], id="test_big_numbers"),


    ]
)
def test_get_human_age(cat: int, dog: int, result: list) -> None:
    assert get_human_age(cat, dog) == result
