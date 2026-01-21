import pytest
from app.main import get_human_age


class TestGetHumanAgeClass():
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(0, 0, [0, 0],
                         id="zero values should return result 0"),
            pytest.param(14, 14, [0, 0],
                         id="first 15 cat or dog years give 1 human year"),
            pytest.param(15, 15, [1, 1],
                         id="first 15 cat or dog years give 1 human year"),
            pytest.param(23, 23, [1, 1],
                         id="next 9 cat or dog years give 1 more human year"),
            pytest.param(24, 24, [2, 2],
                         id="next 9 cat or dog years give 1 more human year"),
            pytest.param(28, 28, [3, 2],
                         id="every 4 next cat and 5 dog years add 1 year"),
            pytest.param(100, 100, [21, 17],
                         id="every 4 next cat and 5 dog years add 1 year"),
            pytest.param(-2, -3, [0, 0],
                         id="should return 0 for negative values"),
            pytest.param(99999, 999999, [24995, 199997],
                         id="should return correct values for large numbers")
        ]
    )
    def test_return_values_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "0", 0, TypeError,
                id="should raise exception when cat age is not integer"
            ),
            pytest.param(
                0, "0", TypeError,
                id="should raise exception when dog age is not integer"
            ),
        ]
    )
    def test_raise_exception_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
