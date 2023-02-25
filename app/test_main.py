import pytest


from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_ages",
        [
            pytest.param(0, 0, [0, 0], id="zero ages should equal [0, 0]"),
            pytest.param(12, 13, [0, 0], id="less than 15 ages should equal [0, 0]"),
            pytest.param(15, 15, [1, 1], id="both 15 ages should equal [1, 1]"),
            pytest.param(23, 23, [1, 1], id="less than 24 ages should equal [1, 1]"),
            pytest.param(24, 24, [2, 2], id="both 24 ages should equal [2, 2]"),
            pytest.param(27, 27, [2, 2], id="less than 28 ages should equal [2, 2]"),
            pytest.param(28, 28, [3, 2], id="both 28 ages should equal [3, 2]"),
            pytest.param(-120, -20, [0, 0], id="negative ages should return [0, 0]"),
            pytest.param(100, 100, [21, 17], id="both 100 ages should return [21, 17]"),
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
            pytest.param(1, "2", TypeError, id="wrong type of age param raises exception"),
            pytest.param([2], 2, TypeError, id="wrong type of age param raises exception"),
            pytest.param([2], "2", TypeError, id="wrong type of age param raises exception")
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