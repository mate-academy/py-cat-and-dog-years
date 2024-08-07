import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "input_cat_data, input_dog_data, expected_result",
        [
            pytest.param(
                45,
                60,
                [7, 9],
                id="should return correct when both ages more than 15"
            ),
            pytest.param(
                12,
                12,
                [0, 0],
                id="should return correct when both ages less than 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="fulfillment of the 15 years condition"
            ),
            pytest.param(
                76,
                12,
                [15, 0],
                id="cat age more than 15 but dog not"
            ),
            pytest.param(
                10,
                58,
                [0, 8],
                id="dog age more than 15 but cat not"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return 0 if both ages are 0"
            ),
            pytest.param(
                -10,
                50,
                [0, 7],
                id="should return 0 if age less than zero"
            ),
            pytest.param(
                10000,
                20000,
                [2496, 3997],
                id="should correctly calculate big ages"
            ),
            pytest.param(
                None,
                45,
                6,
                id="should correctly calculate age for dog"
            ),
            pytest.param(
                35,
                None,
                4,
                id="should correctly calculate age for cat"
            )
        ]
    )
    def test_get_ages_correctly(
            self,
            input_cat_data: int,
            input_dog_data: int,
            expected_result: list
    ) -> None:
        if not input_cat_data and not input_dog_data:
            result = get_human_age(input_cat_data, input_dog_data)
            assert result == expected_result
            return
        if not input_dog_data:
            assert get_human_age(input_cat_data, 1)[0] == expected_result
            return
        if not input_cat_data:
            assert get_human_age(1, input_dog_data)[1] == expected_result
            return
        result = get_human_age(input_cat_data, input_dog_data)
        assert result == expected_result

    @pytest.mark.parametrize(
        "input_cat_data, input_dog_data, expected_error",
        [
            pytest.param(
                None,
                None,
                TypeError,
                id="should raise an error when age is None"
            ),
            pytest.param(
                "15",
                15,
                TypeError,
                id="should raise an error when age is string"
            ),
            pytest.param(
                [1],
                15,
                TypeError,
                id="should raise an error when cat age is list"
            ),
            pytest.param(
                15,
                [1],
                TypeError,
                id="should raise an error when dog age is list"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            input_cat_data: int,
            input_dog_data: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(input_cat_data, input_dog_data)
