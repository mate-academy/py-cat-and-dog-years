from app.main import get_human_age
import pytest


class TestCatDogHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return zeros when both ages are zeros",
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="both ages are year behind first threshold",
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="both cross first threshold but not second",
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="both ages are year behind second threshold",
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="both cross second threshold but behind third",
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="both ages are year behind third threshold",
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="cross third threshold but behind fourth",
            ),
            pytest.param(
                31,
                34,
                [3, 4],
                id="dog cross fourth and cat one year behind his fourth",
            ),
            pytest.param(
                33,
                34,
                [4, 4],
                id="both cat and dog ahead of fourth threshold",
            ),
        ],
    )
    def test_get_correct_data_array(
        self, cat_age: int, dog_age: int, expected_result: list
    ) -> None:
        result_from_program = get_human_age(cat_age, dog_age)
        assert result_from_program == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                -3,
                -2,
                ValueError,
                id="should raise error when age is less than 0",
            ),
            pytest.param(
                20,
                "Arsen",
                TypeError,
                id="should raise error when type is not int",
            ),
        ],
    )
    def test_raising_errors_correctly(
        self, cat_age: int, dog_age: int, expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
