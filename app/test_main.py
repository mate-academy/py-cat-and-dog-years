import pytest

from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(0, 0, [0, 0],
                     id="0  must be equal to [0, 0] human age"),
        pytest.param(14, 14, [0, 0],
                     id="14 must be equal to [0, 0] human age"),
        pytest.param(15, 15, [1, 1],
                     id="15 must be equal to [1, 1] human age"),
        pytest.param(23, 23, [1, 1],
                     id="23 must be equal to [1, 1] human age"),
        pytest.param(24, 24, [2, 2],
                     id="24 must be equal to [2, 2] human age"),
        pytest.param(27, 27, [2, 2],
                     id="27 must be equal to [2, 2] human age"),
        pytest.param(28, 28, [3, 2],
                     id="28 must be equal to [3, 2] human age"),
        pytest.param(100, 100, [21, 17],
                     id="100 must be equal to [21, 17] human age"),
        pytest.param(-1, -1, [0, 0],
                     id="-1  must be equal to [0, 0] human age")
    ]
)
def test_check(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expect_error",
    [
        pytest.param([], [], TypeError,
                     id="`list` should raise `TypeError`"),
        pytest.param({}, {}, TypeError,
                     id="`dict` should raise `TypeError`"),
        pytest.param((), (), TypeError,
                     id="`tuple` should raise `TypeError`"),
        pytest.param("", "", TypeError,
                     id="`str` should raise `TypeError`"),
        pytest.param({1, 2}, {1, 2}, TypeError,
                     id="`set` should raise `TypeError`")
    ]
)
def test_check_raise_error(
        cat_age: Any,
        dog_age: Any,
        expect_error: Any
) -> None:
    with pytest.raises(expect_error):
        get_human_age(cat_age, dog_age)
