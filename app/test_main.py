import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "animal_age_in,human_age_out",
    [
        ([14, 14], [0, 0]),
        ([24, 24], [2, 2]),
        ([23, 23], [1, 1]),
        ([27, 28], [2, 2]),
        ([15, 15], [1, 1]),
        ([28, 29], [3, 3]),
        ([-1, 101], [0, 17])
    ]
)
def test_cat_dog_years_should_convert_into_human_age(
        animal_age_in: list,
        human_age_out: list) -> None:
    assert get_human_age(*animal_age_in) == human_age_out
