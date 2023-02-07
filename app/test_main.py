import pytest

from app.main import get_human_age


class TestResults:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="Zero years check"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="Under 15 years check"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="Average years check"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="Old pets check"
            )
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
                25.5, 76.5,
                id="Function should not accept floats"
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
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)
