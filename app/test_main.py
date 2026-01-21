import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        pytest.param(0, 0, [0, 0],
                     id="Checking ages: 0."),
        pytest.param(15, 15, [1, 1],
                     id="Checking ages: 15."),
        pytest.param(24, 24, [2, 2],
                     id="Checking ages: 24."),
        pytest.param(28, 28, [3, 2],
                     id="Checking ages: 28."),
        pytest.param(34, 34, [4, 4],
                     id="Checking ages: 34."),
        pytest.param(50, 50, [8, 7],
                     id="Checking ages: 50."),
        pytest.param(100, 100, [21, 17],
                     id="Checking ages: 100."),
        pytest.param(10_000, 10_000, [2496, 1997],
                     id="Checking ages: 10,000.")
    ]
)
def test_get_human_age_from_range_of_ages(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        pytest.param(-1, 1, [0, 0],
                     id="Checking negative cat age: -1."),
        pytest.param(-100, 100, [0, 17],
                     id="Checking negative cat age: -100."),
        pytest.param(1, -1, [0, 0],
                     id="Checking negative dog age: -1."),
        pytest.param(100, -100, [21, 0],
                     id="Checking negative dog age: -100."),
        pytest.param(-5, -5, [0, 0],
                     id="Checking negative dog and cat age: -5."),
        pytest.param(-100, -100, [0, 0],
                     id="Checking negative dog and cat age: -100.")
    ]
)
def test_get_human_age_if_animal_age_is_negative(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
