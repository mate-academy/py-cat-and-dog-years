import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result", [
    pytest.param(0, 0, [0, 0],
                 id="zero values"
    ),
    pytest.param(14, 14, [0, 0],
                id="first year border"
    ),
    pytest.param(15, 15, [1, 1],
                id="achieving first year border"
    ),
    pytest.param(23, 23, [1, 1],
                id="second year border"
    ),
    pytest.param(24, 24, [2, 2],
                id="achieving second year border"
    ),
    pytest.param(27, 27, [2, 2],
                id="cat's third year border"
    ),
    pytest.param(28, 28, [3, 2],
                id="difference between animals"
    ),
    pytest.param(200, 200, [46, 37],
                id="big numbers"
    )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list):
    assert (
        get_human_age(cat_age, dog_age) == result
    )
