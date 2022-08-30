from app.main import get_human_age
import pytest


class TestGetHumanAge:
    def test_should_raise_typeerror_when_not_int_param(self):
        with pytest.raises(TypeError):
            get_human_age([14], "14")

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_value",
        [
            (
                -1,
                -1,
                [0, 0]
            ),
            (
                14,
                14,
                [0, 0]
            ),
            (
                15,
                15,
                [1, 1]
            ),
            (
                23,
                23,
                [1, 1]
            ),
            (
                24,
                24,
                [2, 2]
            ),
            (
                25,
                25,
                [2, 2]
            ),
            (
                28,
                28,
                [3, 2]
            ),
            (
                32,
                33,
                [4, 3]
            ),
            (
                100,
                100,
                [21, 17]
            )
        ]
    )
    def test_get_human_should_work_properly(self,
                                            cat_age,
                                            dog_age,
                                            expected_value):
        assert get_human_age(cat_age, dog_age) == expected_value
