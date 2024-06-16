import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_years, dog_years, expected", [
    pytest.param(0, 0, [0, 0], id="Both 0 years"),
    pytest.param(14, 14, [0, 0], id="Both 14 years"),
    pytest.param(15, 15, [1, 1], id="Both 15 years"),
    pytest.param(23, 23, [1, 1], id="Both 23 years"),
    pytest.param(24, 24, [2, 2], id="Both 24 years"),
    pytest.param(27, 27, [2, 2], id="Both 27 years"),
    pytest.param(28, 28, [3, 2], id="Both 28 years"),
    pytest.param(100, 100, [21, 17], id="Both 100 years"),
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
