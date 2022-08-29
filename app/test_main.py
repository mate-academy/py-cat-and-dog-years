from app.main import get_human_age
import pytest


class TestGetHumanAge:
    def test_should_raise_typeerror_when_not_int_param(self):
        with pytest.raises(TypeError):
            get_human_age([14], "14")

    def test_should_return_int(self):
        assert isinstance(get_human_age(24, 24.1)[1], int)

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
            )
        ]
    )
    def test_get_human_should_work_properly(self,
                                            cat_age,
                                            dog_age,
                                            expected_value):
        assert get_human_age(cat_age, dog_age) == expected_value
