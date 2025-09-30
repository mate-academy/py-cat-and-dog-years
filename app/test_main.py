import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_returns_correct_values_and_contract(
    cat_age: int, dog_age: int, expected_human_ages: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected_human_ages
    assert isinstance(result, list), "O resultado deve ser uma lista."
    assert len(result) == 2, "A lista de resultado deve conter 2 elementos."
    assert isinstance(result[0], int), "A idade do gato deve ser um inteiro."
    assert isinstance(result[1], int), "A idade do cão deve ser um inteiro."


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("20", 30),
        (20, "30"),
        (None, 30),
        ([20], 30),
        ({20}, 30),
    ],
)
def test_get_human_age_raises_type_error_for_invalid_types(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
    ],
)
def test_get_human_age_raises_value_error_for_negative_ages(
    cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]
