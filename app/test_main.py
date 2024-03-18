from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="should convert correctly first year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should convert correctly second year"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="should convert correctly each year"
            ),
            pytest.param(
                1000000000,
                1000000000,
                [249999996, 199999997],
                id="realy large numbers"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="get human age with zero ages"
            ),
            pytest.param(
                -10,
                -10,
                [0, 0],
                id="negative number"
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "10",
                "100",
                TypeError,
                id="str type"
            )
        ]
    )
    def test_raising_error_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
