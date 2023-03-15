import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="animals' age 0 converts to 0 h.a."),
        pytest.param(14, 14, [0, 0], id="animals' age 14 converts to 0 h.a."),
        pytest.param(15, 15, [1, 1], id="animals' age 15 converts to 1 h.a."),
        pytest.param(23, 23, [1, 1], id="animals' age 23 converts to 1 h.a."),
        pytest.param(24, 24, [2, 2], id="animals' age 24 converts to 2 h.a."),
        pytest.param(27, 27, [2, 2], id="animals' age 27 converts to 2 h.a."),
        pytest.param(28, 28, [3, 2], id="cat/dog age 28 converts to 3/2 h.a."),
        pytest.param(99, 99, [20, 17], id="cat/dog age 99 is 20/17 h.a.")
    ]
)
def test_when_age_changes(
    cat_age: int,
    dog_age: int,
    result: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == result)
