import pytest
from app.main import get_human_age, convert_to_human


@pytest.mark.parametrize(
    "animal_age,first_year,second_year,each_year,human_age", [
        (0, 10, 5, 1, 0),
        (20, 1, 1, 1, 20),
        (123, 15, 9, 5, 21),
        (-1, 15, 9, 5, 0)
    ]
)
def test_if_convert_to_human_returns_correct_value(
    animal_age: int,
    first_year: int,
    second_year: int,
    each_year: int,
    human_age: int
) -> None:
    assert (convert_to_human(
        animal_age, first_year, second_year, each_year) == human_age
    ), (f"Animal age({animal_age})"
        f" in human years should be equal to {human_age}")


@pytest.mark.parametrize(
    "cat_age,dog_age,age_list", [
        (0, 0, [0, 0]),
        (14, 15, [0, 1]),
        (24, 23, [2, 1]),
        (27, 27, [2, 2]),
        (100, 100, [21, 17]),
        (-67, -3, [0, 0])
    ]
)
def test_if_get_human_age_returns_correct_value(
    cat_age: int,
    dog_age: int,
    age_list: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == age_list
            ), (f"Cat age({cat_age}) and dog age({dog_age})"
                f" in human years should be equal to {age_list}")


def test_type_error_get_human_age() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", "3")


def test_type_error_convent_to_human() -> None:
    with pytest.raises(TypeError):
        convert_to_human("2", [3], False, {"each_year": 2})
