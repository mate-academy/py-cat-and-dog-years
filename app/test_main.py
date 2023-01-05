import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(0, 0, [0, 0], id="should return zero"),
            pytest.param(14, 14, [0, 0], id="should return zero"),
            pytest.param(15, 15, [1, 1], id="should return one"),
            pytest.param(23, 23, [1, 1], id="should return one"),
            pytest.param(24, 24, [2, 2], id="should return two"),
            pytest.param(27, 28, [2, 2], id="should return two"),
            pytest.param(28, 29, [3, 3], id="should return three"),
            pytest.param(-12, -3, [0, 0], id="should return two"),
            pytest.param(100, 100, [21, 17], id="should return two"),
        ],
    )
    def test_utmost_cases(self, cat_age: int,
                          dog_age: int,
                          result: tuple) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [pytest.param("cat", "4", TypeError,
                      id="should raise error if not list")],
    )
    def test_raising_errors_correctly(self, cat_age: int,
                                      dog_age: int,
                                      expected_error: tuple) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
