import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age_result",
    [
        (9, 5, [0, 0]),
        (14, 14, [0, 0]),
        (15, 14, [1, 0]),
        (23, 23, [1, 1]),
        (23, 24, [1, 2]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        pytest.param(0, 0, [0, 0],
                     id="checks for null values in cat and dog age"),
        pytest.param(-5, -10, [0, 0],
                     id="checks for negative values in cat and dog age"),
        pytest.param(1225, 956, [302, 188],
                     id="checks for big values in cat and dog age"),
    ]
)
def test_get_human_age_function_for_integer_values(
        cat_age: int,
        dog_age: int,
        human_age_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_result
