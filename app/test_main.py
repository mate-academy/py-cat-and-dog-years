from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="Zero number"),
        pytest.param(-1, -1, [0, 0], id="Negative number"),
        pytest.param(14.5, 14.5, [0, 0], id="Float numbers"),
        # pytest.param("15", "15", TypeError),
        # pytest.param({"14": 14}, {"14": 14}, [0, 0]),
        # pytest.param([15], [15], [0, 0]),
        pytest.param(14, 14, [0, 0], id="higher bound 0"),
        pytest.param(15, 15, [1, 1], id="lower bound 1 year"),
        pytest.param(23, 23, [1, 1], id="higher bound 1 year"),
        pytest.param(24, 24, [2, 2], id="lower bound 2 years"),
        pytest.param(27, 28, [2, 2], id="higher bound 2 years"),
        pytest.param(28, 29, [3, 3], id="lower bound for 3 years"),
        pytest.param(1000, 1500, [246, 297], id="Huge values"),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list) -> None:

    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    (
        [
            pytest.param([15], [15], id="List"),
            pytest.param("15", "15", id="String"),
            pytest.param({"14": 14}, {"14": 14}, id="Dictionary")
        ]
    )
)
def test_get_human_age_raise_error(cat_age: Any, dog_age: Any) -> None:

    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
