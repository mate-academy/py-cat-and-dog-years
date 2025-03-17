from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "first_animal_age, second_animal_age, expected_age",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="expected have 0, 0"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="expected have 1, 1"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="expected have 2, 2"),
        pytest.param(
            28,
            28,
            [3, 2],
            id="expected have 3, 2"),
        pytest.param(
            100,
            100,
            [21, 17],
            id="expected have 21, 17")
    ]
)
def test_get_human_age(first_animal_age: int,
                       second_animal_age: int,
                       expected_age: list
                       ) -> None:
    assert get_human_age(first_animal_age, second_animal_age) == expected_age
