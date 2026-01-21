import pytest

from .main import get_human_age


def test_add_not_int_argument() -> None:
    with pytest.raises(TypeError):
        get_human_age(12.52, "52.12")


def test_negative_value() -> None:
    assert (get_human_age(-12, -2) == [0, 0]), \
        "The age shouldn't be negative"


def test_get_human_age_should_return_list_two_elem() -> None:
    assert isinstance(get_human_age(16, 15), list)


@pytest.mark.parametrize(
    "cat_to_human_years,dog_to_human_years,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "Cat and Dog age = 0",
        "0 <= Cat and Dog age < 15",
        "Cat and Dog age = 15",
        "15 < Cat and Dog age <= 24",
        "24 < Cat and Dog age <= 28",
        "Cat and Dog age = 29",
        "Cat and Dog age = 100"
    ]
)
def test_functionality(cat_to_human_years: int,
                       dog_to_human_years: int,
                       result: list[int, int]
                       ) -> None:
    assert (get_human_age(cat_to_human_years, dog_to_human_years) == result),\
        (f"Cat: {cat_to_human_years}, and Dog: {dog_to_human_years}"
         f" should be equal to {result}")
