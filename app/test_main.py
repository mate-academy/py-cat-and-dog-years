from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_years,dog_years,result_human_years",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (24, 29, [2, 3]),
        (14, 29, [0, 3]),
        (100, 100, [21, 17]),
        pytest.param(-24, 29, [0, 3], id="negative value return zero."),
        pytest.param(10.0, 10.0, [0, 0], id="float value return 0")
    ]
)
def test_logic_return_human_years(
    cat_years: int,
    dog_years: int,
    result_human_years: list
) -> None:

    assert get_human_age(cat_years, dog_years) == result_human_years


def test_input_type() -> None:
    with pytest.raises(TypeError):
        # just input type int are accepted
        get_human_age([10], 10)
        get_human_age("10", 10)
        get_human_age({10}, 10)
