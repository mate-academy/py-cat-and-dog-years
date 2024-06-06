import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Dog/cat age 0 should return 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Dog/cat under 15 years should give 0 human year."
        ),
        pytest.param(
            23, 23, [1, 1],
            id="First 15-23 dog/cat years should give 1 human year."
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Next 9(24+) dog/cat years should give 1 more human year."
        ),
        pytest.param(
            32, 29, [4, 3],
            id="Every next 4 cat years should give 1 more human year."
        ),
        pytest.param(
            28, 34, [3, 4],
            id="Every next 5 dog years should give 1 more human year."
        ),
        pytest.param(
            -10, -10, [0, 0],
            id="Negative dog/cat age should give 0 human age."
        ),
        pytest.param(
            1000000, 1000000, [249996, 199997],
            id="Really big numbers should work correctly."
        )
    ]
)
def test_cat_dog_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
