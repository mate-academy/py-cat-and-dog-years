import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_output",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17])

    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_output: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_output


def test_get_human_age_should_raise_type_error_for_invalid_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)
