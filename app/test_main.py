import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="14 cat/dog years should convert into 0 human age"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 cat/dog years should convert into 1 human age"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 cat/dog years should convert into 1 human age"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24 cat/dog years should convert into 2 human age"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="27/28 cat/dog years should convert into 2 human age"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28/29 cat/dog years should convert into 3 human age"
        )
    ]
)
def test_correct_convert_animal_age_to_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
