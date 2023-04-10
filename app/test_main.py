import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "input_value_cat,input_value_dog,expected_value",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should work correctly with the value zero"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should work correctly with a normal value"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should work correctly with a normal value"
            ),
            pytest.param(
                -2,
                -3,
                [0, 0],
                id="should work correctly with a negative value"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should work correctly with a normal value"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should work correctly with a normal value"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should work correctly with a normal value"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should work correctly with a normal value"
            ),
            pytest.param(
                1000,
                1000,
                [246, 197],
                id="should work correctly with a large value"
            )
        ])
    def test_convert_to_human_correctly(self,
                                        input_value_cat: int,
                                        input_value_dog: int,
                                        expected_value: list[int]) -> None:
        assert get_human_age(input_value_cat,
                             input_value_dog) == expected_value

    with pytest.raises(TypeError):
        get_human_age("12", 22)
