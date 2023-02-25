import pytest


from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_ages",
        [
            pytest.param(0, 0, [0, 0]),
            pytest.param(12, 13, [0, 0]),
            pytest.param(15, 15, [1, 1]),
            pytest.param(23, 23, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(27, 27, [2, 2]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(-120, -20, [0, 0]),
            pytest.param(100, 100, [21, 17]),
        ],
        ids=[
            "zero ages equal [0, 0]",
            "less than 15 ages equal [0, 0]",
            "both 15 ages equal [1, 1]",
            "less than 24 ages equal [1, 1]",
            "both 24 ages equal [2, 2]",
            "less than 28 ages equal [2, 2]",
            "both 28 ages equal [3, 2]",
            "negative ages return [0, 0]",
            "both 100 ages return [21, 17]"
        ]
    )
    def test_get_human_age(
            self, cat_age: int,
            dog_age: int,
            expected_ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_ages

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(1, "2", TypeError),
            pytest.param([2], 2, TypeError),
            pytest.param([2], "2", TypeError)
        ],
        ids=[
            "wrong type of age param raises exception",
            "wrong type of age param raises exception",
            "wrong type of age param raises exception"
        ]
    )
    def test_get_human_age_wrong_types(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
