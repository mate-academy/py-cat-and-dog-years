from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "initial_number_1, initial_number_2, expected_numbers",
    [
        (
            0,
            0,
            [0, 0]
        ),

        (
            15,
            15,
            [1, 1]
        ),

        (
            14,
            14,
            [0, 0]
        ),

        (
            24,
            24,
            [2, 2]
        ),

        (
            23,
            23,
            [1, 1]
        ),

        (
            28,
            28,
            [3, 2]
        ),

        (
            27,
            27,
            [2, 2]
        ),

        (
            28,
            29,
            [3, 3]
        ),

    ]
)
def test_human_age_transition(initial_number_1: int,
                              initial_number_2: int,
                              expected_numbers: list) -> None:
    assert get_human_age(initial_number_1,
                         initial_number_2) == expected_numbers
