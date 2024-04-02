import pytest
from app.main import get_human_age


class AgeConvertor:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (-50, -100, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (23, 23, [1, 1]),
            (27, 27, [2, 2]),
            (28, 27, [3, 2]),
            (100, 100, [21, 17]),
            (4123321456, 1231231231, [4123321456, 1231231231]),
        ],
        ids=[
            "Animals with negative years should be equal to 0",
            "If animals years are equal to 0 they should be equal to 0 in human age",
            "Animals with years under 15 should be equal to 0",
            "Animals with years  in range (15, 23) should be equal to 1",
            "After 24 every 4 years for cat and 5 for dog give 1 extra year",
            "After 24 every 4 years for cat and 5 for dog give 1 extra year",
            "After 24 every 4 years for cat and 5 for dog give 1 extra year",
            "Func should works correctly with big int",
        ]
    )
    def test_should_return_correct_result_with_correct_and_incorrect_data(
        self,
        cat_age: int,
        dog_age: int,
        expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "wrong_input_value",
        [
            {0},
            None,
            "45",
            (1, 2, 3),
            {"a": 123}
        ],
    )
    def test_should_raise_error_if_age_not_int(
            self,
            wrong_input_value
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(wrong_input_value, wrong_input_value)
