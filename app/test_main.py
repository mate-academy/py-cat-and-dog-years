import pytest

from app.main import get_human_age


class TestMain:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(0, 0, [0, 0], id="min value for age"),
            pytest.param(14, 14, [0, 0], id="max value before first year"),
            pytest.param(15, 15, [1, 1], id="min value for first year"),
            pytest.param(23, 23, [1, 1], id="max value for first year"),
            pytest.param(24, 24, [2, 2], id="min value for second year"),
            pytest.param(27, 28, [2, 2], id="max value for second year"),
            pytest.param(28, 29, [3, 3], id="min value for third year"),
            pytest.param(32, 34, [4, 4], id="min value for fourth year"),
            pytest.param(220, 500, [51, 97], id="age for big values"),
            pytest.param(-1, -2, [0, 0], id="age for negative values")
        ]
    )

    def test_get_human_age(self, cat_age: int, dog_age: int, human_age: int) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,error_",
        [
            pytest.param("str", 2, TypeError, id="str instead int for cat"),
            pytest.param(4, "str", TypeError, id="str instead int for dog")
        ]
    )

    def test_error(self, cat_age: int, dog_age: int, error_: Exception) -> None:
        with pytest.raises(error_):
            get_human_age(cat_age, dog_age)
