import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            14, 14, [0, 0], id="cat and dog is too yang"
        ),
        pytest.param(
            15, 15, [1, 1], id="cat and dog equal to one year toddler"
        ),
        pytest.param(
            27, 27, [2, 2], id="cat and dog equal to two year toddler"
        ),
        pytest.param(
            28, 28, [3, 2], id="cat is smarter than dog"
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("0", "0", id="cannot take a string"),
        pytest.param([14], [14], id="cannot take a list"),
        pytest.param((14, 14), 1, id="cannot take a tuple")
    ]
)
def test_error_in_func(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


class ImpossibleValue(Exception):
    pass


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(120, 200, id="your pets is too old!"),
        pytest.param(-3, 5, id="negative age is not possible"),
        pytest.param(0, 0, id="everybody is zero"),
    ]
)
def test_impossible_value(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ImpossibleValue):
        get_human_age(cat_age, dog_age)
