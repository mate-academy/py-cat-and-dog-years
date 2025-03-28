import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(0, 0, [0, 0],
                     id="should return 0s when years equal 0"),
        pytest.param(14, 14, [0, 0],
                     id="should return 0s when years equal 14"),
        pytest.param(15, 15, [1, 1],
                     id="should return 1s when years equal 15"),
        pytest.param(23, 23, [1, 1],
                     id="should return 1s when years equal 23"),
        pytest.param(24, 24, [2, 2],
                     id="should return 2s when years equal 24"),
        pytest.param(27, 27, [2, 2],
                     id="should return 2s when years equal 27"),
        pytest.param(28, 28, [3, 2],
                     id="should return 3 and 2 when years equal 28"),
        pytest.param(100, 100, [21, 17],
                     id="should return 21 and 17 when years equal 100"),

    ]
)
def test_get_human_age(cat_age: int, dog_age: int,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
