import pytest

from app.main import get_human_age


def test_type_of_returned_data() -> None:
    ages = get_human_age(15, 15)
    assert isinstance(ages, list)
    assert isinstance(ages[0], int)
    assert isinstance(ages[1], int)
    assert len(ages) == 2


@pytest.mark.parametrize(
    "ages,expected",
    [
        ([14, 14], [0, 0]),
        ([15, 15], [1, 1]),
        ([23, 23], [1, 1]),
        ([24, 24], [2, 2]),
        ([27, 28], [2, 2]),
        ([28, 29], [3, 3]),
        ([200, 200], [46, 37]),
        ([340, 210], [81, 39]),
        ([0, 0], [0, 0]),
        ([100, 0], [21, 0]),
        ([0, 100], [0, 17])
    ]
)
def test_correct_data(ages: list, expected: list) -> None:
    assert get_human_age(*ages) == expected


def test_negative_value() -> None:
    assert get_human_age(-200, -200) == [0, 0]


def test_wrong_input_case() -> None:
    with pytest.raises(TypeError):
        get_human_age("14", "14")
