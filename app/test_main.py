import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,cat_to_human,dog_to_human",
    [
        (-2, -4, 0, 0),
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17),
    ]
)
def test_value_must_be_ok(cat_age: int, dog_age: int,
                          cat_to_human: int, dog_to_human: int) -> None:
    assert (get_human_age(cat_age, dog_age) == [cat_to_human, dog_to_human]), \
        (f"Cat age = {cat_age} must be on human {cat_to_human}, "
         f"Dog age = {dog_age} must be on human {dog_to_human}!")


def test_raising_error_correctly() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", "2")
