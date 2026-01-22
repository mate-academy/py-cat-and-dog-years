import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,result",
    [
        pytest.param(15, 15, [1, 1],
                     id="this values give us exactly one human year"),
        pytest.param(24, 24, [2, 2],
                     id="this values give us exactly two human years"),
        pytest.param(28, 29, [3, 3],
                     id="this values give us exactly three human years"),
        pytest.param(32, 34, [4, 4],
                     id="this values give us exactly four human years"),
        pytest.param(0, 0, [0, 0],
                     id="zero animal years == zero human years"),
        pytest.param(14, 14, [0, 0],
                     id=("boundary values give us zero years, "
                         " we discard the reminder")),
        pytest.param(23, 23, [1, 1],
                     id=("boundary values give us 1 year, "
                         "we discard the reminder")),
        pytest.param(27, 28, [2, 2],
                     id=("boundary values give us  2 years, "
                         "we discard the reminder")),
        pytest.param(31, 33, [3, 3],
                     id=("boundary values give us  3 years, "
                         "we discard the reminder")),
        pytest.param(33, 35, [4, 4],
                     id=("boundary values give us 4 years, "
                         "we discard the reminder")),
        pytest.param(127, 100, [27, 17],
                     id="big years value"),
        pytest.param(-120, -1, [0, 0],
                     id="negative years values give us zero human years"),
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
