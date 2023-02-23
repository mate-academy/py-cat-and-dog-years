import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_result",
    [
        pytest.param(0, 0, [0, 0], id="test with arguments equal 0"),
        pytest.param(14, 14, [0, 0], id="test with arguments 14"),
        pytest.param(16, 14, [1, 0], id="test with different arguments"),
        pytest.param(23, 23, [1, 1], id="test with arguments equal 23"),
        pytest.param(28, 28, [3, 2], id="test with arguments equal 28"),
        pytest.param(100, 100, [21, 17], id="test with arguments equal 100"),
        pytest.param(-5, -5, [0, 0], id="test with negative arguments"),
        pytest.param(-5, 5, [0, 0], id="test with first negative argument"),
        pytest.param(5, -5, [0, 0], id="test with second negative argument"),
        pytest.param(2.5, 3, [0, 0], id="test with bool argument"),

    ]
)
def test_function_human_age(
        cat_years: int, dog_years: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result


@pytest.mark.parametrize(
    "cat_years,dog_years,expected_result",
    [
        pytest.param("20", 20, TypeError, id="test with bad params")
    ]
)
def test_on_raising_errors(
        cat_years: int,
        dog_years: int,
        expected_result: TypeError
) -> None:
    with pytest.raises(expected_result):
        get_human_age(cat_years, dog_years)
