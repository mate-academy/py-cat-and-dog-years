import pytest

from app.main import get_human_age


def test_output_should_be_list() -> None:
    assert isinstance(get_human_age(1, 1), list)


def test_output_should_be_two_elements() -> None:
    assert len(get_human_age(1, 1)) == 2


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_output",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (25, 25, [2, 2]),
        (35, 35, [4, 4]),
        (40, 40, [6, 5]),
        (50, 50, [8, 7]),
        (80, 90, [16, 15]),
        (200, 300, [46, 57])
    ]
)
def test_correct_results(cat_age, dog_age, expected_output) -> None:
    assert get_human_age(cat_age, dog_age) == expected_output
