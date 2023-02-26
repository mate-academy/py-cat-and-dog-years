import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,result",
    [
        pytest.param(15, 15, [1, 1], id="exactly one year"),
        pytest.param(24, 24, [2, 2], id="exactly two years"),
        pytest.param(28, 29, [3, 3], id="exactly three years"),
        pytest.param(32, 34, [4, 4], id="exactly four years"),
        pytest.param(0, 0, [0, 0], id="zero years"),
        pytest.param(7, 14, [0, 0], id="zero years - we discard the reminder"),
        pytest.param(15, 20, [1, 1], id="1 year, we discard the reminder"),
        pytest.param(27, 25, [2, 2], id="2 years, we discard the reminder"),
        pytest.param(29, 33, [3, 3], id="3 years, we discard the reminder"),
        pytest.param(33, 35, [4, 4], id="4 years, we discard the reminder"),
        pytest.param(127, 100, [27, 17], id="big years value"),
        pytest.param(-120, -1, [0, 0], id="negative years"),
        pytest.param(1234567890, 987654321,
                     [308641968, 197530861], id="large numbers"),

    ]
)
def test_convert_animal_years_to_human(cat_years: int,
                                       dog_years: int,
                                       result: list) -> None:
    assert get_human_age(cat_years, dog_years) == result, (
        (f"{cat_years} cat years and {dog_years} dog years "
         f"are equal to {result} human years")
    )


def test_raise_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("-122", None)
