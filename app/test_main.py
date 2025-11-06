import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -3, [0, 0]),
    ],
    ids=[
        "get_human_age_0",
        "get_human_age_14",
        "get_human_age_15",
        "get_human_age_23",
        "get_human_age_24",
        "get_human_age_27",
        "get_human_age_28",
        "get_human_age_100",
        "get_human_age_negative",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_get_human_age_for_str() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", "3")
