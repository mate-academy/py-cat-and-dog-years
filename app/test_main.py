import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="check_that_0_years_age_is_0"),
        pytest.param(14, 14, [0, 0], id="check_that_before_15_years_age_is_0"),
        pytest.param(15, 15, [1, 1], id="check_that_15_years_age_is_1"),
        pytest.param(23, 23, [1, 1], id="check_that_before_24_years_age_is_1"),
        pytest.param(24, 24, [2, 2], id="check_that_24_years_age_is_2"),
        pytest.param(27, 27, [2, 2], id="check_that_27, 27_years_age_is_2"),
        pytest.param(28, 28, [3, 2], id="check_that_28, 28_years_age_is_2"),
        pytest.param(100, 100, [21, 17], id="years_calculation_after_24"),
        pytest.param(-24, -24, [0, 0], id="check_negative_int"),
    ]
)
def test_check_correct_calculating(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "calculating is not correct"


def test_raises_type_error_for_non_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("24", "24")
