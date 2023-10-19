import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (-23, 23, [0, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (100, 100, [21, 17])
    ]
)
def test_human_age_by_cat_and_dog_age(cat_age: int,
                                      dog_age: int,
                                      result: list) -> None:

    assert (get_human_age(cat_age, dog_age) == result), \
        f"should convert into {result} human age"


def test_type_of_cat_arg() -> None:
    with pytest.raises(TypeError):
        get_human_age("28", 28)


def test_type_of_dog_arg() -> None:
    with pytest.raises(TypeError):
        get_human_age(28, "28")
