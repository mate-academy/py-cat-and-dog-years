import pytest
from typing import Any
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "age, expected_result",
        [
            (-1, [0, 0]),
            (0, [0, 0]),
            (14, [0, 0]),
            (15, [1, 1]),
            (23, [1, 1]),
            (24, [2, 2]),
            (27, [2, 2]),
            (28, [3, 2]),
            (100, [21, 17]),
            (500, [121, 97])
        ],
        ids=[
            "Negative years should be equal to 0 human age",
            "Animals under 15 years of age should be equal to 0 human age",
            "Animals under 15 years of age should be equal to 0 human age",
            "Animals 15 to 23 years old must be equal to 1 human year old",
            "Animals 15 to 23 years old must be equal to 1 human year old",
            "The next 9 years after first 15 years give 1 more human year",
            "The next 9 years after first 15 years give 1 more human year",
            "After 24 every 4 years for cat and 5 for dog give 1 extra year",
            "After 24 every 4 years for cat and 5 for dog give 1 extra year",
            "Lovely pets never die in our hearts!"
        ]
    )
    def test_get_human_age(self, age: int, expected_result: list[int]) -> None:
        assert get_human_age(age, age) == expected_result

    @pytest.mark.parametrize(
        "wrong_type",
        [
            "Some string",
            None,
            [0, 0],
            {0: 0},
            {0, 0}
        ]
    )
    def test_wrong_type_get_human_age(self, wrong_type: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(wrong_type, wrong_type)
