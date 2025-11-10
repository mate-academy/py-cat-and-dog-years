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

    def test_return_type_is_list(self) -> None:
        result = get_human_age(15, 15)
        assert isinstance(result, list)
        assert not isinstance(result, tuple)

    def test_list_contains_exactly_two_elements(self) -> None:
        result = get_human_age(50, 60)
        assert len(result) == 2

    def test_returned_elements_are_integers(self) -> None:
        result = get_human_age(100, 100)
        assert all(isinstance(age, int) for age in result)

    def test_independent_calculations(self) -> None:
        cat_only = get_human_age(50, 0)
        dog_only = get_human_age(0, 60)
        both = get_human_age(50, 60)

        assert cat_only[0] == both[0], "Cat age should be independent"
        assert dog_only[1] == both[1], "Dog age should be independent"

    @pytest.mark.parametrize(
        ("cat_age", "dog_age"),
        [
            pytest.param(1000, 1000, id="very large equal"),
            pytest.param(5000, 3000, id="extremely large"),
        ],
    )
    def test_very_large_numbers(self, cat_age: int, dog_age: int) -> None:
        result = get_human_age(cat_age, dog_age)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(age, int) and age >= 0 for age in result)

    @pytest.mark.parametrize(
        ("cat_age", "dog_age"),
        [
            pytest.param(-1, 25, id="negative cat_age"),
            pytest.param(25, -1, id="negative dog_age"),
            pytest.param(-5, -6, id="both negative"),
        ],
    )
    def test_negative_numbers_return_zero(
            self, cat_age: int, dog_age: int
    ) -> None:
        result = get_human_age(cat_age, dog_age)

        if cat_age < 0:
            assert result[0] == 0

        if dog_age < 0:
            assert result[1] == 0
