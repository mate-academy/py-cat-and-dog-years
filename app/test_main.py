import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_years, dog_years, expected", [
    pytest.param(0, 0, [0, 0], id="Both 0 years"),
    pytest.param(14, 14, [0, 0], id="Both 14 years"),
    pytest.param(15, 15, [1, 1], id="Both 15 years"),
    pytest.param(23, 23, [1, 1], id="Both 23 years"),
    pytest.param(24, 24, [2, 2], id="Both 24 years"),
    pytest.param(27, 27, [2, 2], id="Both 27 years"),
    pytest.param(100, 100, [21, 17], id="Both 100 years"),
    pytest.param(8000000000,
                 15000, [1999999996, 2997],
                 id="Cag - 8.000.000.000, Dog - 15000 years"),
    pytest.param(15000,
                 8000000000,
                 [3746, 1599999997],
                 id="Cag - 15000, Dog - 8.000.000.000 years"),
    pytest.param(40000000000,
                 40000000000, [9999999996, 7999999997],
                 id="Both 40.000.000.000 years"),
    pytest.param(-1000, -1000, [0, 0], id="Both -1000 years"),
    pytest.param(-15, 29, [0, 3], id="Cag - -15, Dog - 29 years"),
    pytest.param(55, -88, [9, 0], id="Cag - 55, Dog - -88 years"),
])
def test_get_human_age(cat_years: int,
                       dog_years: int,
                       expected: list[int]) -> None:
    assert get_human_age(cat_years, dog_years) == expected


@pytest.mark.parametrize("cat_years, dog_years", [
    pytest.param("ten", 10, id="Cat years as string"),
    pytest.param(10, "ten", id="Dog years as string"),
    pytest.param(None, 10, id="Cat years as None"),
    pytest.param(10, {20}, id="Dog years as Dict"),
])
def test_get_human_age_type_error(cat_years: int,
                                  dog_years: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
