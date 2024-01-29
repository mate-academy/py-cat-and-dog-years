import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_years",
    [
        (-10, -2, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_should_correctly_convert_animals_age_to_human_age(
        cat_age: int,
        dog_age: int,
        human_years: list
) -> None:
    assert (get_human_age(cat_age, dog_age)
            == human_years), (f"{cat_age} and {dog_age} "
                              f"should be equal to {human_years}")


def test_should_raise_error_when_animal_age_is_not_an_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("34", 12)
