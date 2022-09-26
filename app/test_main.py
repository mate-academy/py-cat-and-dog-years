import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Should return zeros when cat and dog were not born"
        ),

        pytest.param(
            14, 15, [0, 1],
            id="Should return [0,1] when cat doesn`t exist and dog = 1"
        ),
        pytest.param(
            23, 24, [1, 2],
            id="Should return [1,2] when cat = 1 and dog = 2"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="Should return [2,2] when cat and dog are 27"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="Should return [3,2] when cat and dog are 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Should return [21,17] when animals still alive"
        ),
        pytest.param(
            -12, -12, [0, 0],
            id="Should return [0,0] when age negative"
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
