import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(0, 0, [0, 0],
                         id="zero values should return result 0"),
            pytest.param(14, 14, [0, 0],
                         id="up to 15 dog and cat years 0 human years"),
            pytest.param(15, 15, [1, 1],
                         id="from 15 to 23 cat and dog years 1 human year"),
            pytest.param(23, 23, [1, 1],
                         id="from 15 to 23 cat and dog years 1 human year"),
            pytest.param(24, 24, [2, 2],
                         id="from 24 to 27 cat and dog years 2 human years"),
            pytest.param(27, 27, [2, 2],
                         id="from 24 to 27 cat and dog years 2 human years"),
            pytest.param(28, 28, [3, 2],
                         id="every 4 next cat and 5 dog years add 1 year"),
            pytest.param(100, 100, [21, 17],
                         id="every 4 next cat and 5 dog years add 1 year"),
            pytest.param(- 1, - 3, [0, 0],
                         id="should return 0 for negative values")
        ],
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                1, "1", TypeError,
                id="should raise exception when dog age is not integer"
            ),
            pytest.param(
                "1", 1, TypeError,
                id="should raise exception when cat age is not integer"
            ),
            pytest.param(
                "1", "1", TypeError,
                id="should raise exception when cat and dog age is not integer"
            )
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
