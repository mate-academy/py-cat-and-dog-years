import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_years", "dog_years", "result"),
    [
        pytest.param(0, 0, [0, 0], id="Should return 0 if age < 15"),
        pytest.param(14, 14, [0, 0], id="Should return 0 if age < 15"),
        pytest.param(15, 15, [1, 1], id="Should return 1 if age >= 15"),
        pytest.param(23, 23, [1, 1], id="Should return 1 if age < 24"),
        pytest.param(24, 24, [2, 2], id="Should return 2 if age >= 24"),
        pytest.param(27, 27, [2, 2], id="Should return 2 if age < 28"),
        pytest.param(28, 28, [3, 2], id="Should add +1 year every 5y to dogs"),
        pytest.param(100, 100, [21, 17], id="Should change age every 4 or 5 years"),
        pytest.param(-24, -121, [0, 0], id="Should return zero when age < 0"),
    ]
)
def test_correct_result(cat_years: int, dog_years: int, result: list) -> None:
    assert get_human_age(cat_years, dog_years) == result


def test_should_return_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
