import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            0, 0, [0, 0],
            id="if animal age is 0 -> return 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="if animal age less than 15 -> return 0"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="if animal 15 <= age <= 23 -> return 1"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="check age with remainder"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="after 27 cat and dog age should be different"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="big age check"
        ),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
