import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "input_value_cat,input_value_dog,expected_value",
        [
            (
                0,
                0,
                [0, 0]
            ),
            (
                100,
                100,
                [21, 17]
            ),
            (
                23,
                23,
                [1, 1]
            ),
            (
                -2,
                -3,
                [0, 0]
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
