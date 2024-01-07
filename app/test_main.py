import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (54, 54, [9, 8]),
        (100, 100, [21, 17]),
        (-15, 1522, [0, 301])
    ],
    ids=[
        "with zeros",
        "with less 15 years",
        "with 15 years",
        "with 23 years",
        "with 24 years",
        "with 27 years",
        "with 28 years",
        "with 54 years",
        "with 100 years",
        "with unrealistic data"

    ],
)
def test_get_human_age(cat_age: int, dog_age: int, human_ages: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_ages
    ), f"Human's ages {human_ages} should be equal [{cat_age, dog_age}]"


def test_get_human_age_with_non_integers_values() -> None:
    with pytest.raises(TypeError):
        get_human_age("14", 14)

    with pytest.raises(TypeError):
        get_human_age(14, "14")
