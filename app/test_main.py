import pytest

from app.main import get_human_age


class TestAgeClass:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(0, 0, [0, 0], id="human age zero"),
            pytest.param(14, 14, [0, 0], id="before first year"),
            pytest.param(15, 15, [1, 1], id="first year"),
            pytest.param(23, 23, [1, 1], id="before second year"),
            pytest.param(24, 24, [2, 2], id="second year"),
            pytest.param(28, 24, [3, 2], id="different cat and dog age"),
            pytest.param(120, 130, [26, 23], id="big age"),
            pytest.param(27, 27, [2, 2], id="before cat third year"),
            pytest.param(28, 28, [3, 2], id="cat third year"),
            pytest.param(29, 29, [3, 3], id="dog third year"),
        ],
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param("15", "15", id="age is string"),
            pytest.param(14, None, id="dog age is None"),
            pytest.param(15.5, 15, id="cat age is float"),
            pytest.param(15, 15.5, id="dog age is float"),
        ],
    )
    def test_get_human_age_raises_type_error_for_invalid_types(
        self, cat_age: int, dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param(-1, 0, id="cat age is negative"),
            pytest.param(0, -1, id="dog age is negative"),
            pytest.param(-1, -1, id="both ages are negative"),
        ],
    )
    def test_get_human_age_raises_value_error_for_negative_ages(
            self, cat_age: int, dog_age: int
    ) -> None:
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)
