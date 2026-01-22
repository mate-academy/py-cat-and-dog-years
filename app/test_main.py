from app.main import get_human_age
import pytest


def test_type_of_the_final_object() -> None:
    assert isinstance(get_human_age(14, 14), list)


def test_length_of_the_final_list() -> None:
    assert len(get_human_age(14, 14)) == 2


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("11", "11"),
        (11, "11"),
        ("11", 11),

    ],
)
def test_should_raise_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


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
        (-2, 23, [0, 1]),
        (23, -2, [1, 0]),

    ],
)
def test_correct_counting_of_years(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
