from typing import Any

import pytest

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
        pytest.param(-1, 23, [0, 1],
                     id="test receives negative number for cat"),
        pytest.param(15, -7, [1, 0],
                     id="test receives negative number for dog"),
        pytest.param(0, 0, [0, 0],
                     id="test receives zeros"),
        pytest.param(23, 23, [1, 1],
                     id="test receives normal range numbers"),
        pytest.param(28, 28, [3, 2],
                     id="test receives normal range numbers"),
        pytest.param(15, 15, [1, 1],
                     id="test receives normal range numbers"),
        pytest.param(100, 100, [21, 17],
                     id="test receives large numbers"),
        pytest.param(500, 300, [121, 57],
                     id="test receives large numbers"),
        pytest.param(1002, 600, [246, 117],
                     id="test receives large numbers")
    ]
)
def test_check_for_receiving_different_range_of_numbers_data(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
