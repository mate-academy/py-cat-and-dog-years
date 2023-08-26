import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should check zero age"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should check age under 1 human year"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should check animal age under 2 human years"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="should check animal age above 2 human years"
        ),
        pytest.param(
            -1, -9, [0, 0],
            id="should check negative ages"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should check large ages"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
