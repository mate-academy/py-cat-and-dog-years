import pytest

from app.main import get_human_age


class TestResults:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="With pets age = 0 should return [0, 0]"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="With values under 15 should return [0, 0]"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="With values 23 and 23 should return [1, 1]"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="With values 28 and 28 should return [3, 2]"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="With values 100 and 100 should return [21, 17]"
            ),
        ],
    )
    def test_age_values(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


class TestErrors:
    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                20, [40],
                id="Test cannot add 'int' and 'list'"
            ),
            pytest.param(
                50, "70",
                id="Test cannot add 'int' and 'str'"
            ),
            pytest.param(
                {"cat": 40}, 90,
                id="Test cannot add 'dict' and 'int'"
            ),
            pytest.param(
                {3}, 50,
                id="Test cannot add 'set' and 'int'"
            ),
            pytest.param(
                (8, 2), 30,
                id="Test cannot add 'tuple' and 'int'"
            ),
        ]
    )
    def test_cannot_add_instances(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                1200, 1200,
                id="Function should not accept such a large numbers"
            ),
            pytest.param(
                -5, -10,
                id="Function should not accept negative numbers"
            )
        ]
    )
    def test_values_out_of_range(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(AssertionError):
            assert 0 < cat_age < 100
            assert 0 < dog_age < 100

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                23.5, 76.5,
                id="Function should not accept floats"
            )
        ]
    )
    def test_values_are_float(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(AssertionError):
            assert isinstance(cat_age, int)
            assert isinstance(dog_age, int)
