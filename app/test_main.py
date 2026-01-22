from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_output",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (-1, -1, [0, 0])
        ],
        ids=[
            "zero years for both animals",
            "check biggest value for zero year",
            "15 cat/dog years should convert into 1 human age.",
            "check biggest value for first year",
            "check lowest value for second year",
            "check biggest value for second year",
            "check difference in aging",
            "check if difference in aging is bigger ",
            "check two negative values"

        ]
    )
    def test_get_human_age_output(
            self,
            cat_age: int,
            dog_age: int,
            expected_output: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_output

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "1",
                "1",
                TypeError,
                id="Should raise TypeError if arguments is not int"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: str,
            dog_age: str,
            expected_error: type[Exception],
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
