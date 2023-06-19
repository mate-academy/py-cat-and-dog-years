import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,result",
    [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
    ]
)
def test_get_human_age(
        cat_years: int,
        dog_years: int,
        result: int
) -> None:
    assert get_human_age(cat_years, dog_years) == result


def test_get_human_age_with_incorrect_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("bob", False)
