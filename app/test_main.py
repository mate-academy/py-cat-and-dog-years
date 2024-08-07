from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        pytest.param(
            100,
            100,
            [21, 17],
            id="should return valid list"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return zero if the animal age under fifteen"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return zero if the animal age under fifteen"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="age should be two when animal older twenty three"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat age should be three when animal older twenty four"
        )
    ]
)
def test_for_get_human_age(cat: int, dog: int, result: list[int]) -> None:
    assert get_human_age(cat, dog) == result
