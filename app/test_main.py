from app.main import get_human_age

# write your code here
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (3, 3, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (88, 88, [18, 14]),
    ]
)
def test_can_get_human_age(cat_age: int, dog_age: int,
                           result: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"Age: cat_to_human dog_to_human of {cat_age} and {dog_age} "
        f"should be equal to {result}")


def test_can_get_human_age_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", 1)

    with pytest.raises(TypeError):
        get_human_age(3, "3")

    with pytest.raises(TypeError):
        get_human_age([3], 3)

    with pytest.raises(TypeError):
        get_human_age(3, {3})

    with pytest.raises(TypeError):
        get_human_age((3, 3))
