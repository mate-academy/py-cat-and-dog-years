import pytest

from app.main import get_human_age


class TestCorrectResultClass:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_value",
        [
            pytest.param(
                1,
                1,
                [0, 0],
                id="cat and dog age < 15 (1, 1)"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="cat and dog age < 15 (14, 14)"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="cat and dog age < 24 (15, 15)"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="cat and dog age < 24 (23, 23)"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="cat and dog age >= 24 (24, 24)"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="cat and dog age >= 24 (27, 27)"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="cat and dog age >= 24 (28, 28)"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="cat and dog age >= 24 (100, 100)"
            ),
        ]
    )
    def test_expected_correct_result(
            self,
            cat_age: int,
            dog_age: int,
            expected_value: Exception
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_value


class TestErrorsValue:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "s",
                "t",
                TypeError,
                id="cat and dog age arguments must not be str"
            ),
            pytest.param(
                "s",
                1,
                TypeError, id="cat age argument must not be str"
            ),
            pytest.param(
                1,
                "t",
                TypeError,
                id="dog age argument must not be str"
            ),
            pytest.param(
                0,
                -1,
                ValueError,
                id="cat and dog age arguments must be positive"
            ),
            pytest.param(
                0,
                1,
                ValueError,
                id="cat age argument must be positive"
            ),
            pytest.param(
                1,
                0,
                ValueError,
                id="dog age argument must be positive"
            ),
            pytest.param(
                101,
                101,
                ValueError,
                id="cat and dog age arguments must not be greater than 100"
            ),
            pytest.param(
                100,
                101,
                ValueError,
                id="cat age argument must not be greater than 100"
            ),
            pytest.param(
                101,
                100,
                ValueError,
                id="dog age argument must not be greater than 100"
            ),
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
