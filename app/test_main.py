import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="both ages zero"),
        pytest.param(14, 14, [0, 0], id="both ages zero"),
        pytest.param(15, 15, [1, 1], id="first human year"),
        pytest.param(23, 23, [1, 1], id="first human year"),
        pytest.param(24, 24, [2, 2], id="second human year"),
        pytest.param(27, 27, [2, 2], id="second human year"),
        pytest.param(28, 28, [3, 2], id="difference years cat and dog"),
        pytest.param(100, 100, [21, 17], id="difference years cat and dog")
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: Exception
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
