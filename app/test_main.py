import pytest

from app.main import get_human_age


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                0, 0, [0, 0],
                id="If values =(0, 0), the result should be =(0, 0)"),
            pytest.param(
                14, 14, [0, 0],
                id="If values =(14, 14), the result should be =(0, 0)"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="If values =(14, 15, the result should be =(1, 1)"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="If values =(23, 23), the result should be =(1, 1)"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="If values =(24, 24), the result should be =(2, 2)"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="If values =(27, 27), the result should be =(2, 2)"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="If values =(28, 28), the result should be =(3, 2)"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="If values =(100, 100), the result should be =(21, 17)"),
            pytest.param(-1, -1, [0, 0],
                         id="Age negative"
                         )
        ]
    )
    def test_with_different_parameters(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    def test_receives_an_incorrect_type_of_data(self) -> None :
        with pytest.raises(TypeError):
            get_human_age("", [])
