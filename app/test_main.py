import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        ("cat_age", "dog_age", "result"),
        [
            pytest.param(0, 0, [0, 0], id="two zeros"),
            pytest.param(14, 14, [0, 0], id="just before first threshold"),
            pytest.param(15, 15, [1, 1], id="exactly at first threshold"),
            pytest.param(23, 23, [1, 1], id="just before second threshold"),
            pytest.param(24, 24, [2, 2], id="exactly at second threshold"),
            pytest.param(27, 27, [2, 2], id="just before cat third threshold"),
            pytest.param(28, 28, [3, 2], id="cat at third, dog not yet"),
            pytest.param(28, 29, [3, 3], id="both at third threshold"),
            pytest.param(100, 100, [21, 17], id="large equal numbers"),

            pytest.param(27, 16, [2, 1], id="cat: one before boundary (27)"),
            pytest.param(28, 16, [3, 1], id="cat: exactly at boundary (28)"),
            pytest.param(31, 16, [3, 1], id="cat: between increments (31)"),
            pytest.param(32, 16, [4, 1], id="cat: next increment (32)"),

            pytest.param(16, 28, [1, 2], id="dog: one before boundary (28)"),
            pytest.param(16, 29, [1, 3], id="dog: exactly at boundary (29)"),
            pytest.param(16, 33, [1, 3], id="dog: between increments (33)"),
            pytest.param(16, 34, [1, 4], id="dog: next increment (34)"),

            pytest.param(105, 120, [22, 21], id="different large numbers"),
            pytest.param(200, 150, [46, 27], id="very large asymmetric"),

            pytest.param(0, 50, [0, 7], id="cat zero, dog adult"),
            pytest.param(50, 0, [8, 0], id="cat adult, dog zero"),

            pytest.param(1000, 1000, [246, 197], id="very large equal"),
            pytest.param(5000, 3000, [1246, 597], id="extremely large"),
        ],
    )
    def test_should_return_list_of_ages(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        ("cat_age", "dog_age", "expected_error"),
        [
            pytest.param((15,), 25, TypeError, id="tuple for cat_age"),
            pytest.param("str", 25, TypeError, id="string for cat_age"),
            pytest.param([25], 25, TypeError, id="list for cat_age"),
            pytest.param(None, 25, TypeError, id="None for cat_age"),

            pytest.param(25, (15,), TypeError, id="tuple for dog_age"),
            pytest.param(25, "str", TypeError, id="string for dog_age"),
            pytest.param(25, [25], TypeError, id="list for dog_age"),
            pytest.param(25, None, TypeError, id="None for dog_age"),

            pytest.param("cat", "dog", TypeError, id="both strings"),
            pytest.param([15], [25], TypeError, id="both lists"),
        ],
    )
    def test_should_raise_error_if_parameter_has_wrong_data_type(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        ("cat_age", "dog_age", "result"),
        [
            pytest.param(-1, 25, [0, 2], id="negative cat_age"),
            pytest.param(25, -1, [2, 0], id="negative dog_age"),
            pytest.param(-5, -6, [0, 0], id="both negative"),
        ],
    )
    def test_negative_numbers_return_zero(
            self, cat_age: int, dog_age: int, result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result
