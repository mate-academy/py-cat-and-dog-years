import pytest

from app.main import get_human_age


def test_should_raise_error_if_age_is_not_number() -> None:
    with pytest.raises(TypeError):
        get_human_age(10, "10")


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "Negative cat/dog age should equal 0 human age",
        "Zero cat/dog age should equal 0 human age",
        "14 cat/dog age should equal 0 human age",
        "15 cat/dog age should equal 1 human age",
        "23 cat/dog should equal 1 human age",
        "24 cat/dog age should equal 2 human age",
        "27/28 cat/dog age should equal 2 human age",
        "28/29 cat/dog age should equal 3 human age",
        "100/100 cat/dog age should equal 27/17 human age",
    ],
)
def test_correct_convert_of_age(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
