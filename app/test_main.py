import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "first_year, second_year, each_year_cat, each_year_dog",
    [
        pytest.param(0, 0, 0, 0, id="return 0 for age less than 15"),
        pytest.param(14, 14, 0, 0, id="return 0 for age less than 15"),
        pytest.param(15, 15, 1, 1, id="return 1 for age between 15 and 23"),
        pytest.param(23, 23, 1, 1, id="return 1 for age between 15 and 23"),
        pytest.param(
            24,
            24,
            2,
            2,
            id="increment human age after  24 cat years and 24 dog years"
        ),
        pytest.param(
            27,
            27,
            2,
            2,
            id="increment human age after  24 cat years and 24 dog years"
        ),
        pytest.param(
            28,
            28,
            3,
            2,
            id="increment human age after  24 cat years and 24 dog years"
        ),
        pytest.param(100, 100, 21, 17, id="correctly convert large ages"),
    ],
)
def test_ages(
    first_year: int,
    second_year: int,
    each_year_cat: int,
    each_year_dog: int
) -> None:
    assert (get_human_age(first_year, second_year)
            == [each_year_cat, each_year_dog])
