import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,output",
    [
        (14, 8, [0, 0]),
        (15, 15, [1, 1]),
        (15, 14, [1, 0]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        pytest.param(0, 0, [0, 0], id="should work with zeros"),
        pytest.param(-2, -5, [0, 0], id="should work with negative numbers"),
        pytest.param(2.0, 3.2, [0, 0], id="should work with float numbers"),
        pytest.param(824, 1024, [202, 202], id="should work with big numbers")
    ]
)
def test_should_return_age_of_animals_in_human_years(
    cat_age: int,
    dog_age: int,
    output: int
) -> None:
    assert get_human_age(cat_age, dog_age) == output


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("14", "15"),
        (23, "25"),
        ("36", 25)
    ]
)
def test_should_raise_correct_error_when_incorrect_type(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
