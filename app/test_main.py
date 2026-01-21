from __future__ import annotations

import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(0, 0, [0, 0], id="both pets are newborn"),
    pytest.param(14, 14, [0, 0], id="both pets are under 15 years old"),
    pytest.param(15, 15, [1, 1], id="both pets are exactly 15 years old"),
    pytest.param(23, 23, [1, 1], id="both pets are under 24 years old"),
    pytest.param(24, 24, [2, 2], id="both pets are exactly 24 years old"),
    pytest.param(27, 27, [2, 2], id="both pets are under 28 years old"),
    pytest.param(28, 28, [3, 2], id="both pets are exactly 28 years old"),
    pytest.param(100, 100, [21, 17], id="both pets are over 28 years old"),
    pytest.param(-1, -1, [0, 0], id="pet has negative age"),
    pytest.param("0", 0, TypeError, id="cat age is not an integer"),
])
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list | TypeError) -> None:
    if isinstance(expected, list):
        assert get_human_age(cat_age, dog_age) == expected
    else:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
