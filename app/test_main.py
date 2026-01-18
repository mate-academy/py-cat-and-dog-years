import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_list",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_should_return_list_animal_age_to_human_age(
        cat_age: int,
        dog_age: int,
        human_age_list: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_list


def test_should_raises_type_error_exception() -> None:
    with pytest.raises(TypeError):
        get_human_age("0", "0")
