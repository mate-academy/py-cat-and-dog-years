import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_result",
    [
        pytest.param(0, 0, [0, 0], id="test with arguments equal 0"),
        pytest.param(14, 14, [0, 0], id="test with arguments 14"),
        pytest.param(16, 14, [1, 0], id="test with different arguments"),
        pytest.param(23, 23, [1, 1], id="test with arguments equal 23"),
        pytest.param(28, 29, [3, 3], id="test with arguments equal 28"),
        pytest.param(100, 100, [21, 17], id="test with arguments equal 100"),
        pytest.param(-5, -5, [0, 0], id="test with negative arguments"),
        pytest.param(2.5, 3, [0, 0], id="test with float argument"),

    ]
)
def test_function_human_age(
        cat_years: int, dog_years: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result


def test_on_raising_errors() -> None:
    cat_years = "20"
    dog_years = 20
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
