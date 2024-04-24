import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (26, 28, [2, 2]),
        (28, 29, [3, 3]),
        (-3, -7, [0, 0])
    ],
    ids=[
        "If cat age = 0, and dog age = 0 should return list with two zeros",
        "You should return list with two ones",
        "You should return list with two twos",
        "You should return list with two threes",
        "If function receives negative numbers, return list with two zeros",

    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_cannot_add_int_and_str() -> None:
    with pytest.raises(TypeError):
        get_human_age(2, "3"), (
            "Should return TypeError if function receives not int "
        )
