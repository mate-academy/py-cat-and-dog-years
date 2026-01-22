from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 27, [3, 2]),
        (100, 100, [21, 17]),
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (-1, -1, [0, 0])
    ]
)
def test_get_result(cat_age: int, dog_age: int, result: list[str]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    )


def test_incorrect_data() -> None:
    with pytest.raises(TypeError):
        get_human_age(2, "3")
