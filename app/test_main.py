import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            0, 0, [0, 0],
            id="animal age is 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="animal age less than 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="animal age is more 15 and less 23"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="animal age is more 15 and less 23"
        ),
        pytest.param(
            23.9, 23.1, [1, 1],
            id="animal age with remainder"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="animal age is more 23"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="after 27 cat and dog age should be different"
        ),
        pytest.param(
            137, 111, [30, 19],
            id="age is more big"
        ),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
