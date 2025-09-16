import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (14.9, 15.1, [0, 1]),
        (-5, -15, [0, 0]),
        (15000, 12500, [3746, 2497]),
    ]
)
def test_logic_of_the_function(
    cat_age: int, dog_age: int, human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_ages_are_numbers() -> None:
    with pytest.raises(TypeError):
        get_human_age("5", 10)
    with pytest.raises(TypeError):
        get_human_age(5, "10")
