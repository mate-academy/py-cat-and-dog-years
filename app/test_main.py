import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,human_age",
    [
        pytest.param(
            14, 14, [0, 0],
            id="For 14 cat and dog years result should be [0, 0]"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="For 24 cat and dog years result should be [2, 2]"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="For 23 cat and dog years result should be [1, 1]"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="For 15 cat and dog years result should be [1, 1]"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="For 27 cat and 28 dog years result should be [2, 2]"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="For 28 cat and 29 dog years result should be [3, 3]"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="For 0 cat and dog years result should be [0, 0]"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="For 28 cat and dog years result should be [3, 2]"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="For 100 cat and dog years result should be [21, 17]"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="For negative cat and dog years result should be [0, 0]"
        ),
    ]
)
def test_get_human_age(
        cat_years: int,
        dog_years: int,
        human_age: list
) -> None:
    assert get_human_age(cat_years, dog_years) == human_age
