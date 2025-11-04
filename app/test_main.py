import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [(-1, -2, [0, 0]), (15, 15, [1, 1]), (24, 24, [2, 2]),
     (14, 14, [0, 0]), (23, 23, [1, 1]), (27, 28, [2, 2]),
     (28, 29, [3, 3])
     ]
)
def test_should_correctly_convert_to_human(
        cat_age: int, dog_age: int, expected_result: list
) -> None:

    result = get_human_age(cat_age, dog_age)
    assert result == expected_result


def test_should_raise_error_when_animal_age_is_str() -> None:
    with pytest.raises(TypeError):
        get_human_age("13", 28)
