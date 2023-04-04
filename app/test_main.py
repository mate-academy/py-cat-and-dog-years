import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,output_age",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        pytest.param(
            0, 0, [0, 0], id="should work with zeros"
        ),
        pytest.param(
            -9, -6, [0, 0], id="should work with negative numbers"
        ),
        pytest.param(
            1051, 4355, [258, 868], id="should work with large numbers"
        ),
        pytest.param(
            23.9, 24.1, [1, 2], id="should work with float numbers"
        )
    ]
)
def test_should_return_correct_age_of_animals_in_human_years(
        cat_age: int,
        dog_age: int,
        output_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == output_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("14", "14"),
        (23, "15"),
        ("32", 9)
    ]
)
def test_should_raise_right_error_when_incorrect_type(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
