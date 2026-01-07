import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="test_zero_human_year_bottom_edge"),
        pytest.param(14, 14, [0, 0], id="test_zero_human_year_upper_edge"),
        pytest.param(15, 15, [1, 1], id="test_first_human_year_bottom_edge"),
        pytest.param(23, 23, [1, 1], id="test_first_human_years_upper_edge"),
        pytest.param(24, 24, [2, 2], id="test_second_human_years_bottom_edge"),
        pytest.param(27, 28, [2, 2], id="test_second_human_years_upper_edge"),
        pytest.param(28, 29, [3, 3],
                     id="test_more_than_two_human_years_bottom_edge"),
        pytest.param(100, 100, [21, 17], id="test_more_than_two_human_years"),
        pytest.param(-10, -10, [0, 0], id="test_negative_input"),
    ]
)
def test_can_convert(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_incorrect_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("str", 3.14)
