import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_result",
    [
        pytest.param(0, 0, [0, 0], id="test with arguments equal 0"),
        pytest.param(14, 14, [0, 0], id="test with arguments 14"),
        pytest.param(15, 15, [1, 1], id="test with arguments equal 15"),
        pytest.param(23, 23, [1, 1], id="test with zero arguments equal 23"),
        pytest.param(24, 24, [2, 2], id="test with arguments equal 24"),
        pytest.param(28, 28, [3, 2], id="test with arguments equal 28"),
        pytest.param(100, 100, [21, 17], id="test with arguments equal 100"),
    ]
)
def test_function_human_age(
        cat_years: int, dog_years:
        int, expected_result: list
) -> bool:
    assert get_human_age(cat_years, dog_years) == expected_result
