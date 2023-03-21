import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (-1, -1, [0, 0]),
            (0, 0, [0, 0]),
            (13, 13, [0, 0]),
            (15, 15, [1, 1]),
            (22, 22, [1, 1]),
            (25, 25, [2, 2]),
            (28, 28, [3, 2]),
            (29, 29, [3, 3]),
            (111, 111, [23, 19]),
            (12345, 12345, [3082, 2466]),
        ],
        ids=[
            "Should return '[0, 0]' if cat's and dog's age < 0",
            "Should return '[0, 0]' if cat's and dog's age == 0",
            "Should return '[0, 0]' if cat's and dog's age == 13",
            "Should return '[1, 1]' if cat's and dog's age == 15",
            "Should return '[2, 2]' if cat's and dog's age == 22",
            "Should return '[2, 2]' if cat's and dog's age == 25",
            "Should return '[3, 2]' if cat's and dog's age == 28",
            "Should return '[3, 3]' if cat's and dog's age == 29",
            "Should return '[23, 19]' if cat's and dog's age == 111",
            "Should return '[3082, 2466]' if cat's and dog's age == 12345"
        ]
    )
    def test_of_correct_years_converting(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    def test_for_correct_parameters(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("2", 1)
