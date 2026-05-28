import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (-15, -24, [0, 0]),
        (150, 150, [0, 0]),
    ],
    ids=[
        "human age when animals have 0 years",
        "human age when cat and dog have 15 years",
        "human age when cat and dog have 24 years",
        "human age when cat has 28 and dog has 29 years",
        "human age when cat and dog have negative years",
        "human age when cat and dog have values > 100",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_get_human_age_correct_animal_age_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", 5)
