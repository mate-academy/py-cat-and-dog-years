from app.main import get_human_age
import pytest


class TestGetHumanAge:
    def test_should_raise_typeerror_when_not_int_param(self):
        with pytest.raises(TypeError):
            get_human_age([14], "14")

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_value",
        [
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return cat's and dog's age in human"
            ),
            pytest.param(
                6,
                6,
                [0, 0],
                id="should return zero if cat's or dog's age is under 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return 1 if cat's and dog's age >= 15 or <= 23"
            ),
            pytest.param(
                32,
                33,
                [4, 3],
                id="test when values are boundary"
            )
        ]
    )
    def test_get_human_should_work_properly(self,
                                            cat_age,
                                            dog_age,
                                            expected_value):
        assert get_human_age(cat_age, dog_age) == expected_value
