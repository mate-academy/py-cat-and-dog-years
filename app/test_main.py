import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        ("str", [], TypeError)
    ]
)
def test_check_for_receiving_incorrect_type_of_data(
        cat_age: Any,
        dog_age: Any,
        expected_result: TypeError
) -> None:
    with pytest.raises(expected_result):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(-1, -1, [0, 0], id="test receives negative number"),
        pytest.param(-5, -7, [0, 0], id="test receives negative number"),
        pytest.param(0, 0, [0, 0], id="test receives zero"),
        pytest.param(23, 23, [1, 1], id="test receives normal range number"),
        pytest.param(28, 28, [3, 2], id="test receives normal range number"),
        pytest.param(15, 15, [1, 1], id="test receives normal range number"),
        pytest.param(100, 100, [21, 17], id="test receives large number"),
        pytest.param(500, 300, [121, 57], id="test receives large number"),
        pytest.param(1002, 600, [246, 117], id="test receives large number")
    ]
)
def test_check_for_receiving_different_range_of_numbers_data(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
