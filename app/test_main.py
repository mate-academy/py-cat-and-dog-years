import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,human",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (100, 100, [21, 17])
    ]
)
def test_turns_animal_years_into_human_years(cat, dog, human):
    assert get_human_age(cat, dog) == human, \
        "Years should be converted correctly"
