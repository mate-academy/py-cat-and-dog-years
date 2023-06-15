import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,converted_ages",
        [
            pytest.param(-1, -2, [0, 0]),
            pytest.param(0, 0, [0, 0]),
            pytest.param(14, 14, [0, 0]),
            pytest.param(15, 15, [1, 1]),
            pytest.param(23, 23, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(27, 28, [2, 2]),
            pytest.param(28, 29, [3, 3]),
            pytest.param(100, 100, [21, 17]),
            pytest.param(1000, 1000, [246, 197]),
        ]
    )
    def test_get_correct_human_age_on_boundary_animal_age_values(
            self,
            cat_age: int,
            dog_age: int,
            converted_ages: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == converted_ages

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param("13", 15, TypeError),
            pytest.param(14, "15", TypeError)
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
